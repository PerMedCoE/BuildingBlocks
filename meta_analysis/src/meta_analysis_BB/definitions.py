import os
from permedcoe.bb import CONTAINER_PATH
from permedcoe.bb import COMPUTING_UNITS

# Do not change this line
BB_SOURCE_PATH=os.path.dirname(os.path.abspath(__file__))
CONTAINER_ENGINE = os.environ["CONTAINER_ENGINE"]

# Update the following lines:
#  - Assets folder within the Building Block
ASSETS_PATH = os.path.join(BB_SOURCE_PATH, "assets")
#  - Container definition for Meta Analysis Building Block
CONTAINER_NAME = "meta_analysis.sif"
if CONTAINER_ENGINE == "SINGULARITY":
    CONTAINER = os.path.join(CONTAINER_PATH, CONTAINER_NAME)
    CONTAINER_OPTIONS = "[unassigned]"
elif CONTAINER_ENGINE == "UDOCKER":
    CONTAINER = CONTAINER_NAME.split(".")[0]
    home_directory = os.environ["HOME"]
    CONTAINER_OPTIONS = "-v " + home_directory + ":" + home_directory + " --rm"
else:
    raise Exception("UNSUPPORTED CONTAINER ENGINE: %s (must be SINGULARITY or UDOCKER)" % CONTAINER_ENGINE)

