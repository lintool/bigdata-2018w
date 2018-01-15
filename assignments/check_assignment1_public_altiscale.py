#!/usr/bin/python
"""
CS 451 Data-Intensive Distributed Computing (Winter 2018):
Assignment 1 public check script for Altiscale

Sample usage:
$ ./check_assignment1_public_altiscale.py lintool
"""

import sys
import os
from subprocess import call
import re

def check_a1(u):
  """Run Assignment 0 on Altiscale"""
  call(["mvn", "clean", "package"])

  call([ "hadoop", "jar", "target/assignments-1.0.jar", "ca.uwaterloo.cs451.a1.PairsPMI",
         "-input", "/shared/uwaterloo/cs451/data/simplewiki-20161220-sentences.txt",
         "-output", "cs451-"+u+"-a1-wiki-pairs", "-reducers", "5", "-threshold", "50"])
  call([ "hadoop", "jar", "target/assignments-1.0.jar", "ca.uwaterloo.cs451.a1.StripesPMI",
         "-input", "/shared/uwaterloo/cs451/data/simplewiki-20161220-sentences.txt",
         "-output", "cs451-"+u+"-a1-wiki-stripes", "-reducers", "5", "-threshold", "50"])
  print("\n\nQuestion 7.")
  call("hadoop fs -cat cs451-"+u+"-a1-wiki-pairs/part-r-0000* | grep '(hockey,' | sort -t'(' -k 3 -n -r | head -5",shell=True)
  print("\n\nQuestion 8.")
  call("hadoop fs -cat cs451-"+u+"-a1-wiki-pairs/part-r-0000* | grep '(data,' | sort -t'(' -k 3 -n -r | head -5",shell=True)
  print("");

if __name__ == "__main__":
  try:
    if len(sys.argv) < 2:
        print "usage: "+sys.argv[0]+" [github-username]"
        exit(1)
    check_a1(sys.argv[1])
  except Exception as e:
    print(e)
