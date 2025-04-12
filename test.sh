#!/bin/sh

set -e

echo "Resetting."
conan remove useless* -c
rm -rf a/build
rm -rf b/build

echo "Exporting pkg a"
conan export a/

cd b

echo "Install pkg b dependencies"
conan install . --build missing -s build_type=Debug

echo "Configure. This will succeed."
cmake --preset conan-debug

echo "Calling install for pkg b again"
conan install . --build missing -s build_type=Debug

echo "Configure again. This will fail."
cmake --preset conan-debug

