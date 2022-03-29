from CRABClient.UserUtilities import config 
config = config()

config.General.requestName = 'JpsiK_20222903_MiniAOD'
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'EGM-Run3Winter21DRMiniAOD-00021_2_cfg.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset ='/BuToKJpsi_Toee_2021206/jodedra-SPRING22_HLTRAW-e883a391f51bce07095a9ce0ff860c5b/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

config.Data.outLFNDirBase = '/store/user/jodedra/' + config.General.requestName #% (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'Spring22_MiniAOD'
config.Site.storageSite = 'T2_CH_CSCS'
config.General.workArea = 'crab_MiniAOD29032022'
