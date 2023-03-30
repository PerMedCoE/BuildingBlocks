import os
from permedcoe.bb import CONTAINER_PATH
from permedcoe.bb import COMPUTING_UNITS

# Do not change this line
BB_SOURCE_PATH=os.path.dirname(os.path.abspath(__file__))

# Update the following lines:
#  - Assets folder within the Building Block
ASSETS_PATH = None
#  - Container definition for Carnival Building Block
CONTAINER_NAME = "signaling_solvers.sif"
CONTAINER = os.path.join(CONTAINER_PATH, CONTAINER_NAME)
