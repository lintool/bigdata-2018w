#!/usr/bin/python
"""
CS 451 Data-Intensive Distributed Computing (Winter 2018):
Assignment 0 public check script for the Linux Student CS environment

Sample usage:
$ ./check_assignment0_public_linux.py lintool
"""

import sys
import os
from subprocess import call
import re

def check_a0(u):
  """Run Assignment 0 in the Linux Student CS environment"""
  call(["mvn", "clean", "package"])
  call(["hadoop", "jar", "target/assignments-1.0.jar",
        "ca.uwaterloo.cs451.a0.PerfectX",
        "-input", "data/Shakespeare.txt",
        "-output", "cs451-"+u+"-a0-shakespeare" ])
  print("Question 1.")
  call("hadoop fs -cat cs451-"+u+"-a0-shakespeare/part-r-00000 | sort -k 2 -n -r | head -1", shell=True)

if __name__ == "__main__":
  try:
    if len(sys.argv) < 2:
        print "usage: "+sys.argv[0]+" [github-username]"
        exit(1)
    check_a0(sys.argv[1])
  except Exception as e:
    print(e)
