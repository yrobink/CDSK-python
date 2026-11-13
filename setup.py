# -*- coding: utf-8 -*-

## Copyright(c) 2021 Yoann Robin
## 
## This file is part of CDSK.
## 
## CDSK is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## CDSK is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with CDSK.  If not, see <https://www.gnu.org/licenses/>.

##############
## Packages ##
##############

import setuptools
from setuptools import setup
from pathlib import Path

########################
## Infos from release ##
########################

cpath = Path(__file__).parent
release: dict[str,str] = {}
exec( (cpath / "CDSK" / "__release.py").read_text() , {} , release )
long_description = (cpath / "README.md").read_text()

## Required elements
requires         = [ "numpy",
                     "scipy",
                     "matplotlib",
                     "scikit-learn",
                     "SDFC (>=0.5.0)"]
list_packages = setuptools.find_packages()
package_dir   = { "CDSK" : "CDSK" }


#######################
## And now the setup ##
#######################


setup(
    name         = release['name'],
    description  = release['description'],
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    version      = release['version'],
    author       = release['author'],
    author_email = release['author_email'],
    license      = release['license'],
    platforms        = [ "linux" , "macosx" ],
    classifiers      = [
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    install_requires = requires,
    zip_safe         = False,
    packages         = list_packages,
    package_dir      = package_dir
)
