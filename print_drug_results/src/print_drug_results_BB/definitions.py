import os

# Assets folder within the Building Block
PRINT_DRUG_RESULTS_ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# Container definition for Print Drug Results Building Block
try:
    CONTAINER_PATH = os.environ["PERMEDCOE_IMAGES"]
except KeyError:
    # Within the container when running with PyCOMPSs
    CONTAINER_PATH = "./"
PRINT_DRUG_RESULTS_CONTAINER = CONTAINER_PATH + "printResults.sif"

# Computing units
COMPUTING_UNITS_VARIABLE_NAME = "COMPUTING_UNITS"
if COMPUTING_UNITS_VARIABLE_NAME in os.environ:
    COMPUTING_UNITS = int(os.environ[COMPUTING_UNITS_VARIABLE_NAME])
else:
    COMPUTING_UNITS = 1
