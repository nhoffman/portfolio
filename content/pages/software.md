Title: Software
page-order: 40

Here is some software that I have either authored or contributed
significantly to. Most of these projects are hosted under the user
name "[nhoffman](https://github.com/nhoffman)" on GitHub - <img
src="../images/gh.svg"></img> icons below link to individual
repositories.

<style>
li {margin-top: 0em; margin-bottom: 0em;}
div.toc {margin-bottom: 1em;}
</style>

[TOC]

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

## dada2-nf

The [dada2](https://benjjneb.github.io/dada2/) R package ("DADA2: Fast and accurate sample inference from amplicon data with single-nucleotide resolution") by Benjamin Callahan and colleagues has been an incredible boon to researchers studying the microbiome using amplicon-based sequencing. The R community has a very strong culture of interactive computing, which has is merits, but the absence of command-line oriented tools can create challenges when incorporating into a pipeline with additional components. The dada2-nf project wraps dada2 in a [nextflow](https://www.nextflow.io) pipeline (using either Docker or Singularity) and provides some additional conveniences. This project provides a mechanism for using dada2 in both clinical and research pipelines.

[![GitHub](../images/gh.svg)](https://github.com/nhoffman/dada2-nf)

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
[![Build Status](https://github.com/nhoffman/org-export/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/nhoffman/org-export/actions/workflows/test.yml)

## alnvu

Formats multiple alignments in plain text, pdf, and html formats, for example:

<img src="https://raw.githubusercontent.com/nhoffman/alnvu/master/doc/html.png" width="100%"></src>

[![GitHub](../images/gh.svg)](https://github.com/nhoffman/alnvu)
[![pypi](https://img.shields.io/pypi/v/alnvu.svg)](https://pypi.python.org/pypi/alnvu)
[![Build Status](https://travis-ci.org/nhoffman/alnvu.svg?branch=master)](https://travis-ci.org/nhoffman/alnvu)

# Tools and applications for the clinical laboratory

Most of the applications that I write for the clinical laboratory are for internal use. Web applications are typically implemented using Python, Flask, and Postgresql (old school, I know). My role has often been to design and provide the initial implementation of each application, and then partner with departmental software engineers for ongoing development and maintenance. There are a few that I have been able to publish that may be of general interest.

## Laboratory Test Guide

I am the primary author of our public [Laboratory Test
Guide](https://testguide.labmed.uw.edu). This application provides a
searchable interface for clinical laboratory tests offered by the
University of Washington Department of Laboratory Medicine.

## Pending Log Monitor

I designed a web application (known as the "Pending Log Monitor" or PLM) that displays the status of pending orders for lab tests. This application provides a highly extensible framework for displaying pending orders in near real time, and is now used in dozens of locations throughout the clinical laboratory (thanks to the ongoing efforts of Tom E.).

I described this application in a [presentation](../images/hoffman-api2017.pptx) at the 2017 Pathology Informatics Summit (annual meeting of the Association for Pathology Informatics). Here's the abstract for that presentation:

> Many laboratory information systems (LIS) do not provide real-time
notification of new orders, relying instead on batched, asynchronous
display of information such as printed pending lists. To improve
situational awareness of pending laboratory orders, we developed a web
application (the "Pending Log Monitor") that displays data continually
updated from our LIS on large wall-mounted monitors or PC
workstations. Users may enter comments associated with individual
items. A survey was administered to evaluate usage patterns.  The
application is implemented in Python 2.7 using the Flask web
microframework, and is hosted on a virtual machine running Ubuntu
14.04. Data is extracted from the LIS database (Sunquest Information
Systems, Tucson, AZ) using custom code written in Cache (InterSystems
Corporation, Cambridge, MA), and is transferred to the application
server by a batched process using secure shell. User-provided comments
associated with pending tests are stored in an SQLite database.  The
application was designed for maintainability, ease of customization,
stability, and rapid recovery in the result of a component
failure. Logic for display and formatting of pending tests is
implemented as Python functions. A simple JSON-format specification
can accommodate any tabular data. Lists of pending tests defined for a
given area typically correspond to one or more worksheets defined in
the LIS.  Customized displays of pending tests have been implemented
for over 35 combinations of worksheets in multiple lab areas. Pending
orders for each lab area are filtered, ordered, and color coded based
on elapsed time since order or receipt, priority, specimen stability,
or other criteria. Data is transferred from the LIS by a batched
process every four minutes. This application has replaced the use of
printed pending lists in many areas. The majority of survey
respondents described the application as "very important" to lab
operations, with many lab areas referring to the monitor "constantly."
Use of comments varies widely between lab areas, but most respondents
strongly agreed with the statement that comments improve
communication.  A simple web application implemented at low cost using
open source technology has provided significant workflow and
communication improvements throughout the laboratory.

## Automated Chemistry Quality Control

Right around the time I started my faculty position, I implemented a
system for QC review of our automated chemistry analyzers, consisting
of some R scripts that emitted Levy-Jennings charts highlighting out
of control standards. Here's an example:

<a href="../images/UCDXC_QC20150227_flags.pdf"><img src="../images/UCDXC_QC20150227_flags.png"></img></a>

QC checks were documented in a [roundup](http://roundup-tracker.org/)
bug tracker. This was the primary mechanism for monitoring and
documenting quality control for 7 or 8 years, until it was replaced by
a commercial product in 2016.

## Opiates

Automated QA for a clinical LC/MS urine opaites assay. This project was initiated to address the complexity of the calculations required for our [Urine Opioid Confirmatory assay by LC/MS](https://testguide.labmed.uw.edu/UOPIAC), and was described in the following publication:

Dickerson JA, Schmeling M, Hoofnagle AN, and Hoffman
NG. **Design and implementation of software for automated quality
control and data analysis for a complex LC/MS/MS assay for urine
opiates and metabolites.** Clin Chim Acta. 2012 Nov 15. PubMed:
[23159299](http://www.ncbi.nlm.nih.gov/pubmed/23159299)

The code accompanying the publication is available on GitHub.

Much more recently, I designed and implemented the foundation for a Flask-based web application to support laboratory workflows, perform calculations (replacing the original command line interface), and support clinical signout. This was ultimately extended to report results directly into the lab information system via a middleware application.

[![GitHub](../images/gh.svg)](https://github.com/nhoffman/opiates)

## moin-labmanual

A plugin for using the MoinMoin wiki as a CMS for document control in the clinical laboratory. Our department has (or had) many hundreds of policies and procedures managed as MoinMoin wiki pages. Unfortunately, the MoinMoin project has stalled in its development and support for Python 3 has been a [long time coming](http://moinmo.in/MoinMoin2.0), so we have had to move much of our documentation to other platforms.

[![GitHub](../images/gh.svg)](https://github.com/nhoffman/moin-labmanual)

## Infrastructure for role-based user management in the clinical laboratory

Significant (and mainly hidden) administrative costs in any
organization relate to processes and tools for user management and
access to electronic resources. Compounding factors include:

- multiple domains
- users with roles spanning institutions
- applications with varying technical requirements for implementing single sign-on (SSO)
- regulated environments with specific policy requirements for user management
- high user turnover.

We have all of these! Because of the heterogeneity of our environment,
no existing system or domain could serve as a single source of truth
for users and their roles. To provide a single source of truth for our
department and affiliates, I wrote an internal web application (Flask,
Postgresql) for user management. Users are associated with attributes
(role, location, departmental/divisional affiliations, etc) or
assigned directly to groups (eg for access to a specific
application). Groups are then synchronized to multiple domains so that
they can be used as the basis for authorization for a wide variety of
applications.

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

I'm pretty happy with my emacs config, and have gotten a number of people started with emacs using this. My [first iteration](https://github.com/nhoffman/.emacs.d) was written as an org-mode file that could be exported to html or tangled into an elisp file. More recently, I've simplified my approach and use a [more conventional setup](https://github.com/nhoffman/emacs-config).

[![GitHub](../images/gh.svg)](https://github.com/nhoffman/emacs-config)

## argparse-bash

Why doesn't bash have decent command line argument parsing? Who knows?
Let's use Python's
[argparse](https://docs.python.org/3/library/argparse.html) instead!

[![GitHub](../images/gh.svg)](https://github.com/nhoffman/argparse-bash)
[![Build Status](https://travis-ci.org/nhoffman/argparse-bash.svg?branch=master)](https://travis-ci.org/nhoffman/argparse-bash)

