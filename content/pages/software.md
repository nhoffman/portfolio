Title: Software
page-order: 40

Here is some software that I have either authored or contributed
significantly to. Most of these projects are hosted under the user
name "[nhoffman](https://github.com/nhoffman)" on GitHub - <img
src="../images/gh.svg"></img> icons below link to individual
repositories.

# Molecular microbiology and the microbiome

[Taxtastic](https://github.com/fhcrc/taxtastic) and
[DeeNuRP](https://github.com/fhcrc/deenurp) are a collaboration with
Erick Matsen and his group in Computational Biology at FHCRC, and were
developed in parallel with Erick's fantastic
[pplacer](http://matsen.fhcrc.org/pplacer/), which adds aligned
sequences to a ML phylogenetic tree. My interest in pplacer is mainly
for performing sequence-based taxonomic assignment of microorganisms
using a phylogenetic approach, but it offers much more than that, so
check it out!

## Taxtastic

Taxtastic is used for assembling phylogenetic "reference packages" for
use with pplacer, but more generally provides tools for representing,
querying, and manipulating the NCBI taxonomy as a relational
database. It is used in both research and clinical pipelines. I was
the initial author and am the current maintainer; see the project repo
for the full list of contributors.

[![GitHub](../images/gh.svg)](https://github.com/fhcrc/taxtastic)
[![pypi](https://img.shields.io/pypi/v/taxtastic.svg)](https://pypi.python.org/pypi/taxtastic)
[![Build Status](https://travis-ci.org/fhcrc/taxtastic.svg?branch=master)](https://travis-ci.org/fhcrc/taxtastic)

## DeeNuRP

A package for 16S rRNA gene sequence curation and phylogenetic
reference set creation. I've contributed most significantly to
``deenurp filter-outliers``, which predicts likely mis-annotation of
sequence records by identifying outliers based on sequence identity.

[![GitHub](../images/gh.svg)](https://github.com/fhcrc/deenurp)
[![Build Status](https://travis-ci.org/fhcrc/deenurp.svg?branch=master)](https://travis-ci.org/fhcrc/deenurp)

## Yet another 16S rRNA database (ya16sdb)

One of my active areas of research is creating a curated and up to
date set of bacterial 16S rRNA sequences. Christopher Rosenthal
([crosenth](https://github.com/crosenth)), a longtime programmer in my
research group has written
[ya16sdb](https://github.com/nhoffman/ya16sdb), implementing a
pipeline for downloading and curating 16S rRNA records from NCBI.

[![GitHub](../images/gh.svg)](https://github.com/nhoffman/ya16sdb)

## barcodecop

A simple utility for reducing NGS read mis-assignment based on index
read match identity and quality score.

[![GitHub](../images/gh.svg)](https://github.com/nhoffman/barcodecop)
[![pypi](https://img.shields.io/pypi/v/barcodecop.svg)](https://pypi.python.org/pypi/barcodecop)
[![Build Status](https://travis-ci.org/nhoffman/barcodecop.svg?branch=master)](https://travis-ci.org/nhoffman/barcodecop)

# Bioinformatics and reproducible research

## bioscons

There has been quite a proliferation of build tools that are either
designed for or may be adapted to bioinformatics pipelines (eg,
[luigi](https://pypi.python.org/pypi/luigi),
[airflow](https://airflow.apache.org/), and [many, many
more](https://github.com/pditommaso/awesome-pipeline)), but I haven't
found one better suited to my needs than
[SCons](http://www.scons.org/). Most of the pipelines that I have
designed for both research and clinical applications are built using
scons, with some additional functionality (at this point, mostly job
dispatch with slurm) provided by ``bioscons``.

[![GitHub](../images/gh.svg)](https://github.com/nhoffman/bioscons)
[![pypi](https://img.shields.io/pypi/v/bioscons.svg)](https://pypi.python.org/pypi/bioscons)
[![Build Status](https://travis-ci.org/nhoffman/bioscons.svg?branch=master)](https://travis-ci.org/nhoffman/bioscons)

## fastalite

This "simplest possible fasta parser" finds its way into most of my projects.

[![GitHub](../images/gh.svg)](https://github.com/nhoffman/fastalite)
[![pypi](https://img.shields.io/pypi/v/fastalite.svg)](https://pypi.python.org/pypi/fastalite)
[![Build Status](https://travis-ci.org/nhoffman/fastalite.svg?branch=master)](https://travis-ci.org/nhoffman/fastalite)

## org-export

Although rmarkdown and Jupyter notebooks are much better known, emacs
[org-mode](http://orgmode.org/) is another nice option for
notebook-style reproducible research. ``org-export`` is a command-line
utility for compiling ``org-mode`` documents non-interactively, and has
the option of styling html documents with bootstrap.

[![GitHub](../images/gh.svg)](https://github.com/nhoffman/org-export)
[![Build Status](https://travis-ci.org/nhoffman/org-export.svg?branch=master)](https://travis-ci.org/nhoffman/org-export)


## alnvu

Formats multiple alignments in plain text, pdf, and html formats, for example:

<img src="https://raw.githubusercontent.com/nhoffman/alnvu/master/doc/html.png" width="100%"></src>

[![GitHub](../images/gh.svg)](https://github.com/nhoffman/alnvu)
[![pypi](https://img.shields.io/pypi/v/alnvu.svg)](https://pypi.python.org/pypi/alnvu)
[![Build Status](https://travis-ci.org/nhoffman/alnvu.svg?branch=master)](https://travis-ci.org/nhoffman/alnvu)

# Tools and applications for the clinical laboratory

Most of the applications that I write for the clinical laboratory are
for internal use. There are a few that I have been able to publish
that may be of general interest.

## Opiates

Automated QA for a clinical LC/MS urine opaites assay.

Published as Dickerson JA, Schmeling M, Hoofnagle AN, and Hoffman
NG. **Design and implementation of software for automated quality
control and data analysis for a complex LC/MS/MS assay for urine
opiates and metabolites.** Clin Chim Acta. 2012 Nov 15. PubMed:
[23159299](http://www.ncbi.nlm.nih.gov/pubmed/23159299)

[![GitHub](../images/gh.svg)](https://github.com/nhoffman/opiates)

## moin-labmanual

A plugin for using the MoinMoin wiki as a CMS for document control in
the clinical laboratory. Our department has many hundreds of policies
and procedures managed as MoinMoin wiki pages. Go open source!

[![GitHub](../images/gh.svg)](https://github.com/nhoffman/moin-labmanual)

## UW Groups API

Python bindings for the UW Groups web services API.

[![GitHub](../images/gh.svg)](https://github.com/nhoffman/uwgroups)

# Yak shaving

## borborygmi: a blog built with emacs org-mode and pelican

I built this [blog](https://nhoffman.github.io/borborygmi/) when I was
particularly into using ``org-mode``; it's a useful platform for
publishing notes and lectures.

[![GitHub](../images/gh.svg)](https://github.com/nhoffman/borborygmi)

## My .emacs.d

I'm pretty happy with my emacs config, and have gotten a number of
people started with emacs using this. It's written as an org-mode file
that can be exported to html and
[published](http://nhoffman.github.io/.emacs.d/).

[![GitHub](../images/gh.svg)](https://github.com/nhoffman/.emacs.d)

## argparse-bash

Why doesn't bash have decent command line argument parsing? Who knows?
Let's use Python's
[argparse](https://docs.python.org/3/library/argparse.html) instead!

[![GitHub](../images/gh.svg)](https://github.com/nhoffman/argparse-bash)
[![Build Status](https://travis-ci.org/nhoffman/argparse-bash.svg?branch=master)](https://travis-ci.org/nhoffman/argparse-bash)

