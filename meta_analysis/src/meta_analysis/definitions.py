import os

# Assets folder for Meta Analysis Building Block
ASSETS_PATH = os.environ["PERMEDCOE_ASSETS"]
META_ANALYSIS_ASSETS = os.path.join(ASSETS_PATH, "meta_analysis")

# Container definition for Meta Analysis Building Block
CONTAINER_PATH = os.environ["PERMEDCOE_IMAGES"]
META_ANALYSIS_CONTAINER = CONTAINER_PATH + "meta_analysis.sif"

# Computing units
COMPUTING_UNITS_VARIABLE_NAME = "COMPUTING_UNITS"
if COMPUTING_UNITS_VARIABLE_NAME in os.environ:
    COMPUTING_UNITS = int(os.environ[COMPUTING_UNITS_VARIABLE_NAME])
else:
    COMPUTING_UNITS = 1
