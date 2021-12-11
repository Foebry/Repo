from setuptools import setup
from codecs import open

here = os.path.abspath(os.path.dirname(__file__))
packages = ['repo', 'repo/app']
requires = ['requesting', 'termcolor', 'git+github.com/foebry/requesting']

about = {}
with open(os.path.join(here, 'repo', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description'],
    long_description=readme,
    author=about['__author__'],
    author_email=about["__author_email__"],
    url=about["__url__"],
    packages=packages,
    package_data={"": ['LICENSE', 'NOTICE']},
    package_dir={'repo': 'repo'},
    install_requires=requires,
    license=about['__license__'],
)
