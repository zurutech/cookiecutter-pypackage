{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{%- if is_open_source -%}
![Python - Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.package_name }}.svg)
![PyPy - Version](https://badge.fury.io/py/{{ cookiecutter.package_name }}.svg)
![PyPI - License](https://img.shields.io/pypi/l/{{ cookiecutter.package_name }}.svg)
![{{ cookiecutter.project_name }} - Badge](https://img.shields.io/badge/package-{{ cookiecutter.repo_name }}-brightgreen.svg)
{%- if cookiecutter.add_pyup_badge == 'y' -%}
[![Updates](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/shield.svg)](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/)
{%- endif %}
[![Build Status](https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg)](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }})
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?version=latest)](https://{{ cookiecutter.repo_name }}.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }})
[![CodeFactor](https://www.codefactor.io/repository/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/badge)](https://www.codefactor.io/repository/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }})
{%- endif -%}
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)
[![Code Style - Zuru](https://img.shields.io/badge/codestyle-zuru-red)](https://github.com/zurutech/styleguide)
[![Black - Badge](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)

## Description

{{ cookiecutter.project_short_description }}

## Installation

```console
pip install {{ cookiecutter.distribution_name }}
```

## Features

## Testing

Run complete test suite + linting:

```console
tox
```

## Credits

This package was created with [Cookiecutter] and the [zurutech/cookiecutter-pypackage] project template.

Requirements are structured according to [zurutech/styleguide] and should be handled with [pip-tools] or [reqompyler].

[Cookiecutter]: https://github.com/audreyr/cookiecutter
[pip-tools]: https://github.com/jazzband/pip-tools
[reqompyler]: https://github.com/zurutech/reqompyler
[zurutech/cookiecutter-pypackage]: https://github/zurutech/cookiecutter-pypackage
[zurutech/styleguide]: https://github.com/zurutech/styleguide/python.md
