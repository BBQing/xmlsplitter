import pathlib
from lxml import etree



class XmlSplitter:

    def __init__(self, target_xpath,  default_xpath_tag = 'default'):
        self.target_xpath = target_xpath
        self.default_xpath_tag = default_xpath_tag
        self._namespaces = None

    @property
    def namespaces(self):
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespace):
        self._namespaces = self.name_default_namespace(namespace)
    
    def name_default_namespace(self, namespace):
        if namespace.get(None):
            namespace[self.default_xpath_tag] = namespace.get(None)
            del namespace[None]
        return namespace

    def split(self, file_path, target_dir):
        tree = etree.parse(file_path)
        encoding = tree.docinfo.encoding
        self.namespaces = tree.getroot().nsmap
        
        target_dir = pathlib.Path(target_dir)
        if not target_dir.exists():
            target_dir.mkdir()
        for ind, elem in enumerate(tree.xpath(self.target_xpath, namespaces=self.namespaces), 1):
            etree.ElementTree(elem).write(str(target_dir / f'chunk_{ind}.xml'), xml_declaration = True, encoding=encoding)

    @classmethod
    def with_file(cls,target_xpath, xpath_default, target_dir, file):
        cls(target_xpath, xpath_default).split(file, target_dir)