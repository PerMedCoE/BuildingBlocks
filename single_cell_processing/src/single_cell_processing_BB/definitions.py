import os

# Assets folder within the Building Block
SINGLE_CELL_ASSETS_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "assets"
)

# Container definition for Meta Analysis Building Block
CONTAINER_PATH = os.environ["PERMEDCOE_IMAGES"]
SINGLE_CELL_PROCESSING_CONTAINER = CONTAINER_PATH + "single_cell.sif"

# Computing units
COMPUTING_UNITS_VARIABLE_NAME = "COMPUTING_UNITS"
if COMPUTING_UNITS_VARIABLE_NAME in os.environ:
    COMPUTING_UNITS = int(os.environ[COMPUTING_UNITS_VARIABLE_NAME])
else:
    COMPUTING_UNITS = 1
