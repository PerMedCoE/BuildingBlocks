import os

# Container definition for Omnipath Building Block
CONTAINER_PATH = os.environ["PERMEDCOE_IMAGES"]
OMNIPATH_CONTAINER = CONTAINER_PATH + "toolset.sif"

# Computing units
COMPUTING_UNITS_VARIABLE_NAME = "COMPUTING_UNITS"
if COMPUTING_UNITS_VARIABLE_NAME in os.environ:
    COMPUTING_UNITS = int(os.environ[COMPUTING_UNITS_VARIABLE_NAME])
else:
    COMPUTING_UNITS = 1
