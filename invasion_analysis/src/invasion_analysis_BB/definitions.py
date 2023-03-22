import os
from permedcoe.bb import CONTAINER_PATH
from permedcoe.bb import COMPUTING_UNITS

# Do not change this line
BB_SOURCE_PATH=os.path.dirname(os.path.abspath(__file__))

# Update the following lines:
#  - Assets folder within the Building Block
INVASION_ANALYSIS_ASSETS_PATH = os.path.join(BB_SOURCE_PATH, "assets")
#  - Container definition for the Invasion Analysis Building Block
CONTAINER = "InvasionAnalysis.sif"
INVASION_ANALYSIS_CONTAINER = os.path.join(CONTAINER_PATH, CONTAINER)
