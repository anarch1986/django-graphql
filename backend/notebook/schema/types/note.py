import graphene
from graphene_django import DjangoObjectType

from ..schema_util import authenticated
from ...models import Note
from ...models import Category


class NoteType(DjangoObjectType):
    class Meta:
        model = Note
        fields = ("id", "title", "text", "status", "category")

    def find_all_notes(fields):
        if 'category' in fields:
            return Note.objects.select_related("category").all()
        else:
            return Note.objects.all()

    def get_note_by_id(id):
        try:
            return Note.objects.get(pk=id)
        except Note.DoesNotExist:
            return None

    def get_note_by_title(title):
        try:
            return Note.objects.get(title=title)
        except Note.DoesNotExist:
            return None


class CreateNote(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        text = graphene.String(required=False)
        category = graphene.ID(required=False)

    note = graphene.Field(NoteType)

    @authenticated
    def mutate(root, info, title, text=None, category=None):
        title = title.strip()
        if len(title) <= 0:
            raise Exception("Title is not valid")
        if category:
            category = Category.objects.get(pk=category)
        else:
            raise Exception("Missing category.")
        note = Note.objects.create(title=title, text=text, category=category)
        note.save()
        return CreateNote(note=note)


class UpdateNote(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        text = graphene.String(required=False)
        category = graphene.ID(required=False)

    note = graphene.Field(NoteType)

    @authenticated
    def mutate(root, info, id, title, text=None, category=None):
        note = Note.objects.get(pk=id)
        title = title.strip()
        if len(title) <= 0:
            raise Exception("Title is not valid")
        note.title = title
        note.text = text
        if category:
            category = Category.objects.get(pk=category)
        else:
            raise Exception("Missing category.")
        note.category = category
        return UpdateNote(note=note)


class DeleteNote(graphene.Mutation):
    id = graphene.ID()
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    @authenticated
    def mutate(root, info, id):
        note = Note.objects.get(pk=id)
        note.delete()
        return DeleteNote(id=id, ok=True)
