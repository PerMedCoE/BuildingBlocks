import os
from permedcoe.bb import CONTAINER_PATH
from permedcoe.bb import COMPUTING_UNITS

# Do not change this line
BB_SOURCE_PATH=os.path.dirname(os.path.abspath(__file__))

# Update the following lines:
#  - Assets folder within the Building Block
MABOSS_ASSETS_PATH = os.path.join(BB_SOURCE_PATH, "assets")
#  - Container definition for MaBoSS Building Block
CONTAINER = ["maboss.sif", "maboss_sensitivity.sif"]
MABOSS_CONTAINER = os.path.join(CONTAINER_PATH, CONTAINER[0])
MABOSS_SENSITIVITY_CONTAINER = os.path.join(CONTAINER_PATH, CONTAINER[1])
