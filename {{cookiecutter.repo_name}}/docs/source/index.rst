Welcome to {{ cookiecutter.project_name }}'s documentation!
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
   installation
   usage
   contributing
   api
   dependencies_graph
   {% if cookiecutter.create_author_file == 'y' -%}authors
   {%- endif %}
Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
