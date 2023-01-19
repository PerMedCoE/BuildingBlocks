import os
from permedcoe.bb import CONTAINER_PATH
from permedcoe.bb import COMPUTING_UNITS

# Do not change this line
BB_SOURCE_PATH=os.path.dirname(os.path.abspath(__file__))

# Update the following lines:
#  - Assets folder within the Building Block
COBREXA_ASSETS_PATH = os.path.join(BB_SOURCE_PATH, "assets")
#  - Container definition for COBREXA Building Block
COBREXA_CONTAINER = CONTAINER_PATH + "cobrexa.jl_latest.sif"
