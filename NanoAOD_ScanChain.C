//  .
// ..: P. Chang, philip@physics.ucsd.edu

#include "NanoAOD_ScanChain.h"

//_________________________________________________________________________________________________
void ScanChain(TChain* chain, TString output_name, TString base_optstr, int nevents)
{
    // -~-~-~-~-~-~
    // Event Looper
    // -~-~-~-~-~-~
    Looper<NanoAOD> looper(chain, &naod, nevents);
    chain->GetEntry(0);
    naod.Init(chain->GetTree());

    // -~-~-~-~-~-~-~-~-~-~-
    // Parse option settings
    // -~-~-~-~-~-~-~-~-~-~-
    TString option = base_optstr;
    RooUtil::print("the base option string = " + base_optstr);

    // -~-~-~-~-~
    // Set output
    // -~-~-~-~-~
    RooUtil::AutoHist hists;

    while (looper.nextEvent())
    {
        if (naod.nMuon < 2)
            continue;

        std::vector<TLorentzVector> muons;
        for (UInt_t imu = 0; imu < naod.nMuon && imu < 7; ++imu) // The "array" type TTree branches have hard limit on total number of entries
        {
            if (!( fabs(naod.Muon_dxy[imu]) < 0.05 )) return;
            if (!( fabs(naod.Muon_dz[imu]) < 0.1 )) return;
            if (!( fabs(naod.Muon_ip3d[imu]) < 0.015 )) return;
            if (!( fabs(naod.Muon_sip3d[imu]) < 4 )) return;
            if (!( fabs(naod.Muon_pfRelIso03_all[imu]) < 0.06 )) return;
            if (!( fabs(naod.Muon_ptErr[imu]/naod.Muon_pt[imu]) < 0.2 )) return;
            TLorentzVector mu;
            mu.SetPtEtaPhiM(naod.Muon_pt[imu], naod.Muon_eta[imu], naod.Muon_phi[imu], 0);
            muons.push_back(mu);
        }

        if (muons.size() < 2)
            continue;

        hists.fill((muons[0] + muons[1]).M(), "Mmumu", naod.genWeight, 120, 60., 120.);
    }
    hists.save(output_name);
}
// eof
