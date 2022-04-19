#!/bin/bash
export X509_USER_PROXY=$1

cd /afs/cern.ch/user/j/jodedra/charmoniumanalysis/CMSSW_12_1_0/src/Run3TriggerPerf-1/analysis

eval `scramv1 runtime -sh`

python3 analysis.py @/afs/cern.ch/user/j/jodedra/charmoniumanalysis/CMSSW_12_1_0/src/Run3TriggerPerf-1/analysis/outputcharmonium"$2".txt -o puritycheckcharm"$2".root

mv puritycheckcharm"$2".root /afs/cern.ch/user/j/jodedra/charmoniumanalysis/CMSSW_12_1_0/src/Run3TriggerPerf-1/analysis/charmoniumoutputs/