"""

    Declare a Python package youraddon

    See 

    * http://wiki.python.org/moin/Distutils/Tutorial

    * http://packages.python.org/distribute/setuptools.html#developer-s-guide

    * http://plone.org/products/plone/roadmap/247

"""

from setuptools import setup

setup(name = "youraddon",
    version = "0.0",
    description = "A Plone theme",
    author = "",
    author_email = "",
    url = "",
    install_requires = ["five.grok", "z3c.jbot"],
    packages = ['youraddon'],
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],     
    license="GPL2",
    include_package_data = True,
    entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,        
) 
