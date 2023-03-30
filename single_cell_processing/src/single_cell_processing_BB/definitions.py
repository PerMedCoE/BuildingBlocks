import os
from permedcoe.bb import CONTAINER_PATH
from permedcoe.bb import COMPUTING_UNITS

# Do not change this line
BB_SOURCE_PATH=os.path.dirname(os.path.abspath(__file__))

# Update the following lines:
#  - Assets folder within the Building Block
ASSETS_PATH = os.path.join(BB_SOURCE_PATH, "assets")
#  - Container definition for Meta Analysis Building Block
CONTAINER = "single_cell.sif"
SINGLE_CELL_PROCESSING_CONTAINER = os.path.join(CONTAINER_PATH, CONTAINER)
