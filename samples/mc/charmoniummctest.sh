#!/bin/bash
export X509_USER_PROXY=$1

cd /afs/cern.ch/user/j/jodedra/charmoniumMC/CMSSW_11_2_4_patch1/src/Run3TriggerPerf-1/samples/mc/

eval `scramv1 runtime -sh`

report_name.xml

cmsRun -e -j report_name.xml GS_CharmoniumbtojpsiKll.py

mv report_name.xml /afs/cern.ch/user/j/jodedra/charmoniumMC/CMSSW_11_2_4_patch1/src/Run3TriggerPerf-1/samples/mc/