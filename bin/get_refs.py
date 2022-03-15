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
from operator import itemgetter
from functools import partial
from textwrap import dedent


def search_pubmed(query):

    url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?'
    data = {
        'db': 'pubmed',
        'usehistory': 'y',
        'term': query,
        'retmode': 'json',
        'retmax': 0,
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
        'retmax': 0,
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

    pubdate = data['PubDate']
    if isinstance(pubdate, str):
        year = int(pubdate.split()[0])
    else:
        year = int(pubdate.strftime('%Y'))

    data['year'] = year
    data['ord'] = (-1 * year, data['Title'])

    return data


def fmt_authors(authors):
    if len(authors) > 2:
        return ', '.join(authors[:-1]) + ', and ' + authors[-1]
    else:
        return ' and '.join(authors)


def html_underline(mo):
    if mo.group(0):
        # return '<strong>' + mo.group(0) + '</strong>'
        return '<u>' + mo.group(0) + '</u>'


def fmt_portfolio(data, author_rexp=None):

    result = (
        '<li>'
        '{authors}.<br>'
        '<strong>{Title}</strong><br>'
        '<em>{Source}.</em> {SO} '
        '<a href="https://pubmed.ncbi.nlm.nih.gov/{Id}/">PMID {Id}</a>'
        '</li>\n'
    ).format(**data)

    if author_rexp:
        result = re.sub(author_rexp, html_underline, result)

    return result


def latex_underline(mo):
    if mo.group(0):
        return r'\uline{%s}' % mo.group(0)


def fmt_cv(data, author_rexp=None):
    result = dedent(r"""
    \refitem{%(authors)s}{%(Title)s}{%(Source)s}{%(SO)s}{PMID %(Id)s}
    """) % data

    if author_rexp:
        result = re.sub(author_rexp, latex_underline, result)

    return result


def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-f', '--format', choices=['portfolio', 'cv'],
                        default='portfolio', help='[%(default)s]')
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)

    query = ('(hoffman ng[author] or 11543657[uid] or 32529017[uid] '
             'not 26646360[uid] and (1996[PDAT]:3000[PDAT]))')

    search_result = search_pubmed(query)
    xmltext = get_pubmed(search_result['esearchresult']['webenv'])
    articles = []
    for doc in ET.fromstring(xmltext):
        article = get_article(get_tree(doc))
        articles.append(article)

    articles.sort(key=itemgetter('ord'))

    author_rexp = r'Hoffman NG?'
    pre, post = '', ''
    if args.format == 'portfolio':
        formatter = partial(fmt_portfolio, author_rexp=author_rexp)
        pre = dedent("""
        Title: Publications
        page-order: 01

        <ol>
        """).lstrip()

        post = '\n</ol>'
    elif args.format == 'cv':
        formatter = partial(fmt_cv, author_rexp=author_rexp)

    args.outfile.write(pre)
    for article in articles:
        args.outfile.write(formatter(article))
    args.outfile.write(post)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
