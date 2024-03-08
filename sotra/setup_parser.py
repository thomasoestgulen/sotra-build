'''setup_parser.py'''

import argparse
from pathlib import Path
from datetime import date


def parser():
    parser = argparse.ArgumentParser(
        prog="sotra-build",
        description="Some useful functions for automating Sotra")
    subparsers = parser.add_subparsers(dest="command")

    ### build bridge
    bridge_parser = subparsers.add_parser(
        "build",
        help="Build a bridge in terminal"
    )
    bridge_parser.add_argument(
        "-n",
        "--name",
        type=str,
        help="Name the bridge",
    )
    bridge_parser.add_argument(
        "--desc"
        "--description",
        type=str,
        help="Describe the bridge",
    )
    bridge_parser.add_argument(
        "--bro",
        action='store_true',
        help="Print the bridge",
    )

    ### single obs
    one_parser = subparsers.add_parser(
        "obs",
        help="Make txt files for all documents connected to given OBS",
    )
    one_parser.add_argument(
        '-d',
        '--dest',
        default=Path.cwd(),
        help='The destination of the folder. Default is the current directory.'
    )
    one_parser.add_argument(
        "-l",
        "--list",
        type=str,
        nargs="*",
        help="List multiple obs'",
    )
    one_parser.add_argument(
        "-c",
        "--cwd",
        action='store_true',
        help="OBS based on current working directory'",
    )

    ### archive models to "Resultatdokument"
    archive_parser = subparsers.add_parser(
        "archive",
        help="Make txt files for all documents connected to given OBS",
    )
    archive_parser.add_argument(
        "-s",
        "--src",
        type=str,
        default=Path.cwd(),
        help="The folder that will be added to Resultatdokument",
    )
    archive_parser.add_argument(
        "-o",
        "--obs",
        type=str,
        default=Path.cwd(),
        help="The OBS control object to be added",
    )
    archive_parser.add_argument(
        "-d",
        "--date",
        type=str,
        default=str(date.today()),
        help="The date that should be used on the folder. Formatted: yyyy-mm-dd",
    )
    return parser