import graphene

import json
from graphene_django import DjangoObjectType

from ..schema_util import authenticated
from ...models import Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "notes")

    def find_all_categories():
        return Category.objects.all()

    def get_category_by_id(id):
        try:
            return Category.objects.get(pk=id)
        except Category.DoesNotExist:
            return None

    def get_category_by_name(name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    category = graphene.Field(CategoryType)

    @authenticated
    def mutate(root, info, name):
        try:
            category = Category.objects.get(name__iexact=name)
            raise Exception("A category with this name is already exists.")
        except Category.DoesNotExist:
            name = name.strip()
            if len(name) <= 0:
                raise Exception("Category name is not valid")
            category = Category.objects.create(name=name)
            category.save()
            return CreateCategory(category=category)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @authenticated
    def mutate(root, info, id, name):
        category = Category.objects.get(pk=id)
        try:
            existing_name_category = Category.objects.get(name__iexact=name)
            raise Exception("A category with this name is already exists.")
        except Category.DoesNotExist:
            name = name.strip()
            if len(name) <= 0:
                raise Exception("Category name is not valid")
            category.name = name
            category.save()
            return UpdateCategory(category=category)


class DeleteCategory(graphene.Mutation):
    id = graphene.ID()
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    @authenticated
    def mutate(root, info, id):
        category = Category.objects.get(pk=id)
        category.delete()
        return DeleteCategory(id=id, ok=True)
