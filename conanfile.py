
import os
from conans import ConanFile, CMake, tools
from conans.errors import ConanException


class PistacheConan(ConanFile):
    name = "pistache"
    version = "d5608a1"
    license = "Apache License 2.0"
    url = "https://github.com/conan-community/conan-pistache.git"
    description = "A high-performance REST Toolkit written in C++"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"
    generators = "cmake"

    @property
    def src_folder(self):
        return "{}-{}".format(self.name, self.version)

    def configure(self):
        if self.settings.os != "Linux":
            raise ConanException("Only Linux supported")

    def source(self):
        git = tools.Git(folder=self.src_folder)
        git.clone("https://github.com/oktal/pistache.git", "master")
        git.checkout(element=self.version)
        tools.replace_in_file(os.path.join(self.src_folder, 'CMakeLists.txt'), 'project (pistache)',
            """project (pistache)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
""")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["PISTACHE_BUILD_TESTS"] = False
        cmake.definitions["PISTACHE_BUILD_EXAMPLES"] = False
        cmake.configure(source_folder=self.src_folder)
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["pistache", "atomic", ]
        self.cpp_info.cppflags = ["-pthread", ]

