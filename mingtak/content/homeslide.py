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



class IHomeSlide(form.Schema, IImageScaleTraversable):
    slide_1_Title = schema.TextLine(
        title=_(u'Slide 1 title'),
        required=True,
    )

    slide_1_Image = NamedBlobImage(
        title=_(u'Slide 1 image'),
        required=True,
    )

    slide_1_Text = schema.Text(
        title=_(u'Slide 1 text'),
        required=True,
    )

    slide_1_ButtonText = schema.TextLine(
        title=_(u'Slide 1 button'),
        required=True,
    )

    slide_1_ButtonUrl = schema.URI(
        title=_(u'Slide 1 button url'),
        required=True,
    )

    slide_2_Title = schema.TextLine(
        title=_(u'Slide 2 title'),
        required=True,
    )

    slide_2_Image = NamedBlobImage(
        title=_(u'Slide 2 image'),
        required=True,
    )

    slide_2_Text = schema.Text(
        title=_(u'Slide 2 text'),
        required=True,
    )

    slide_2_ButtonText = schema.TextLine(
        title=_(u'Slide 2 button'),
        required=True,
    )

    slide_2_ButtonUrl = schema.URI(
        title=_(u'Slide 2 button url'),
        required=True,
    )

    slide_3_Title = schema.TextLine(
        title=_(u'Slide 3 title'),
        required=True,
    )

    slide_3_Image = NamedBlobImage(
        title=_(u'Slide 3 image'),
        required=True,
    )

    slide_3_Text = schema.Text(
        title=_(u'Slide 3 text'),
        description=_(u'Please only use li tag, one line one text string'),
        required=True,
    )

    slide_4_Title = schema.TextLine(
        title=_(u'Slide 4 title'),
        required=True,
    )

    slide_4_Image = NamedBlobImage(
        title=_(u'Slide 4 image'),
        required=True,
    )

    slide_4_Text = schema.Text(
        title=_(u'Slide 4 text'),
        required=True,
    )

    slide_4_ButtonText = schema.TextLine(
        title=_(u'Slide 4 button'),
        required=True,
    )

    slide_4_ButtonUrl = schema.URI(
        title=_(u'Slide 4 button url'),
        required=True,
    )


class HomeSlide(Container):
    grok.implements(IHomeSlide)


class SampleView(grok.View):
    """ sample view class """

    grok.context(IHomeSlide)
    grok.require('zope2.View')

    #grok.name('view')
