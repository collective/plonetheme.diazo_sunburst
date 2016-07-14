from setuptools import find_packages
from setuptools import setup

VERSION = '0.1.0'

setup(author="Alex Clark",
      author_email="aclark@aclark.net",
      classifiers=[
          'Framework :: Plone :: 4.3',
          'Programming Language :: Python :: 2.7',
      ],
      description="Plone 4's default Sunburst theme reimplemented in Diazo",
      keywords='Diazo Modern Plone Sunburst Theme Theming',
      include_package_data=True,
      install_requires=[
          'setuptools',
      ],
      long_description=(
          open("README.rst").read() + '\n' + open("CHANGES.rst").read()),
      entry_points={
          'z3c.autoinclude.plugin': 'target = plone',
      },
      license="GPL2",
      name='plonetheme.diazo_sunburst',
      namespace_packages=[
          'plonetheme',
      ],
      packages=find_packages(),
      test_suite='plonetheme.diazo_sunburst.tests.TestSuite',
      url="https://github.com/collective/plonetheme.diazo_sunburst",
      version=VERSION,
      zip_safe=False, )
