import os, sys

def main(cache_path, pickle_path):
    
    os.chdir("/opt/FromSpeciesToMaBoSSModel")    
    os.makedirs(cache_path)
    
    from pypath.share import settings
    
    settings.setup(cachedir=(cache_path)) # ==> actual cache folder to use with legacy.main
    # settings.setup(progressbars = True)

    #importing legacy, which is the 'old' version of pypath, the only one (for now), with the graph object implemented
    from pypath.legacy import main as legacy
    
    #initialization of the 'old' PyPath object
    pw_legacy = legacy.PyPath()

    #instead of loading the databases using steps, I prefer loading the activity flow networks with literature references
    #(you can look at the possible datasets at: https://workflows.omnipathdb.org/pypath_guide.html#network-resources)

    for database in legacy.data_formats.omnipath.keys():
        
        if database in ["hprd", "hprd_p", "cellinker"]:
        #if database not in ["signor"]:
            continue
        try:
            print(database, " : ", legacy.data_formats.omnipath[database])
            lst={database: legacy.data_formats.omnipath[database]}
            pw_legacy.init_network(lst)
        except Exception as inst:
            print("Error for "+database)

    # for database in legacy.data_formats.ligand_receptor.keys():
    #     try:
    #         print(database, " : ", legacy.data_formats.ligand_receptor[database])
    #         lst={database: legacy.data_formats.ligand_receptor[database]}
    #         pw_legacy.init_network(lst)
    #     except Exception as inst:
    #         print("Error for "+database)

    # for database in legacy.data_formats.tf_mirna.keys():
    #     try:
    #         print(database, " : ", legacy.data_formats.tf_mirna[database])
    #         lst={database: legacy.data_formats.tf_mirna[database]}
    #         pw_legacy.init_network(lst)
    #     except Exception as inst:
    #         print("Error for "+database)

    #save the network

    pw_legacy.save_to_pickle(pickle_path)

    return 0

if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))