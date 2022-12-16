import os
from permedcoe.bb import CONTAINER_PATH
from permedcoe.bb import COMPUTING_UNITS

# Assets folder within the Building Block
PRINT_DRUG_RESULTS_ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# Container definition for Print Drug Results Building Block
PRINT_DRUG_RESULTS_CONTAINER = CONTAINER_PATH + "printResults.sif"
