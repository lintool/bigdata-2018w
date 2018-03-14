#!/usr/bin/python
"""
CS 451 Data-Intensive Distributed Computing (Winter 2018):
Assignment 6 public check script

Sample usage:
$ ./check_assignment6_public.py lintool --env linux
"""

import sys
import os
from subprocess import call
import argparse
import re

def check_a6(pn,memory, env,iterations):
  spark_cmd = "spark-submit"
  cp_cmd = ["cp"]
  mkdir_cmd = ["mkdir"]
  eval_cmd = "spam_eval.sh"
  data_prefix = "/u3/cs451/public_html/spam"
  if env != 'linux':
    cp_cmd = ["hadoop","fs", "-cp"]
    mkdir_cmd = ["hadoop","fs","-mkdir"]
    eval_cmd = "spam_eval_hdfs.sh"
    data_prefix = "/shared/uwaterloo/cs451/data"

  print("0. maven")
  call(["mvn","clean","package"])
  print("1. Train and Classify with Group-X")
  call([spark_cmd,"--driver-memory",memory,
         "--class", "ca.uwaterloo.cs451.a6.TrainSpamClassifier".format(pn),
         "target/assignments-1.0.jar", "--input", "{0}/spam.train.group_x.txt".format(data_prefix), 
         "--model", "cs451-{0}-a6-model-group_x".format(pn)])
  call([ spark_cmd,"--driver-memory",memory,
         "--class", "ca.uwaterloo.cs451.a6.ApplySpamClassifier".format(pn),
         "target/assignments-1.0.jar", "--input", "{0}/spam.test.qrels.txt".format(data_prefix), 
         "--model", "cs451-{0}-a6-model-group_x".format(pn),
         "--output", "cs451-{0}-a6-output-group_x".format(pn)])
  print("2. Train and Classify with Group-Y")
  call([ spark_cmd,"--driver-memory",memory,
         "--class", "ca.uwaterloo.cs451.a6.TrainSpamClassifier".format(pn),
         "target/assignments-1.0.jar", "--input", "{0}/spam.train.group_y.txt".format(data_prefix), 
         "--model", "cs451-{0}-a6-model-group_y".format(pn)])
  call([ spark_cmd,"--driver-memory",memory,
         "--class", "ca.uwaterloo.cs451.a6.ApplySpamClassifier".format(pn),
         "target/assignments-1.0.jar", "--input", "{0}/spam.test.qrels.txt".format(data_prefix),
         "--model", "cs451-{0}-a6-model-group_y".format(pn),
         "--output", "cs451-{0}-a6-output-group_y".format(pn)])
  print("3. Train and Classify with Britney")
  call([ spark_cmd,"--driver-memory",memory,
         "--class", "ca.uwaterloo.cs451.a6.TrainSpamClassifier".format(pn),
         "target/assignments-1.0.jar", "--input", "{0}/spam.train.britney.txt".format(data_prefix), 
         "--model", "cs451-{0}-a6-model-britney".format(pn)])
  call([ spark_cmd,"--driver-memory",memory,
         "--class", "ca.uwaterloo.cs451.a6.ApplySpamClassifier".format(pn),
         "target/assignments-1.0.jar", "--input", "{0}/spam.test.qrels.txt".format(data_prefix),
         "--model", "cs451-{0}-a6-model-britney".format(pn),
         "--output", "cs451-{0}-a6-output-britney".format(pn)])
  print("4. Evaluate Group-X, Group-Y, and Britney")
  call(["bash",eval_cmd,"cs451-{0}-a6-output-group_x".format(pn)])
  call(["bash",eval_cmd,"cs451-{0}-a6-output-group_y".format(pn)])
  call(["bash",eval_cmd,"cs451-{0}-a6-output-britney".format(pn)])
  raw_input('Press <ENTER> to continue.')
  print("5. Voting Ensemble Classify and Evaluate")
  call(mkdir_cmd +["cs451-{0}-a6-model-fusion".format(pn)])
  call(cp_cmd + ["cs451-{0}-a6-model-group_x/part-00000".format(pn), "cs451-{0}-a6-model-fusion/part-00000".format(pn)])
  call(cp_cmd + ["cs451-{0}-a6-model-group_y/part-00000".format(pn), "cs451-{0}-a6-model-fusion/part-00001".format(pn)])
  call(cp_cmd + ["cs451-{0}-a6-model-britney/part-00000".format(pn), "cs451-{0}-a6-model-fusion/part-00002".format(pn)])
  call([ spark_cmd,"--driver-memory",memory,
         "--class", "ca.uwaterloo.cs451.a6.ApplyEnsembleSpamClassifier".format(pn),
         "target/assignments-1.0.jar", "--input", "{0}/spam.test.qrels.txt".format(data_prefix),
         "--model", "cs451-{0}-a6-model-fusion".format(pn),
         "--output", "cs451-{0}-a6-output-fusion-average".format(pn),
         "--method","average"])
  call([spark_cmd,"--driver-memory",memory,
         "--class", "ca.uwaterloo.cs451.a6.ApplyEnsembleSpamClassifier".format(pn),
         "target/assignments-1.0.jar", "--input", "{0}/spam.test.qrels.txt".format(data_prefix),
         "--model", "cs451-{0}-a6-model-fusion".format(pn),
         "--output", "cs451-{0}-a6-output-fusion-voting".format(pn),
         "--method","vote"])
  call(["bash",eval_cmd,"cs451-{0}-a6-output-fusion-average".format(pn)])
  call(["bash",eval_cmd,"cs451-{0}-a6-output-fusion-voting".format(pn)])
  raw_input('Press <ENTER> to continue.')
  print("6. Training, Test, and Evaluate on All Data")
  call([ spark_cmd,"--driver-memory",memory,
         "--class", "ca.uwaterloo.cs451.a6.TrainSpamClassifier".format(pn),
         "target/assignments-1.0.jar", "--input", "{0}/spam.train.all.txt".format(data_prefix), 
         "--model", "cs451-{0}-a6-model-all".format(pn)])
  call([ spark_cmd,"--driver-memory",memory,
         "--class", "ca.uwaterloo.cs451.a6.ApplySpamClassifier".format(pn),
         "target/assignments-1.0.jar", "--input", "{0}/spam.test.qrels.txt".format(data_prefix),
         "--model", "cs451-{0}-a6-model-all".format(pn),
         "--output", "cs451-{0}-a6-output-all".format(pn)])
  call(["bash",eval_cmd,"cs451-{0}-a6-output-all".format(pn)])
  raw_input('Press <ENTER> to continue.')
  print("6. Data Shuffling ({0} Iterations)".format(iterations))
  for i in range(iterations):
    call([ spark_cmd,"--driver-memory",memory,
           "--class", "ca.uwaterloo.cs451.a6.TrainSpamClassifier".format(pn),
           "target/assignments-1.0.jar", "--input", "{0}/spam.train.britney.txt".format(data_prefix), 
           "--model", "cs451-{0}-a6-model-britney-shuffle".format(pn),
           "--shuffle"])
    call([ spark_cmd,"--driver-memory",memory,
           "--class", "ca.uwaterloo.cs451.a6.ApplySpamClassifier".format(pn),
           "target/assignments-1.0.jar", "--input", "{0}/spam.test.qrels.txt".format(data_prefix),
           "--model", "cs451-{0}-a6-model-britney-shuffle".format(pn),
           "--output", "cs451-{0}-a6-output-britney-shuffle".format(pn)])
    call(["bash",eval_cmd,"cs451-{0}-a6-output-britney-shuffle".format(pn)])
    raw_input('Press <ENTER> to continue.')

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="CS 451 Winter 2018 Assignment 6 Public Test Script")
  parser.add_argument('username',metavar='Github Username', help="Github username",type=str)
  parser.add_argument('-m','--memory',help="Amount of memory to give Spark jobs",type=str,default="2G")
  parser.add_argument('-e', '--env', help='Environment to test under.',type=str,default='linux')
  parser.add_argument('-i', '--iterations', help='Number of shuffle iterations',type=int,default=1)
  args=parser.parse_args()
  try:
    check_a6(args.username, args.memory,args.env,args.iterations)
  except Exception as e:
    print(e)
