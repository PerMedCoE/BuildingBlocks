"""
NOTE: Do not modify this file unless you want to change the name
      of the main.py file. Then it is necessary to adapt the import.
"""

import os
from permedcoe import invoker
from CarnivalPy_BB.main import invoke
from CarnivalPy_BB.definitions import ASSETS_PATH
from CarnivalPy_BB.definitions import BB_SOURCE_PATH


def main():
    invoker(invoke,
            os.path.join(BB_SOURCE_PATH, "definition.json"),
            require_tmpdir=True,
            assets_path=ASSETS_PATH)


if __name__ == "__main__":
    main()
