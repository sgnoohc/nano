# nano

Currently the code just plots two muon mass.
The empty looper is tagged at 0.0.1.

# First time installing

    git clone --recursive -j8 git@github.com:sgnoohc/nano
    cd nano
    source scripts/setup.sh
    compile.sh

# Second time

    source scripts/setup.sh

# Running locally

    run.sh -c NanoAOD_ScanChain.C output.root Events -1 dummy /hadoop/cms/store/user/namin/NanoAODv1/ProjectMetis/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10_ext1-v1_MINIAODSIM_NanoAODv1/merged_ntuple_1.root

# Running batch jobs

Few options are at the top of the following scripts.  
Samples are turned off all except one DY sample.  
Feel free to turn additional samples.

    python nanometis.py

# Plotting after batch job finishes

First hadd your output that resides somewhere in the hadoop area that you configured in nanometis.py.  
Hadded file should be called ```output.root``` in order for the following script to recognize.

    python nanoplot.py
