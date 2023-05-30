import re
import inspect
import types

from constants import CODE_ATTRIBUTES, OBJECT_ATTRIBUTES, BASE_TYPES, BASE_COLLECTIONS


class Serializer:

    def get_type_of_obj(self, obj):
        return re.search(r"\'(\w+)\'", str(type(obj)))[1]

    def get_globals(self, obj, class_object=None):

        res = {}
        globals = obj.__globals__

        for value in obj.__code__.co_names:  # co_names - кортеж имён локальных переменных

            if value in globals:

                if inspect.isclass(globals[value]):
                    if (class_object and obj.__globals__[value != class_object]) or not class_object:
                        res[value] = self.serialize(globals[value])

                elif isinstance(globals[value], types.ModuleType):
                    res["module" + value] = self.serialize(globals[value].__name__)

                elif value != obj.__code__.co_name:  # co_name - имя, с которым этот объект кода был определён
                    res[value] = self.serialize(globals[value])

                else:
                    res[value] = self.serialize(obj.__name__)

        return res

    def serialize_type_function(self, obj, class_object=None):

        res = {}
        arguments = {}
        res["__name__"] = obj.__name__
        res["__globals__"] = self.get_globals(obj, class_object)

        if obj.__closure__:
            res["__closure__"] = self.serialize(obj.__closure__)

        else:
            res["__closure__"] = self.serialize(tuple())

        for (key, value) in inspect.getmembers(obj.__code__):
            if key in CODE_ATTRIBUTES:
                arguments[key] = self.serialize(value)

        res["__code__"] = arguments
        return res

    def serialize_type_object(self, obj):

        res = {}
        res["__class__"] = self.serialize(obj.__class__)  # __class__ - класс, которому принадлежит объект

        fields = {}
        for (key, value) in inspect.getmembers(obj):
            if not inspect.isfunction(value) and not inspect.ismethod(value) and not key.startswith("__"):
                fields[key] = self.serialize(value)

        res["__members__"] = fields
        return res



    def serialize(self, obj):

        res = {}

        if isinstance(obj, (int, float, bool, str)):
            res["type"] = self.get_type_of_obj(obj)
            res["value"] = obj

        elif isinstance(obj, (list, tuple, set, frozenset, bytearray, bytes)):
            res["type"] = self.get_type_of_obj(obj)
            ser_object = []

            for value in obj:
                ser_object.append(self.serialize(value))

            res["value"] = ser_object

        elif isinstance(obj, dict):
            res["type"] = "dict"
            ser_object = []

            for value in obj.items():
                ser_object.append(self.serialize(value))

            res["value"] = ser_object

        elif isinstance(obj, types.CellType):
            res["type"] = "cell"
            res["value"] = self.serialize(obj.cell_contents)

        elif inspect.isfunction(obj):
            res["type"] = "function"
            res["value"] = self.serialize_type_function(obj)

        elif inspect.iscode(obj):
            res["type"] = "code"
            args = dict()

            for (key, value) in inspect.getmembers(obj):
                if key in CODE_ATTRIBUTES:
                    args[key] = self.serialize(value)

            res["value"] = args




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

        elif type_obj == "bytearray":
            return bytearray(self.deserialize(elem) for elem in obj)

        elif type_obj == "bytes":
            return bytes(self.deserialize(elem) for elem in obj)

    def deserialize(self, obj):

        if obj["type"] in BASE_TYPES:
            return self.deserialize_base_types(obj["type"], obj["value"])

        elif obj["type"] in BASE_COLLECTIONS:
            return self.deserialize_base_collection(obj["type"], obj["value"])

        elif obj["type"] == "dict":
            return self.deserialize_base_collection("list", obj["value"])

        elif obj["type"] == "cell":
            return types.CellType(self.deserialize(obj["value"]))
        
