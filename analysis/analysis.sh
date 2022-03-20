#!/bin/bash
export X509_USER_PROXY=$1

cd /afs/cern.ch/user/j/jodedra/CMSSW_12_3_0_pre5/src/week113032022/Run3TriggerPerf-1/analysis/

eval `scramv1 runtime -sh`

python3 analysis.py @/afs/cern.ch/user/j/jodedra/CMSSW_12_3_0_pre5/src/week113032022/Run3TriggerPerf-1/analysis/completefilenamesforuse/fullfilenamedatasetroot"$2".txt -o puritycheck"$2".root

mv puritycheck"$2".root /afs/cern.ch/user/j/jodedra/CMSSW_12_3_0_pre5/src/week113032022/Run3TriggerPerf-1/analysis/alloutputs/output"$2"/
