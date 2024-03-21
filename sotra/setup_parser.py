'''setup_parser.py'''

import argparse
from pathlib import Path
from datetime import date
from sotra import obs


def parser():
    parser = argparse.ArgumentParser(
        prog="sotra-build",
        description="Some useful functions for automating Sotra")
    subparsers = parser.add_subparsers(dest="command")

    ### build bridge
    build_parser = subparsers.add_parser(
        "build",
        help="Build a bridge in terminal"
    )
    build_parser.add_argument(
        "-n",
        "--name",
        type=str,
        help="Name the bridge",
    )
    build_parser.add_argument(
        "--d"
        "--desc",
        type=str,
        help="Describe the bridge",
    )
    build_parser.add_argument(
        "--bro",
        action='store_true',
        help="Build the bridge",
    )

    ### single obs
    obs_parser = subparsers.add_parser(
        "obs",
        help="Make txt files for all documents connected to given OBS",
    )
    obs_parser.add_argument(
        '-d',
        '--dest',
        default=Path.cwd(),
        help='The destination of the folder. Default is the current directory.'
    )
    obs_parser.add_argument(
        "-l",
        "--list",
        type=str,
        nargs="*",
        help="List multiple obs'",
    )
    obs_parser.add_argument(
        "-c",
        "--cwd",
        action='store_true',
        help="OBS based on current working directory'",
    )

    ### archive models to "Resultatdokument"
    archive_parser = subparsers.add_parser(
        "archive",
        help="Archive delivery folder to Resultatdokument",
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
        help="The OBS control object to be added",
    )
    archive_parser.add_argument(
        "-d",
        "--date",
        type=str,
        # action='store_true',
        default=str(date.today()),
        help="The date that should be used on the folder. Formatted: yyyy-mm-dd",
    )    
    archive_parser.add_argument(
        "-c",
        "--cwd",
        action='store_true',
        help="OBS based on current working directory'",
    )

    ### Documentlist
    doc_parser = subparsers.add_parser(
        "doc",
        help="Document delivery list handler",
    )
    doc_parser.add_argument(
        '-p',
        '--print',
        action='store_true',
        help='Print the document delivery list'
    )
    doc_parser.add_argument(
        '-r',
        '--revisions',
        action='store_true',
        help='Get all latest revisions from the log file and output to excel'
    )

    return parser