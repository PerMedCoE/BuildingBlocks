import os

# Assets folder within the Building Block
TF_ENRICHMENT_ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# Container definition for Carnival Building Block
CONTAINER_PATH = os.environ["PERMEDCOE_IMAGES"]
TF_ENRICHMENT_CONTAINER = CONTAINER_PATH + "toolset.sif"

# Computing units
COMPUTING_UNITS_VARIABLE_NAME = "COMPUTING_UNITS"
if COMPUTING_UNITS_VARIABLE_NAME in os.environ:
    COMPUTING_UNITS = int(os.environ[COMPUTING_UNITS_VARIABLE_NAME])
else:
    COMPUTING_UNITS = 1
