import FWCore.ParameterSet.Config as cms

from SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff import *

hcalTupleHBHEDigis = cms.EDProducer("HcalTupleMaker_HBHEDigis",
  source    = cms.untracked.InputTag("hcalDigis"),
  Prefix    = cms.untracked.string ( "HBHEDigi"),
  recHits   = cms.untracked.InputTag("hbhereco"),
  Suffix    = cms.untracked.string ( ""),
  DoChargeReco = cms.untracked.bool ( True ) ,
  DoEnergyReco = cms.untracked.bool ( True ) ,
  SaveChargeInfo  = cms.untracked.bool ( False ) ,
  SaveChannelInfo = cms.untracked.bool ( False ) ,
  SaveDetIdInfo   = cms.untracked.bool ( False ) ,
  SaveRecHitInfo  = cms.untracked.bool ( False ) ,
  TotalFCthreshold = cms.untracked.double ( -9999 ) 
)

hcalTupleHBHEDigisMethod2 = cms.EDProducer("HcalTupleMaker_HBHEDigis",
  source    = cms.untracked.InputTag("hcalDigis"),
  Prefix    = cms.untracked.string ( "HBHEDigi"),
  recHits   = cms.untracked.InputTag("hbhereco"),
  Suffix    = cms.untracked.string ( ""),
  DoChargeReco = cms.untracked.bool ( True ) ,
  DoEnergyReco = cms.untracked.bool ( True ) ,
  SaveChargeInfo  = cms.untracked.bool ( False ) ,
  SaveChannelInfo = cms.untracked.bool ( False ) ,
  SaveDetIdInfo   = cms.untracked.bool ( False ) ,
  SaveRecHitInfo  = cms.untracked.bool ( False ) ,
  TotalFCthreshold = cms.untracked.double ( -9999 ) 
)

hcalTupleHBHEDigisMethod0 = cms.EDProducer("HcalTupleMaker_HBHEDigis",
  source    = cms.untracked.InputTag("hcalDigis"),
  Prefix    = cms.untracked.string ( "HBHEDigi"),
  recHits   = cms.untracked.InputTag("hbhereco"),
  Suffix    = cms.untracked.string ( ""),
  DoChargeReco = cms.untracked.bool ( True ) ,
  DoEnergyReco = cms.untracked.bool ( True ) ,
  SaveChargeInfo  = cms.untracked.bool ( False ) ,
  SaveChannelInfo = cms.untracked.bool ( False ) ,
  SaveDetIdInfo   = cms.untracked.bool ( False ) ,
  SaveRecHitInfo  = cms.untracked.bool ( False ) ,
  TotalFCthreshold = cms.untracked.double ( -9999 ) 
)

hcalTupleHBHECosmicsDigis = cms.EDProducer("HcalTupleMaker_HBHEDigis",
  source  = cms.untracked.InputTag("hcalCosmicDigis"),
  recHits = cms.untracked.InputTag("hbhereco"),
  Prefix  = cms.untracked.string ( "HBHECosmicDigi"),
  Suffix  = cms.untracked.string ( ""),
  DoChargeReco = cms.untracked.bool ( True ) ,
  DoEnergyReco = cms.untracked.bool ( True ) , 
  SaveChannelInfo = cms.untracked.bool ( False ) ,
  TotalFCthreshold = cms.untracked.double ( -9999 ) 
)

hcalTupleHBHEL1JetsDigis = cms.EDProducer("HcalTupleMaker_HBHEDigis",
  source  = cms.untracked.InputTag("hcalL1JetDigis"),
  recHits = cms.untracked.InputTag("hbhereco"),
  Prefix  = cms.untracked.string ( "HBHEL1JetDigi"),
  Suffix  = cms.untracked.string ( ""),
  DoChargeReco = cms.untracked.bool ( True ) ,
  DoEnergyReco = cms.untracked.bool ( True ) ,
  SaveChannelInfo = cms.untracked.bool ( False ) ,
  TotalFCthreshold = cms.untracked.double ( -9999 ) 
)
