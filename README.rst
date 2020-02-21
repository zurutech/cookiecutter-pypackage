=======================================
Zuru Tech Cookiecutter PyPackage 🍪 🐍
=======================================

|development-status| |pyup| |license|

Cookiecutter_ opinionated template for a Python package compliant with `zurutech/styleguide`_.

Features
--------

* Testing setup with pytest_
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ automation:
    * Testing: Setup to easily test for Python 3.6, 3.7, 3.8 with code coverage computation and upload via codecov_
    * Linting: Setup to automatically lint your codebase with black_, isort_, pylint_, flake8_
    * Docs: Setup to easily generate docs for local reading
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
    * `Read the Docs Sphinx Theme`_
    * `Google Style Docstrings`_
    * Type hints for ``autodoc`` via sphinx-autodoc-typehints_
    * Dependency Graph
    * Integrate Markdown and RST via m2r_
    * sphinx-copybutton_
    * doc8_ and pydocstyle_
* Opinionated configurations enforcing compliance with `zurutech/styleguide`_ for:
    * isort_
    * pylint_
    * flake8_ extended via flake8-bugbear_
* Easy refactoring with rope_
* Modular requirements.in structure to be used with reqompyler_ or pip-tools_
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Command line interface using Click_ (optional)

Quickstart
----------

This is the flow we reccommend for new projects.

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/zurutech/cookiecutter-pypackage.git

Then:

* Create a GitHub repo and put it there.
* Expand on the copmatible Python versions that your package support by specifying them in
  in the ``setup.py`` file while also testing for them via Tox_ and Travis-CI_.
* Add license headers to your project using licenseheaders_.
* Add the repo to your Travis-CI_ account.
* Register_ your project with PyPI.
* Run the Travis CLI command ``travis encrypt --add deploy.password`` to encrypt your PyPI API token in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your ReadTheDocs_ account + turn on the ReadTheDocs service hook.
* Release your package by pushing a new tag to master.
* Activate your project on `pyup.io`_ (`pyup.io`_ is a service that helps in keeping dependencies
  fresh by automatically generating a PR whenever one of them gets a new release,
  it's free for public repos).

For more details, see the `cookiecutter-pypackage tutorial`_.


Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `audreyr/cookiecutter-pypackage`_: The One and only. This is the original ``pypackage``
  Cookiecutter. `zurutech/cookiecutter-pypackage`_ started as an internal fork of this one and became
  more opinionated over time.

* `ionelmc/cookiecutter-pylibrary`_: Cookiecutter template for a Python python library.
  Extremely configurable. `zurutech/cookiecutter-pypackage`_ is a cross between this and `audreyr/cookiecutter-pypackage`_

* `Nekroze/cookiecutter-pypackage`_: A fork of this with a PyTest test runner,
  strict flake8 checking with Travis/Tox, and some docs and `setup.py` differences.

* `tony/cookiecutter-pypackage-pythonic`_: Fork with py2.7+3.3 optimizations.
  Flask/Werkzeug-style test runner, ``_compat`` module and module/doc conventions.
  See ``README.rst`` or the `github comparison view`_ for exhaustive list of
  additions and modifications.

* `ardydedase/cookiecutter-pypackage`_: A fork with separate requirements files rather
  than a requirements list in the ``setup.py`` file.

* `lgiordani/cookiecutter-pypackage`_: A fork of Cookiecutter that uses Punch_ instead of
  Bumpversion_ and with separate requirements files.

* Also see the `network`_ and `family tree`_ for this repo. (If you find
  anything that should be listed here, please add it and send a pull request!)

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.


.. |license| image:: https://img.shields.io/github/license/zurutech/cookiecutter-pypackage
    :target: https://github.com/zurutech/cookiecutter-pypackage/LICENSE
    :alt: License

.. |development-status| image:: https://img.shields.io/badge/%F0%9F%8F%97%20_development--status-alpha-blue
    :alt: Development Status: Alpha

.. |pyup| image:: https://pyup.io/repos/github/zurutech/cookiecutter-pypackage/shield.svg
     :target: https://pyup.io/repos/github/zurutech/cookiecutter-pypackage/
     :alt: Updates


.. _black: https://github.com/psf/black
.. _Click: https://github.com/pallets/click/
.. _codecov: https://github.com/codecov/codecov-python
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _doc8: https://github.com/PyCQA/doc8
.. _flake8-bugbear: https://github.com/PyCQA/flake8-bugbear
.. _flake8: https://github.com/PyCQA/flake8
.. _isort: https://github.com/timothycrosley/isort
.. _licenseheaders: https://github.com/johann-petrak/licenseheaders
.. _m2r: https://github.com/miyakogi/m2r
.. _pip-tools: https://github.com/jazzband/pip-tools
.. _pydocstyle: https://github.com/PyCQA/pydocstyle
.. _pylint: https://github.com/PyCQA/pylint
.. _pytest: https://github.com/pytest-dev/pytest
.. _reqompyler: https://github.com/zurutech/reqompyler
.. _rope: https://github.com/python-rope/rope
.. _sphinx-autodoc-typehints: https://github.com/agronholm/sphinx-autodoc-typehints
.. _sphinx-copybutton: https://github.com/choldgraf/sphinx-copybutton
.. _`Google Style Docstrings`: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
.. _`Read the Docs Sphinx Theme`: https://sphinx-rtd-theme.readthedocs.io/en/stable/

.. _`pyup.io`: https://pyup.io/
.. _Bumpversion: https://github.com/peritus/bumpversion
.. _Punch: https://github.com/lgiordani/punch
.. _PyPi: https://pypi.python.org/pypi
.. _ReadTheDocs: https://readthedocs.io/
.. _Sphinx: http://sphinx-doc.org/
.. _Tox: http://testrun.org/tox/
.. _Travis-CI: http://travis-ci.org/

.. _`zurutech/styleguide`: https://github.com/zurutech/styleguide

.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html
.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Register: https://packaging.python.org/distributing/#register-your-project

.. _`ardydedase/cookiecutter-pypackage`: https://github.com/ardydedase/cookiecutter-pypackage
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`ionelmc/cookiecutter-pylibrary`: https://github.com/ionelmc/cookiecutter-pylibrary
.. _`lgiordani/cookiecutter-pypackage`: https://github.com/lgiordani/cookiecutter-pypackage
.. _`Nekroze/cookiecutter-pypackage`: https://github.com/Nekroze/cookiecutter-pypackage
.. _`tony/cookiecutter-pypackage-pythonic`: https://github.com/tony/cookiecutter-pypackage-pythonic
.. _`zurutech/cookiecutter-pypackage`: https://github.com/zurutech/cookiecutter-pypackage

.. _`family tree`: https://github.com/audreyr/cookiecutter-pypackage/network/members
.. _`network`: https://github.com/audreyr/cookiecutter-pypackage/network
.. _github comparison view: https://github.com/tony/cookiecutter-pypackage-pythonic/compare/audreyr:master...master
