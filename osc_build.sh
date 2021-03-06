#!/bin/bash
# Build packaing using osc.
set -x
set -e
PACKAGE_NAME=$(basename $(realpath .))
echo "Building for repo $1 package $2"
if [ ! -f ./_service:recompress:tar_scm:${PACKAGE_NAME}*.tar* ]; then
    osc service run
fi
if [[ "$1" == *"Debian"* ]]; then
    osc build --noservice $1 --no-verify $PACKAGE_NAME.dsc | tee __build_$1.log
elif [[ "$1" == *"Ubuntu"* ]]; then
    osc build --noservice $1 --no-verify $PACKAGE_NAME.dsc | tee __build_$1.log
else
    osc build --noservice $1 --no-verify $PACKAGE_NAME.spec  | tee __build_$1.log
fi


