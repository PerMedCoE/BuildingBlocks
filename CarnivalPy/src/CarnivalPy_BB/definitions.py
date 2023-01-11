import os

# Do not change this line
BB_SOURCE_PATH=os.path.dirname(os.path.abspath(__file__))

# Computing units
COMPUTING_UNITS_VARIABLE_NAME = "COMPUTING_UNITS"
if COMPUTING_UNITS_VARIABLE_NAME in os.environ:
    COMPUTING_UNITS = int(os.environ[COMPUTING_UNITS_VARIABLE_NAME])
else:
    COMPUTING_UNITS = 1

# Update the following lines:
#  - Assets folder within the Building Block
CARNIVALPY_ASSETS_PATH = os.path.join(BB_SOURCE_PATH, "assets")
#  - Container definition for Carnival Building Block
CONTAINER_PATH = os.environ["PERMEDCOE_IMAGES"]
CARNIVALPY_CONTAINER = CONTAINER_PATH + "carnivalpy.sif"
