from django.core.management import BaseCommand

from djecrety.utils import generate_secret_key, save_to_settings


class Command(BaseCommand):
    help = 'Generate a new secret key with 50 characters length.'

    def add_arguments(self, parser):
        parser.add_argument('-s', '--save', action='store_true',
                            help='Save the generated secret key '
                                 'to `settings.py` file.')
        parser.add_argument('-p', '--print', action='store_true',
                            help='Display the generated secret key '
                                 'while saving on file.')
        parser.add_argument('-d', '--settings-dir-name', type=str,
                            help='Specify `settings.py` directory name.')

    def handle(self, *args, **kwargs):
        parameter_name = 'SECRET_KEY'
        new_key = generate_secret_key()
        parameter_value = new_key

        if kwargs['save']:
            settings_dir_name = kwargs['settings_dir_name']
            try:
                save_to_settings(f"'{parameter_value}'", parameter_name,
                                 settings_dir_name)
                self.stdout.write(self.style.SUCCESS(
                    f'{parameter_name} updated successfully.'))
                if kwargs['print']:
                    self.stdout.write('{} {}'.format(
                        self.style.SUCCESS(f'{parameter_name} set to:'),
                        parameter_value))
                self._print_tips()
            except (FileNotFoundError, NameError) as e:
                self.stdout.write(self.style.ERROR(e.__str__()))
        else:
            self.stdout.write('{} {}'.format(
                self.style.SUCCESS(f'{parameter_name}:'), parameter_value))
            self._print_tips()

    def _print_tips(self):
        self.stdout.write(self.style.WARNING('\nRecommendation:'))
        self.stdout.write('\t1. Keep it safe.\n\t2. Ignore `settings.py` '
                          'file in your commits.\n\t'
                          '3. Change the secret key on your deploy.\n\t'
                          '4. If you lost the secret key for any reason or\n\t'
                          '   the server got compromised change it as soon as '
                          'possible.\n\r')
