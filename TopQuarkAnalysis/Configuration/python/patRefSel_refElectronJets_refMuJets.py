#
# This file contains the Top PAG reference selection for electron + jets analysis.
#


### ------------------------- Reference selection -------------------------- ###


### Trigger selection

# HLT selection
triggerSelectionDataElectron  = 'HLT_Ele23_WPLoose_Gsf_CentralPFJet30_BTagCVS07_v1'#FIXME check if right data section
triggerSelectionMCElectron    = 'HLT_Ele22_eta2p1_WP75_Gsf*' #'HLT_Ele27_eta2p1_WP75_Gsf_CentralPFJet30_BTagCSV07_v1'

triggerSelectionDataMuon  = 'HLT_IsoMu18_v*' #'HLT_IsoMu24_eta2p1_v*'
triggerSelectionMCMuon    = 'HLT_IsoMu17_eta2p1_v*' #'HLT_*' # not recommended

### Muon selection

# Minimal selection for all muons, also basis for signal and veto muons
# Muon ID ("loose")
muonCut  =     'isPFMuon'                                                                      # general reconstruction property
muonCut += ' && (isGlobalMuon || isTrackerMuon)'                                               # general reconstruction property
# Kinematics
muonCut += ' && pt > 10.'                                                                      # transverse momentum
muonCut += ' && abs(eta) < 2.5'                                                                # pseudo-rapisity range
# (Relative) isolation
muonCut += ' && (chargedHadronIso+neutralHadronIso+photonIso-0.5*puChargedHadronIso)/pt < 0.2' # relative isolation w/ Delta beta corrections (factor 0.5)

# Signal muon selection on top of 'muonCut'
# Muon ID ("tight")
signalMuonCut  =     'isPFMuon'                                                                               # general reconstruction property
signalMuonCut += ' && isGlobalMuon'                                                                           # general reconstruction property
signalMuonCut += ' && globalTrack.normalizedChi2 < 10.'                                                       # muon ID: 'isGlobalMuonPromptTight'
signalMuonCut += ' && track.hitPattern.trackerLayersWithMeasurement > 5'                                      # muon ID: 'isGlobalMuonPromptTight'
signalMuonCut += ' && globalTrack.hitPattern.numberOfValidMuonHits > 0'                                       # muon ID: 'isGlobalMuonPromptTight'
signalMuonCut += ' && abs(dB) < 0.2'                                                                          # 2-dim impact parameter with respect to beam spot (s. "PAT muon configuration" above)
signalMuonCut += ' && innerTrack.hitPattern.numberOfValidPixelHits > 0'                                       # tracker reconstruction
signalMuonCut += ' && numberOfMatchedStations > 1'                                                            # muon chamber reconstruction
# Kinematics
signalMuonCut += ' && pt > 26.'                                                                               # transverse momentum
signalMuonCut += ' && abs(eta) < 2.1'                                                                         # pseudo-rapisity range
# (Relative) isolation
signalMuonCut += ' && (chargedHadronIso+max(0.,neutralHadronIso+photonIso-0.5*puChargedHadronIso))/pt < 0.12' # relative isolation w/ Delta beta corrections (factor 0.5)

muonVertexMaxDZ = 0.5 # DeltaZ between muon vertex and PV

### Jet selection

# Signal jet selection
# Jet ID
jetCut  =     'numberOfDaughters > 1'                                 # PF jet ID:
jetCut += ' && neutralHadronEnergyFraction < 0.99'                    # PF jet ID:
jetCut += ' && neutralEmEnergyFraction < 0.99'                        # PF jet ID:
jetCut += ' && (chargedEmEnergyFraction < 0.99 || abs(eta) >= 2.4)'   # PF jet ID:
jetCut += ' && (chargedHadronEnergyFraction > 0. || abs(eta) >= 2.4)' # PF jet ID:
jetCut += ' && (chargedMultiplicity > 0 || abs(eta) >= 2.4)'          # PF jet ID:
# Kinematics
jetCut += ' && abs(eta) < 2.4'                                        # pseudo-rapisity range
# varying jet pt thresholds
veryLooseJetCut = 'pt > 30.' # transverse momentum (4 jets)
looseJetCut     = 'pt > 30.' # transverse momentum (3 jets)
tightJetCut     = 'pt > 30.' # transverse momentum (2 jets)
veryTightJetCut = 'pt > 30.' # transverse momentum (leading jet)

