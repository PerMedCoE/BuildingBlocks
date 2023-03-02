#!/usr/bin/env bash
build() {
    TAG=$1
    DIR=$2
    buildah build --tag "$TAG" "$DIR"
}

push() {
    TAG=$1
    OWNER=${2:-"permedcoe"}
    buildah tag "localhost/$TAG" "ghcr.io/$OWNER/$TAG"
    buildah push "ghcr.io/$OWNER/$TAG"
}

pull() {
    TAG=$1
    OWNER=${2:-"permedcoe"}
    FILE_SIF=${3:-"$(echo "$TAG" | tr ':' '-').sif"}
    apptainer pull "$FILE_SIF" "docker://ghcr.io/$OWNER/$TAG"
}

# Pass the arguments
case $1 in
    (build)
        shift
        build "$@"
        ;;
    (push)
        shift
        push "$@"
        ;;
    (pull)
        shift
        pull "$@"
        ;;
    (*) exit 1 ;;
esac

