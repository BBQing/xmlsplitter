import click
from xmlsplitter import XmlSplitter

# help="Split XML document into several XML documents on target XPath"
@click.command()
@click.argument("target_xpath")
@click.option("--xpath_default", default='default', help="namespace name used as default namespace name")
@click.argument("target_dir")
@click.argument("file")
def cli(target_xpath, xpath_default, target_dir, file):
    XmlSplitter.with_file(target_xpath, xpath_default, target_dir, file)