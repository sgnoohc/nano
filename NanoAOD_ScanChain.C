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
    }
}
// eof
