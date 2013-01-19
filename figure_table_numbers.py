#!/usr/bin/env python

import re

chapters = ['abstract',
            'foreword',
            'acknowledgements',
            'preface',
            'introduction',
            'eom',
            'extensions',
            'physicalparameters',
            'parameterstudy',
            'delftbicycle',
            'motioncapture',
            'davisbicycle',
            'control',
            'systemidentification']

def old2new(matchobj):
    oldNum, figNum, typ = matchobj.groups()
    newNum = str(int(oldNum) - 2)
    return '{}.{}<{}'.format(newNum, figNum, typ)

def new2old(matchobj):
    newNum, figNum, typ = matchobj.groups()
    oldNum = str(int(newNum) + 2)
    return '{}.{}<{}'.format(oldNum, figNum, typ)

funcs = {'new2old': new2old, 'old2new': old2new}

def convert(to):
    for chapter in chapters:
        with open(chapter + '.rst') as f:
            text = f.read()
        newText = re.sub(r'(\d*)\.(\d*) *<(fig|tab)', funcs[to], text)
        with open(chapter + '.rst', 'w') as f:
            f.write(newText)
