#!/usr/bin/env python

"""This script counts the number of words at each commit and plots a graph of
word count versus time."""

import os

import pandas as pd
import matplotlib.pyplot as plt


sh_command = """\
rm count.txt
for commit in `git rev-list --all`; do
    git log -n 1 --pretty=%ad $commit >> count.txt;
    git archive $commit | tar -x -O --wildcards '*.rst' | wc -w >> count.txt;
done\
"""
os.system(sh_command)

data = {'date': [], 'count': []}

with open('count.txt', 'r') as f:
    for line in f:
        if '-' in line:
            data['date'].append(pd.to_datetime(line.strip().split(' -')[0]))
        else:
            data['count'].append(line.strip())

df = pd.Series(data['count'], data['date'])
df = df[df != '0']
fig, ax = plt.subplots()
df.astype(float).plot(ax=ax)
ax.axvline(pd.to_datetime('August 22, 2012'), color='black')
ax.set_ylabel('Word Count')
ax.set_xlabel('Date')
plt.tight_layout()
plt.show()
