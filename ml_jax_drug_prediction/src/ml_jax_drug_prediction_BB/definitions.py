import os
from permedcoe.bb import CONTAINER_PATH

# Assets folder within the Building Block
ML_JAX_DRUG_PREDICTION_ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# Container definition for Carnival Building Block
ML_JAX_DRUG_PREDICTION_CONTAINER = CONTAINER_PATH + "tf-jax.sif"

# Computing units
COMPUTING_UNITS_VARIABLE_NAME = "COMPUTING_UNITS"
if COMPUTING_UNITS_VARIABLE_NAME in os.environ:
    COMPUTING_UNITS = int(os.environ[COMPUTING_UNITS_VARIABLE_NAME])
else:
    COMPUTING_UNITS = 1
