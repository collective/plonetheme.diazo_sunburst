from setuptools import find_packages
from setuptools import setup


setup(
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    name='plontheme.diazo_sunburst',
    namespace_packages=[
        'plonetheme',
    ],
    packages=find_packages(),
)
