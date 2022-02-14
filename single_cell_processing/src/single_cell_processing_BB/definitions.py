import os

# Assets folder for Meta Analysis Building Block
ASSETS_PATH = os.environ["PERMEDCOE_ASSETS"]
SINGLE_CELL_PROCESSING_ASSETS = os.path.join(ASSETS_PATH, "single_cell")

# Container definition for Meta Analysis Building Block
CONTAINER_PATH = os.environ["PERMEDCOE_IMAGES"]
SINGLE_CELL_PROCESSING_CONTAINER = CONTAINER_PATH + "single_cell.sif"

# Computing units
COMPUTING_UNITS_VARIABLE_NAME = "COMPUTING_UNITS"
if COMPUTING_UNITS_VARIABLE_NAME in os.environ:
    COMPUTING_UNITS = int(os.environ[COMPUTING_UNITS_VARIABLE_NAME])
else:
    COMPUTING_UNITS = 1
