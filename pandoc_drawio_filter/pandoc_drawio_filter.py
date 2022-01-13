#!/usr/bin/env python

"""
Pandoc filter to process *.drawio images to PDFs.
Needs drawio.
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
                cmd_line = [
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
                subprocess.call(cmd_line, stdout=sys.stderr.fileno())

            return Image(attrs, alt, [pdf_name, title])


def main():
    toJSONFilter(drawio)


if __name__ == "__main__":
    main()
