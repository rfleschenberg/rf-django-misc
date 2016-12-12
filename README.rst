========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/rf-django-misc/badge/?style=flat
    :target: https://readthedocs.org/projects/rf-django-misc
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/rfleschenberg/rf-django-misc.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/rfleschenberg/rf-django-misc

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/rfleschenberg/rf-django-misc?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/rfleschenberg/rf-django-misc

.. |requires| image:: https://requires.io/github/rfleschenberg/rf-django-misc/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/rfleschenberg/rf-django-misc/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/rfleschenberg/rf-django-misc/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/rfleschenberg/rf-django-misc

.. |version| image:: https://img.shields.io/pypi/v/rf-django-misc.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/rf-django-misc

.. |downloads| image:: https://img.shields.io/pypi/dm/rf-django-misc.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/rf-django-misc

.. |wheel| image:: https://img.shields.io/pypi/wheel/rf-django-misc.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/rf-django-misc

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/rf-django-misc.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/rf-django-misc

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/rf-django-misc.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/rf-django-misc


.. end-badges

Miscellaneous things for Django projects

* Free software: BSD license

Installation
============

::

    pip install rf-django-misc

Documentation
=============

https://rf-django-misc.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
