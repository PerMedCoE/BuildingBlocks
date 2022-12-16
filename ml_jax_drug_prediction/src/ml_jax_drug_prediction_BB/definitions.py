import os
from permedcoe.bb import CONTAINER_PATH
from permedcoe.bb import COMPUTING_UNITS

# Assets folder within the Building Block
ML_JAX_DRUG_PREDICTION_ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# Container definition for Carnival Building Block
ML_JAX_DRUG_PREDICTION_CONTAINER = CONTAINER_PATH + "tf-jax.sif"
