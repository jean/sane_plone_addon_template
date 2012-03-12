"""

    Declare a Python package yourtheme

    See 

    * http://wiki.python.org/moin/Distutils/Tutorial

    * http://packages.python.org/distribute/setuptools.html#developer-s-

    * http://plone.org/products/plone/roadmap/247

"""

from distutils.core import setup

setup(name = "yourtheme",
    version = "0.0",
    description = "A Plone theme",
    author = "",
    author_email = "",
    url = "",
    install_requires = ["five.grok"],
    packages = ['yourtheme'],
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