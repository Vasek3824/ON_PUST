import inspect
from pprint import pprint

def introspection_info(obj):

    return {f'{"Тип"}:{type(obj)}\n{"Атрибуты и методы"}:{dir(obj)}\n{"Модуль"}:{inspect.getmodule(introspection_info)}'}

number_info = introspection_info('str')

pprint(number_info)
