#!/bin/bash
export X509_USER_PROXY=$1

cd /afs/cern.ch/user/j/jodedra/CharmoniumDataMuonselection/CMSSW_12_1_0/src/Run3TriggerPerf-1/analysis/

eval `scramv1 runtime -sh`

python3 muonanalysischarmoniumelectronside.py @/afs/cern.ch/user/j/jodedra/CharmoniumDataMuonselection/CMSSW_12_1_0/src/Run3TriggerPerf-1/analysis/outputcharmonium"$2".txt -o puritycheckcharmelectronside"$2".root

mv puritycheckcharmelectronside"$2".root /afs/cern.ch/user/j/jodedra/CharmoniumDataMuonselection/CMSSW_12_1_0/src/Run3TriggerPerf-1/analysis/charmoniumoutputs/