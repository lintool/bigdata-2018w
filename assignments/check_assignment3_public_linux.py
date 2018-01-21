#!/usr/bin/python
"""
CS 451 Data-Intensive Distributed Computing (Winter 2018):
Assignment 3 public check script for the Linux Student CS environment

Sample usage:
$ ./check_assignment3_public_linux.py lintool
"""

import sys, os, re, argparse
from subprocess import call

def check_a3(username,reducers):
  """Run Assignment 3 in the Linux Student CS environment"""
  call(["mvn", "clean", "package"])
  call(["hadoop", "jar", "target/assignments-1.0.jar",
        "ca.uwaterloo.cs451.a3.BuildInvertedIndexCompressed".format(username),
        "-input", "data/Shakespeare.txt", 
        "-output", "cs451-{0}-a3-index-shakespeare".format(username), "-reducers", str(reducers) ])
  print("\n\nQuestion 1.")
  call(["du", "-h", "cs451-{0}-a3-index-shakespeare".format(username)])
  print("\n\n")
  call(["hadoop", "jar", "target/assignments-1.0.jar",
        "ca.uwaterloo.cs451.a3.BooleanRetrievalCompressed".format(username),
        "-index", "cs451-{0}-a3-index-shakespeare".format(username),
        "-collection", "data/Shakespeare.txt", "-query", "outrageous fortune AND"])
  call(["hadoop", "jar", "target/assignments-1.0.jar",
        "ca.uwaterloo.cs451.a3.BooleanRetrievalCompressed".format(username),
        "-index", "cs451-{0}-a3-index-shakespeare".format(username), 
        "-collection", "data/Shakespeare.txt",
        "-query", "white red OR rose AND pluck AND"])

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="CS 451/651 A3 Public Check Script for Linux")
  parser.add_argument('username',metavar='[Github Username]', help="Github username",type=str)
  parser.add_argument('-r','--reducers',help="Number of reducers to use.",type=int,default=1)
  args=parser.parse_args()
  try:
    check_a3(args.username,args.reducers)
  except Exception as e:
    print(e)
