#!/bin/bash
export X509_USER_PROXY=$1

cd /eos/user/j/jodedra/charmoniumanalysis/CMSSW_12_1_0/src/Run3TriggerPerf-1/analysis

eval `scramv1 runtime -sh`

python3 analysis.py @/eos/user/j/jodedra/charmoniumanalysis/CMSSW_12_1_0/src/Run3TriggerPerf-1/analysis/outputcharmonium0"$2".txt -o puritycheckcharm"$2".root

mv puritycheckcharm"$2".root /eos/user/j/jodedra/charmoniumanalysis/CMSSW_12_1_0/src/Run3TriggerPerf-1/analysis/charmoniumoutputs/
