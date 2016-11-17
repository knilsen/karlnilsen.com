#! /Users/karlnilsen/bin/anaconda/bin/python
import os
import string
import argparse


def build_single(source_item, out_dir, header, nav):

    schema_file = os.path.splitext(source_item)[0] + "_schema.txt"
    with open(schema_file, "r", encoding="utf-8") as f:
        schema = f.read()
    with open(source_item, "r", encoding="utf-8") as f:
        page = f.read()


def build_all(source_item, base_dir):

    header_file = "{}source/templates/header.html".format(base_dir)
    with open(header_file, "r") as f:
        header = f.read()

    for file in source_item:
        if file.startswith("{}source/content/root/".format(base_dir)):
            out_dir = "{}build/".format(base_dir)
            root_nav_file = "{}source/templates/root_nav.html".format(base_dir)
            with open(root_nav_file, "r") as f:
                nav = f.read()
            schema_file = os.path.dirname(
                file) + "/" + os.path.splitext(os.path.basename(file))[0] + "_schema.txt"
            with open(schema_file, "r", encoding="utf-8") as f:
                schema = f.read()
            with open(file, "r") as f:
                page = f.read()
        elif file.startswith("{}source/content/nb/".format(base_dir)):
            out_dir = "{}build/nb/".format(base_dir)
            nb_nav_file = "{}source/templates/nb_nav.html".format(base_dir)
            with open(nb_nav_file, "r") as f:
                nav = f.read()
            schema_file = os.path.dirname(
                file) + "/" + os.path.splitext(os.path.basename(file))[0] + "_schema.txt"
            with open(schema_file, "r", encoding="utf-8") as f:
                schema = f.read()
            with open(file, "r") as f:
                page = f.read()

        header_section = str.replace(header, "{{ SCHEMA }}", schema)
        page_section = str.replace(page, "{{ NAV }}", nav)
        text = header_section + page_section

        # text = BeautifulSoup(text)
        # text = text.prettify()

        file_name = out_dir + os.path.basename(file)
        with open(file_name, "w") as f:
            f.write(text)


def main():

    base_dir = "/Users/karlnilsen/apps/karlnilsen.com/"

    header_file = "{}source/templates/header.html".format(base_dir)
    with open(header_file, "r") as f:
        header = f.read()

    parser = argparse.ArgumentParser(description=None)
    parser.add_argument("--root", action="store_true",
                        help="process single page from root directory")
    parser.add_argument("--nb", action="store_true",
                        help="process single page from notebook directory")
    parser.add_argument("filename", nargs="?", help="enter the file name")
    args = parser.parse_args()

    if args.root:
        try:
            source_item = "{}source/content/root/{}".format(base_dir, args.filename)
        except:
            print("error:", sys.exc_info()[0])
            raise
        out_dir = "{}build/".format(base_dir)
        root_nav_file = "{}source/templates/root_nav.html".format(base_dir)
        with open(root_nav_file, "r") as f:
            nav = f.read()
        build_single(source_item, out_dir, header, nav)
    elif args.nb:
        try:
            source_item = "{}source/content/nb/{}".format(base_dir, args.filename)
        except:
            print("error:", sys.exc_info()[0])
            raise
        out_dir = "{}build/nb/".format(base_dir)
        nb_nav_file = "{}source/templates/nb_nav.html".format(base_dir)
        with open(nb_nav_file, "r") as f:
            nav = f.read()
        build_single(source_item, out_dir, header, nav)
    else:
        source_item = []
        for dir_name, sub_dirs, files in os.walk("{}source/content/".format(base_dir)):
            for file in files:
                if file.endswith(".html"):
                    source_item.append(os.path.join(dir_name, file))
        build_all(source_item, base_dir)

if __name__ == "__main__":
    main()

# The MIT License (MIT)
# Copyright (c) 2016 Karl Nilsen
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
