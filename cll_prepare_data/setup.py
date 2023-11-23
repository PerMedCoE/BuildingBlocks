# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="cll_prepare_data",
    version="0.0.1",
    description="This package provides the cll_prepare_data Building Block",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="TO_BE_DEFINED",
    author="Author",
    author_email="author@example.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Operating System :: Unix",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    keywords="BuildingBlock, cll_prepare_data",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6, <4",
    install_requires=["permedcoe>=0.0.8"],
    extras_require={
        "dev": ["check-manifest"],
    },
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    package_data={
        "cll_prepare_data": ["assets/*",
                     "definition.json"],
    },
    entry_points={
        "console_scripts": [
            "cll_prepare_data=cll_prepare_data.__main__:main",
        ],
    },
    project_urls={
        "Bug Reports": "TO_BE_DEFINED",
        "Source": "TO_BE_DEFINED",
    },
)
