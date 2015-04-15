#------------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------------

import FWCore.ParameterSet.Config as cms

#------------------------------------------------------------------------------------
# Declare the process
#------------------------------------------------------------------------------------

process = cms.Process('RECO')

#------------------------------------------------------------------------------------
# Set up the input source
#------------------------------------------------------------------------------------

process.source = cms.Source("PoolSource")

#------------------------------------------------------------------------------------
# What files should we run over?
#------------------------------------------------------------------------------------

process.source.fileNames = cms.untracked.vstring(
    #FILENAMES
    "root://eoscms//eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/237/251/00000/02541D01-25C6-E411-B1AE-02163E011868.root"
    #"root://eoscms//eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/233/238/00000/0007721D-39A9-E411-A6B5-02163E01054C.root"
    #"root://eoscms//eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/233/238/00000/009CD888-36A9-E411-8CF3-02163E010547.root"
    #"root://eoscms//eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/233/238/00000/02143792-36A9-E411-BBCE-02163E0118B1.root"
    #"root://eoscms//eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/233/238/00000/0284245C-37A9-E411-BD19-02163E0124A5.root"
    #"root://eoscms//eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/233/238/00000/0490A416-3AA9-E411-B81E-02163E0105E1.root"
)

process.source.skipEvents = cms.untracked.uint32(0
    #SKIPEVENTS
)

#------------------------------------------------------------------------------------
# How many events should we run over?
#------------------------------------------------------------------------------------

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(20))

#------------------------------------------------------------------------------------
# Set up the output
#------------------------------------------------------------------------------------

process.TFileService = cms.Service("TFileService",
    fileName = cms.string( 'test.root')
    #root://eoscms//eos/cms/store/user/hsaka/HcalNoise/HCALPFGRootNtuple/HcalPFGTree_Commissioning2015_MinimumBias_Run233238_Method0and2_V3F1_02163E01054C.root')
)

#------------------------------------------------------------------------------------
# Various python configuration files
# Used cmsDriver.py reco -s RAW2DIGI,L1Reco,RECO --conditions STARTUP_V4::All --eventcontent RECO --magField=0T --scenario=cosmics
#------------------------------------------------------------------------------------

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentCosmics_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
#process.load('Configuration.StandardSequences.MagneticField_0T_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.ReconstructionCosmics_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff')

#-- Message Logger ------------------------------------------------------------
process.MessageLogger = cms.Service("MessageLogger",
 cout = cms.untracked.PSet(
   default = cms.untracked.PSet( ## kill all messages in the log
   limit = cms.untracked.int32(0)
  ),
  FwkJob = cms.untracked.PSet( ## but FwkJob category - those unlimitted 
   limit = cms.untracked.int32(-1)
  ),
  FwkReport = cms.untracked.PSet(
   reportEvery = cms.untracked.int32(10), ## print event record number
   limit = cms.untracked.int32(-1)
  ),
  FwkSummary = cms.untracked.PSet(
    optionalPSet = cms.untracked.bool(True),
    limit = cms.untracked.int32(-1)
   )
  ),
 categories = cms.untracked.vstring('FwkJob','FwkReport','FwkSummary'),
 destinations = cms.untracked.vstring('cout')
)

#process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

# Set up cosmic digis
#process.load("HCALPFG.HcalTupleMaker.HcalCosmicDigisProducer_cfi")

# Set up L1 Jet digis
#process.load("HCALPFG.HcalTupleMaker.HcalL1JetDigisProducer_cfi")

# Set up our analyzer
#process.load('RecoLocalCalo.Configuration.hcalLocalReco_cff') # could replace ReconstructionCosmics_cff above
#process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_cfi")
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_Tree_cfi")
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_Event_cfi")

#configure HBHEDigi producer
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_HBHEDigis_cfi")
process.hcalTupleHBHEDigisMethod2.recHits        = cms.untracked.InputTag("hbherecoMethod2")#this is used to store rechit time and energy in digi analysis
process.hcalTupleHBHEDigisMethod2.Suffix         = cms.untracked.string( "" )
process.hcalTupleHBHEDigisMethod2.TotalFCthreshold= cms.untracked.double (10)
process.hcalTupleHBHEDigisMethod2.SaveChargeInfo = cms.untracked.bool (True)
process.hcalTupleHBHEDigisMethod2.SaveChannelInfo= cms.untracked.bool (False)
process.hcalTupleHBHEDigisMethod2.SaveDetIdInfo  = cms.untracked.bool (True) 
process.hcalTupleHBHEDigisMethod2.SaveRecHitInfo = cms.untracked.bool (True)

