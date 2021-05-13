#!/usr/bin/env python3

"""Get formatted references from pubmed

"""

import sys
import argparse
import json
from urllib.request import urlopen
from urllib.parse import urlencode
import xml.etree.ElementTree as ET
from datetime import datetime
import re


def search_pubmed(query):

    url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?'
    data = {
        'db': 'pubmed',
        'usehistory': 'y',
        'term': query,
        'retmode': 'json',
        'retmax': 0
    }
    qstr = url + urlencode(data)
    with urlopen(qstr) as response:
        return json.loads(response.read().decode('utf-8'))


def get_pubmed(webenv):

    url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?'
    data = {
        'db': 'pubmed',
        'usehistory': 'y',
        'webenv': webenv,
        'query_key': 1,
        'retmode': 'xml',
        'retmax': 0
    }

    qstr = url + urlencode(data)
    with urlopen(qstr) as response:
        return response.read().decode('utf-8')


def get_date(val):
    for fmt in ['%Y/%m/%d %H:%M', '%Y %b %d']:
        try:
            return datetime.strptime(val, fmt)
        except Exception:
            continue

    return val


def get_tree(c):
    d = dict(c.items())
    name = d.get('Name') or c.tag
    dtype = d.get('Type')

    if len(c) > 0:
        return (name, [get_tree(child) for child in c])
    else:
        if dtype == 'Date':
            val = get_date(c.text)
        elif dtype == 'Integer':
            val = int(c.text)
        else:
            val = c.text

        return (name, val)


def get_article(tree):
    data = {}
    for key, val in tree[1]:
        if isinstance(val, list):
            if key == 'AuthorList':
                data[key] = [v for k, v in val]
            else:
                data[key] = dict(val)
        else:
            data[key] = val

    data['authors'] = fmt_authors(data['AuthorList'])

    return data


def fmt_authors(authors):
    if len(authors) > 2:
        return ', '.join(authors[:-1]) + ', and ' + authors[-1]
    else:
        return ' and '.join(authors)


def fmt_article(data):

    return (
        '<li>'
        '{authors}. '
        '{Title} '
        '<em>{Source}.</em> '
        '{SO} '
        '<a href="https://pubmed.ncbi.nlm.nih.gov/{Id}/">PMID {Id}</a>'
        '</li>\n'
    ).format(**data)


def emphasize(mo):
    if mo.group(0):
        return '<strong>' + mo.group(0) + '</strong>'


def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)

    query = ('(hoffman ng[author] or 11543657[uid] or 32529017[uid] '
             'not 26646360[uid] and (1996[PDAT]:3000[PDAT]))')

    search_result = search_pubmed(query)
    xmltext = get_pubmed(search_result['esearchresult']['webenv'])

    args.outfile.write('<ol>')
    for doc in ET.fromstring(xmltext):
        article = get_article(get_tree(doc))
        html = fmt_article(article)
        html = re.sub(r'(Hoffman NG|Hoffman N)', emphasize, html)
        args.outfile.write(html)
    args.outfile.write('</ol>')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
