#!/usr/bin/python
"""
CS 451 Data-Intensive Distributed Computing (Winter 2018):
Assignment 3 public check script for Altiscale

Sample usage:
$ ./check_assignment3_public_altiscale.py lintool
"""

import sys, os, re, argparse
from subprocess import call

def check_a3(username,reducers):
  """Run Assignment 3 on Altiscale"""
  call(["mvn", "clean", "package"])
  call(["hadoop", "jar", "target/assignments-1.0.jar",
        "ca.uwaterloo.cs451.a3.BuildInvertedIndexCompressed".format(username),
        "-input", "/shared/uwaterloo/cs451/data/enwiki-20161220-sentences-0.1sample.txt", 
        "-output", "cs451-{0}-a3-index-wiki".format(username), "-reducers", str(reducers) ])
  print("\n\nQuestion 2.\n")
  call(["hadoop", "fs", "-du", "-h", "cs451-{0}-a3-index-wiki".format(username)])
  print("\n\nQuestion 3.\n")
  call(["hadoop", "jar", "target/assignments-1.0.jar",
        "ca.uwaterloo.cs451.a3.BooleanRetrievalCompressed".format(username),
        "-index", "cs451-{0}-a3-index-wiki".format(username), 
        "-collection", "/shared/uwaterloo/cs451/data/enwiki-20161220-sentences-0.1sample.txt",
        "-query", "waterloo stanford OR cheriton AND"])
  print("\n\nQuestion 4.\n")
  call(["hadoop", "jar", "target/assignments-1.0.jar",
        "ca.uwaterloo.cs451.a3.BooleanRetrievalCompressed".format(username),
        "-index", "cs451-{0}-a3-index-wiki".format(username),
        "-collection", "/shared/uwaterloo/cs451/data/enwiki-20161220-sentences-0.1sample.txt",
        "-query", "big data AND hadoop spark OR AND"])

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="CS 451/651 A3 Public Check Script for Altiscale")
  parser.add_argument('username',metavar='[Github Username]', help="Github username",type=str)
  parser.add_argument('-r','--reducers',help="Number of reducers to use.",type=int,default=1)
  args=parser.parse_args()
  try:
    check_a3(args.username,args.reducers)
  except Exception as e:
    print(e)