process.hcalTupleHBHEDigisMethod0.recHits        = cms.untracked.InputTag("hbherecoMethod0")#this is used to store rechit time and energy in digi analysis
process.hcalTupleHBHEDigisMethod0.Suffix         = cms.untracked.string( "Method0" )
process.hcalTupleHBHEDigisMethod0.TotalFCthreshold= cms.untracked.double (10)
process.hcalTupleHBHEDigisMethod0.SaveChargeInfo = cms.untracked.bool (False)
process.hcalTupleHBHEDigisMethod0.SaveChannelInfo= cms.untracked.bool (False)
process.hcalTupleHBHEDigisMethod0.SaveDetIdInfo  = cms.untracked.bool (False) 
process.hcalTupleHBHEDigisMethod0.SaveRecHitInfo = cms.untracked.bool (True)


process.hcalTupleHBHECosmicsDigis.recHits = cms.untracked.InputTag("hbherecoMethod2")#this is used to store rechit time and energy in digi analysis
process.hcalTupleHBHEL1JetsDigis.recHits  = cms.untracked.InputTag("hbherecoMethod2")#this is used to store rechit time and energy in digi analysis
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_HBHERecHits_CosmicsData_cfi")
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_Trigger_cfi")

process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_HODigis_cfi")
process.hcalTupleHODigis.TotalFCthreshold= cms.untracked.double (10)
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_HFDigis_cfi")

# Set up noise filters: Method 2 (default) and Method 0
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_HcalNoiseFilters_cfi")

# Set up noise filters: Method 2 (default) and Method 0
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_CaloJetMet_cfi")


# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run1_data', '')

process.my_hlt = cms.EDFilter("HLTHighLevel",
     TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
     HLTPaths = cms.vstring("HLT_L1SingleJet16*"), # provide list of HLT paths (or patterns) you want
     eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
     andOr = cms.bool(True),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
     throw = cms.bool(False)    # throw exception on unknown path names
)

    
process.tuple_step = cms.Sequence(
    # Make HCAL tuples: Event, run, ls number
    process.hcalTupleEvent*
    #  Make HCAL tuples: digi info
    process.hcalTupleHBHEDigisMethod2*
    process.hcalTupleHBHEDigisMethod0*
    process.hcalTupleHODigis*
    process.hcalTupleHFDigis*
    #    process.hcalTupleTriggerPrimitives*
    #    # Make HCAL tuples: digi info
    #    process.hcalTupleHBHECosmicsDigis*
    #    process.hcalTupleHOCosmicsDigis*
    #    # Make HCAL tuples: digi info
    #    process.hcalTupleHBHEL1JetsDigis*
    #    process.hcalTupleHFL1JetsDigis*
    #    process.hcalTupleL1JetTriggerPrimitives*
    #    # Make HCAL tuples: reco info
    #process.hcalTupleHBHERecHits*
    #process.hcalTupleHBHERecHitsMethod0*
    process.hcalTupleHcalNoiseFilters*
    process.hcalTupleHcalNoiseFiltersMethod0*
    #
    process.hcalTupleCaloJetMet*
    process.hcalTupleCaloJetMetMethod0*
    #    process.hcalTupleHORecHits*
    #    process.hcalTupleHFRecHits*
    #    # Trigger info
    #    process.hcalTupleTrigger*
    #    process.hcalTupleTriggerObjects*
    #    # L1 jet info
    #    process.hcalTupleL1Jets*
    #    # Make HCAL tuples: cosmic muon info
    #    process.hcalTupleCosmicMuons*
    #    # Package everything into a tree
    #
    process.hcalTupleTree
)



# Path and EndPath definitions
process.preparation = cms.Path(
    process.my_hlt *
    process.RawToDigi *
    #process.L1Reco *
    process.reconstructionCosmics *
    #
    #process.horeco *
    #process.hfreco *
    #
    process.hbherecoMethod0 *
    process.hbherecoMethod2 *
    #
    process.towerMakerMethod0 *
    process.towerMakerMethod2 *
    #
    process.hcalnoiseMethod0 *
    process.hcalnoiseMethod2 *
    #
    process.HBHENoiseFilterResultProducerMethod0 *
    process.HBHENoiseFilterResultProducerMethod2 *
    #
    #process.hcalCosmicDigis *
    #process.hcalL1JetDigis *
    process.tuple_step
)

#process.FEVToutput = cms.OutputModule("PoolOutputModule",
#    splitLevel = cms.untracked.int32(0),
#    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
#    outputCommands = process.FEVTEventContent.outputCommands,
#    fileName = cms.untracked.string('Run239754_DigiRECO.root'),
#    dataset = cms.untracked.PSet(
#        filterName = cms.untracked.string(''),
#        dataTier = cms.untracked.string('DIGI-RECO')
#    )
#)
#process.FEVToutput_step = cms.EndPath(process.FEVToutput)

from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1
process = customisePostLS1(process)
