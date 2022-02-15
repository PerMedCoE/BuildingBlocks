import os

# Assets folder for From Species To MaBoSS Model Building Block
ASSETS_PATH = os.environ["PERMEDCOE_ASSETS"]
BUILD_MODEL_FROM_SPECIES_ASSETS = os.path.join(ASSETS_PATH, "FromSpeciesToMaBoSSModel")

# Container definition for From Species To MaBoSS Model Building Block
CONTAINER_PATH = os.environ["PERMEDCOE_IMAGES"]
BUILD_MODEL_FROM_SPECIES_CONTAINER = CONTAINER_PATH + "FromSpeciesToMaBoSSModel.sif"

# Computing units
COMPUTING_UNITS_VARIABLE_NAME = "COMPUTING_UNITS"
if COMPUTING_UNITS_VARIABLE_NAME in os.environ:
    COMPUTING_UNITS = int(os.environ[COMPUTING_UNITS_VARIABLE_NAME])
else:
    COMPUTING_UNITS = 1
