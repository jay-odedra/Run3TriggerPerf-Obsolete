from DataFormats.FWLite import Events, Handle
from common.deltar             import deltaR, bestMatch, bestMatchAtVtx
from ROOT import TFile, TTree, TLorentzVector
from array import array
import math, copy
from os import listdir
from os.path import isfile, join
from TreeProducerGen import *
import argparse
import json
import itertools
import pprint
import numpy as np

from optparse import OptionParser, OptionValueError
usage = "usage: python runTauDisplay_BsTauTau.py"
parser = OptionParser(usage)

parser = argparse.ArgumentParser(description='example e/gamma HLT analyser', fromfile_prefix_chars='@')
#parser.add_argument('in_filenames',nargs="+",help='input filename')
parser.add_argument('in_filenames',nargs="+")
#parser.parse_args(['@filesdatasetfullname1.txt'])
parser.add_argument('--out','-o',default="puritycheck.root",help='output filename')
parser.add_argument('--type','-t',default="data",help='type')
args = parser.parse_args()

print('filename=', args.in_filenames)

events = Events(args.in_filenames)

#import pdb; pdb.set_trace()
print('nevents = ', events.size())
Nevt = int(events.size())

me = 0.000511
mpi = 0.139571
mk = 0.493677
mB = 5.27963
mmu = 0.105658


def hlt_criteria(hlt_eg):
    flag = False


 # if statement for hlt criteria if true change flag

    return flag

def squareddistance(muon1,muon2):
    value = (muon1.vertex().x()-muon2.vertex().x())**2 + (muon1.vertex().y()-muon2.vertex().y())**2 + (muon1.vertex().z()-muon2.vertex().z())**2
    distance = np.sqrt(value)
    return distance
def squareddistancepfbool(muon1,muon2,pf,dis):
    value1 = (muon1.vertex().x()-pf.vertex().x())**2 + (muon1.vertex().y()-pf.vertex().y())**2 + (muon1.vertex().z()-pf.vertex().z())**2
    value2 = (muon2.vertex().x()-pf.vertex().x())**2 + (muon2.vertex().y()-pf.vertex().y())**2 + (muon2.vertex().z()-pf.vertex().z())**2
    distance1 = np.sqrt(value1)
    distance2 = np.sqrt(value2)
    if distance1 < dis or distance2 < dis: 
        return True
    else:
        return False
def squareddistancepfvalue(muon1,muon2,pf):
    value1 = (muon1.vertex().x()-pf.vertex().x())**2 + (muon1.vertex().y()-pf.vertex().y())**2 + (muon1.vertex().z()-pf.vertex().z())**2
    value2 = (muon2.vertex().x()-pf.vertex().x())**2 + (muon2.vertex().y()-pf.vertex().y())**2 + (muon2.vertex().z()-pf.vertex().z())**2
    distance1 = np.sqrt(value1)
    distance2 = np.sqrt(value2)
    return (distance1 + distance2)/2.0

def createRunDict(file2read):

    rundict = {}

    run_save = None
    
    llist = {}

    for line in open(file2read):

        if line.find('STABLE BEAMS')==-1: continue

        line = line.rstrip().split(',')
    
        run = line[0].split(':')[0]
        ls = line[1].split(':')[0]
        ls_end = line[1].split(':')[1]
        _instL = float(line[5])*0.0001
        _npu = float(line[7])


        
        if run_save!=None and run != run_save:
            rundict[run_save] = llist
            llist = {}

        if ls==ls_end: 
            llist[ls] = {'instL':_instL, 'npu':_npu}
            run_save = line[0].split(':')[0]
            

    return rundict

l1_ptthreshold = 4
hlt_ptthreshold = 4 
offline_ptthreshold = 4

handle_mu  = Handle ('vector<pat::Muon>')
label_mu = ("slimmedMuons",  "", "RECO")

handle_e  = Handle ('vector<pat::Electron>')
label_e = ("slimmedElectrons",  "", "RECO")

handle_pf = Handle ('vector<pat::PackedCandidate>')
label_pf = ("packedPFCandidates",  "",  "RECO")

