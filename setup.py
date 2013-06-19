from setuptools import find_packages
from setuptools import setup


setup(
    author="Alex Clark",
    author_email="aclark@aclark.net",
    classifiers=[
        'Framework :: Plone :: 4.3',
        'Programming Language :: Python :: 2.7',
    ],
    description="Plone 4's 'Sunburst' theme reimplemented in Diazo",
    keywords='Diazo Modern Plone Sunburst Theme Theming',
    include_package_data=True,
    long_description=(
        open("README.rst").read() + '\n' +
        open("HISTORY.txt").read()
    ),
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    license="GPL2",
    name='plonetheme.diazo_sunburst',
    namespace_packages=[
        'plonetheme',
    ],
    packages=find_packages(),
    url="https://github.com/aclark4life/plonetheme.diazo_sunburst",
    version="0.0.1",
    zip_safe=False,
)
