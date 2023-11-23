# Building Block cll_tf_activities

This package provides the cll_tf_activities **Building Block (BB)** using the **HPC/Exascale Centre of Excellence in Personalised Medicine**
([PerMedCoE](https://permedcoe.eu/)) base Building Block.

## Table of Contents

- [Building Block cll_tf_activities](#building-block-new_name)
  - [Table of Contents](#table-of-contents)
  - [User instructions](#user-instructions)
    - [Requirements](#requirements)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Uninstall](#uninstall)
  - [Developer instructions](#developer-instructions)
    - [Building block](#building-block)
    - [Best practices](#best-practices)
  - [License](#license)
  - [Contact](#contact)

## User instructions

### Requirements

- Python >= 3.6
- Singularity

### Installation

To install from source code:

```bash
./install.sh
```

Once the package is uploaded to Pypi, it can be installed as usual Pypi packages:

```bash
pip install cll_tf_activities
```

### Usage

The `cll_tf_activities` package provides a clear interface that allows it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and Snakemake).

- Command line interface:

    Once installed the `cll_tf_activities` package, it provides the `cll_tf_activities`
    command, that can be used from the command line. For example:

    ```text
    $ cll_tf_activities -h
    usage: cll_tf_activities [-h] --model MODEL --result RESULT [-c CONFIG] [-d] [-l {debug,info,warning,error,critical}] [--tmpdir TMPDIR] [--processes PROCESSES] [--gpus GPUS] [--memory MEMORY]
                [--mount_points MOUNT_POINTS]

    cll_tf_activities Building Block short description. Give more details about the Building Block.

    options:
      -h, --help            show this help message and exit
      --model MODEL         (INPUT - str (file)) Input file (model)
      --result RESULT       (OUTPUT - str) Result file
      -c CONFIG, --config CONFIG
                            (CONFIG) Configuration file path
      -d, --debug           Enable Building Block debug mode. Overrides log_level
      -l {debug,info,warning,error,critical}, --log_level {debug,info,warning,error,critical}
                            Set logging level
      --tmpdir TMPDIR       Temp directory to be mounted in the container
      --processes PROCESSES
                            Number of processes for MPI executions
      --gpus GPUS           Requirements for GPU jobs
      --memory MEMORY       Memory requirement
      --mount_points MOUNT_POINTS
                            Comma separated alias:folder to be mounted in the container
    ```

    This interface can be used within any workflow manager that requires binaries (e.g. NextFlow and Snakemake).

    In addition, any building block requires to have a function being called from the `__main__`, so that it can also be invoked from Python scripts. This allows to use the BB from PyCOMPSs seamlessly.

    ```python
    from cll_tf_activities import invoke

    invoke(arguments, config)
    ```

- Extension for PyCOMPSs:

    Moreover, a BB can also implement a Python function not limited to the input (file or directory), output (file or directory) and config (yaml file) signature. This enables application developers to use the BB with PyCOMPSs using Python objects instead of files among BBs.

    ```python
    from cll_tf_activities import cll_tf_activities_extended

    cll_tf_activities_extended(*args, **kwargs)  # specific interface
    ```

### Uninstall

Uninstall can be done as usual `pip` packages:

```bash
pip uninstall cll_tf_activities
```

or more specifically:

```bash
./uninstall.sh
./clean.sh
```

## Developer instructions

### Building block

There are a set of rules to implement a PerMedCoE compliant Building Block:

- Complete `definition.json` file with the Building Block required parameters.
  - Declare inputs and outputs.
- Complete `definitions.py` with the appropriate container file name.
  - Define the container/s within `definitions.py` file (`CONTAINER` variable).
- Provide a Python script `main.py` with the following structure and adapt to your needs (check all `ToDo` marked lines):

  ```Python
  # Decorator imports
  from permedcoe import constraint       # To define constraints needs (e.g. number of cores)
  from permedcoe import container        # To define container related needs
  from permedcoe import binary           # To define binary to execute related needs
  from permedcoe import mpi              # To define an mpi binary to execute related needs (can not be used with @binary)
  from permedcoe import task             # To define task related needs
  # @task supported types
  from permedcoe import FILE_IN          # To define file type and direction
  from permedcoe import FILE_OUT         # To define file type and direction
  from permedcoe import FILE_INOUT       # To define file type and direction
  from permedcoe import DIRECTORY_IN     # To define directory type and direction
  from permedcoe import DIRECTORY_OUT    # To define directory type and direction
  from permedcoe import DIRECTORY_INOUT  # To define directory type and direction
  # Other permedcoe available functionalities
  from permedcoe import Arguments        # Arguments definition
  from permedcoe import get_environment  # Get variables from invocation (tmpdir, processes, gpus, memory)
  from permedcoe import TMPDIR           # Default tmpdir key

  # Import single container and assets definitions
  from cll_tf_activities.definitions import cll_tf_activities_ASSETS_PATH  # binary could be in this folder
  from cll_tf_activities.definitions import cll_tf_activities_CONTAINER
  from cll_tf_activities.definitions import COMPUTING_UNITS

  def function_name(*args, **kwargs):
      """Extended python interface:
      To be used only with PyCOMPSs - Enables to define a workflow within the building block.
      Tasks are not forced to be binaries: PyCOMPSs supports tasks that are pure python code.

      # PyCOMPSs help: https://pycompss.readthedocs.io/en/latest/Sections/02_App_Development/02_Python.html

      Requirement: all tasks should be executed in a container (with the same container definition)
                   to ensure that they all have the same requirements.
      """
      print("Building Block entry point to be used with PyCOMPSs")
      # ToDo: (optional) Pure python code calling to PyCOMPSs tasks (that can be defined in this file or in another).

  @container(engine="SINGULARITY", image=cll_tf_activities_CONTAINER)
  @binary(binary="cp")                                        # ToDo: Define the binary to be used (can be within cll_tf_activities_ASSETS_PATH (e.g. my_binary.sh)).
  @task(input_file=FILE_IN, output_file=FILE_OUT)             # ToDo: Define the inputs and output parameters.
  def building_block_task(                                    # ToDo: Define a representative task name.
      input_file=None,                                        # ToDo: Define the binary parameters.
      output_file=None,                                       # ToDo: Define the binary parameters.
      verbose="-v"):                                          # ToDo: Define the binary parameters.
      # ToDo: Add tmpdir=TMPDIR if the tmpdir will be used by the asset script.
      """Summary.

      The Definition is equal to:
         cp <input_file> <output_file> -v
      Empty function since it represents a binary execution:

      :param input_file: Input file description, defaults to None
      :type input_file: str, optional
      :param verbose: Verbose description, defaults to "-v"
      :type verbose: str, optional
      # :param tmpdir: Temporary directory, defaults to TMPDIR
      # :type tmpdir: str, optional
      """
      pass

  def invoke(arguments, config):
      """Common interface.

      Args:
          arguments (args): Building Block parsed arguments.
          config (dict): Configuration dictionary.
      Returns:
          None
      """
      # ToDo: Define the arguments required by the Building Block in definition.json file.

      # ToDo: Declare how to run the binary specification (convert config into building_block_task call).
      # Sample config parameter get:
      #     operation = config["operation"]
      # Then operation can be used to tune the building_block_task parameters or even be a parameter.
      # Sample permedcoe environment get:
      #     env_vars = get_environment()
      # Retrieves the extra flags from permedcoe.
      input_file = arguments.model
      output_file = arguments.result
      # tmpdir = arguments.tmpdir
      building_block_task(input_file=input_file,
                          output_file=output_file)
                          # tmpdir=tmpdir)
  ```

  - Use the decorators provided by `permedcoe` package. They provide the capability to use the BB in various workflow managers transparently. In other words, the BB developer does not have to deal with the peculiarities of the workflow managers.

  - A BB can be a single executable, but it can be a more complex code if the `cll_tf_activities_extended` function is implemented and used with PyCOMPSs.

  - It is necessary to have function (`invoke`) with a specific signature: `(arguments, config)`.

  - The `invoke` function provides the command line interface for
  the BB as shown in the [usage](#usage) section. In addition, it
  parses the Yaml config file and invokes the `cll_tf_activities` function
  with the appropriate parameters.

  - The BB `binary` must be defined with the `@task`, `@binary` and `@container` decorators (`cll_tf_activities_task`). This function needs to declare the binary flags, and it is invoked from the `cll_tf_activities` function.

  - The `@task` decorator must declare the type of the file or directories for the binary invocation. In particular, using the parameter name and `FILE_IN`/`FILE_OUT`/`DIRECTORY_IN`/`DIRECTORY_OUT` to define if the parameter is a file or a directory and if the binary is consuming the file/directory or it is producing it.

  - Uncomment `tmpdir` variable if the binary uses an asset that requires to writting
  permissions. So the asset writes in a controlled temporary directory. Don't forget
  to set `require_tmpdir=True` in `__main__.py` within the `invoker` call.

### Best practices

There are a set of best practices suggested to BB developers:

- Use a code style:
  - [pep8](https://www.python.org/dev/peps/pep-0008/)
  - [black](https://github.com/psf/black)

- Document your Building Block.

## License

Add license.

## Contact

Add your email here.
