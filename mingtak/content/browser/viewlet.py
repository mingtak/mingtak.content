#-*- coding:utf-8 -*-
from zope.interface import Interface
from five import grok
from plone.app.layout.viewlets.interfaces import IPortalHeader, IAboveContentTitle, IAboveContentBody, IBelowContentBody
#IAboveContentTitle, IBelowContentBody, IAboveContentBody, IBelowContentBody


#設定viewlet介面、pt檔目錄
grok.context(Interface)
grok.templatedir('viewlet_templates')


class MingtakHomeSlider(grok.Viewlet):
    grok.viewletmanager(IPortalHeader)
#下列可再新增viewlet, 可用的interface可查詢 plone.app.layout.viewlets.interfaces


class GoogleAdAboveDocumentBody(grok.Viewlet):
    grok.viewletmanager(IAboveContentBody)


class GoogleAdBelowDocumentBody(grok.Viewlet):
    grok.viewletmanager(IBelowContentBody)
