#!/usr/bin/python
"""
CS 451 Data-Intensive Distributed Computing (Winter 2018):
Assignment 2 public check script for the Linux Student CS environment

Sample usage:
$ ./check_assignment2_public_linux.py lintool
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

def check_a2(u):
  """Run Assignment 2 in the Linux Student CS environment"""
  call(["mvn", "clean", "package"])
  call([ "spark-submit", "--class", "ca.uwaterloo.cs451.a2.ComputeBigramRelativeFrequencyPairs",
         "target/assignments-1.0.jar", "--input", "data/Shakespeare.txt",
         "--output", "cs451-"+u+"-a2-shakespeare-bigrams-pairs", "--reducers", "5"])
  call([ "spark-submit", "--class", "ca.uwaterloo.cs451.a2.ComputeBigramRelativeFrequencyStripes",
         "target/assignments-1.0.jar", "--input", "data/Shakespeare.txt",
         "--output", "cs451-"+u+"-a2-shakespeare-bigrams-stripes", "--reducers", "5"])
  call([ "spark-submit", "--class", "ca.uwaterloo.cs451.a2.PairsPMI",
         "target/assignments-1.0.jar", "--input", "data/Shakespeare.txt",
         "--output", "cs451-"+u+"-a2-shakespeare-pmi-pairs", "--reducers", "5", "--threshold", "10"])
  call([ "spark-submit", "--class", "ca.uwaterloo.cs451.a2.StripesPMI",
         "target/assignments-1.0.jar", "--input", "data/Shakespeare.txt",
         "--output", "cs451-"+u+"-a2-shakespeare-pmi-stripes", "--reducers", "5", "--threshold", "10"])
  print("\n\nBigram pairs:")
  call("hadoop fs -cat cs451-"+u+"-a2-shakespeare-bigrams-pairs/part-0000* | grep '((dream,' | sort | head", shell=True, stderr=DEVNULL)
  print("\n\nBigram stripes:")
  call("hadoop fs -cat cs451-"+u+"-a2-shakespeare-bigrams-stripes/part-0000* | grep '(dream,'", shell=True, stderr=DEVNULL)
  print("\n\nPMI pairs:")
  call("hadoop fs -cat cs451-"+u+"-a2-shakespeare-pmi-pairs/part-0000* | grep '((dream,' | sort | head", shell=True, stderr=DEVNULL)
  print("\n\nPMI stripes:")
  call("hadoop fs -cat cs451-"+u+"-a2-shakespeare-pmi-stripes/part-0000* | grep '(dream,'", shell=True, stderr=DEVNULL)
  print("")

if __name__ == "__main__":
  try:
    if len(sys.argv) < 2:
        print "usage: "+sys.argv[0]+" [github-username]"
        exit(1)
    check_a2(sys.argv[1])
  except Exception as e:
    print(e)
