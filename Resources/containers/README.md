The structure of the container files consists of a directory with the container name, the container file (Dockerfile) and the additional files need to build the container.

```text
<name>
├── Dockerfile
└── <files>
```

Ubuntu 22.04 works for building the images.
We recommend a virtual machine due to the long build times of some of the container images.

```sh
sudo apt-get update
sudo apt-get install --yes buildah
```

Building images

```sh
buildah build --tag "maboss:latest" "maboss/"
```

Pushing images to GitHub container registry

```sh
buildah login ghcr.io -u "permedcoe"  # supply an access token
buildah tag "localhost/maboss:latest" "ghcr.io/permedcoe/maboss:latest"
buildah push "ghcr.io/permedcoe/maboss:latest"
```

Pulling images with Apptainer (or Singularity)

```sh
apptainer pull "maboss-latest.sif" "ghcr.io/permedcoe/maboss:latest"
```


Idea

* We define containers using the Dockerfile format.
* We build OCI compliant containers using Buildah.
* Containers should be compatible with Apptainer.
* We push the container images to GitHub container registry.
* We pull the container images from the GitHub container registry using Apptainer.
* We run the container images using Apptainer on Mahti cluster.

Todo

- Should we merge `meta_analysis` into `toolset`? Both contains bunch of R dependencies.
- We should move all assets to under BuildingBlocks assets instead of the container directory
- Lock versions for dependencies
    - apt-get
    - pip (`pip freeze > requirements-freeze.txt`)
    - conda (`mamba env export --name <env> > env.lock`)
    - R installs
    - wget
- For each containers, add
    - version (for tag)
    - readme
    - license
    - tests
    - examples
- We should reduce image sizes and remove unnecessary files after builds.
- Containers should load specific dependencies from the @permedcoe GitHub team.
- We should avoid having to build dependencies more than once (e.g. MaBoSS, R dependencies).
    * Can we use precompiled binaries to speed things up?
- Can we make one container available from another container to avoid having to place the build the same software in multiple containers and to decouple dependencies.
- Can we decouple application in containers with more than one application?
- Check the licenses for the dependecies.
- We will move the contents of this repository to `github.com/permedcoe/BuildingBlocks/containers` when they are ready.
- Create base images for containers?


Done

- Try Buildah (or Podman) for building OCI compliant containers instead of Docker.
    - Seems to work!
- Change base image to latest ubuntu version if possible.

Resources

- https://devhints.io/bash
- https://jcristharif.com/conda-docker-tips.html
- https://cloud.r-project.org/bin/linux/ubuntu/
- https://github.com/conda-forge/miniforge-images
