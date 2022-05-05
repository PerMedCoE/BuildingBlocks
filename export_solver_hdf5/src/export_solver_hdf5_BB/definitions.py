import os

# Assets folder within the Building Block
EXPORT_SOLVER_HDF5_ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# Container definition for Export Solver HDF5 Building Block
CONTAINER_PATH = os.environ["PERMEDCOE_IMAGES"]
EXPORT_SOLVER_HDF5_CONTAINER = CONTAINER_PATH + "toolset.sif"

# Computing units
COMPUTING_UNITS_VARIABLE_NAME = "COMPUTING_UNITS"
if COMPUTING_UNITS_VARIABLE_NAME in os.environ:
    COMPUTING_UNITS = int(os.environ[COMPUTING_UNITS_VARIABLE_NAME])
else:
    COMPUTING_UNITS = 1
