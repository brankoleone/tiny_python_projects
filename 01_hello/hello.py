#!/usr/bin/env python3
# Purpose: Say Hello

import argparse

parser = argparse.ArgumentParser(description="Say Hello")
parser.add_argument("name", help="Name to great")
args = parser.parse_args()
print("Hello, " + args.name + "!")
