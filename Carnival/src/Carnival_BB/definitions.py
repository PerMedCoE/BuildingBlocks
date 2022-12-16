import os
from permedcoe.bb import CONTAINER_PATH

# Container definition for Carnival Building Block
CARNIVAL_CONTAINER = CONTAINER_PATH + "signaling-solvers.sif"

# Computing units
COMPUTING_UNITS_VARIABLE_NAME = "COMPUTING_UNITS"
if COMPUTING_UNITS_VARIABLE_NAME in os.environ:
    COMPUTING_UNITS = int(os.environ[COMPUTING_UNITS_VARIABLE_NAME])
else:
    COMPUTING_UNITS = 1
