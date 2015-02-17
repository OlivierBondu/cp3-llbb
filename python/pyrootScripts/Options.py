"""
Script containing some options for python scripts
"""

#Define a list of intersting plots
Vars = {}
Vars2D = {}
Vars["Zbb"] = {
    "boostselectionbestzmassMu":{"name":"boostselectionbestzmassMu","title":"boostselectionbestzmassMu","bin":30,"xmin":76,"xmax":106},
    "boostselectionbestzmassEle":{"name":"boostselectionbestzmassEle","title":"boostselectionbestzmassEle","bin":30,"xmin":76,"xmax":106},
    "boostselectionbestzptMu":{"name":"boostselectionbestzptMu","title":"boostselectionbestzptMu","bin":30,"xmin":0,"xmax":300},
    "boostselectionbestzptEle":{"name":"boostselectionbestzptEle","title":"boostselectionbestzptEle","bin":30,"xmin":0,"xmax":300},
    "boostselectiondphiZbb":{"name":"boostselectiondphiZbb","title":"boostselectiondphiZbb","bin":20,"xmin":0,"xmax":3.15},
    "boostselectiondrZbb":{"name":"boostselectiondrZbb","title":"boostselectiondrZbb","bin":50,"xmin":0,"xmax":10},
    "boostselectionZbbM":{"name":"boostselectionZbbM","title":"boostselectionZbbM","bin":1000/50,"xmin":0,"xmax":1000},
    "boostselectionZbbPt":{"name":"boostselectionZbbPt","title":"boostselectionZbbPt","bin":1000/20,"xmin":0,"xmax":1000},
    #"boostselectiondetab1l2":{"name":"boostselectiondetab1l2","title":"boostselectiondetab1l2","bin":20,"xmin":0,"xmax":5},
    #"boostselectiondetab2l1":{"name":"boostselectiondetab2l1","title":"boostselectiondetab2l1","bin":20,"xmin":0,"xmax":5},
    "jetmetMET":{"name":"jetmetMET","title":"jetmetMET","bin":100/5,"xmin":0,"xmax":100},
    #"jetmetMETphi":{"name":"jetmetMETphi","title":"jetmetMETphi","bin":30,"xmin":-3.15,"xmax":3.15},
    "jetmetMETsignificance":{"name":"jetmetMETsignificance","title":"jetmetMETsignificance","bin":20,"xmin":0,"xmax":20},
    "jetmetnj":{"name":"jetmetnj","title":"jetmetnj","bin":10,"xmin":-0.5,"xmax":9.5},
    "jetmetbjet1pt":{"name":"jetmetbjet1pt","title":"jetmetbjet1pt","bin":25,"xmin":0,"xmax":250},
    "jetmetbjet2pt":{"name":"jetmetbjet2pt","title":"jetmetbjet2pt","bin":15,"xmin":0,"xmax":150},
    "jetmetbjet1CSVdisc":{"name":"jetmetbjet1CSVdisc","title":"jetmetbjet1CSVdisc","bin":10,"xmin":0,"xmax":1},
    "jetmetbjet2CSVdisc":{"name":"jetmetbjet2CSVdisc","title":"jetmetbjet2CSVdisc","bin":10,"xmin":0,"xmax":1},
    "matrixElementsbjet1pt":{"name":"matrixElementsbjet1pt","title":"matrixElementsbjet1pt","bin":25,"xmin":0,"xmax":250},
    "matrixElementsbjet2pt":{"name":"matrixElementsbjet2pt","title":"matrixElementsbjet2pt","bin":15,"xmin":0,"xmax":150},
    #"matrixElementsbjet1etapm":{"name":"matrixElementsbjet1etapm","title":"matrixElementsbjet1etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    #"matrixElementsbjet2etapm":{"name":"matrixElementsbjet2etapm","title":"matrixElementsbjet2etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    "detab1b2":{"name":"detab1b2","title":"matrixElementsbjet1etapm-matrixElementsbjet2etapm","bin":25,"xmin":-5,"xmax":5},
    "matrixElementsmu1pt":{"name":"matrixElementsmu1pt","title":"matrixElementsmu1pt","bin":25,"xmin":0,"xmax":250},
    "matrixElementsmu2pt":{"name":"matrixElementsmu2pt","title":"matrixElementsmu2pt","bin":15,"xmin":0,"xmax":150},
    #"matrixElementsmu1etapm":{"name":"matrixElementsmu1etapm","title":"matrixElementsmu1etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    #"matrixElementsmu2etapm":{"name":"matrixElementsmu2etapm","title":"matrixElementsmu2etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    "matrixElementsel1pt":{"name":"matrixElementsel1pt","title":"matrixElementsel1pt","bin":25,"xmin":0,"xmax":250},
    "matrixElementsel2pt":{"name":"matrixElementsel2pt","title":"matrixElementsel2pt","bin":15,"xmin":0,"xmax":150},
    #"matrixElementsel1etapm":{"name":"matrixElementsel1etapm","title":"matrixElementsel1etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    #"matrixElementsel2etapm":{"name":"matrixElementsel2etapm","title":"matrixElementsel2etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    "boostselectionCentrality":{"name":"boostselectionCentrality","title":"boostselectionCentrality","bin":20,"xmin":0,"xmax":1},
    "boostselectionCentralityBoost":{"name":"boostselectionCentralityBoost","title":"boostselectionCentralityBoost","bin":20,"xmin":0,"xmax":1},
    "boostselectiondijetM":{"name":"boostselectiondijetM","title":"boostselectiondijetM","bin":1000/50,"xmin":0,"xmax":1000},
    "boostselectiondijetPt":{"name":"boostselectiondijetPt","title":"boostselectiondijetPt","bin":30,"xmin":0,"xmax":300},
    "boostselectiondijetdR":{"name":"boostselectiondijetdR","title":"boostselectiondijetdR","bin":25,"xmin":0,"xmax":5},
    "boostselectiondrllMu":{"name":"boostselectiondrllMu","title":"boostselectiondrllMu","bin":25,"xmin":0,"xmax":5},
    "boostselectiondrllEle":{"name":"boostselectiondrllEle","title":"boostselectiondrllEle","bin":25,"xmin":0,"xmax":5},
    #"":{"name":"","title":"","bin":30,"xmin":76,"xmax":106},
}

