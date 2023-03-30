#!/usr/bin/env python
# coding: utf-8

import os
import sys

# guard against the case when no arguments are provided
if len(sys.argv) < 3:
    print("Error: Please provide arguments for the GitHub repo and name.")
    sys.exit()


# get the GitHub repo argument
name = sys.argv[1]
github_repo = sys.argv[2]

# clone the repo
os.system(f"git clone --branch {name} {github_repo} ./tools/rippled-{name}")

print("Rippled repo installation complete!")
