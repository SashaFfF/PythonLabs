from json_serializer import JsonSerializer
from xml_serializer import XMLSerializer


class SerializerFactory:

    @staticmethod
    def serializer(name_type:str):

        if name_type.lower() == "json":
            return JsonSerializer()

        elif name_type.lower() == "xml":
            return XMLSerializer()

        else:
            raise  ValueError

        # match name_type.lower():
        #
        #     case "json":
        #         return JsonSerializer()
        #
        #     case "xml":
        #         return XMLSerializer()
        #
        #     case _:
        #         raise ValueError