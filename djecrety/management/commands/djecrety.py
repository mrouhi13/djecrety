from django.core.management import BaseCommand

from djecrety.utils import generate_secret_key, save_to_settings


class Command(BaseCommand):
    help = 'Generate a new secret key with 50 characters length.'

    def add_arguments(self, parser):
        parser.add_argument('-s', '--save', action='store_true',
                            help='Save the generated secret key to settings.py file.')
        parser.add_argument('-p', '--print', action='store_true',
                            help='Display the generated secret key when saving on file.')
        parser.add_argument('-d', '--settings-dir-name', type=str,
                            help='Specify settings directory name.')

    def handle(self, *args, **kwargs):
        new_key = '\'{}\''.format(generate_secret_key())

        if kwargs['save']:
            settings_dir_name = kwargs['settings_dir_name']
            result, message = save_to_settings(new_key, 'SECRET_KEY', settings_dir_name=settings_dir_name)

            if result:
                self.stdout.write(self.style.SUCCESS(message))

                if kwargs['print']:
                    self.stdout.write('{} {}'.format(self.style.SUCCESS('SECRET_KEY set to:'), new_key))

                self._print_tips()
            else:
                self.stdout.write(self.style.ERROR(message))
        else:
            self.stdout.write('{} {}'.format(self.style.SUCCESS('New secret key:'), new_key))
            self._print_tips()

    def _print_tips(self):
        self.stdout.write(self.style.WARNING('\nrecommended:'))
        self.stdout.write('\t1. Keep it safe.\n\t2. Ignore \'settings.py\' file in your commits.\n\t'
                          '3. Change the secret key on your deploy.\n\t'
                          '4. If you lost the secret key for any reason or\n\t'
                          '   the server got compromised change it as soon as possible.')
