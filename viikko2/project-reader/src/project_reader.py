import toml
import json
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        content = toml.loads(content)
        #print(content)
        name = content['tool']['poetry']['name']
        descr = content['tool']['poetry']['description']
        depds = content['tool']['poetry']['dependencies']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, descr, list(depds), [])