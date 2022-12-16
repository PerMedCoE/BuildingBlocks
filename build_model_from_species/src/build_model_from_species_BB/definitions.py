import os
from permedcoe.bb import CONTAINER_PATH
from permedcoe.bb import COMPUTING_UNITS

# Assets folder within the Building Block
BUILD_MODEL_FROM_SPECIES_ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# Container definition for From Species To MaBoSS Model Building Block
BUILD_MODEL_FROM_SPECIES_CONTAINER = CONTAINER_PATH + "FromSpeciesToMaBoSSModel.sif"
