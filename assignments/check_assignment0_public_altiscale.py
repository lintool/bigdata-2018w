#!/usr/bin/python
"""
CS 451 Data-Intensive Distributed Computing (Winter 2018):
Assignment 0 public check script for Altiscale

Sample usage:
$ ./check_assignment0_public_altiscale.py lintool
"""

import sys
import os
from subprocess import call
import re

def check_a0(u):
  """Run assignment0 in linux environment"""
  call(["mvn", "clean", "package"])
  call(["hadoop", "jar", "target/assignments-1.0.jar",
        "ca.uwaterloo.cs451.a0.PerfectX",
        "-input", "/shared/uwaterloo/cs451/data/enwiki-20161220-sentences-0.1sample.txt",
        "-output", "cs451-"+u+"-a0-wiki" ])
  print("Question 5.")
  call("hadoop fs -cat cs451-"+u+"-a0-wiki/part* | sort -k 2 -n -r | head -10",shell=True)

if __name__ == "__main__":
  try:
    if len(sys.argv) < 2:
        print "usage: "+sys.argv[0]+" [github-username]"
        exit(1)
    check_a0(sys.argv[1])
  except Exception as e:
    print(e)
