from five import grok
from Acquisition import aq_inner
from zope.interface import Interface
from Products.CMFCore.utils import getToolByName

from plone.app.layout.viewlets.interfaces import IPortalHeader
from plone.app.layout.navigation.interfaces import INavigationRoot

from comrat.sitecontent.banner import IBanner


class BannerViewlet(grok.Viewlet):
    grok.name('comrat.sitecontent.BannerViewlet')
    grok.context(INavigationRoot)
    grok.require('zope2.View')
    grok.viewletmanager(IPortalHeader)

    def update(self):
        context = aq_inner(self.context)
        self.context_url = context.absolute_url()
        self.has_banners = len(self.banners()) > 0

    def banners(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(object_provides=IBanner.__identifier__,
                          sort_on='getObjPositionInParent',
                          review_state='published')
        return results
