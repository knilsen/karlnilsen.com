#! /Users/karlnilsen/bin/anaconda/bin/python
import os
import string
# from bs4 import BeautifulSoup


def build(header, page, nav, schema, page_name, out_path):

    header_section = str.replace(header, "{{ SCHEMA }}", schema)
    page_section = str.replace(page, "{{ NAV }}", nav)
    text = header_section + page_section

    # text = BeautifulSoup(text)
    # text = text.prettify()

    file_name = out_path + page_name
    with open(file_name, 'w') as f:
        f.write(text)


def main():

    header_file = "/Users/karlnilsen/apps/karlnilsen.com/source/templates/header.html"
    with open(header_file, 'r') as f:
        header = f.read()

    # build root documents (index, cv, notebook, contact)
    root_path = "/Users/karlnilsen/apps/karlnilsen.com/source/root/"
    out_path = "/Users/karlnilsen/apps/karlnilsen.com/build/"

    root_nav_file = "/Users/karlnilsen/apps/karlnilsen.com/source/templates/root_nav.html"
    with open(root_nav_file, 'r') as f:
        nav = f.read()

    for file in os.listdir(root_path):
        if file.endswith(".html"):
            file_path = root_path + file
            page_name = file
            schema_file = root_path + os.path.splitext(file)[0] + "_schema.txt"
            with open(schema_file, 'r', encoding="utf-8") as f:
                schema = f.read()
            with open(file_path, 'r', encoding="utf-8") as f:
                page = f.read()
            build(header, page, nav, schema, page_name, out_path)

    # build notebook documents
    nb_path = "/Users/karlnilsen/apps/karlnilsen.com/source/nb/"
    out_path = "/Users/karlnilsen/apps/karlnilsen.com/build/nb/"

    nb_nav_file = "/Users/karlnilsen/apps/karlnilsen.com/source/templates/nb_nav.html"
    with open(nb_nav_file, 'r') as f:
        nav = f.read()

    for file in os.listdir(nb_path):
        if file.endswith(".html"):
            file_path = nb_path + file
            page_name = file
            schema_file = nb_path + os.path.splitext(file)[0] + "_schema.txt"
            with open(schema_file, 'r', encoding="utf-8") as f:
                schema = f.read()
            with open(file_path, 'r', encoding="utf-8") as f:
                page = f.read()
            build(header, page, nav, schema, page_name, out_path)

if __name__ == '__main__':
    main()

# The MIT License (MIT)
# Copyright (c) 2016 Karl Nilsen
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
