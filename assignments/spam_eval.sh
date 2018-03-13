#!/bin/bash

files=${1}
cat ${files}/part-* | tr ',' ' ' | tr -d '()' | sed -e 's_ham_1_g' -e 's_spam_2_g' | sort -k3,3gr -t ' ' | ./compute_spam_metrics
