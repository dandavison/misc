from rest_framework.serializers import Serializer, CharField


class ChildSerializer(Serializer):
    myfield = CharField()

    def __init__(self, *args, **kwargs):
        __import__('pdb').set_trace()
        # I would like to access the parent serializer instance at this point
        super().__init__(*args, **kwargs)


class ParentSerializer(Serializer):
    children = ChildSerializer(many=True)


class Child:
    def __init__(self):
        self.myfield = "myfield val"


class Parent:
    def __init__(self):
        self.children = [Child()]


ParentSerializer(Parent())
