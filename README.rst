=========================
plonetheme.diazo_sunburst
=========================

Diazo theme 'Sunburst' is a Plone 4's default theme 'Sunburst' reimplemented with Diazo [1]_ theme support [2]_.

Introduction
============

*plonetheme.diazo_sunburst* package is an installable Plone_ Theme using the **theming** and **packaging** 
features available in `plone.app.theming`_ in `Plone`.


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest version (https://plone.org/download)
- The ``plone.app.theming`` package (*will be installed as a dependency of this package*)


Screenshots
===========

Layout of the site when viewed in a computer resolution:

.. image:: https://raw.githubusercontent.com/collective/plonetheme.diazo_sunburst/master/plonetheme/diazo_sunburst/theme/images/preview.png
    :align: center


Features
========

- It's an installable Plone_ Theme package.
- After installation from Add-ons controlpanel, this theme is enabled automatically.
- Also it's a simple Diazo_ package (Zip file).
- It's have support for clean uninstallation.


Installation
============


Buildout
--------

If you are a **developer user**, you might enjoy installing it via buildout.

For install ``plonetheme.diazo_sunburst`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        plonetheme.diazo_sunburst


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'plonetheme.diazo_sunburst',
    ],


Enabling the theme
^^^^^^^^^^^^^^^^^^

Browse to ``http://yoursite/Plone/@@theming-controlpanel`` click on ``Enable`` 
on ``Diazo Sunburst`` theme from the Diazo control panel. That's it!


Contribute
==========

- Issue Tracker: https://github.com/collective/plonetheme.diazo_sunburst/issues
- Source Code: https://github.com/collective/plonetheme.diazo_sunburst


License
=======

This package is licensed under the GPL Version 2.


Credits
-------

- Alex Clark (aclark at aclark dot net).
- Leonardo J. Caballero G. (leonardocaballero at gmail dot com).

.. [1] https://en.wikipedia.org/wiki/Diazo
.. [2] http://diazo.org

.. _`Plone`: http://plone.org
.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming/
.. _`Diazo`: http://diazo.org
