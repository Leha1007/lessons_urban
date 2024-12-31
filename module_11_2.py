import inspect


class InspectClass:

    operand1 = '+'
    operand2 = '-'

    def __init__(self, number, name):
        self._number = number
        self._name = name

    def get_number(self):
        return self._number

    def get_name(self):
        return self._name

insp_cl = InspectClass(34, 'Slava')

def introspection_info(obj):
    type_value = type(obj)
    module_value = inspect.getmodule(obj)
    attr_value = list(obj.__dict__.keys())
    methods_value = [i for i in dir(obj) if inspect.ismethod(i)]

    return {'type': type_value, 'attributes': attr_value, 'methods': methods_value, 'module': module_value}

print(introspection_info(insp_cl))