handle_trigger = Handle ('edm::TriggerResults')
label_trigger = ("TriggerResults", "", "HLT")

handle_pf = Handle ('vector<pat::PackedCandidate>')
label_pf = ("packedPFCandidates",  "",  "RECO")

rundict = createRunDict('./LumiData_2018_20200401.csv')
gjson = None

with open("/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt") as f:
    gjson = json.load(f)

nevents = 0
nevents_interesting = 0

out = TreeProducerGen(args.out, args.type)





counter =0
import time
start = time.time()
for ev in events:
    nevents += 1
    
    if nevents%10000==0: print('{0:.2f}'.format(float(nevents)/float(Nevt)*100.), '% processed')
        
    out.hist.Fill(0)

    _runnum = str(ev.object().eventAuxiliary().run())
    _ls = str(ev.object().eventAuxiliary().luminosityBlock())
        
    flag_gjson = False

    if _runnum in gjson:
            
        for lrange in gjson[_runnum]:

            if int(_ls) > min(lrange) and int(_ls) < max(lrange):
                flag_gjson = True
                break


    out.isgjson[0] = flag_gjson
    

    if not flag_gjson: continue

    out.evt[0] = ev.object().eventAuxiliary().event()
    out.lumi[0] = ev.object().eventAuxiliary().luminosityBlock()
    out.run[0] = ev.object().eventAuxiliary().run()
    
    if _runnum in rundict and _ls in rundict[_runnum]:
        out.instL[0] = rundict[_runnum][_ls]['instL']
        out.npu[0] = rundict[_runnum][_ls]['npu']
    else:
        out.instL[0] = -1
        out.npu[0] = -1

    out.hist.Fill(1)
    ev.getByLabel(label_trigger, handle_trigger)
    triggers = handle_trigger.product()
    names = ev.object().triggerNames(triggers)
    triggersaccepted = []
    for i in range(triggers.size()):
        if triggers.accept(i):
            triggersaccepted.append(names.triggerName(i))
    #print(triggersaccepted)
    hltpath = "HLT_DoubleMu4_JpsiTrk_Displaced_v"
    if any(hltpath in mystring for mystring in triggersaccepted)==False: continue

    nevents_interesting += 1
    
    out.Di_Muon_Trigger_fired[0] = True
    #out.trigger.Fill()
    ev.getByLabel(label_mu, handle_mu) 
    muons = handle_mu.product()
    #print(muons.size())
    offline_muons = []
    for iu, muon in enumerate(muons):
        if abs(muon.eta()) > 2.5: continue
        if muon.pt() < offline_ptthreshold: continue
        offline_muons.append(iu)
    
    if len(offline_muons) < 2: continue
    out.hist.Fill(6)
    
    highest_jpsiuu_pt = -1
    highest_jpsiuu = TLorentzVector()
    highest_mu1 = TLorentzVector()
    highest_mu2 = TLorentzVector()
    highest_pf = TLorentzVector()


    ev.getByLabel(label_pf, handle_pf)
    pfs = handle_pf.product()
    for muon1,muon2 in itertools.combinations(offline_muons,2):
        val = squareddistance(muons[muon1],muons[muon2])
        #print(val) 
        flag_trackmatching = False
        if val > 0.5:continue
        if deltaR(muons[muon1].eta(),muons[muon1].phi(),muons[muon2].eta(),muons[muon2].phi()) > 1.0: continue
        tlvu1 = TLorentzVector()
        tlvu1.SetPtEtaPhiM(muons[muon1].et(), 
                          muons[muon1].eta(), 
                          muons[muon1].phi(),
                          mmu)

        tlvu2 = TLorentzVector()
        tlvu2.SetPtEtaPhiM(muons[muon2].et(), 
                          muons[muon2].eta(), 
                          muons[muon2].phi(),
                          mmu)
        jpsiuu = tlvu1 + tlvu2
        jpsiuu_mass = jpsiuu.M()
        #if jpsi_mass < 2.95: continue
        #if jpsi_mass > 3.25: continue
        #out.hist_mee_wide.Fill(jpsiuu_mass)
        jpsiuu_pt = jpsiuu.Pt()
        tlvpf = TLorentzVector()
        tlvpfclosestdistnace= 9999.
        tlvpfclosest=TLorentzVector()
        for ipf, pf in enumerate(pfs):
            if pf.pt() < 0.5: continue
            if not pf.hasTrackDetails(): continue
            if not pf.trackHighPurity(): continue
            if pf.pseudoTrack().hitPattern().numberOfValidPixelHits() < 0: continue
            if pf.pseudoTrack().hitPattern().numberOfValidHits() < 3: continue
            if pf.pseudoTrack().normalizedChi2() > 100: continue
            if abs(pf.pdgId())!=211 : continue
            if abs(pf.eta()) > 2.5: continue
            if squareddistancepfbool(muons[muon1],muons[muon2],pf,0.1) == False: # or deltaR(jpsiuu.Eta(),jpsiuu.Phi(),pf.eta(),pf.phi()) < 0.5:
                continue
            else:
                flag_trackmatching = True
                tlvpf.SetPtEtaPhiM(pf.et(),pf.eta(),pf.phi(),mk)
                if squareddistancepfvalue(muons[muon1],muons[muon2],pf) < tlvpfclosestdistnace:
                    tlvpfclosestdistnace = squareddistancepfvalue(muons[muon1],muons[muon2],pf)
                    tlvpfclosest = tlvpf

        #mumuxcand = jpsiuu + tlvpfclosest
        #out.mumux_mass[0]= mumuxcand.M()
        #out.trigger.Fill()
        if not flag_trackmatching: continue
       # print("muon1eta: ",muons[muon1].eta(),"  muon2eta: ",muons[muon2].eta())

        if jpsiuu_pt > highest_jpsiuu_pt:
            highest_jpsiuu_pt = jpsiuu_pt
            highest_pf = tlvpfclosest 
            highest_jpsiuu = jpsiuu
            highest_mu1 = tlvu1
            highest_mu2 = tlvu2
    if highest_jpsiuu_pt==-1: continue
    mumuxcand = highest_jpsiuu + highest_pf
    out.mumux_mass[0]= mumuxcand.M()
    out.trigger.Fill()

    '''
    out.jpsi_mass[0] = highest_jpsiuu.M()
    out.jpsi_pt[0] = highest_jpsiuu.Pt()
    out.jpsi_e1_pt[0] = highest_mu1.Pt()
    out.jpsi_e1_eta[0] = highest_mu1.Eta()
    out.jpsi_e1_phi[0] = highest_mu1.Phi()
    out.jpsi_e2_pt[0] = highest_mu2.Pt()
    out.jpsi_e2_eta[0] = highest_mu2.Eta()
    out.jpsi_e2_phi[0] = highest_mu2.Phi()
    '''
    ev.getByLabel(label_e, handle_e) 
    electrons = handle_e.product()
    
    
    offline_electrons = []
    for ie, electron in enumerate(electrons):
        if abs(electron.eta()) > 2.5: continue
        if electron.pt() < 4: continue
        offline_electrons.append(ie)

    if len(offline_electrons) < 2: continue
    
    highest_jpsiee_pt = -1
    highest_jpsiee = TLorentzVector()
    highest_e1 = TLorentzVector()
    highest_e2 = TLorentzVector()

    ev.getByLabel(label_pf, handle_pf)
    pfs = handle_pf.product()
    print(len(offline_electrons))
    for ele1,ele2 in itertools.combinations(offline_electrons,2):
        vale = squareddistance(electrons[ele1],electrons[ele2])
        if vale > 0.5: continue
        if deltaR(electrons[ele1].eta(),electrons[ele1].phi(),electrons[ele2].eta(),electrons[ele2].phi()) > 1.0: continue
        flag_trackmatchingelectron = False

        tlve1 = TLorentzVector()
        tlve1.SetPtEtaPhiM(electrons[ele1].et(), 
                          electrons[ele1].eta(), 
                          electrons[ele1].phi(),
                          me)

        tlve2 = TLorentzVector()
        tlve2.SetPtEtaPhiM(electrons[ele2].et(), 
                          electrons[ele2].eta(), 
                          electrons[ele2].phi(),
                          me)
        
        jpsiee = tlve1 + tlve2
        jpsiee_mass = jpsiee.M()
        out.hist_mee_wide.Fill(jpsiee_mass)
        jpsiee_pt = jpsiee.Pt()
        
        out.jpsi_mass[0] = jpsiee.M()
        out.jpsi_pt[0] = jpsiee.Pt()
        out.jpsi_e1_pt[0] = tlve1.Pt()
        out.jpsi_e1_eta[0] = tlve1.Eta()
        out.jpsi_e1_phi[0] = tlve1.Phi()
        out.jpsi_e2_pt[0] = tlve2.Pt()
        out.jpsi_e2_eta[0] = tlve2.Eta()
        out.jpsi_e2_phi[0] = tlve2.Phi()
        
        for ipf, pf in enumerate(pfs):
            if pf.pt() < 0.5: continue
            if not pf.hasTrackDetails(): continue
            if not pf.trackHighPurity(): continue
            if abs(pf.pdgId())!=211 : continue
            if abs(pf.eta()) > 2.5: continue
            if squareddistancepfbool(electrons[ele1],electrons[ele2],pf,0.5) == True or deltaR(jpsiee.Eta(),jpsiee.Phi(),pf.eta(),pf.phi()) > 1.0:
                continue
            else:
                flag_trackmatchingelectron = True
                break

        if not flag_trackmatchingelectron: continue
        out.tree.Fill()



    '''
        if jpsiee_pt > highest_jpsiee_pt:
            highest_jpsiee_pt = jpsiee_pt 
            highest_jpsiee = jpsiee
            highest_e1 = tlve1
            highest_e2 = tlve2
    
    if highest_jpsiee_pt==-1: continue
    out.hist.Fill(7)
    
    out.jpsi_mass[0] = highest_jpsiee.M()
    out.jpsi_pt[0] = highest_jpsiee.Pt()
    out.jpsi_e1_pt[0] = highest_e1.Pt()
    out.jpsi_e1_eta[0] = highest_e1.Eta()
    out.jpsi_e1_phi[0] = highest_e1.Phi()
    out.jpsi_e2_pt[0] = highest_e2.Pt()
    out.jpsi_e2_eta[0] = highest_e2.Eta()
    out.jpsi_e2_phi[0] = highest_e2.Phi()
    '''


        



    






























    '''
    ev.getByLabel(label_pf, handle_pf)
    pfs = handle_pf.product()
    ev.getByLabel(label_mu, handle_mu) 
    muons = handle_mu.product()
    
    tlv1 = TLorentzVector()
    tlv1.SetPtEtaPhiM(muons[1].et(), 
                        muons[1].eta(), 
                        muons[1].phi(),
                        mmu)

    tlv2 = TLorentzVector()
    tlv2.SetPtEtaPhiM(muons[2].et(), 
                        muons[2].eta(), 
                        muons[2].phi(),
                        mmu)

    jpsi = tlv2 + tlv1
    print(dir(muons[1]))
    print("mu1 eta : ", muons[1].phi(), " mu2 eta : ", muons[2].phi(), " jpsi eta: ", jpsi.Phi())
    for imu, muon in enumerate(muons):
        print(dir(muon.vertex()))
        print(muon.vertex().eta())
        break
   

    for ipf, pf in enumerate(pfs):
        
        if pf.pt() < 0.5: continue
        if not pf.hasTrackDetails(): continue
        if pf.charge() == 0: continue
        if deltaR(pf.eta(), pf.phi(), highest_jpsi.Eta(), highest_jpsi.Phi()) < 0.2: continue
        
        if not pf.trackHighPurity(): continue
        if pf.pseudoTrack().normalizedChi2() > 10: continue



        if abs(pf.pdgId())!=211 : continue
        if abs(pf.eta()) > 2.5: continue
        
        if not pf.trackHighPurity(): continue
        
        print(dir(pf))


        break
    

    
    break
    '''

















    #out.tree.Fill()
    print(nevents, 'has been analyzed (', nevents_interesting, ' interesting events)')
out.endJob()


        










end = time.time()
print("timetakenloop",end - start)



