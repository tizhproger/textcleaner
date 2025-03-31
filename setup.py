from setuptools import setup, find_packages

exec(open("textcleaner/version.py").read())

setup(
    name='textcleaner',
    version=__version__,
    description='Multilingual text cleaner with emoji removal, normalization and token tagging',
    author='tizhproger',
    author_email='you@example.com',
    packages=find_packages(),
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
    ],
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
)
