import os

# Container definition for Carnival Building Block
CONTAINER_PATH = os.environ["PERMEDCOE_IMAGES"]
ML_JAX_DRUG_PREDICTION_CONTAINER = CONTAINER_PATH + "tf-jax.sif"

# Computing units
COMPUTING_UNITS_VARIABLE_NAME = "COMPUTING_UNITS"
if COMPUTING_UNITS_VARIABLE_NAME in os.environ:
    COMPUTING_UNITS = int(os.environ[COMPUTING_UNITS_VARIABLE_NAME])
else:
    COMPUTING_UNITS = 1
