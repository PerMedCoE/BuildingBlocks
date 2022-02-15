import os

# Assets folder for Print Drug Results Building Block
ASSETS_PATH = os.environ["PERMEDCOE_ASSETS"]
PRINT_DRUG_RESULTS_ASSETS = os.path.join(ASSETS_PATH, "print_drug_results")

# Container definition for Print Drug Results Building Block
CONTAINER_PATH = os.environ["PERMEDCOE_IMAGES"]
PRINT_DRUG_RESULTS_CONTAINER = CONTAINER_PATH + "printResults.sif"

# Computing units
COMPUTING_UNITS_VARIABLE_NAME = "COMPUTING_UNITS"
if COMPUTING_UNITS_VARIABLE_NAME in os.environ:
    COMPUTING_UNITS = int(os.environ[COMPUTING_UNITS_VARIABLE_NAME])
else:
    COMPUTING_UNITS = 1
