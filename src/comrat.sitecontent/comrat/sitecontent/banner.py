from five import grok
from plone.directives import dexterity, form

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedBlobImage

from comrat.sitecontent import MessageFactory as _


# Interface class; used to define content-type schema.

class IBanner(form.Schema, IImageScaleTraversable):
    """
    A configurable image banner for galleries
    """
    image = NamedBlobImage(
        title=_(u"Banner Image"),
        description=_(u"Upload banner image ideally already resized"),
        required=True,
    )


class Banner(dexterity.Item):
    grok.implements(IBanner)


class View(grok.View):
    grok.context(IBanner)
    grok.require('zope2.View')
    grok.name('view')
