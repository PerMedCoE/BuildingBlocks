import os
from permedcoe.bb import CONTAINER_PATH
from permedcoe.bb import COMPUTING_UNITS

# Assets folder within the Building Block
MABOSS_ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# Container definition for MaBoSS Building Block
MABOSS_CONTAINER = CONTAINER_PATH + "MaBoSS.sif"
MABOSS_SENSITIVITY_CONTAINER = CONTAINER_PATH + "MaBoSS_sensitivity.sif"
