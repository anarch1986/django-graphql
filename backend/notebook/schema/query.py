from django.conf import settings
import graphene
from graphene_django.debug import DjangoDebug

from .types.category import CategoryType
from .types.note import NoteType
from graphql.utils.ast_to_dict import ast_to_dict
from.schema_util import get_fields, authenticated
from ..models import Category, Note


class Query(graphene.ObjectType):
    if settings.DEBUG == True:
        debug = graphene.Field(DjangoDebug, name='_debug')

    all_notes = graphene.List(NoteType)
    note_by_id = graphene.Field(NoteType, id=graphene.Int(required=True))
    note_by_title = graphene.Field(
        NoteType, title=graphene.String(required=True))

    all_categories = graphene.List(CategoryType)
    category_by_id = graphene.Field(
        CategoryType, id=graphene.Int(required=True))
    category_by_name = graphene.Field(
        CategoryType, name=graphene.String(required=True))

    @authenticated
    def resolve_all_notes(root, info):
        fields = get_fields(info)
        return NoteType.find_all_notes(fields)

    @authenticated
    def resolve_note_by_id(root, info, id):
        return NoteType.get_note_by_id(id)

    @authenticated
    def resolve_note_by_title(root, info, title):
        return NoteType.get_note_by_title(title)

    @authenticated
    def resolve_all_categories(root, info):
        return CategoryType.find_all_categories()

    @authenticated
    def resolve_category_by_id(root, info, id):
        return CategoryType.get_category_by_id(id)

    @authenticated
    def resolve_category_by_name(root, info, name):
        return CategoryType.get_category_by_name(name)
