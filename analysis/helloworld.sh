#!/bin/bash
export X509_USER_PROXY=$1
voms-proxy-info -all
voms-proxy-info -all -file $1
echo $1
python3 /afs/cern.ch/user/j/jodedra/CMSSW_12_3_X_2022-02-28-1100/src/test/Run3TriggerPerf-1/analysis/helloworld.py
