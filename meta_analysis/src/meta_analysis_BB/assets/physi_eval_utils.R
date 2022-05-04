
get_col_labels <- function(xml_file){
  require(XML)

  dom <- xmlParse(xml_file)
  root_node <- xmlRoot(dom)
  labels_node <- root_node[["cellular_information"]][["cell_populations"]][["cell_population"]][["custom"]]["simplified_data"][[2]][["labels"]]
  labels <- c()
  for(i in 1:xmlSize(labels_node)) {
    label <- xmlValue(labels_node[[i]])
    label_length <- as.numeric(xmlAttrs(labels_node[[i]])["size"])
    if(label_length>1){
      label <- paste0(label, "_", 1:label_length)
    }
    labels <- c(labels, label)
  }
  return(labels)
}


get_cell_matrix <- function(cell_file, labels){
  # require(R.matlab)
  require(rmatio)
  # mat <- t(readMat(cell_file)$cells)
  obj <- read.mat(cell_file)
  field_index <- grepl("cells", names(obj))
  # print(names(obj))
  mat <- t(obj[[field_index[1]]])
  colnames(mat) <- labels
  return(mat)
}


summarize_mat <- function(mat, exclude=c("ID"), categorical=c(), op=mean){
  # valid <- setdiff(colnames(mat), exclude)
  # summary <- apply(mat[,valid],2,mean)
  summary <- c()
  for(j in 1:ncol(mat)){
    if(!(colnames(mat)[j] %in% exclude)){
      if(colnames(mat)[j] %in% categorical){
        this_summ <- summarize_categorical_variable(mat[,j], colnames(mat)[j])
      } else {
        this_summ <- summarize_numerical_variable(mat[,j], colnames(mat)[j], op=op)
      }
      summary <- c(summary, this_summ)
    }
  }
  return(summary)
}

summarize_numerical_variable <- function(values, label, op=mean){
  summ <- op(values)
  names(summ) <- label
  return(summ)
}

summarize_categorical_variable <- function(values, label){
  counts <- table(values)
  freqs <- counts/sum(counts)
  names(freqs) <- paste0(label,"_", names(freqs))
  return(freqs)
}


summarize_single_experiment <- function(exp_folder, exclude=c("ID", "experiment"), categorical=c("cell_type", "cycle_model", "current_phase"), verbose=T){

  if(verbose==T) cat(">> Processing experiment ", basename(exp_folder), "\n", sep="")

  prefixes <- gsub("_cells_physicell.mat","",list.files(exp_folder, recursive = T, pattern = "output(.)+cells_physicell.mat", full.names = F))
  prefixes <- c("initial", prefixes, "final")

  cell_files <- paste0(exp_folder, "/", prefixes, "_cells_physicell.mat")
  xml_files <- paste0(exp_folder, "/", prefixes, ".xml")

  mats <- mapply(function(cell_file, xml_file){
    # print(cell_file)
    # print(xml_file)
    labels <- get_col_labels(xml_file)
    mat <- get_cell_matrix(cell_file, labels)
    mat <- data.frame(experiment=gsub(".xml","",basename(xml_file)), mat, stringsAsFactors = F)
    mat$ID <- paste0("cell", mat$ID)
    return(mat)
  }, cell_files, xml_files, SIMPLIFY = F)
  names(mats) <- prefixes

  mats_frame <- do.call("rbind", mats)
  rownames(mats_frame) <- NULL


  ### BY CELL SUMMARY
  bycell <- split(mats_frame, mats_frame$ID)
  bycell_summary <- lapply(bycell, function(cell_mat){
    summarize_mat(cell_mat, exclude=exclude, categorical=categorical)
  })
  ## TO-FIX
  all_fields <- sort(unique(unlist(lapply(bycell_summary, names))))
  bycell_summary2 <- lapply(bycell_summary, function(cs){
    missing <- setdiff(all_fields, names(cs))
    if(length(missing)>0){
      missing_fields <- rep(0, length(missing))
      names(missing_fields) <- missing
      cs <- c(cs, missing_fields)
    }
    cs[all_fields]
  })
  #
  cell_summary <- do.call("rbind", bycell_summary2)

  ### EXPERIMENT SUMMARY
  exp_summary <- apply(cell_summary, 2, mean)

  ### FINAL CELLS SUMMARY
  labels <- get_col_labels(paste0(exp_folder, "/final.xml"))
  final_mat <- get_cell_matrix(paste0(exp_folder, "/final_cells_physicell.mat"), labels)
  final_summary <- summarize_mat(final_mat, exclude=exclude, categorical=categorical)

  return(list(
    cell_summary=cell_summary,
    exp_summary=exp_summary,
    final_summary=final_summary
  ))
}


######################################################################################

