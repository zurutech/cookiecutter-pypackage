"""Set of hooks to be run after generation is done."""

# TODO: substitute os with pathlib

import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    """Remove the file."""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def blacking() -> None:
    """Invoke `black` formatter on the generated project."""
    subprocess.run(["black", PROJECT_DIRECTORY], capture_output=True)


if __name__ == "__main__":

    print("“Keep calm and eat cookies.”")
    blacking()

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.md")
        remove_file("docs/source/authors.rst")

    if "{{ cookiecutter.use_pytest }}" == "y":
        remove_file("tests/__init__.py")

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        CLI_FILE = os.path.join("src", "{{ cookiecutter.package_name }}", "cli.py")
        remove_file(CLI_FILE)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    if "{{ cookiecutter.gitignore|lower }}" not in ["y", "yes"]:
        remove_file(".gitignore")
