#!/usr/bin/python
"""
CS 451 Data-Intensive Distributed Computing (Winter 2018):
Assignment 1 public check script for the Linux Student CS environment

Sample usage:
$ ./check_assignment1_public_linux.py lintool
"""

import sys
import os
from subprocess import call
import re

try:
  from subprocess import DEVNULL # py3k
except ImportError:
  import os
  DEVNULL = open(os.devnull, 'wb')

def check_a1(u):
  """Run Assignment 1 in the Linux Student CS environment"""
  call(["mvn", "clean", "package"])
  call([ "hadoop", "jar", "target/assignments-1.0.jar", "ca.uwaterloo.cs451.a1.PairsPMI",
         "-input", "data/Shakespeare.txt",
         "-output", "cs451-"+u+"-a1-shakespeare-pairs", "-reducers", "5", "-threshold", "10"])
  call([ "hadoop", "jar", "target/assignments-1.0.jar", "ca.uwaterloo.cs451.a1.StripesPMI",
         "-input", "data/Shakespeare.txt",
         "-output", "cs451-"+u+"-a1-shakespeare-stripes", "-reducers", "5", "-threshold", "10"])
  print("\n\nQuestion 4.")
  call("hadoop fs -cat cs451-"+u+"-a1-shakespeare-pairs/part-r-0000* | wc", shell=True)
  print("\n\nQuestion 5. (highest PMI)")
  call("hadoop fs -cat cs451-"+u+"-a1-shakespeare-pairs/part-r-0000* | sort -t'(' -k 3 -g -r | head -2", shell=True, stderr=DEVNULL)
  print("\n\nQuestion 5. (lowest PMI)")
  call("hadoop fs -cat cs451-"+u+"-a1-shakespeare-pairs/part-r-0000* | sort -t'(' -k 3 -g | head -2", shell=True, stderr=DEVNULL)
  print("\n\nQuestion 6. ('tears')")
  call("hadoop fs -cat cs451-"+u+"-a1-shakespeare-pairs/part-r-0000* | grep '(tears,' | sort -t'(' -k 3 -g -r | head -3", shell=True)
  print("\n\nQuestion 6. ('death')")
  call("hadoop fs -cat cs451-"+u+"-a1-shakespeare-pairs/part-r-0000* | grep '(death,' | sort -t'(' -k 3 -g -r | head -3", shell=True)
  print("")

if __name__ == "__main__":
  try:
    if len(sys.argv) < 2:
        print "usage: "+sys.argv[0]+" [github-username]"
        exit(1)
    check_a1(sys.argv[1])
  except Exception as e:
    print(e)
