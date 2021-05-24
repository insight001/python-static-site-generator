import re
from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    def load(self):
        _, fm, content = self.__regex.split("string", 2)
        load(fm, Loader=FullLoader)
        return cls("",content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"] if self.data.has_key("type") else None

    @type.setter
    def type(self, value):
        self.data["type"] = value

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):
        next(self.data)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {}
        for key, value in self.data.items():
            if key is not "content":
                value = data[key]
        return str(data)
