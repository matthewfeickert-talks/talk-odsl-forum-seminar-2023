#!/usr/bin/env bash

set -x

docker pull ghcr.io/prefix-dev/pixi:noble

docker system prune -f

# docker build \
#     --file ./examples/pixi_build/Dockerfile \
#     --tag talk-odsl-forum-seminar/pixi-build:debug \
#     .

docker build \
    --file ./examples/pixi_build/uv_Dockerfile \
    --tag talk-odsl-forum-seminar/pixi-build:uv-debug \
    .
