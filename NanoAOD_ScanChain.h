//  .
// ..: P. Chang, philip@physics.ucsd.edu

#include <algorithm>

// RooUtil tool
#include "rooutil/looper.h"
#include "rooutil/autohist.h"
#include "rooutil/eventlist.h"
#include "rooutil/ttreex.h"
#include "NanoCORE/NanoAOD.h"

using namespace std;
using namespace RooUtil;

void ScanChain(TChain* chain, TString output_name, TString optstr, int nevents = -1);

//#include "analysis.C"
