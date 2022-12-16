import os
from permedcoe.bb import CONTAINER_PATH
from permedcoe.bb import COMPUTING_UNITS

# Assets folder within the Building Block
SINGLE_CELL_ASSETS_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "assets"
)

# Container definition for Meta Analysis Building Block
SINGLE_CELL_PROCESSING_CONTAINER = CONTAINER_PATH + "single_cell.sif"
