"""Setup for the pylint-quotes package.
"""
from setuptools import setup


setup(
    name='pylint-quotes',
    description='Quote consistency checker for Pylint',
    long_description=open('README.md').read(),
    license='MIT',
    version='0.1.0',
    author='Erick Daniszewski',
    author_email='edaniszewski@gmail.com',
    url='https://github.com/edaniszewski/pylint-quotes',
    install_requires=[
        'pylint',
    ],
    packages=[
        '',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ],
    keywords='pylint linting string quotes'
)