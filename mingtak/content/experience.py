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


from mingtak.content import MessageFactory as _


class IExperience(form.Schema, IImageScaleTraversable):

    siteUrl = schema.URI(
        title=_(u'site url'),
        description=_(u'usite url, must includeing string http://.'),
        required=False,
    )

    detail = RichText(
        title=_(u'detail description'),
        description=_(u'Text block, detail more information'),
        required=True,
    )

    miniImage = NamedBlobImage(
        title=_(u'website capture image, w:h must be 2:1'),
        description=_(u'Website capture image, please upload, w:h=2:1.'),
        required=True,
    )

    image = NamedBlobImage(
        title=_(u'website capture image'),
        description=_(u'Website capture image, please upload full size.'),
        required=True,
    )



class Experience(Container):
    grok.implements(IExperience)


class SampleView(grok.View):
    grok.context(IExperience)
    grok.require('zope2.View')
    grok.name('view')