Vars2D["Zjj"] = [
    ["minjeteta","jetmetjet1pt_etaorder"],
    ["maxjeteta","jetmetjet2pt_etaorder"],
    ["minjeteta","maxjeteta"],
    ["jetmetjet1pt_etaorder","jetmetjet2pt_etaorder"],
    ["boostselectiondijetM","boostselectionZbbM"],
    ]
    

Vars["Zjj"] = {
    #"boostselectionbestzmassMu":{"name":"boostselectionbestzmassMu","title":"boostselectionbestzmassMu","bin":60,"xmin":60,"xmax":120},
    #"boostselectionbestzmassEle":{"name":"boostselectionbestzmassEle","title":"boostselectionbestzmassEle","bin":60,"xmin":60,"xmax":120},
    "boostselectionbestzptMu":{"name":"boostselectionbestzptMu","title":"boostselectionbestzptMu","bin":35,"xmin":0,"xmax":350},
    "boostselectionbestzptEle":{"name":"boostselectionbestzptEle","title":"boostselectionbestzptEle","bin":35,"xmin":0,"xmax":350},
    #"boostselectionbestzetaMu":{"name":"boostselectionbestzetaMu","title":"boostselectionbestzetaMu","bin":50,"xmin":-10,"xmax":10},
    #"boostselectionbestzetaEle":{"name":"boostselectionbestzetaEle","title":"boostselectionbestzetaEle","bin":50,"xmin":-10,"xmax":10},
    #"boostselectionbestzphiMu":{"name":"boostselectionbestzphiMu","title":"boostselectionbestzphiMu","bin":40,"xmin":-3.15,"xmax":3.15},
    #"boostselectionbestzphiEle":{"name":"boostselectionbestzphiEle","title":"boostselectionbestzphiEle","bin":40,"xmin":-3.15,"xmax":3.15},
    #"boostselectiondphiZbb":{"name":"boostselectiondphiZbb","title":"boostselectiondphiZbb","bin":20,"xmin":0,"xmax":3.15},
    #"boostselectiondrZbb":{"name":"boostselectiondrZbb","title":"boostselectiondrZbb","bin":50,"xmin":0,"xmax":10},
    "boostselectionZbbM":{"name":"boostselectionZbbM","title":"boostselectionZbbM","bin":1000/20,"xmin":0,"xmax":1000},
    #"boostselectionZbbPt":{"name":"boostselectionZbbPt","title":"boostselectionZbbPt","bin":1000/20,"xmin":0,"xmax":1000},
    #"boostselectionZbbEta":{"name":"boostselectionZbbEta","title":"boostselectionZbbEta","bin":50,"xmin":-10,"xmax":10},
    #"boostselectionZbbPhi":{"name":"boostselectionZbbPhi","title":"boostselectionZbbPhi","bin":40,"xmin":-3.15,"xmax":3.15},
    #"boostselectiondphiZbj1":{"name":"boostselectiondphiZbj1","title":"boostselectiondphiZbj1","bin":20,"xmin":0,"xmax":3.15},
    #"detaZbbMu":{"name":"detaZbbMu","title":"boostselectionbestzetaMu-boostselectiondijetEta","bin":50,"xmin":-10,"xmax":10},
    #"detaZbbEle":{"name":"detaZbbEle","title":"boostselectionbestzetaEle-boostselectiondijetEta","bin":50,"xmin":-10,"xmax":10},
    #"dphiZjcentralMu":{"name":"dphiZjcentralMu","title":"(abs(boostselectionbestzphiMu-((jetmetjet1eta<jetmetjet2eta)*jetmetjet1phi+(jetmetjet2eta<jetmetjet1eta)*jetmetjet2phi))>TMath::Pi())*(TMath::TwoPi()-abs(boostselectionbestzphiMu-((jetmetjet1eta<jetmetjet2eta)*jetmetjet1phi+(jetmetjet2eta<jetmetjet1eta)*jetmetjet2phi)))+(abs(boostselectionbestzphiMu-((jetmetjet1eta<jetmetjet2eta)*jetmetjet1phi+(jetmetjet2eta<jetmetjet1eta)*jetmetjet2phi))<=TMath::Pi())*(abs(boostselectionbestzphiMu-((jetmetjet1eta<jetmetjet2eta)*jetmetjet1phi+(jetmetjet2eta<jetmetjet1eta)*jetmetjet2phi)))","bin":20,"xmin":0,"xmax":3.15},
    #"dphiZjcentralEle":{"name":"dphiZjcentralEle","title":"(abs(boostselectionbestzphiEle-((jetmetjet1eta<jetmetjet2eta)*jetmetjet1phi+(jetmetjet2eta<jetmetjet1eta)*jetmetjet2phi))>TMath::Pi())*(TMath::TwoPi()-abs(boostselectionbestzphiEle-((jetmetjet1eta<jetmetjet2eta)*jetmetjet1phi+(jetmetjet2eta<jetmetjet1eta)*jetmetjet2phi)))+(abs(boostselectionbestzphiEle-((jetmetjet1eta<jetmetjet2eta)*jetmetjet1phi+(jetmetjet2eta<jetmetjet1eta)*jetmetjet2phi))<=TMath::Pi())*(abs(boostselectionbestzphiEle-((jetmetjet1eta<jetmetjet2eta)*jetmetjet1phi+(jetmetjet2eta<jetmetjet1eta)*jetmetjet2phi)))","bin":20,"xmin":0,"xmax":3.15},
    #"dphiZjforwMu":{"name":"dphiZjforwMu","title":"(abs(boostselectionbestzphiMu-((jetmetjet1eta>jetmetjet2eta)*jetmetjet1phi+(jetmetjet2eta>jetmetjet1eta)*jetmetjet2phi))>TMath::Pi())*(TMath::TwoPi()-abs(boostselectionbestzphiMu-((jetmetjet1eta>jetmetjet2eta)*jetmetjet1phi+(jetmetjet2eta>jetmetjet1eta)*jetmetjet2phi)))+(abs(boostselectionbestzphiMu-((jetmetjet1eta>jetmetjet2eta)*jetmetjet1phi+(jetmetjet2eta>jetmetjet1eta)*jetmetjet2phi))<=TMath::Pi())*(abs(boostselectionbestzphiMu-((jetmetjet1eta>jetmetjet2eta)*jetmetjet1phi+(jetmetjet2eta>jetmetjet1eta)*jetmetjet2phi)))","bin":20,"xmin":0,"xmax":3.15},
    #"dphiZjforwEle":{"name":"dphiZjforwEle","title":"(abs(boostselectionbestzphiEle-((jetmetjet1eta>jetmetjet2eta)*jetmetjet1phi+(jetmetjet2eta>jetmetjet1eta)*jetmetjet2phi))>TMath::Pi())*(TMath::TwoPi()-abs(boostselectionbestzphiEle-((jetmetjet1eta>jetmetjet2eta)*jetmetjet1phi+(jetmetjet2eta>jetmetjet1eta)*jetmetjet2phi)))+(abs(boostselectionbestzphiEle-((jetmetjet1eta>jetmetjet2eta)*jetmetjet1phi+(jetmetjet2eta>jetmetjet1eta)*jetmetjet2phi))<=TMath::Pi())*(abs(boostselectionbestzphiEle-((jetmetjet1eta>jetmetjet2eta)*jetmetjet1phi+(jetmetjet2eta>jetmetjet1eta)*jetmetjet2phi)))","bin":20,"xmin":0,"xmax":3.15},
    #"boostselectiondrZbj1":{"name":"boostselectiondrZbj1","title":"boostselectiondrZbj1","bin":50,"xmin":0,"xmax":10},
    #"boostselectionZbM":{"name":"boostselectionZbM","title":"boostselectionZbM","bin":1000/20,"xmin":0,"xmax":1000},
    #"boostselectionZbPt":{"name":"boostselectionZbPt","title":"boostselectionZbPt","bin":1000/20,"xmin":0,"xmax":1000},
    #"boostselectionscaldptZbj1":{"name":"boostselectionscaldptZbj1","title":"boostselectionscaldptZbj1","bin":1000/20,"xmin":-500,"xmax":500},
    #"boostselectiondetab1l2":{"name":"boostselectiondetab1l2","title":"boostselectiondetab1l2","bin":20,"xmin":0,"xmax":5},
    #"boostselectiondetab2l1":{"name":"boostselectiondetab2l1","title":"boostselectiondetab2l1","bin":20,"xmin":0,"xmax":5},
    #"jetmetMET":{"name":"jetmetMET","title":"jetmetMET","bin":100/5,"xmin":0,"xmax":100},
    #"jetmetMETphi":{"name":"jetmetMETphi","title":"jetmetMETphi","bin":30,"xmin":-3.15,"xmax":3.15},
    #"jetmetMETsignificance":{"name":"jetmetMETsignificance","title":"jetmetMETsignificance","bin":20,"xmin":0,"xmax":20},
    #"jetmetnj":{"name":"jetmetnj","title":"jetmetnj","bin":10,"xmin":-0.5,"xmax":9.5},
    #"matrixElementsbjet1pt":{"name":"matrixElementsbjet1pt","title":"matrixElementsbjet1pt","bin":25,"xmin":0,"xmax":250},
    #"matrixElementsbjet2pt":{"name":"matrixElementsbjet2pt","title":"matrixElementsbjet2pt","bin":15,"xmin":0,"xmax":150},
    "jetmetjet1pt":{"name":"jetmetjet1pt","title":"jetmetjet1pt","bin":25,"xmin":0,"xmax":250},
    "jetmetjet2pt":{"name":"jetmetjet2pt","title":"jetmetjet2pt","bin":15,"xmin":0,"xmax":150},
    #"jetmetjet1pt_etaorder":{"name":"jetmetjet1pt_etaorder","title":"(jetmetjet1eta<jetmetjet2eta)*jetmetjet1pt+(jetmetjet2eta<jetmetjet1eta)*jetmetjet2pt","bin":50,"xmin":0,"xmax":500},
    #"jetmetjet2pt_etaorder":{"name":"jetmetjet2pt_etaorder","title":"(jetmetjet1eta>jetmetjet2eta)*jetmetjet1pt+(jetmetjet2eta>jetmetjet1eta)*jetmetjet2pt","bin":50,"xmin":0,"xmax":500},
    #"jetmetjet1energy":{"name":"jetmetjet1energy","title":"jetmetjet1energy","bin":40,"xmin":0,"xmax":400},
    #"jetmetjet2energy":{"name":"jetmetjet2energy","title":"jetmetjet2energy","bin":40,"xmin":0,"xmax":400},
    #"matrixElementsbjet1etapm":{"name":"matrixElementsbjet1etapm","title":"matrixElementsbjet1etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    #"matrixElementsbjet2etapm":{"name":"matrixElementsbjet2etapm","title":"matrixElementsbjet2etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    #"detab1b2":{"name":"detab1b2","title":"matrixElementsbjet1etapm-matrixElementsbjet2etapm","bin":25,"xmin":-5,"xmax":5},
    #"jetmetjet1etapm":{"name":"jetmetjet1etapm","title":"jetmetjet1etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    #"jetmetjet2etapm":{"name":"jetmetjet2etapm","title":"jetmetjet2etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    #"minjeteta":{"name":"minjeteta","title":"min(jetmetjet1eta,jetmetjet2eta)","bin":50,"xmin":0,"xmax":2.4},
    #"maxjeteta":{"name":"maxjeteta","title":"max(jetmetjet1eta,jetmetjet2eta)","bin":50,"xmin":0,"xmax":2.4},
    #"matrixElementsmu1pt":{"name":"matrixElementsmu1pt","title":"matrixElementsmu1pt","bin":25,"xmin":0,"xmax":250},
    #"matrixElementsmu2pt":{"name":"matrixElementsmu2pt","title":"matrixElementsmu2pt","bin":15,"xmin":0,"xmax":150},
    #"matrixElementsmu1etapm":{"name":"matrixElementsmu1etapm","title":"matrixElementsmu1etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    #"matrixElementsmu2etapm":{"name":"matrixElementsmu2etapm","title":"matrixElementsmu2etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    #"matrixElementsel1pt":{"name":"matrixElementsel1pt","title":"matrixElementsel1pt","bin":25,"xmin":0,"xmax":250},
    #"matrixElementsel2pt":{"name":"matrixElementsel2pt","title":"matrixElementsel2pt","bin":15,"xmin":0,"xmax":150},
    #"matrixElementsel1etapm":{"name":"matrixElementsel1etapm","title":"matrixElementsel1etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    #"matrixElementsel2etapm":{"name":"matrixElementsel2etapm","title":"matrixElementsel2etapm","bin":25,"xmin":-2.5,"xmax":2.5},
    #"jetmetjet1CSVdisc":{"name":"jetmetjet1CSVdisc","title":"jetmetjet1CSVdisc","bin":10,"xmin":0,"xmax":1},
    #"jetmetjet2CSVdisc":{"name":"jetmetjet2CSVdisc","title":"jetmetjet2CSVdisc","bin":10,"xmin":0,"xmax":1},
    #"jetmetjet1JPdisc":{"name":"jetmetjet1JPdisc","title":"jetmetjet1JPdisc","bin":15,"xmin":0,"xmax":2.5},
    #"jetmetjet2JPdisc":{"name":"jetmetjet2JPdisc","title":"jetmetjet2JPdisc","bin":15,"xmin":0,"xmax":2.5},
    #"jetmetjet1PUIdMva":{"name":"jetmetjet1PUIdMva","title":"jetmetjet1PUIdMva","bin":10,"xmin":0,"xmax":1},
    #"jetmetjet2PUIdMva":{"name":"jetmetjet2PUIdMva","title":"jetmetjet2PUIdMva","bin":10,"xmin":0,"xmax":1},
    #"jetmetjet1PUIdWP":{"name":"jetmetjet1PUIdWP","title":"jetmetjet1PUIdWP","bin":8,"xmin":-0.5,"xmax":7.5},
    #"jetmetjet2PUIdWP":{"name":"jetmetjet2PUIdWP","title":"jetmetjet2PUIdWP","bin":8,"xmin":-0.5,"xmax":7.5},
    #"jetmetjet1beta":{"name":"jetmetjet1beta","title":"jetmetjet1beta","bin":10,"xmin":0,"xmax":1},
    #"jetmetjet2beta":{"name":"jetmetjet2beta","title":"jetmetjet2beta","bin":10,"xmin":0,"xmax":1},
    #"jetmetjet1betaStar":{"name":"jetmetjet1betaStar","title":"jetmetjet1betaStar","bin":10,"xmin":0,"xmax":1},
    #"jetmetjet2betaStar":{"name":"jetmetjet2betaStar","title":"jetmetjet2betaStar","bin":10,"xmin":0,"xmax":1},
    #"jetmetjet1npf":{"name":"jetmetjet1npf","title":"jetmetjet1npf","bin":50,"xmin":-0.5,"xmax":49.5},
    #"jetmetjet2npf":{"name":"jetmetjet2npf","title":"jetmetjet2npf","bin":50,"xmin":-0.5,"xmax":49.5},
    #"jetmetjet1nch":{"name":"jetmetjet1nch","title":"jetmetjet1nch","bin":50,"xmin":-0.5,"xmax":49.5},
    #"jetmetjet2nch":{"name":"jetmetjet2nch","title":"jetmetjet2nch","bin":50,"xmin":-0.5,"xmax":49.5},
    #"jetmetjet1Chf":{"name":"jetmetjet1Chf","title":"jetmetjet1Chf","bin":50,"xmin":0,"xmax":1.5},
    #"jetmetjet2Chf":{"name":"jetmetjet2Chf","title":"jetmetjet2Chf","bin":50,"xmin":0,"xmax":1.5},
    #"jetmetjet1Nhf":{"name":"jetmetjet1Nhf","title":"jetmetjet1Nhf","bin":50,"xmin":0,"xmax":1.5},
    #"jetmetjet2Nhf":{"name":"jetmetjet2Nhf","title":"jetmetjet2Nhf","bin":50,"xmin":0,"xmax":1.5},
    #"jetmetjet1cef":{"name":"jetmetjet1cef","title":"jetmetjet1cef","bin":50,"xmin":0,"xmax":1.5},
    #"jetmetjet2cef":{"name":"jetmetjet2cef","title":"jetmetjet2cef","bin":50,"xmin":0,"xmax":1.5},
    #"jetmetjet1nef":{"name":"jetmetjet1nef","title":"jetmetjet1nef","bin":50,"xmin":0,"xmax":1.5},
    #"jetmetjet2nef":{"name":"jetmetjet2nef","title":"jetmetjet2nef","bin":50,"xmin":0,"xmax":1.5},
    #"jetmetjet1Phf":{"name":"jetmetjet1Phf","title":"jetmetjet1Phf","bin":50,"xmin":0,"xmax":1.5},
    #"jetmetjet2Phf":{"name":"jetmetjet2Phf","title":"jetmetjet2Phf","bin":50,"xmin":0,"xmax":1.5},
    #"jetmetjet1Elf":{"name":"jetmetjet1Elf","title":"jetmetjet1Elf","bin":50,"xmin":0,"xmax":1.5},
    #"jetmetjet2Elf":{"name":"jetmetjet2Elf","title":"jetmetjet2Elf","bin":50,"xmin":0,"xmax":1.5},
    #"jetmetjet1Muf":{"name":"jetmetjet1Muf","title":"jetmetjet1Muf","bin":50,"xmin":0,"xmax":1.5},
    #"jetmetjet2Muf":{"name":"jetmetjet2Muf","title":"jetmetjet2Muf","bin":50,"xmin":0,"xmax":1.5},
    #"jetmetjet1Flavor":{"name":"jetmetjet1Flavor","title":"jetmetjet1Flavor","bin":22,"xmin":-0.5,"xmax":21.5},
    #"jetmetjet2Flavor":{"name":"jetmetjet2Flavor","title":"jetmetjet2Flavor","bin":22,"xmin":-0.5,"xmax":21.5},
    #"boostselectionCentrality":{"name":"boostselectionCentrality","title":"boostselectionCentrality","bin":20,"xmin":0,"xmax":1},
    #"boostselectionCentralityBoost":{"name":"boostselectionCentralityBoost","title":"boostselectionCentralityBoost","bin":20,"xmin":0,"xmax":1},
    "boostselectiondijetM":{"name":"boostselectiondijetM","title":"boostselectiondijetM","bin":50,"xmin":0,"xmax":1000},
    #"boostselectiondijetPt":{"name":"boostselectiondijetPt","title":"boostselectiondijetPt","bin":30,"xmin":0,"xmax":300},
    #"boostselectiondijetEta":{"name":"boostselectiondijetEta","title":"boostselectiondijetEta","bin":50,"xmin":-10,"xmax":10},
    #"boostselectiondijetPhi":{"name":"boostselectiondijetPhi","title":"boostselectiondijetPhi","bin":40,"xmin":-3.15,"xmax":3.15},
    "boostselectiondijetdR":{"name":"boostselectiondijetdR","title":"boostselectiondijetdR","bin":25,"xmin":0,"xmax":5},
    "boostselectiondrllMu":{"name":"boostselectiondrllMu","title":"boostselectiondrllMu","bin":25,"xmin":0,"xmax":5},
    "boostselectiondrllEle":{"name":"boostselectiondrllEle","title":"boostselectiondrllEle","bin":25,"xmin":0,"xmax":5},
    #"vertexAssociationnvertices":{"name":"vertexAssociationnvertices","title":"vertexAssociationnvertices","bin":60,"xmin":-0.5,"xmax":59.5},
    #"":{"name":"","title":"","bin":30,"xmin":76,"xmax":106},
}

