[![Build Status](https://travis-ci.org/conan-community/conan-pistache.svg?branch=release%2Fd5608a1)](https://travis-ci.org/conan-community/conan-pistache)


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
