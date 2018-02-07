#!/usr/bin/python
"""
CS 451 Data-Intensive Distributed Computing (Winter 2018):
Assignment 4 public check script for Altiscale

Sample usage:
$ ./check_assignment4_public_altiscale.py lintool
"""

import sys
import os
from subprocess import call
import re

def check_assignment(u):
    """Run Assignment 4 on Altiscale"""
    call(["mvn","clean","package"])

    # First, convert the adjacency list into PageRank node records:
    call([ "hadoop","jar","target/assignments-1.0.jar",
           "ca.uwaterloo.cs451.a4.BuildPersonalizedPageRankRecords",
           "-input", "/shared/uwaterloo/cs451/data/wiki-adj",
           "-output", "cs451-"+u+"-a4-wiki-PageRankRecords",
           "-numNodes", "16117779", "-sources", "73273,73276" ])

    # Next, partition the graph (hash partitioning) and get ready to iterate:
    call("hadoop fs -mkdir cs451-"+u+"-a4-wiki-PageRank",shell=True)
    call([ "hadoop","jar","target/assignments-1.0.jar",
           "ca.uwaterloo.cs451.a4.PartitionGraph",
           "-input", "cs451-"+u+"-a4-wiki-PageRankRecords",
           "-output", "cs451-"+u+"-a4-wiki-PageRank/iter0000",
           "-numPartitions", "10", "-numNodes", "16117779" ])

    # After setting everything up, iterate multi-source personalized PageRank:
    call([ "hadoop","jar","target/assignments-1.0.jar",
           "ca.uwaterloo.cs451.a4.RunPersonalizedPageRankBasic",
           "-base", "cs451-"+u+"-a4-wiki-PageRank",
           "-numNodes", "16117779", "-start", "0", "-end", "20", "-sources", "73273,73276" ])

    # Finally, run a program to extract the top ten personalized PageRank values, with respect to each source.
    call([ "hadoop","jar","target/assignments-1.0.jar",
           "ca.uwaterloo.cs451.a4.ExtractTopPersonalizedPageRankNodes",
           "-input", "cs451-"+u+"-a4-wiki-PageRank/iter0020",
           "-output", "cs451-"+u+"-a4-wiki-PageRank-top10",
           "-top", "10", "-sources", "73273,73276" ])


if __name__ == "__main__":
  try:
    if len(sys.argv) < 2:
        print "usage: "+sys.argv[0]+" [github-username]"
        exit(1)
    check_assignment(sys.argv[1])
  except Exception as e:
    print(e)
