#!/usr/bin/env python

"""
Pandoc filter to process *.drawio images to PDFs.
Needs xvfb and drawio.
"""

import os
import subprocess
import sys
import tempfile

from pandocfilters import toJSONFilter, Image


def modification_time(path):
    try:
        return os.path.getmtime(path)
    except OSError:
        return -1


def drawio(key, value, format_, _):
    if key == "Image":
        attrs, alt, [src, title] = value
        src_basename, src_extension = os.path.splitext(src)
        if src_extension == ".drawio":
            pdf_name = f"{src_basename}.pdf"
            if modification_time(pdf_name) < modification_time(src):
                """
                Drawio needs to run in a virtual X session, because Electron
                refuses to work and dies with an unhelpful error message
                otherwise:
                The futex facility returned an unexpected error code.
                """
                cmd_line = [
                    "xvfb-run",
                    "drawio",
                    "--crop",
                    "-f",
                    "pdf",
                    "-x",
                    src,
                    "-o",
                    pdf_name,
                ]
                print("Running {}".format(" ".join(cmd_line)), file=sys.stderr)
                """
                Electron really wants a configuration directory to not die with:
                Error: Failed to get 'appData' path
                """
                my_env = os.environ.copy()
                my_env["XDG_CONFIG_HOME"] = tempfile.gettempdir()

                subprocess.call(cmd_line, stdout=sys.stderr.fileno(), env=my_env)

            return Image(attrs, alt, [pdf_name, title])


def main():
    toJSONFilter(drawio)


if __name__ == "__main__":
    main()
