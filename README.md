```bash
cmsrel CMSSW_12_1_0
cd CMSSW_12_1_0/src
cmsenv
git cms-init
git cms-addpkg HLTrigger/Configuration
git cms-merge-topic Sam-Harper:EGHLTCustomisation_1130pre4
```
```bash
scram b -j8
```
```bash
hltGetConfiguration /users/swmukher/testv3/egm_ele5_open/V2 --setup /dev/CMSSW_12_1_0/GRun --globaltag auto:run3_hlt --input root://cms-xrd-global.cern.ch///store/data/Run2018B/ParkingBPH5/RAW/v1/000/317/488/00000/0009AF7C-3669-E811-A47D-FA163EC57F99.root --data --process MYHLT --unprescale --max-events 20 --output none --customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2018Input,HLTrigger/Configuration/customizeHLTforEGamma.customiseEGammaMenuDev --l1-emulator uGT   --l1 L1Menu_Collisions2018_v2_1_0-d1_xml > hltdevpath.py

cmsRun hltdevpath.py    #just to check no errors
```
usually you would have to copy hltdevpath.py to dir but this github repo has correct version included. The hltdevpath.py included in this repo has some extra code to make outputs work during crab jobs.

```bash
git clone git@github.com:jay-odedra/Run3TriggerPerf-1.git
cd Run3TriggerPerf-1/
git checkout origin/branchForRobExtendedMiniAOD
cd samples/data/
```
Then submit job, check crab file points to correct miniaod and raw files

```bash
PROXY=(DIR TO GRID CERTIFICATE)
crab submit --proxy=$PROXY crab.py
```

job submitted
