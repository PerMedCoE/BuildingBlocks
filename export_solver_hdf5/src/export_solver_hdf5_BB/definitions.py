import os
from permedcoe.bb import CONTAINER_PATH
from permedcoe.bb import COMPUTING_UNITS

# Do not change this line
BB_SOURCE_PATH=os.path.dirname(os.path.abspath(__file__))

# Update the following lines:
#  - Assets folder within the Building Block
EXPORT_SOLVER_HDF5_ASSETS_PATH = os.path.join(BB_SOURCE_PATH, "assets")
#  - Container definition for Export Solver HDF5 Building Block
EXPORT_SOLVER_HDF5_CONTAINER = CONTAINER_PATH + "toolset.sif"
