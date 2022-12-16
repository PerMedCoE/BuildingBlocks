"""
NOTE: Do not modify this file unless you want to change the name
      of the main.py file. Then it is necessary to adapt the import.
"""

from permedcoe import invoker
from tf_enrichment_BB.main import invoke
from tf_enrichment_BB.main import arguments_info


def main():
    invoker(invoke, arguments_info)


if __name__ == "__main__":
    main()
