import os

def parent_path():
    path = os.path.dirname(__file__)
    x = y
    return path

def my_method(name, version, *sub_version):
    if name:
        my_module.my_class.my_method(name, version, sub_version)
    else:
        my_module.my_class.my_method(name, version, 'placeholder')
