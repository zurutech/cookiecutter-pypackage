#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    README = readme_file.read()

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{% if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{% endif %}
        'Natural Language :: English',
{%- for version in cookiecutter.python_version.split(", ") -%}
        'Programming Language :: Python :: {{ version }}',
{%- endfor -%}
    ],
    description="{{ cookiecutter.project_short_description }}",
{%- if 'no' not in cookiecutter.command_line_interface|lower -%}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.package_name }}={{ cookiecutter.package_name }}.cli:main',
        ],
    },
{%- endif -%}
    install_requires=[{%- if cookiecutter.command_line_interface|lower == "click" %}"Click>=7.0",{%- endif -%}],
    python_requires="{{ cookiecutter.python_version }}",
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    long_description=README,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='{{ cookiecutter.package_name }}',
    name='{{ cookiecutter.package_name }}',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    version='{{ cookiecutter.version }}',
    zip_safe=False,
)
