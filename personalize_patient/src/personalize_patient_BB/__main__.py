"""
NOTE: Do not modify this file unless you want to change the name
      of the main.py file. Then it is necessary to adapt the import.
"""

import os
from permedcoe import invoker
from personalize_patient_BB.main import invoke
from personalize_patient_BB.definitions import BB_SOURCE_PATH


def main():
    invoker(invoke, os.path.join(BB_SOURCE_PATH, "definition.json"))


if __name__ == "__main__":
    main()
