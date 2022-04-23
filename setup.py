from setuptools import setup

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='chull',
    version='1.0.0',
    py_modules=['chull'],
    license='MIT',
    python_requires='>=3.6',
    platforms=['any'],
    description='convex hull from points',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Szabolcs Dombi',
    author_email='cprogrammer1994@gmail.com',
    url='https://github.com/szabolcsdombi/chull/',
    project_urls={
        'Documentation': 'https://chull.readthedocs.io/',
        'Source': 'https://github.com/szabolcsdombi/chull/',
        'Bug Tracker': 'https://github.com/szabolcsdombi/chull/issues/',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords=[
        'convex',
        'hull',
        'shape',
    ],
    install_requires=['scipy', 'numpy'],
)
