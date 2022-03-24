import os

from setuptools import find_packages, setup

version = __import__('djecrety').__version__

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    long_description = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='djecrety',
    version=version,
    python_requires='>=3.6',
    packages=find_packages(exclude=['testproject']),
    include_package_data=True,
    license='GNU Version 3 License',
    description='Djecrety package provides a command to generate a new secret '
                'key for your project and save it to settings.py file.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://djecrety.ir/',
    author='Majid Rouhi',
    author_email='mrouhi13@gmail.com',
    zip_safe=False,
    install_requires=[
        'Django>=2.0',
    ],
    classifiers=[
        'Environment :: Console',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
