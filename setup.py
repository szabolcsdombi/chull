from setuptools import setup

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='chull',
    version='1.0.0',
    py_modules=['chull'],
    install_requires=['scipy', 'numpy'],
    author='Szabolcs Dombi',
    author_email='cprogrammer1994@gmail.com',
    description='convex hull from points',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
