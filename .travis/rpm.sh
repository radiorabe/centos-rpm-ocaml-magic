#!/bin/bash
#
# RPM build wrapper for ocaml-magic, runs inside the build container on travis-ci

set -xe

chown root:root ocaml-magic.spec

build-rpm-package.sh ocaml-magic.spec
