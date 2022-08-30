import graphene
from .types.note import CreateNote, UpdateNote, DeleteNote
from .types.category import CreateCategory, UpdateCategory, DeleteCategory


class Mutation(graphene.ObjectType):
    create_note = CreateNote.Field()
    delete_note = DeleteNote.Field()
    update_note = UpdateNote.Field()

    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()
