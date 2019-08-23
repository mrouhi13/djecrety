import fileinput
import os
import re
import sys

from django.conf import settings
from django.utils.crypto import get_random_string


def generate_secret_key(length=50):
    """
    Return a 50 character random string
    usable as a `SECRET_KEY` setting value.
    """
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    if not isinstance(length, int):
        raise TypeError(
            f'invalid literal for int() with base 10: {length}')
    return get_random_string(length, chars)


def save_to_settings(value, parameter_name, settings_dir_name=''):
    """
    Save the value to the given parameter in `settings.py` file.
    """
    if not settings_dir_name:
        settings_dir_name = ''

    settings_dir = os.path.join(settings.BASE_DIR, settings_dir_name,
                                'settings.py')
    if not os.path.exists(settings_dir):
        raise FileNotFoundError("Can't find `settings.py` file: "
                                f"{settings_dir}")
    return _replace_line(value, parameter_name, settings_dir)


def _replace_line(value, parameter_name, settings_file):
    parameter_is_exist = False
    if parameter_name:
        new_line = f'{parameter_name} = {value}'
        line_pattern = fr'^{parameter_name} = .*'

        for line in fileinput.input(settings_file, inplace=True):
            if re.match(line_pattern, line):
                parameter_is_exist = True
                line = re.sub(line_pattern, new_line, line)
            sys.stdout.write(line)

        if not parameter_is_exist:
            raise NameError(f"Can't find parameter name: {parameter_name}")
        return True
    return False
