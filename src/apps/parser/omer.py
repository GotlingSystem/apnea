# coding: utf-8
import re
import codecs


class Omer(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.content = {}
        self.summary = {}
        self.read_file(file_name)
        self.parse_summary()

    def read_file(self, file_name):
        with codecs.open(file_name, 'r', encoding='utf16') as f:
            self.content = f.readlines()

    def parse_summary(self):
        pattern = re.compile(ur'\"([^"]+?)\"', re.UNICODE)

        for line in self.content:
            m = pattern.findall(line.strip())

            if m and len(m) == 2:
                key = m[0].encode('utf-8')
                value = m[1].encode('utf-8')

                if key == u'Dive':
                    break

                if value.isdigit():
                    self.summary[str(key)] = int(value)
                else:
                    self.summary[str(key)] = value
