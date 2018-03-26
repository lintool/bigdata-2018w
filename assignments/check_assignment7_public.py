#!/usr/bin/python
"""
CS 451 Data-Intensive Distributed Computing (Winter 2018):
Assignment 7 public check script

Sample usage:
$ ./check_assignment7_public.py
"""

import sys
import os
from subprocess import call
import argparse
import re

def check_a7(username, memory):
  spark_cmd = "spark-submit"
  data_prefix = "/u3/cs451/public_html/taxi-data"

  print("0. maven")
  call(["mvn","clean","package"])
  print("1. EventCount")
  call([spark_cmd,"--driver-memory",memory,
         "--class", "ca.uwaterloo.cs451.a7.EventCount",
         "target/assignments-1.0.jar", "--input", "{0}".format(data_prefix),
         "--checkpoint", "cs451-lintool-checkpoint-q{}".format(1),
         "--output", "output_{}/cs451-{}-output-q{}".format(1, username, 1)])
  print("2. RegionalEventCount")
  call([spark_cmd,"--driver-memory",memory,
         "--class", "ca.uwaterloo.cs451.a7.RegionEventCount",
         "target/assignments-1.0.jar", "--input", "{0}".format(data_prefix),
         "--checkpoint", "cs451-lintool-checkpoint-q{}".format(2),
         "--output", "output_{}/cs451-{}-output-q{}".format(2, username, 2)])
  print("3. TrendingQuery")
  call([spark_cmd,"--driver-memory",memory,
         "--class", "ca.uwaterloo.cs451.a7.TrendingArrivals",
         "target/assignments-1.0.jar", "--input", "{0}".format(data_prefix),
         "--checkpoint", "cs451-lintool-checkpoint-q{}".format(3),
         "--output", "output_{}/cs451-{}-output-q{}".format(3, username, 3)])

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="CS 451 Winter 2018 Assignment7 Public Test Script")
  parser.add_argument('username',metavar='Github Username', help="Github username",type=str)
  parser.add_argument('-m','--memory',help="Amount of memory to give Spark jobs",type=str,default="2G")
  args=parser.parse_args()
  try:
    check_a7(args.username, args.memory)
  except Exception as e:
    print(e)