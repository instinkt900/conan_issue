from conan import ConanFile
from conan.tools.cmake import cmake_layout

class UselessB(ConanFile):
    name = "useless_b"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("useless_a/0.1");

    def build_requirements(self):
        self.tool_requires("cmake/3.27.9")

    def layout(self):
        cmake_layout(self)

