
#function to compute the Bimodality Index (BI) described in Wang et al. (2009)
BI <- function(dataset) {
  x <- dataset
  mc <- Mclust(na.omit(x), G = 2, modelNames = "E", verbose = FALSE)
  if (is.null(mc)) {
    bi <- NA
  } else {
    sigma <- sqrt(mc$parameters$variance$sigmasq)
    delta <- abs(diff(mc$parameters$mean))/sigma
    pi <- mc$parameters$pro[1]
    bi <- delta * sqrt(pi*(1-pi))
  }
  bi
}

#function to binarize the tails of the distribution, based on inter-quartile range (IQR), similar to methods described in teh outlier-sum statistic (Tibshirani and Hastie, 2007). Can be called with a reference dataset
OSclass <- function(exp_dataset, ref_dataset=exp_dataset) {
  classif <-rep(NA,length(exp_dataset))
  q25 <- quantile(ref_dataset,0.25, na.rm = T)
  q75 <- quantile(ref_dataset,0.75, na.rm = T)
  IQR <- q75 - q25 #InterQuartile Range
  classif[exp_dataset>IQR+q75] <- 1
  classif[exp_dataset<q25-IQR] <- 0
  return(classif)
}

#function to to binarize bimodal distributions based on a 2-modes gaussian mixture model (with equal variances). Can be called with a reference dataset
BIMclass <- function(exp_dataset, ref_dataset=exp_dataset) {
  mc <- Mclust(na.omit(ref_dataset), modelNames = "E", G=2, verbose = FALSE)
  classif <- rep(NA,length(exp_dataset))
  if (diff(mc$parameters$mean)>0){
    thresh_down <- max(mc$data[mc$classification==1 & mc$uncertainty <= 0.05])
    thresh_up <- min(mc$data[mc$classification==2 & mc$uncertainty <= 0.05])
    classif[exp_dataset<=thresh_down] <- 0
    classif[exp_dataset>=thresh_up] <- 1
  } else if (diff(mc$parameters$mean)<0){
    thresh_down <- max(mc$data[mc$classification==2 & mc$uncertainty <= 0.05])
    thresh_up <- min(mc$data[mc$classification==1 & mc$uncertainty <= 0.05])
    classif[exp_dataset<=thresh_down] <- 0
    classif[exp_dataset>=thresh_up] <- 1
  }
  return(classif)
}

#function for normalization of zero-inflated data
norm_fun_lin <- function(xdat, reference = xdat){
  x_proc <- (xdat-quantile(reference, 0.01, na.rm = T))/quantile(xdat-quantile(reference, 0.01, na.rm = T), 0.99, na.rm = T)
  x_proc[x_proc<0] <- 0
  x_proc[x_proc>1] <- 1
  x_proc
}

#function for normalization of unimodal data
norm_fun_sig <- function(xdat, reference = xdat){
  xdat <- xdat - median(reference, na.rm = T)
  lambda <- log(3)/mad(reference, na.rm = T)
  transformation <- function(x){
    y <- 1/(1+exp(-lambda*x))
    y
  }
  transformation(xdat) 
}

#function for normalization of unimodal data
norm_fun_bim <- function(xdat, reference = xdat) {
  not_na_xdat <- !is.na(xdat)
  not_na_ref <- !is.na(reference)
  mc <- Mclust(reference[not_na_ref], modelNames = "E", G=2, verbose = FALSE)
  pred <- predict.Mclust(mc,xdat[not_na_xdat])
  normalization <- rep(NA,length(xdat))
  if (diff(mc$parameters$mean)>0){
    normalization[not_na_xdat] <- pred$z[,2]
  } else if (diff(mc$parameters$mean)<0){
    normalization[not_na_xdat] <- pred$z[,1]
  }
  normalization
}

#Here we compute all statistical tools and criteria needed to perform the classification of distributions in the following categories: discarded, zero-inflated, unimodal and bimodal
compute_criteria <- function(exp_dataset){
  # exp_dataset <- exp_dataset %>% select(-PATIENT_ID)
  criteria <- tibble(Gene=colnames(exp_dataset), Dip=NA, BI=NA, Kurtosis=NA, DropOutRate=NA, MeanNZ=NA, DenPeak=NA, Amplitude=NA)
  
  #Compute
  pb = txtProgressBar(min = 1, max = ncol(exp_dataset), initial = 1) 
  for (i in 1:ncol(exp_dataset)){
    x <- na.omit(unlist(exp_dataset[,i]))
    criteria$Amplitude[i] <- max(x)-min(x)
    
    if (criteria$Amplitude[i] !=0){
      criteria$Dip[i] <- dip.test(x)$p.value
      criteria$BI[i] <- BI(x)
      criteria$Kurtosis[i] <- kurtosis(x)-3
      criteria$DropOutRate[i] <- sum(x==0)/length(x)
      criteria$MeanNZ[i] <- sum(x)/sum(x!=0)
      den <- density(x, na.rm = T)
      criteria$DenPeak[i] <- den$x[which.max(den$y)]
    }
    
    setTxtProgressBar(pb,i)
  }
  
  threshold <- median(criteria$Amplitude)/10
  criteria <- criteria %>% 
    mutate(Category=ifelse(Amplitude<threshold | DropOutRate>0.95, "Discarded", NA)) %>%
    mutate(Category=ifelse(is.na(Category) & (BI>1.5 & Dip<0.05 & Kurtosis < 1),"Bimodal",Category)) %>%
    mutate(Category=ifelse(is.na(Category) & DenPeak<threshold, "ZeroInf", Category)) %>%
    mutate(Category=ifelse(is.na(Category), "Unimodal", Category))
  
  return(criteria)
}

