#!/usr/bin/python
"""
CS 451 Data-Intensive Distributed Computing (Winter 2018):
Assignment 2 public check script for Altiscale

Sample usage:
$ ./check_assignment2_public_altiscale.py lintool
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
  """Run Assignment 2 on Altiscale"""
  call(["mvn", "clean", "package"])
  call([ "spark-submit", "--class", "ca.uwaterloo.cs451.a2.ComputeBigramRelativeFrequencyPairs",
         "--num-executors", "2", "--executor-cores", "4", "--executor-memory", "24G", "target/assignments-1.0.jar",
         "--input", "/shared/uwaterloo/cs451/data/enwiki-20161220-sentences-0.1sample.txt",
         "--output", "cs451-"+u+"-a2-wiki-bigram-pairs", "--reducers", "8"])
  call([ "spark-submit", "--class", "ca.uwaterloo.cs451.a2.ComputeBigramRelativeFrequencyStripes",
         "--num-executors", "2", "--executor-cores", "4", "--executor-memory", "24G", "target/assignments-1.0.jar",
         "--input", "/shared/uwaterloo/cs451/data/enwiki-20161220-sentences-0.1sample.txt",
         "--output", "cs451-"+u+"-a2-wiki-bigram-stripes", "--reducers", "8"])
  call([ "spark-submit", "--class", "ca.uwaterloo.cs451.a2.PairsPMI",
         "--num-executors", "2", "--executor-cores", "4", "--executor-memory", "24G", "target/assignments-1.0.jar",
         "--input", "/shared/uwaterloo/cs451/data/simplewiki-20161220-sentences.txt",
         "--output", "cs451-"+u+"-a2-wiki-pmi-pairs", "--reducers", "8", "--threshold", "10"])
  call([ "spark-submit", "--class", "ca.uwaterloo.cs451.a2.StripesPMI",
         "--num-executors", "2", "--executor-cores", "4", "--executor-memory", "24G", "target/assignments-1.0.jar",
         "--input", "/shared/uwaterloo/cs451/data/simplewiki-20161220-sentences.txt",
         "--output", "cs451-"+u+"-a2-wiki-pmi-stripes", "--reducers", "8", "--threshold", "10"])
  print("\n\nBigram pairs:")
  call("hadoop fs -cat cs451-"+u+"-a2-wiki-bigram-pairs/part-0000* | grep '((dream,' | sort | head", shell=True, stderr=DEVNULL)
  print("\n\nBigram stripes:")
  call("hadoop fs -cat cs451-"+u+"-a2-wiki-bigram-stripes/part-0000* | grep '(dream,'", shell=True, stderr=DEVNULL)
  print("\n\nPMI pairs:")
  call("hadoop fs -cat cs451-"+u+"-a2-wiki-pmi-pairs/part-0000* | grep '((dream,' | sort | head", shell=True, stderr=DEVNULL)
  print("\n\nPMI stripes:")
  call("hadoop fs -cat cs451-"+u+"-a2-wiki-pmi-stripes/part-0000* | grep '(dream,'", shell=True, stderr=DEVNULL)
  print("")

if __name__ == "__main__":
  try:
    if len(sys.argv) < 2:
        print "usage: "+sys.argv[0]+" [github-username]"
        exit(1)
    check_a2(sys.argv[1])
  except Exception as e:
    print(e)