#define a template for the rootfile name
fileName = "/nfs/user/acaudron/ControlPlots/cp5314p1/AllRDS/Nominal/RDS_SAMPLE/SAMPLE_Summer12_final_skimed_zmet.root"

#selection to compute rewweighting
Stages = {}
Stages["Zjj"] = {
    #"Mu":{"dir":"Muon","cut":"(rc_stage_3_idx&&jetmetnj>1&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106&&jetmetMETsignificance<10)"},
    #"Ele":{"dir":"Electron","cut":"(rc_stage_14_idx&&jetmetnj>1&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106&&jetmetMETsignificance<10)"}
    "Mu":{"dir":"Muon","cut":"(rc_stage_2_idx&&jetmetnj>1&&jetmetMETsignificance<10&&boostselectionZbbM>0&&boostselectionZbbM<1500&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106)"},
    "Ele":{"dir":"Electron","cut":"(rc_stage_13_idx&&jetmetnj>1&&jetmetMETsignificance<10&&boostselectionZbbM>0&&boostselectionZbbM<1500&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106)"}
    #"Mu":{"dir":"Muon","cut":"(rc_stage_2_idx&&jetmetnj>1&&jetmetMETsignificance<10&&matrixElementsbjet1etapm>-1.5&&matrixElementsbjet1etapm<1.5&&matrixElementsbjet2etapm>-1.5&&matrixElementsbjet2etapm<1.5)"},
    #"Ele":{"dir":"Electron","cut":"(rc_stage_13_idx&&jetmetnj>1&&jetmetMETsignificance<10&&matrixElementsbjet1etapm>-1.5&&matrixElementsbjet1etapm<1.5&&matrixElementsbjet2etapm>-1.5&&matrixElementsbjet2etapm<1.5)"}
    #"Mu":{"dir":"Muon","cut":"(rc_stage_2_idx&&jetmetnj>1&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106&&jetmetnj>1)"},#&&jetmetMETsignificance>10)"},
    #"Ele":{"dir":"Electron","cut":"(rc_stage_13_idx&&jetmetnj>1&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106&&jetmetnj>1)"}#&&jetmetMETsignificance>10)"}
    
    }

