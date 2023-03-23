import os
from permedcoe.bb import CONTAINER_PATH
from permedcoe.bb import COMPUTING_UNITS

# Do not change this line
BB_SOURCE_PATH=os.path.dirname(os.path.abspath(__file__))

# Update the following lines:
#  - Assets folder within the Building Block
BUILD_MODEL_FROM_SPECIES_ASSETS_PATH = os.path.join(BB_SOURCE_PATH, "assets")
#  - Container definition for From Species To MaBoSS Model Building Block
CONTAINER = "from_species_to_maboss_model.sif"
BUILD_MODEL_FROM_SPECIES_CONTAINER = os.path.join(CONTAINER_PATH, CONTAINER)
