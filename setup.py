""" This is the setup.py script for setting up the package and fulfilling any
necessary requirements.
"""
from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

# Set the home path of the setup script/package
home = path.abspath(path.dirname(__file__))
name = 'mgap'


def readme():
    """Get the long description from the README file."""
    with open(path.join(home, 'README.md'), encoding='utf-8') as f:
        return f.read()


setup(
    name=name,
    author='Shaurita Hutchins',
    author_email='shaurita.d.hutchins@gmail.com',
    description="",
    version='0.1',
    long_description=readme(),
    url='https://github.com/vallenderlab/mgap',
    license='MIT',
    keywords='science mgap api',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    project_urls={
        'Documentation': '',
        'Releases': 'https://github.com/vallenderlab/mgap/releases',
        'Issues': 'https://github.com/vallenderlab/mgap/issues',
    },
    # Packages will be automatically found if not in this list.
    packages=find_packages(),
    include_package_data=True,
    entry_points={

    },
    install_requires=[
    ],
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose']
)