Stages["Zbb"] = {
    #"Mu":{"dir":"Muon","cut":"(rc_stage_8_idx&&jetmetMETsignificance<10&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106&&jetmetMETsignificance<10)"},
    #"Ele":{"dir":"Electron","cut":"(rc_stage_19_idx&&jetmetMETsignificance<10&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106&&jetmetMETsignificance<10)"}
    #"Mu":{"dir":"Muon","cut":"(rc_stage_8_idx&&jetmetMETsignificance>10)"},
    #"Ele":{"dir":"Electron","cut":"(rc_stage_19_idx&&jetmetMETsignificance>10)"}
    "Mu":{"dir":"Muon","cut":"(rc_stage_8_idx&&boostselectionbestzmassMu>76&&boostselectionbestzmassMu<106&&jetmetnj>1&&jetmetMETsignificance<10)"},
    "Ele":{"dir":"Electron","cut":"(rc_stage_19_idx&&boostselectionbestzmassEle>76&&boostselectionbestzmassEle<106&&jetmetnj>1&&jetmetMETsignificance<10)"}
    }

DYdiv = {
    "Zbb" : "(abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)==5)",
    "Zbx" : "((abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)!=5))",
    "Zxx" : "(abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)!=5)"
    }

#Define BTAG WP
#BTAG = ""
BTAG = "*btaggingReweightingMM"
#define reweighting formula
baseFrom = "*leptonsReweightingweight*lumiReweightingLumiWeight*mcReweightingweight"
rewFrom = {}
rewFrom["Zjj"] = {
    "Mu":baseFrom,
    "Ele":baseFrom
    }

rewFrom["Zbb"] = {
    "Mu":baseFrom+BTAG,
    "Ele":baseFrom+BTAG 
    }

wZbb = "( abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)==5 && jetmetnj==2 )*1.18"
wZbbj = "( abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)==5 && jetmetnj>2 )*1.29"
wZbx = "( (abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)!=5) )*1.29"
wZxx = "( abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)!=5 )*1.29"
#wZbb = "( abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)==5 && jetmetnj==2 )*1.15"
#wZbbj = "( abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)==5 && jetmetnj>2 )*1.30"
#wZbx = "( (abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5 && abs(jetmetbjet2Flavor)!=5) )*1.30"
#wZxx = "( abs(jetmetbjet1Flavor)!=5 && abs(jetmetbjet2Flavor)!=5 )*1.28"
wtt = "1.05"
wdy = "("+wZbb+"+"+wZbbj+"+"+wZbx+"+"+wZxx+")"
