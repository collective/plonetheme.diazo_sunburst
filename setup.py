from setuptools import find_packages
from setuptools import setup


setup(
    author="Alex Clark",
    author_email="aclark@aclark.net",
    description="Plone 4's 'Sunburst' theme reimplemented in Diazo",
    long_description=(
        open("README.rst").read() + '\n' +
        open("HISTORY.txt").read()
    ),
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    name='plonetheme.diazo_sunburst',
    namespace_packages=[
        'plonetheme',
    ],
    packages=find_packages(),
    url="https://github.com/aclark4life/plonetheme.diazo_sunburst",
    version="0.0.1",
)
