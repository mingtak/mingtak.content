from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.indexer.decorator import indexer
from zope.component.hooks import getSite
from mingtak.content import MessageFactory as _


class IThemeDemo(form.Schema, IImageScaleTraversable):

    themeId = schema.TextLine(
        title=_(u'Theme Id'),
        description=_(u'Theme id, a unique identifier'),
        required=True,
    )

    specification = RichText(
        title=_(u'Specification'),
        description=_(u'Specification description'),
        required=True,
    )

    demoURL = schema.URI(
        title=_(u'Demo site URL'),
        description=_(u'The theme site URL'),
        required=True,
    )

    captureImage = NamedBlobImage(
        title=_(u'Capture Image'),
        description=_(u'The demo site capture image, please upload full size image, must be w:h=1:2'),
        required=True,
    )

    @invariant
    def validateThemeId(data):
        site = getSite()
        catalog = site.portal_catalog
        if not hasattr(data.__context__, 'id'):
            if len(catalog(themeId=data.themeId)) > 0:
                raise Invalid(_(u'Theme Id already in use.'))
            else:
                return
        objectId = data.__context__.id
        if len(catalog(themeId=data.themeId)) > 0 and len(catalog({'id':objectId, 'themeId':data.themeId})) == 0:
            raise Invalid(_(u'Theme Id already in use.'))


@indexer(IThemeDemo)
def themeId_indexer(obj):
     return obj.themeId
grok.global_adapter(themeId_indexer, name='themeId')
 

class ThemeDemo(Container):
    grok.implements(IThemeDemo)


class SampleView(grok.View):

    grok.context(IThemeDemo)
    grok.require('zope2.View')

    grok.name('view')
