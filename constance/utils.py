from __future__ import print_function
from __future__ import unicode_literals

from importlib import import_module

from constance import LazyConfig, settings

config = LazyConfig()


def import_module_attr(path):
    package, module = path.rsplit('.', 1)
    return getattr(import_module(package), module)


def get_constance_values():
    """
    Get dictionary of values from the backend
    :return:
    """
    default_initial = ((name, options[0])
                       for name, options in settings.CONFIG.items())
    # Then update the mapping with actually values from the backend
    initial = dict(default_initial,
                   **dict(config._backend.mget(settings.CONFIG.keys())))

    return initial
