#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
"""
    {{cookiecutter.project_slug}}.cli
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    {{ cookiecutter.project_short_description }}

    :copyright: © 2019 by the Choppy Team.
    :license: AGPLv3+, see LICENSE for more details.
"""

"""Console script for {{cookiecutter.project_slug}}."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
