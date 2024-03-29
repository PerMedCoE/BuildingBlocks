"""
NOTE: Do not modify this file unless you want to change the name
      of the main.py file. Then it is necessary to adapt the import.
"""

import os
from permedcoe import invoker
from COBREXA_FVA.main import invoke
from COBREXA_FVA.definitions import ASSETS_PATH
from COBREXA_FVA.definitions import BB_SOURCE_PATH


def main():
    invoker(invoke,
            os.path.join(BB_SOURCE_PATH, "definition.json"),
            assets_path=ASSETS_PATH)


if __name__ == "__main__":
    main()
