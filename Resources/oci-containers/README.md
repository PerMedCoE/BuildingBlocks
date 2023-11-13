# OCI containers
## Structure
The structure of the container files consists of a directory with the container name, the container file (Dockerfile) and the additional files need to build the container.

```text
<name>
├── Dockerfile
└── <files>
```


## Building images
We use Ubuntu 22.04 for building the container images.

```sh
sudo apt-get update
sudo apt-get install --yes buildah
```

We can build the images as follows:

```sh
buildah build --tag <name>:latest <directory>
```

In order to push images the `permedcoe` GitHub packages, we must log in using a personal access token:

```sh
buildah login -u permedcoe ghcr.io  # supply an access token
```

Then, we can push the images to the GitHub container registry by tagging the images and pushing it:

```sh
buildah tag localhost/<name>:latest ghcr.io/permedcoe/<name>:latest
buildah push ghcr.io/permedcoe/<name>:latest
```


## Usage
We can pull images from GitHub container registry using Apptainer as follows:

```sh
apptainer pull <name>.sif docker://ghcr.io/permedcoe/<name>:latest
```

Finally, we can run command using the container:

```sh
apptainer exec <name>.sif <command>
```


## References
- https://devhints.io/bash
- https://jcristharif.com/conda-docker-tips.html
- https://cloud.r-project.org/bin/linux/ubuntu/
- https://github.com/conda-forge/miniforge-images
