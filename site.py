#! /Users/karlnilsen/bin/anaconda/bin/python
import os
import string
from bs4 import BeautifulSoup

def build(header, page, schema, page_name, out_path):

    header = str.replace(header, "<!-- SCHEMA -->", schema)
    text = header + page

    text = BeautifulSoup(text)
    text = text.prettify()

    file_name = out_path + page_name
    with open(file_name, 'w') as f:
        f.write(text)

def main():

    header_file = "/Users/karlnilsen/apps/karlnilsen.com/templates/header.html"
    with open(header_file, 'r') as f:
        header = f.read()

    root_path = "/Users/karlnilsen/apps/karlnilsen.com/source/root/"
    out_path = "/Users/karlnilsen/apps/karlnilsen.com/build/"
    for file in os.listdir(root_path):
        if file.endswith(".html"):
            file_path = root_path + file
            page_name = file
            schema_file = root_path + os.path.splitext(file)[0] + "_schema.txt"
            with open(schema_file, 'r', encoding="utf-8") as f:
                schema = f.read()
            with open(file_path, 'r', encoding="utf-8") as f:
                page = f.read()
            build(header, page, schema, page_name, out_path)

    nb_path = "/Users/karlnilsen/apps/karlnilsen.com/source/nb/"
    out_path = "/Users/karlnilsen/apps/karlnilsen.com/build/nb/"
    for file in os.listdir(nb_path):
        if file.endswith(".html"):
            file_path = nb_path + file
            page_name = file
            schema_file = nb_path + os.path.splitext(file)[0] + "_schema.txt"
            with open(schema_file, 'r', encoding="utf-8") as f:
                schema = f.read()
            with open(file_path, 'r', encoding="utf-8") as f:
                page = f.read()
            build(header, page, schema, page_name, out_path)

if __name__ == '__main__':
    main()
