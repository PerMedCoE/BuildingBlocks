import os
from permedcoe.bb import CONTAINER_PATH
from permedcoe.bb import COMPUTING_UNITS

# Assets folder within the Building Block
EXPORT_SOLVER_HDF5_ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# Container definition for Export Solver HDF5 Building Block
EXPORT_SOLVER_HDF5_CONTAINER = CONTAINER_PATH + "toolset.sif"