univariate_test <- function(dat, group, group_colors, filename=NULL){

  # nr <- floor(sqrt(ncol(dat)))
  # nc <- ceiling(ncol(dat)/nr)
  nc <- 10 #floor(sqrt(ncol(dat)))
  nr <- ceiling(ncol(dat)/nc)
  print(nc)
  print(nr)
  if(!is.null(filename)) png(filename, width=200 + 125*nc, height=200 + 125*nr, pointsize = 14)
  par(mfrow=c(nr,nc), mar=c(7,3,3,1))
  # tool_f <- factor(gsub("SERIAL","S",gsub("PARALLEL","P",group, names(group_colors))))
  tool_f <- factor(group, levels = names(group_colors), labels = names(group_colors))
  flavour <- c("SERIAL", "PARALLEL")[(grepl("PARALLEL", group))+1]
  univar_tests <- list()
  for(i in 1:ncol(dat)){
    boxplot(dat[,i]~tool_f, border=group_colors, main="", xlab="", ylab="", las=2, cex.axis=.9, outline=F)
    univar_tests[[i]] <- wilcox.test(dat[,i]~flavour)
    mtext(colnames(dat)[i], side=3, padj=-1, cex=.8, col=c("black", "red")[(univar_tests[[i]]$p.value<0.01)+1])
  }
  if(!is.null(filename)) dev.off()

  univar_test_summ <- data.frame(do.call("rbind", lapply(univar_tests, function(x) c(statistic=x$statistic, p.value=x$p.value))))
  rownames(univar_test_summ) <- colnames(dat)
  univar_test_summ$adj.p.value <- p.adjust(univar_test_summ$p.value, method="fdr")

  return(univar_test_summ)

}

plot_pca <- function(pca, groups, group_colors, ...){

  vars <- pca$sdev^2
  vars <- (vars/sum(vars))*100

  par(mfrow=c(2,2), oma=c(1,1,1,1))
  plot_pca_componentes(pca, x1=1, x2=2, groups=groups, group_colors=group_colors, ...)
  plot_pca_componentes(pca, x1=1, x2=3, groups=groups, group_colors=group_colors, ...)
  plot_pca_componentes(pca, x1=2, x2=3, groups=groups, group_colors=group_colors, ...)
  barplot(vars, xlab="component", ylab="% explained variance")
  legend("topright", col=group_colors, legend=names(group_colors), pch=20, bty="n")

}

plot_pca_componentes <- function(pca, x1, x2, groups, group_colors, ...){
  vars <- pca$sdev^2
  vars <- (vars/sum(vars))*100
  vars <- round(vars, digits=2)
  lab1 <- paste0("PC", x1, " (",vars[x1],"%)")
  lab2 <- paste0("PC", x2, " (",vars[x2],"%)")
  plot(pca$x[, x1], pca$x[, x2], xlab=lab1, ylab=lab2, col=group_colors[groups], pch=20, ...)
}


plot_pca_exp_fviz <- function(pca, groups, group_colors, pcs=rbind(c(1,2),c(1,3),c(2,3)), add_ellipse=T, filename=NULL, ...){

  require(factoextra)
  require(gridExtra)

  var_expl <- fviz_eig(pca, title="")

  exp_plots <- list()
  for(i in 1:nrow(pcs)){
    ## sample plot
    exp_plots[[i]] <- fviz_pca_ind(
      pca,
      axes=c(pcs[i,]),
      label = "none", title="",
      col.ind = groups,
      palette = group_colors,
      repel = TRUE,
      pointsize=1.7,

      addEllipses = add_ellipse, ellipse.alpha=.02, ellipse.level=.95,
      ggtheme=theme_gray(),
      ...
    ) +
      theme(legend.key.size=unit(20, units="pt")) +
      theme(text = element_text(size = 15.5), axis.title = element_text(size = 15.5), axis.text = element_text(size = 15.5))
  }

  if(!is.null(filename)) png(filename, width = 1100, height = 800, pointsize = 40)
  ga <- grid.arrange(grobs=c(exp_plots, list(var_expl)), ncol=2, nrow=2)
  if(!is.null(filename)) dev.off()

  # if(!is.null(filename)) ggsave(filename, plot=ga, width = 9, height = 7)
}

plot_pca_var_fviz <- function(pca, pcs=rbind(c(1,2),c(1,3),c(2,3)), filename=NULL, ...){

  require(factoextra)
  require(gridExtra)

  var_plots <- list()
  for(i in 1:nrow(pcs)){
    ## variables plot
    var_plots[[i]] <- fviz_pca_var(pca, axes = c(pcs[i,]),labelsize = 5, col.var = "cos2", gradient.cols = c("#00AFBB", "#FC4E07"), title="", repel = TRUE, ggtheme=theme_gray()) +
      theme(legend.position="none") +
      theme(text = element_text(size = 15.5), axis.title = element_text(size = 15.5), axis.text = element_text(size = 15.5))
  }

  if(!is.null(filename)) png(filename, width = 1000, height = 1000, pointsize = 40)
  ga <- grid.arrange(grobs=var_plots, ncol=2, nrow=2)
  if(!is.null(filename)) dev.off()

  # if(!is.null(filename)) ggsave(filename, plot=ga, width = 4, height = 3)

}

#### HTML

gicon <- function(name, size=28){
  # CSS: https://fonts.googleapis.com/icon?family=Material+Icons
  # https://material.io/resources/icons/
  paste0("<i class=\"material-icons\" style=\"font-size:",size,"px;vertical-align: text-bottom;\">",name,"</i>")
}

add_title_page <- function(label, add_date=F, obj){
  obj <- add_raw("</br>", obj=obj)
  obj <- add_h(label, h=1, obj=obj, classes = c("page_title"))
  if(add_date==T) obj <- add_h(date(), h=3, obj=obj)
  obj <- add_raw("</br>", obj=obj)
  obj <- add_raw("</br>", obj=obj)

  return(obj)
}

add_section <- function(label, obj, icon="cloud"){

  obj <- add_h(paste0(gicon(icon)," ",label), h=2, obj=obj, classes = c("section"), style = "vertical-align: middle;")
  # obj <- add_raw("<hr>", obj=obj)
  obj <- add_raw("<br>", obj=obj)

  return(obj)
}