#function to apply the proper binarization method depending on the gene expression distribution category
binarize_exp <-  function(exp_dataset, ref_dataset, ref_criteria, gene, show.plot=F){
  if(!missing(gene)){
    
    gene_cat <- ref_criteria %>% filter(Gene==gene) %>% select(Category) %>% unlist
    print(gene_cat)
    x <- unlist(select(exp_dataset,gene))
    x_ref <- unlist(select(ref_dataset,gene))
    
    if (gene_cat=="Discarded"){
      stop("Discarded gene")
      
    } else if (gene_cat=="Bimodal"){
      gene_bin <- BIMclass(x,x_ref)
      
    } else {
      gene_bin <- OSclass(x,x_ref)
    }
    # names(gene_bin) <- exp_dataset$PATIENT_ID
    if(show.plot==T){
      if(all(is.na(gene_bin))){
        tibble(Continuous=x) %>% ggplot(aes(x=Continuous))+geom_histogram(bins=30)+ggtitle(gene)
      } else {
        tibble(Continuous=x, Discrete=factor(gene_bin)) %>% ggplot(aes(x=Continuous, fill=Discrete))+geom_histogram(bins=30)+ggtitle(gene)
      }
    } else {
      return(gene_bin)
    }
    
  } else {
    # exp_dataset <- tbl_to_df(exp_dataset) 
    # ref_dataset <- tbl_to_df(ref_dataset)
    if(dim(exp_dataset)[2] != dim(ref_criteria)[1]){stop("Different number of genes")}
    logi_dis <- ref_criteria$Category=="Discarded"
    logi_OS <- ref_criteria$Category=="Unimodal" | ref_criteria$Category=="ZeroInf"
    logi_bim <- ref_criteria$Category=="Bimodal"
    exp_dataset[,logi_dis] <- (exp_dataset*NA)[,logi_dis] #lapply(exp_dataset[,logi_dis], function(x) rep(NA, length(x)))
    print(logi_OS)
    exp_dataset[,logi_OS] <- mapply(function(x,y) OSclass(x,y), as.data.frame(exp_dataset[,logi_OS]), as.data.frame(ref_dataset[,logi_OS]))
    exp_dataset[,logi_bim] <- mapply(function(x,y) BIMclass(x,y), as.data.frame(exp_dataset[,logi_bim]), as.data.frame(ref_dataset[,logi_bim]))
    
    return(exp_dataset)
  }
  
}

# load MaBoSS bnd file
load_model <- function(filename){
  # load raw
  raw <- scan(filename, what = "character", sep = "\n")
  raw <- raw[raw!=""]
  raw <- paste(raw, collapse = " ")
  # separate nodes
  pieces <- strsplit(raw, "}")[[1]]
  duals <- strsplit(pieces, "\\{")
  # node names
  nodes <- gsub(" ", "", gsub("Node", "", sapply(duals, "[[", 1)))
  # contents
  contents <- sapply(duals, "[[", 2)
  contents <- gsub("^ ", "", gsub("\t", "", contents))
  contents <- contents[contents!=""]
  contents <- gsub(";( )*",";", contents)
  raw_model <- strsplit(contents, ";")
  model <- lapply(raw_model, function(x){
    subpieces <- strsplit(x, "=")
    subfields <- gsub(" $","",gsub("^ ","",sapply(subpieces,"[[", 2)))
    names(subfields) <- gsub(" ","", sapply(subpieces,"[[", 1))
    subfields
  })
  names(model) <- nodes
  # return
  
  return(model)
}

load_config <- function(filename){
  raw_cfg <- scan(filename, sep=";", what = "character")
  raw_cfg <- raw_cfg[raw_cfg!=""]
  pieces <- data.frame(t(do.call("rbind",strsplit(gsub(" ", "", raw_cfg), "="))), stringsAsFactors = F)
  cfg <- as.list(pieces[2,])
  names(cfg) <- pieces[1,]
  for(i in 1:length(cfg)) {
    if(!is.na(as.numeric(cfg[[i]]))) {
      class(cfg[[i]]) <- "numeric"
    } else {
      if(!is.na(as.logical(cfg[[i]]))) {
        class(cfg[[i]]) <- "logical"
      }
    }
  }
  return(cfg)
}

save_config <- function(cfg2, filename){
  for(i in 1:length(cfg2)){
    #if(grepl("istate",names(cfg2)[i])){
    if(length(cfg2[[i]])>1){
      str <- paste0(paste0(cfg2[[i]], "[",seq(length(cfg2[[i]]),1)-1,"]"), collapse=", ")
      if(grepl("istate",names(cfg2)[i])){
        write(paste0("[",gsub(".istate","",names(cfg2)[i]), "].istate", " = ", str,";"), file = filename, append=i>1)
      } else {
        write(paste0("[",names(cfg2)[i], "]", " = ", str,";"), file = filename, append=i>1)
      }
    } else {
      write(paste0(names(cfg2)[i], "=", cfg2[[i]], ";"), file = filename, append=i>1)
    }
  }
}

dual_plot <- function(values){
  values <- as.numeric(values)
  print(table(values==0))
  par(mfrow=c(1,2))
  hist(values, 100)
  hist(values[values>0], 100)
}




