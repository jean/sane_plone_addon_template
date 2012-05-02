""" Plone views overrides.

	For more information see

	* http://collective-docs.readthedocs.org/en/latest/views/browserviews.html

"""

# Zope imports
from zope.interface import Interface
from five import grok

# Plone imports
from Products.CMFCore.interfaces import ISiteRoot

# Local imports
from interfaces	import IThemeSpecific

grok.templatedir("templates")
grok.layer(IThemeSpecific)

# EXAMPLES START

class HelloWorld(grok.View):
	"""
	Example view rendering a Plone page in the default Plone framing.
	
	Automatically associates itself with ``helloworld.pt`` templates.
	Make this view available only in Plone site root.

	http://localhost:8080/Plone/@@helloworld
	"""

    # use grok.context(Interface) to associate view with every content item
    # instead
	grok.context(ISiteRoot)

# EXAMPLES END
