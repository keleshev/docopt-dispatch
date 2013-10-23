"""Dispatch from command-line arguments to functions."""
import re
from collections import OrderedDict


__all__ = ('dispatch', 'DispatchError')
__author__ = 'Vladimir Keleshev <vladimir@keleshev.com>'
__version__ = '0.0.1'
__license__ = 'MIT'
__keywords__ = 'docopt dispatch function adapter kwargs'
__url__ = 'https://github.com/halst/docopt-dispatch'


class DispatchError(Exception):
    pass


class Dispatch(object):

    def __init__(self):
        self._functions = OrderedDict()

    def on(self, argument):
        def decorator(function):
            self._functions[argument] = function
            return function
        return decorator

    def __call__(self, *args, **kwargs):
        from docopt import docopt
        arguments = docopt(*args, **kwargs)
        for argument, function in self._functions.items():
            if arguments[argument]:
                function(**self._kwargify(arguments))
                return

        raise DispatchError('None of dispatch conditions (%s) is triggered'
                            % ', '.join(self._functions.keys()))

    @staticmethod
    def _kwargify(arguments):
        kwargify = lambda string: re.sub('\W', '_', string).strip('_')
        return dict((kwargify(key), value) for key, value in arguments.items())


dispatch = Dispatch()
