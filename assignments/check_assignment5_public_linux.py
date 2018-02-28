#!/usr/bin/python
"""
CS 451 Data-Intensive Distributed Computing (Winter 2018):
Assignment 5 public check script for the Linux Student CS environment

Sample usage:
$ ./check_assignment5_public_linux.py lintool
"""

import sys
import os
from subprocess import call
import re

def check_a5(u):
    """Run Assignment 5 in the Linux Student CS environment"""
    call(["mvn", "clean", "package"])

    call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q1",
 	  "target/assignments-1.0.jar", "--input", "TPC-H-0.1-TXT", "--date", "1996-01-01", "--text"])

    call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q1",
          "target/assignments-1.0.jar", "--input", "TPC-H-0.1-PARQUET", "--date", "1996-01-01", "--parquet"])

    call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q2",
 	  "target/assignments-1.0.jar", "--input", "TPC-H-0.1-TXT", "--date", "1996-01-01", "--text"])

    call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q2",
          "target/assignments-1.0.jar", "--input", "TPC-H-0.1-PARQUET", "--date", "1996-01-01", "--parquet"])

    call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q3",
 	  "target/assignments-1.0.jar", "--input", "TPC-H-0.1-TXT", "--date", "1996-01-01", "--text"])

    call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q3",
          "target/assignments-1.0.jar", "--input", "TPC-H-0.1-PARQUET", "--date", "1996-01-01", "--parquet"])

    call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q4",
 	  "target/assignments-1.0.jar", "--input", "TPC-H-0.1-TXT", "--date", "1996-01-01", "--text"])
    
    call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q4",
          "target/assignments-1.0.jar", "--input", "TPC-H-0.1-PARQUET", "--date", "1996-01-01", "--parquet"])

    call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q5",
 	  "target/assignments-1.0.jar", "--input", "TPC-H-0.1-TXT", "--text"])

    call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q5",
          "target/assignments-1.0.jar", "--input", "TPC-H-0.1-PARQUET", "--parquet"])

    call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q6",
 	  "target/assignments-1.0.jar", "--input", "TPC-H-0.1-TXT", "--date", "1996-01-01", "--text"])

    call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q6",
          "target/assignments-1.0.jar", "--input", "TPC-H-0.1-PARQUET", "--date", "1996-01-01", "--parquet"])

    call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q7",
 	  "target/assignments-1.0.jar", "--input", "TPC-H-0.1-TXT", "--date", "1996-01-01", "--text"])
    
    call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q7",
          "target/assignments-1.0.jar", "--input", "TPC-H-0.1-PARQUET", "--date", "1996-01-01", "--parquet"])

if __name__ == "__main__":
  try:
    if len(sys.argv) < 2:
        print "usage: "+sys.argv[0]+" [github-username]"
        exit(1)
    check_a5(sys.argv[1])
  except Exception as e:
    print(e)
