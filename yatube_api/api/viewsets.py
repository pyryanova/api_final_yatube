from rest_framework import viewsets, mixins


class CreateGetListViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    pass
