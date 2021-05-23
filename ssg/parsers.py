from typing import List
from pathlib import Path
import shutil


class Parser:
    extensions = []  # type: List[str]

    def valid_extension(self, extension):
        if extension in self.extensions:
            return True
        else:
            return False

    def parse(self, path, source, dest):
        raise NotImplemented

    def read(self, path):
        with open(path) as f:
            return f.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest / Path.relative_to(source))


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path, source, dest):
        self.copy(path, source, dest)