### Electron selection
#Signalelektron
# Electron ID
electronGsfCut  =     'electronID("cutBasedElectronID-CSA14-PU20bx25-V0-standalone-loose")==1. || electronID("cutBasedElectronID-CSA14-PU20bx25-V0-standalone-loose")==3. || electronID("cutBasedElectronID-CSA14-PU20bx25-V0-standalone-loose")==5. || electronID("cutBasedElectronID-CSA14-PU20bx25-V0-standalone-loose")==7.'   #original: 'electronID("cutBasedElectronID-CSA14-50ns-V1-standalone-veto")'                                                  # electrons ID aktuell? 25ns? yes! look for value map below
# Kinematics
electronGsfCut += ' && ecalDrivenMomentum.pt > 20.'                                                                                     # transverse energy
electronGsfCut += ' && abs(ecalDrivenMomentum.eta) < 2.5'                                                                               # pseudo-rapisity range
# (Relative) isolation
electronGsfCut += ' && (chargedHadronIso+max(0.,neutralHadronIso+photonIso-1.0*userIsolation("User1Iso")))/ecalDrivenMomentum.pt < 0.2' # relative isolation with Delta beta corrections
# ... using re-calibrated (with regression energy) kinematics
electronCalibCut = electronGsfCut.replace( 'ecalDrivenMomentum.', '' )
electronCut = electronGsfCut

signalElectronCut = '' #TODO\


#ElektronVeto
# Minimal selection for veto electrons
# ... using GsfElectron kinematics
# Electron ID
electronGsfVetoCut  =     'electronID("cutBasedElectronID-CSA14-50ns-V1-standalone-veto")'                                                  # electrons ID
# Kinematics
electronGsfVetoCut += ' && ecalDrivenMomentum.pt > 20.'                                                                                     # transverse energy
electronGsfVetoCut += ' && abs(ecalDrivenMomentum.eta) < 2.5'                                                                               # pseudo-rapisity range
# (Relative) isolation
electronGsfVetoCut += ' && (chargedHadronIso+max(0.,neutralHadronIso+photonIso-1.0*userIsolation("User1Iso")))/ecalDrivenMomentum.pt < 0.2' # relative isolation with Delta beta corrections
# ... using re-calibrated (with regression energy) kinematics
electronCalibVetoCut = electronGsfVetoCut.replace( 'ecalDrivenMomentum.', '' )
electronVetoCut = electronGsfVetoCut
### ------------------------------------------------------------------------ ###

#dileptonElecVeto
dileptonElectronVetoCut = 'electronID("cutBasedElectronID-CSA14-PU20bx25-V0-standalone-loose")' #formely on veto, recommendation states loose
#dileptonElectronVetoCut +=' && ecalDrivenMomentum.pt > 20. && abs(ecalDrivenMomentum.eta) < 2.5'    
#dileptonElectronVetoCut +=' && (chargedHadronIso+max(0.,neutralHadronIso+photonIso-1.0*userIsolation("User1Iso")))/ecalDrivenMomentum.pt < 0.2'


### Electron Conversion Rejection
conversionRejectionCut = 'electronID("cutBasedElectronID-CSA14-PU20bx25-V0-standalone-loose")==4. || electronID("cutBasedElectronID-CSA14-PU20bx25-V0-standalone-loose")==5. || electronID("cutBasedElectronID-CSA14-PU20bx25-V0-standalone-loose")==6. || electronID("cutBasedElectronID-CSA14-PU20bx25-V0-standalone-loose")==7.'  #check Electron.h

#reminder ElectronID value map
#0: fails
#1: passes electron ID only
#2: passes electron Isolation only
#3: passes electron ID and Isolation only
#4: passes conversion rejection
#5: passes conversion rejection and ID
#6: passes conversion rejection and Isolation
#7: passes the whole selection




# Signal b-tagged jet selection
bTagCut = 'bDiscriminator("combinedInclusiveSecondaryVertexV2BJetTags") > 0.679'


### Trigger matching
# Trigger object selection
triggerObjectSelectionData = 'type("TriggerMuon") && ( path("%s") )'%( triggerSelectionDataMuon )
triggerObjectSelectionMC   = 'type("TriggerMuon") && ( path("%s") )'%( triggerSelectionMCMuon )
