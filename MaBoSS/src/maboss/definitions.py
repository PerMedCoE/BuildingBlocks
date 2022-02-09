import os

# Assets folder for MaBoSS Building Block
ASSETS_PATH = os.environ["PERMEDCOE_ASSETS"]
MABOSS_ASSETS = os.path.join(ASSETS_PATH, "MaBoSS")

# Container definition for MaBoSS Building Block
CONTAINER_PATH = os.environ["PERMEDCOE_IMAGES"]
MABOSS_CONTAINER = CONTAINER_PATH + "MaBoSS.sif"

# Computing units
COMPUTING_UNITS_VARIABLE_NAME = "COMPUTING_UNITS"
if COMPUTING_UNITS_VARIABLE_NAME in os.environ:
    COMPUTING_UNITS = int(os.environ[COMPUTING_UNITS_VARIABLE_NAME])
else:
    COMPUTING_UNITS = 1
