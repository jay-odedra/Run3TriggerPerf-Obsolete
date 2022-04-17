#!/bin/bash
export X509_USER_PROXY=$1

cd /afs/cern.ch/user/j/jodedra/gentry/CMSSW_11_2_4_patch1/src/

eval `scramv1 runtime -sh`

cmsRun GeneratorInterface/Core/test/runGenFilterEfficiencyAnalyzer_cfg.py > loooool.txt
