[![Build Status](https://travis-ci.org/lasote/conan-zlib.svg)](https://travis-ci.org/lasote/conan-zlib)
[![Build Status](https://ci.appveyor.com/api/projects/status/github/lasote/conan-zlib)](https://ci.appveyor.com/project/lasote/conan-zlib)


^^^ TODO: Change these images to the ones pointing to CI

# conan-pistache


[Conan](https://bintray.com/conan-community/conan/pistache%3Aconan) package for Pistache library.


## Basic setup

    $ conan install pistache/d5608a1@conan/stable
    
## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    pistache/d5608a1@conan/stable

    [options]
    pistache:shared=True # False
    
    [generators]
    cmake

Complete the installation of requirements for your project running:

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.cmake* with all the 
paths and variables that you need to link with your dependencies.
