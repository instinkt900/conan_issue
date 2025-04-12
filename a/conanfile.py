from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMake
from conan.tools.files import load

class UselessA(ConanFile):
    name = "useless_a"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"
    exports_sources = "CMakeLists.txt", "include/*", "src/*"
    version = "0.1"

    def requirements(self):
        self.requires("vulkan-headers/1.3.243.0")
        self.requires("vulkan-loader/1.3.243.0")
        self.requires("vulkan-memory-allocator/3.0.1")

    def build_requirements(self):
        self.tool_requires("cmake/3.27.9")

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

