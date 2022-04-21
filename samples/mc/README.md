# Setup
First of all CMSSW release
```bash
cmsrel CMSSW_11_2_4_patch1

cd CMSSW_11_2_4_patch1/src

cmsenv
```
Now we need to import our own generator interface pkg

```bash
git cms-addpkg GeneratorInterface/EvtGenInterface

scram b -j 4
```
Now we need to add the evt_2014.pdl DECAY_2014_NOLONGLIFE.DEC and Modifiedincl_BtoJpsi_mumu.dec
```bash
cd GeneratorInterface/EvtGenInterface/data/

wget -O DECAY_2014_NOLONGLIFE.DEC https://raw.githubusercontent.com/cms-data/GeneratorInterface-EvtGenInterface/master/DECAY_2014_NOLONGLIFE.DEC

wget -O evt_2014.pdl https://raw.githubusercontent.com/cms-data/GeneratorInterface-EvtGenInterface/master/evt_2014.pdl

wget -O Modifiedincl_BtoJpsi_mumu.dec https://raw.githubusercontent.com/jay-odedra/Run3TriggerPerf-1/charmoniummcedit/samples/mc/Modifiedincl_BtoJpsi_mumu.dec