import os, sys

def main(cache_dir, pickle_dir):
    from pypath import omnipath
    from pypath.resources import network as netres
    from pypath.share import settings
    
    os.chdir('/opt/FromSpeciesToMaBoSSModel')
    #setting the cache directory
    os.makedirs(cache_dir)
    os.makedirs(pickle_dir)
    settings.setup(cachedir = cache_dir, pickle_dir = pickle_dir)
    
    omnipath.db.param['network_mod'] = 'network' 
    omnipath.db.param['network_args'] = {'resources': netres.pathway['signor']} # <-- insert in the dict the pathway
    m = omnipath.db.get_db('network')
    return 0

if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
