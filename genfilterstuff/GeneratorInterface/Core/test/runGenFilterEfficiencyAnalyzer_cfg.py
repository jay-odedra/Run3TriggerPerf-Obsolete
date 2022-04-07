import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils


process = cms.Process("GenFilterEfficiency")

process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

mylist = FileUtils.loadListFromFile ('/afs/cern.ch/user/j/jodedra/gentry/CMSSW_11_2_4_patch1/src/reeereee.txt')
readFiles = cms.untracked.vstring( *mylist)

process.source = cms.Source("PoolSource",
    fileNames = readFiles
)

process.dummy = cms.EDAnalyzer("GenFilterEfficiencyAnalyzer",
                               genFilterInfoTag = cms.InputTag("genFilterEfficiencyProducer")
)

process.p = cms.Path(process.dummy)
