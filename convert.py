import argparse
import xml.dom.minidom
import os
import os.path
import subprocess
import re

parser = argparse.ArgumentParser(description='Convert mediawiki export to markdown')
parser.add_argument('input', help='MediaWiki XML export file to use as input')
#parser.add_argument('output', help='Output directory to place markdown files into')

args = parser.parse_args()

def getLoneTag(el, tag):
    elements = el.getElementsByTagName(tag)
    assert len(elements) == 1
    return elements[0]

def fixPath(path):
    return path.replace('/', '-')

def getText(el):
    return ''.join(node.data for node in el.childNodes
                   if node.nodeType == node.TEXT_NODE)

link_re = re.compile(r'\[\[([^\]]*)\]\]')
def preprocess(mw_src):
    links = link_re.findall(mw_src)
    for link in links:
        mw_src = mw_src.replace('[[{}]]'.format(link), '[[{}.md]]'.format(fixPath(link)))
    return mw_src

with open(args.input) as export:
    with xml.dom.minidom.parse(export) as dom:
        sitename = getText(getLoneTag(dom, 'sitename'))
        print('Exporting to {!r}...'.format(sitename))
        try:
            os.mkdir(sitename)
        except FileExistsError as e:
            pass
        for page in dom.getElementsByTagName('page'):
            title = getText(getLoneTag(page, 'title'))
            fixed_title = fixPath(title)
            if fixed_title != title:
                print('Exporting {!r} as {!r}'.format(title, fixed_title))
            else:
                print('Exporting {!r}'.format(title))
            mediawiki_page_name = os.path.join(sitename, '{}.mediawiki'.format(fixed_title))
            with open(mediawiki_page_name, 'w') as page_file:
                revisions = page.getElementsByTagName('revision')
                page_file.write('={}\n=\n'.format(fixed_title))
                source = getText(getLoneTag(revisions[0], 'text'))
                page_file.write(preprocess(source))
            markdown_page_name = os.path.join(sitename, '{}.md'.format(fixed_title))
            try:
                subprocess.run(['pandoc',
                                '-f', 'mediawiki',
                                '-t', 'markdown_github',
                                mediawiki_page_name,
                                '-o', markdown_page_name],
                                check=True)
            except subprocess.CalledProcessError as e:
                print('Error exporting {!r}'.format(title))
                print(e)
            else:
                os.remove(mediawiki_page_name)
