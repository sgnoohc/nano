# nano

Currently the code just plots two muon mass.
The empty looper is tagged at 0.0.1.

# First time installing

    git clone --recursive -j8 git@github.com:sgnoohc/nano
    cd nano
    source scripts/setup.sh
    compile.sh

# Second time

After you've already installed, and you log off uaf and come back later.  
To set it up to where you were before type:

    source scripts/setup.sh

# Running locally

    run.sh -c NanoAOD_ScanChain.C output.root Events -1 dummy /hadoop/cms/store/user/namin/NanoAODv1/ProjectMetis/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10_ext1-v1_MINIAODSIM_NanoAODv1/merged_ntuple_1.root

# Plotting after local job finishes

The above command creates ```output.root``` with a single histogram object in the ROOT file.  
To plot it, run:

    python nanoplot.py

# Running batch jobs

Few options are at the top of the following scripts.  
Samples are turned off all except one DY sample.  
Feel free to turn additional samples.

    python nanometis.py

# Plotting after batch job finishes

First hadd your output that resides somewhere in the hadoop area that you configured in nanometis.py.  
Hadded file should be called ```output.root``` in order for the following script to recognize.

    python nanoplot.py

# To extend the functionality

If you want to do more stuff with the looper, do your analysis in the while loop of ```NanoAOD_ScanChain.C```.
All variables in the NanoAOD are accessible via ```naod``` instance of the class ```NanoAOD```.  
(e.g. naod.Electron_pt[ith_elec], naod.Jet_pt[ith_jet], etc.)
See ```NanoCORE/NanoAOD.h``` to find out what are available.
