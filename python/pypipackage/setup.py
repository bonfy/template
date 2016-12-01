from setuptools import setup, find_packages

setup(
    name = 'pypitest',
    version = '0.0.1',
    keywords = ('pypi', 'test'),
    description = 'just a simple test',
    license = 'MIT License',
    install_requires = None,

    author = 'bonfy',
    author_email = 'foreverbonfy@163.com',

    packages = find_packages(),
    platforms = 'any',
)
