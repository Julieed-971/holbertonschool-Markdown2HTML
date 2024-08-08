#!/usr/bin/python3
"""File which convert markdown file to HTML file"""

import os
import sys


def md_to_html(md_file, html_file):
    # If the number of arguments is less than 2: print in STDERR
    # Usage: ./markdown2html.py README.md README.html and exit 1
    # if len(sys.argv) < 3:
    #     sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    #     sys.exit(1)
    # If the Markdown file doesn’t exist:
    # print in STDERR Missing <filename> and exit 1
    if not os.path.exists(md_file):
        sys.stderr.write(f"Missing {md_file}\n")
    # Otherwise, print nothing and exit 0
    sys.exit(0)


if __name__ == "__main__":
    # If the number of arguments is less than 2: print in STDERR Usage:
    # ./markdown2html.py README.md README.html and exit 1
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
    md_file = sys.argv[1]
    html_file = sys.argv[2]

    md_to_html(md_file, html_file)
