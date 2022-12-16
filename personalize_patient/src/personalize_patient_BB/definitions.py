import os
from permedcoe.bb import CONTAINER_PATH
from permedcoe.bb import COMPUTING_UNITS

# Assets folder within the Building Block
PERSONALIZE_PATIENT_ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# Container definition for Meta Analysis Building Block
PERSONALIZE_PATIENT_CONTAINER = CONTAINER_PATH + "PhysiCell-COVID19.sif"
