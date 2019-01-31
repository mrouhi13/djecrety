import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-djecrety',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GNU Version 3 License',
    description='Djecrety is a simple Django app to work with "settings.py" file.',
    long_description=README,
    url='https://www.djecrety.ir/',
    author='Majid Rouhi',
    author_email='mrouhi13@gmail.com',
    classifiers=[
        'Environment :: Command Line Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Version 3 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
