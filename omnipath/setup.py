# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="omnipath_BB",
    version="0.0.1",
    description="This package provides the omnipath Building Block",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PerMedCoE/BuildingBlocks",
    author="PerMedCoE Project",
    author_email="infoPerMedCoE@bsc.es",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License"
        "Intended Audience :: Science/Research"
        "Operating System :: Unix"
        "Operating System :: POSIX :: Linux"
        "Topic :: Scientific/Engineering :: Bio-Informatics"
        "Topic :: Scientific/Engineering :: Medical Science Apps."
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="BuildingBlock, PerMedCoE, omnipath",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6, <4",
    install_requires=["permedcoe>=0.0.6"],
    extras_require={
        "dev": ["check-manifest"],
    },
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    package_data={
        "omnipath_BB": ["assets/*",
                        "definition.json"],
    },
    entry_points={
        "console_scripts": [
            "omnipath_BB=omnipath_BB.__main__:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/PerMedCoE/BuildingBlocks/issues",
        "Source": "https://github.com/PerMedCoE/BuildingBlocks/tree/main/omnipath",
    },
)


