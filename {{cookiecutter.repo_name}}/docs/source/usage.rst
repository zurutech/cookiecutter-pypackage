=====
Usage
=====

To use {{ cookiecutter.project_name }} in a project::

    import {{ cookiecutter.package_name }}


{%- if cookiecutter.command_line_interface|lower == 'click' %}
---

.. click:: {{ cookiecutter.package_name }}.cli:main
   :prog: {{ cookiecutter.package_name }}
{%- endif %}
