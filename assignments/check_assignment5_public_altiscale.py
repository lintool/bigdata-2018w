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

def check_a5(u):
    """Run Assignment 5 on Altiscale"""
    call(["mvn","clean","package"])

    with open("q1t.out", "w") as outfile:
        call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q1", "--deploy-mode", "client",
              "--num-executors", "4", "--executor-cores", "4", "--executor-memory", "32G", "--driver-memory", "2g",
              "target/assignments-1.0.jar", "--input", "/shared/uwaterloo/cs451/data/TPC-H-10-TXT",
              "--date", "1996-01-01", "--text"], stdout=outfile)

    with open("q1p.out", "w") as outfile:
        call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q1", "--deploy-mode", "client",
              "--num-executors", "4", "--executor-cores", "4", "--executor-memory", "32G", "--driver-memory", "2g",
              "target/assignments-1.0.jar", "--input", "/shared/uwaterloo/cs451/data/TPC-H-10-PARQUET",
              "--date", "1996-01-01", "--parquet"], stdout=outfile)

    with open("q2t.out", "w") as outfile:
        call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q2", "--deploy-mode", "client",
              "--num-executors", "4", "--executor-cores", "4", "--executor-memory", "32G", "--driver-memory", "2g",
              "target/assignments-1.0.jar", "--input", "/shared/uwaterloo/cs451/data/TPC-H-10-TXT",
              "--date", "1996-01-01", "--text"], stdout=outfile)

    with open("q2p.out", "w") as outfile:
        call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q2", "--deploy-mode", "client",
              "--num-executors", "4", "--executor-cores", "4", "--executor-memory", "32G", "--driver-memory", "2g",
              "target/assignments-1.0.jar", "--input", "/shared/uwaterloo/cs451/data/TPC-H-10-PARQUET",
              "--date", "1996-01-01", "--parquet"], stdout=outfile)

    with open("q3t.out", "w") as outfile:
        call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q3", "--deploy-mode", "client",
              "--num-executors", "4", "--executor-cores", "4", "--executor-memory", "32G", "--driver-memory", "2g",
              "target/assignments-1.0.jar", "--input", "/shared/uwaterloo/cs451/data/TPC-H-10-TXT",
              "--date", "1996-01-01", "--text"], stdout=outfile)

    with open("q3p.out", "w") as outfile:
        call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q3", "--deploy-mode", "client",
              "--num-executors", "4", "--executor-cores", "4", "--executor-memory", "32G", "--driver-memory", "2g",
              "target/assignments-1.0.jar", "--input", "/shared/uwaterloo/cs451/data/TPC-H-10-PARQUET",
              "--date", "1996-01-01", "--parquet"], stdout=outfile)

    with open("q4t.out", "w") as outfile:
        call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q4", "--deploy-mode", "client",
              "--num-executors", "4", "--executor-cores", "4", "--executor-memory", "32G", "--driver-memory", "2g",
              "target/assignments-1.0.jar", "--input", "/shared/uwaterloo/cs451/data/TPC-H-10-TXT",
              "--date", "1996-01-01", "--text"], stdout=outfile)

    with open("q4p.out", "w") as outfile:
        call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q4", "--deploy-mode", "client",
              "--num-executors", "4", "--executor-cores", "4", "--executor-memory", "32G", "--driver-memory", "2g",
              "target/assignments-1.0.jar", "--input", "/shared/uwaterloo/cs451/data/TPC-H-10-PARQUET",
              "--date", "1996-01-01", "--parquet"], stdout=outfile)

    with open("q5t.out", "w") as outfile:
        call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q5", "--deploy-mode", "client",
              "--num-executors", "4", "--executor-cores", "4", "--executor-memory", "32G", "--driver-memory", "2g",
              "target/assignments-1.0.jar", "--input", "/shared/uwaterloo/cs451/data/TPC-H-10-TXT", "--text"], stdout=outfile)

    with open("q5p.out", "w") as outfile:
        call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q5", "--deploy-mode", "client",
              "--num-executors", "4", "--executor-cores", "4", "--executor-memory", "32G", "--driver-memory", "2g",
              "target/assignments-1.0.jar", "--input", "/shared/uwaterloo/cs451/data/TPC-H-10-PARQUET", "--parquet"], stdout=outfile)

    with open("q6t.out", "w") as outfile:
        call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q6", "--deploy-mode", "client",
              "--num-executors", "4", "--executor-cores", "4", "--executor-memory", "32G", "--driver-memory", "2g",
              "target/assignments-1.0.jar", "--input", "/shared/uwaterloo/cs451/data/TPC-H-10-TXT",
              "--date", "1996-01-01", "--text"], stdout=outfile)

    with open("q6p.out", "w") as outfile:
        call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q6", "--deploy-mode", "client",
              "--num-executors", "4", "--executor-cores", "4", "--executor-memory", "32G", "--driver-memory", "2g",
              "target/assignments-1.0.jar", "--input", "/shared/uwaterloo/cs451/data/TPC-H-10-PARQUET",
              "--date", "1996-01-01", "--parquet"], stdout=outfile)

    with open("q7t.out", "w") as outfile:
        call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q7", "--deploy-mode", "client",
              "--num-executors", "4", "--executor-cores", "4", "--executor-memory", "32G", "--driver-memory", "2g",
              "target/assignments-1.0.jar", "--input", "/shared/uwaterloo/cs451/data/TPC-H-10-TXT",
              "--date", "1996-01-01", "--text"], stdout=outfile)

    with open("q7p.out", "w") as outfile:
        call(["spark-submit", "--class", "ca.uwaterloo.cs451.a5.Q7", "--deploy-mode", "client",
              "--num-executors", "4", "--executor-cores", "4", "--executor-memory", "32G", "--driver-memory", "2g",
              "target/assignments-1.0.jar", "--input", "/shared/uwaterloo/cs451/data/TPC-H-10-PARQUET",
              "--date", "1996-01-01", "--parquet"], stdout=outfile)


if __name__ == "__main__":
  try:
    if len(sys.argv) < 2:
        print "usage: "+sys.argv[0]+" [github-username]"
        exit(1)
    check_a5(sys.argv[1])
  except Exception as e:
    print(e)
