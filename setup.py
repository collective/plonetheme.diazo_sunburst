from setuptools import find_packages
from setuptools import setup

VERSION = '0.1.3'

setup(author="Alex Clark",
      author_email="aclark@aclark.net",
      maintainer='Leonardo Caballero',
      maintainer_email='leonardocaballero@gmail.com',
      # Get more strings from
      # https://pypi.org/pypi?:action=list_classifiers
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Plone',
          'Framework :: Plone :: 4.1',
          'Framework :: Plone :: 4.2',
          'Framework :: Plone :: 4.3',
          'Framework :: Plone :: Theme',
          'Framework :: Zope2',
          'Framework :: Zope3',
          'Intended Audience :: Developers',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Internet',
          'Topic :: Software Development :: Libraries :: Python Modules',
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
      name='plonetheme.diazo-sunburst',
      namespace_packages=[
          'plonetheme',
      ],
      packages=find_packages(),
      test_suite='plonetheme.diazo_sunburst.tests.TestSuite',
      url="https://github.com/collective/plonetheme.diazo_sunburst",
      version=VERSION,
      zip_safe=False, )
