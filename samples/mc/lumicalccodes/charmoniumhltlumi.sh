#!/bin/bash

for hltname in HLT_Dimuon0_Jpsi3p5_Muon2_v HLT_Dimuon18_PsiPrime_noCorrL1_v HLT_Dimuon18_PsiPrime_v HLT_Dimuon25_Jpsi_noCorrL1_v HLT_Dimuon25_Jpsi_v HLT_DoubleMu2_Jpsi_DoubleTkMu0_Phi_v HLT_DoubleMu2_Jpsi_DoubleTrk1_Phi1p05_v HLT_DoubleMu4_JpsiTrkTrk_Displaced_v HLT_DoubleMu4_JpsiTrk_Displaced_v HLT_DoubleMu4_PsiPrimeTrk_Displaced_v HLT_DoubleMu4_3_Bs_v HLT_Mu30_TkMu0_Psi_v
do
brilcalc lumi --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json -u /fb -i Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt --hltpath=""$hltname"*" --output-style csv > "$hltname".csv
done
