from CRABClient.UserUtilities import config #, getUsernameFromSiteDB
config = config()

config.General.requestName = 'BtoXjpsillInclusivedecay20221504'
config.General.transferLogs = False
config.General.workArea = 'crab_privateMC'
config.General.transferOutputs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'GS_CharmoniumbtojpsiKll.py'
config.JobType.maxMemoryMB = 5000

config.Data.inputDataset = ''
config.Data.inputDBS = 'global'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 99

NJOBS = 10000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.outLFNDirBase = '/store/user/jodedra/' + config.General.requestName
config.Data.publication = True
config.Data.outputDatasetTag = 'SPRING21'
config.Site.storageSite = 'T2_CH_CSCS'
#config.Site.ignoreGlobalBlacklist = True

config.Data.outputPrimaryDataset = 'BtoXjpsillInclusivedecay20221504'
