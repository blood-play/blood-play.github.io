#!/usr/bin/env python3

from os import listdir
from os.path import join, isfile

directory_path = "static/img/artgallery"
contents = listdir(directory_path)
files = filter(lambda f: isfile(join(directory_path,f)),contents)
html = ""

for file in files:
    html += f"<img src=\"{directory_path}/{file}\">\n"

if __name__ == "__main__":
    with open("output.html", "w") as output:
        output.write(html)