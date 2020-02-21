"""Set of hooks to be run before generation is done."""

import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"


def validate_package_name():
    """Check Valid Package Name."""
    if not re.match(MODULE_REGEX, "{{ cookiecutter.package_name }}"):
        print(
            "ERROR: The package name {{ cookiecutter.package_name }} is not a valid"
            "Python module name. Please do not use a - and use _ instead"
        )

        # Exit to cancel project
        sys.exit(1)


if __name__ == "__main__":
    validate_package_name()
