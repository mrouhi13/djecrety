from django.core.management import call_command
from django.test import TestCase
from io import StringIO

from djecrety.utils import generate_secret_key, save_to_settings


class GenerateSecretKeyTests(TestCase):

    def test_with_none_length(self):
        """
        Check secret key with none type length has been generated or not.
        """
        secret_key_length = None
        self.assertRaises(TypeError, generate_secret_key, secret_key_length)

    def test_with_none_integer_length(self):
        """
        Check secret key with string type length has been generated or not.
        """
        secret_key_length = 'test'
        self.assertRaises(TypeError, generate_secret_key, secret_key_length)

    def test_with_none_integer_empty_string_length(self):
        """
        Check secret key with empty string length has been generated or not.
        """
        secret_key_length = ''
        self.assertRaises(TypeError, generate_secret_key, secret_key_length)

    def test_with_zero_length(self):
        """
        Check secret key with zero length has been generated or not.
        """
        secret_key_length = 0
        secret_key = generate_secret_key(secret_key_length)
        self.assertEqual(len(secret_key), secret_key_length)

    def test_with_passed_integer_length(self):
        """
        Check secret key with passed length has been generated or not.
        """
        secret_key_length = 20
        secret_key = generate_secret_key(secret_key_length)
        self.assertEqual(len(secret_key), secret_key_length)

    def test_without_passed_length(self):
        """
        Check secret key has been generated or not.
        """
        default_length = 50
        secret_key = generate_secret_key()
        self.assertEqual(len(secret_key), default_length)


class SaveToSettingsTests(TestCase):

    def test_with_parameter_value_with_defaults(self):
        """
        Check value has been updated or not.
        """
        parameter_value = f"'{generate_secret_key()}'"
        parameter_name = 'SECRET_KEY'
        settings_dir_name = 'testproject'
        result = save_to_settings(parameter_value, parameter_name,
                                  settings_dir_name)
        self.assertEqual(result, True)

    def test_with_empty_parameter_value(self):
        """
        Check empty value has been updated or not.
        """
        parameter_value = "''"
        parameter_name = 'SECRET_KEY'
        settings_dir_name = 'testproject'
        result = save_to_settings(parameter_value, parameter_name,
                                  settings_dir_name)
        self.assertEqual(result, True)
        self.test_with_parameter_value_with_defaults()

    def test_with_none_parameter_value(self):
        """
        Check None value has been updated or not.
        """
        parameter_value = None
        parameter_name = 'SECRET_KEY'
        settings_dir_name = 'testproject'
        result = save_to_settings(parameter_value, parameter_name,
                                  settings_dir_name)
        self.assertEqual(result, True)
        self.test_with_parameter_value_with_defaults()

    def test_with_correct_parameter_name(self):
        """
        Check passed parameter is successfully update or not.
        """
        parameter_name = 'DEBUG'
        settings_dir_name = 'testproject'
        result = save_to_settings(True, parameter_name,
                                  settings_dir_name)
        self.assertEqual(result, True)

    def test_with_incorrect_parameter_name(self):
        """
        Check passed parameter is existing or not.
        """
        parameter_name = 'TEST'
        settings_dir_name = 'testproject'
        self.assertRaises(NameError, save_to_settings, False, parameter_name,
                          settings_dir_name)

    def test_with_empty_parameter_name(self):
        """
        Check passed parameter is empty or not.
        """
        parameter_name = ''
        settings_dir_name = 'testproject'
        result = save_to_settings(False, parameter_name, settings_dir_name)
        self.assertEqual(result, False)

    def test_with_none_parameter_name(self):
        """
        Check passed parameter is empty or not.
        """
        parameter_name = None
        settings_dir_name = 'testproject'
        result = save_to_settings(False, parameter_name, settings_dir_name)
        self.assertEqual(result, False)

    def test_with_incorrect_settings_dir_name(self):
        """
        Check passed settings dir name is exist or not.
        """
        parameter_value = f"'{generate_secret_key()}'"
        parameter_name = 'SECRET_KEY'
        settings_dir_name = 'test'
        self.assertRaises(FileNotFoundError, save_to_settings, parameter_value,
                          parameter_name, settings_dir_name)

    def test_with_correct_settings_dir_name(self):
        """
        Check passed settings dir name is exist or not.
        """
        parameter_value = f"'{generate_secret_key()}'"
        parameter_name = 'SECRET_KEY'
        settings_dir_name = 'testproject'
        result = save_to_settings(parameter_value, parameter_name,
                                  settings_dir_name)
        self.assertEqual(result, True)

    def test_with_empty_settings_dir_name(self):
        """
        Check passed settings dir name is empty or not.
        """
        parameter_value = f"'{generate_secret_key()}'"
        parameter_name = 'SECRET_KEY'
        settings_dir_name = 'testproject'
        result = save_to_settings(parameter_value, parameter_name,
                                  settings_dir_name)
        self.assertEqual(result, True)

    def test_with_none_settings_dir_name(self):
        """
        Check passed settings dir name is empty or not.
        """
        parameter_value = f"'{generate_secret_key()}'"
        parameter_name = 'SECRET_KEY'
        settings_dir_name = 'testproject'
        result = save_to_settings(parameter_value, parameter_name,
                                  settings_dir_name)
        self.assertEqual(result, True)


class CommandsTestCase(TestCase):

    def test_djecrety(self):
        """
        Test djecrety command.
        """
        parameter_name = 'SECRET_KEY'
        out = StringIO()
        args = []
        opts = {}
        call_command('djecrety', stdout=out, *args, **opts)
        self.assertTrue(parameter_name in out.getvalue())

    def test_djecrety_with_save_arg(self):
        """
        Test djecrety command with save argument.
        """
        parameter_name = 'SECRET_KEY'
        out = StringIO()
        args = ['-s']
        opts = {'settings_dir_name': 'testproject'}
        call_command('djecrety', stdout=out, *args, **opts)
        self.assertTrue(f'{parameter_name} updated successfully.' in
                        out.getvalue())

    def test_djecrety_with_save_and_display_arg(self):
        """
        Test djecrety command with save and display arguments together.
        """
        parameter_name = 'SECRET_KEY'
        out = StringIO()
        args = ['-sp']
        opts = {'settings_dir_name': 'testproject'}
        call_command('djecrety', stdout=out, *args, **opts)
        self.assertTrue(f'{parameter_name} set to:' in out.getvalue())

    def test_djecrety_with_incorrect_settings_dir_arg(self):
        """
        Test djecrety command with specify settings directory name argument.
        """
        out = StringIO()
        args = ['-sp']
        opts = {'settings_dir_name': 'test'}
        call_command('djecrety', stdout=out, *args, **opts)
        self.assertTrue("Can't find `settings.py` file: " in out.getvalue())

    def test_djecrety_with_none_settings_dir_arg(self):
        """
        Test djecrety command with specify settings directory name argument.
        """
        out = StringIO()
        args = ['-sp']
        opts = {'settings_dir_name': None}
        call_command('djecrety', stdout=out, *args, **opts)
        self.assertTrue("Can't find `settings.py` file: " in out.getvalue())

    def test_djecrety_with_empty_settings_dir_arg(self):
        """
        Test djecrety command with specify settings directory name argument.
        """
        out = StringIO()
        args = ['-sp']
        opts = {'settings_dir_name': ''}
        call_command('djecrety', stdout=out, *args, **opts)
        self.assertTrue("Can't find `settings.py` file: " in out.getvalue())
