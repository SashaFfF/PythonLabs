import re
import inspect
import types

from constants import CODE_ATTRIBUTES, OBJECT_ATTRIBUTES, BASE_TYPES, BASE_COLLECTIONS


class Serializer:

    def get_type_of_obj(self, obj):
        return re.search(r"\'(\w+)\'", str(type(obj)))[1]

    # def serialize_type_function(self, obj):
    #     res = {}
    #     arguments = {}
    #
    #     res["__name__"] = obj.__name__



    def serializer(self, obj):

        res={}

        if isinstance(obj, (int, float, bool, str)):
            res["type"] = self.get_type_of_obj(obj)
            res["value"] = obj

        elif isinstance(obj, (list, tuple, set, frozenset)):
            res["type"] = self.get_type_of_obj(obj)
            ser_object = []

            for value in obj:
                ser_object.append(self.serializer(value))

            res["value"] = ser_object

        elif isinstance(obj, types.CellType):
            res["type"] = "cell"
            res["value"] = self.serializer(obj.cell_contents)


class Deserializer:

    def deserialize_base_types(self, type_obj, obj):

        if type_obj == "int":
            return int(obj)

        elif type_obj == "float":
            return float(obj)

        elif type_obj == "bool":
            return bool(obj)

        elif type_obj == "str":
            return str(obj)

    def deserialize_base_collection(self, type_obj, obj):

        if type_obj == "list":
            return list(self.deserialize(elem) for elem in obj)

        elif type_obj == "tuple":
            return tuple(self.deserialize(elem) for elem in obj)

        elif type_obj == "set":
            return set(self.deserialize(elem) for elem in obj)

        elif type_obj == "frozenset":
            return frozenset(self.deserialize(elem) for elem in obj)

    def deserialize(self, obj):

        if obj["type"] in BASE_TYPES:
            return self.deserialize_base_types(obj["type"], obj["value"])

        elif obj["type"] in BASE_COLLECTIONS:
            return self.deserialize_base_collection(obj["type"], obj["value"])

        elif obj["type"] == "dict":
            return self.deserialize_base_collection("list", obj["value"])

        elif obj["type"] == "cell":
            return types.CellType(self.deserialize(obj["value"]))
        
