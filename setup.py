from setuptools import find_packages
from setuptools import setup


setup(
    entry_points={
        'z3c.autoinclude.plugins': 'target = plone',
    },
    name='diazotheme.sunburst',
    namespace_packages=[
        'diazotheme',
    ],
    packages=find_packages(),
)
