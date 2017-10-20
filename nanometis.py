#!/bin/env python

################################
# Job tag and output hadoop path
################################

# NOTE: If you want to resubmit the skimming job, you need to delete $ANALYSIS_BASE/tasks and hadoop_path output path

job_tag = "v2"
hadoop_path = "metis/nano/{}".format(job_tag) # The output goes to /hadoop/cms/store/user/$USER/"hadoop_path"
nevtperfile = "-1"




###################################################################################################################
###################################################################################################################
# Below are the Metis submission code that users do not have to care about.
###################################################################################################################
###################################################################################################################

import time
import json
import metis

from time import sleep

from metis.Sample import DirectorySample
from metis.CondorTask import CondorTask

from metis.StatsParser import StatsParser

import sys
import os
import glob
import subprocess

# file/dir paths
nanodir = os.path.dirname(os.path.realpath(__file__))
anadir = os.getenv("ANALYSIS_BASE")
scriptsdir = os.path.join(os.getenv("ANALYSIS_BASE"), "scripts")
tar_path = os.path.join(nanodir, "package.tar")
targzpath = tar_path + ".gz"
metisdashboardpath = os.path.join(os.path.dirname(os.path.dirname(metis.__file__)), "dashboard")

# Create tarball
os.system("tar -cf {} *.C *.h".format(tar_path))
os.chdir(anadir)
os.system("tar -rf {} rooutil/rooutil.so NanoCORE/NanoCORE.so rooutil/*.h NanoCORE/*.h".format(tar_path))
os.chdir(scriptsdir)
os.system("tar -rf {} *.sh *.C ".format(tar_path))
os.chdir(nanodir)
os.system("gzip -f {}".format(tar_path))

# Configurations
exec_path = os.path.join(scriptsdir, "run.sh")
args = "-c NanoAOD_ScanChain.C output.root Events {} dummy".format(nevtperfile)

dslocs = [

    ["DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v1_MINIAODSIM_NanoAODv1"        , "/hadoop/cms/store/user/namin/NanoAODv1/ProjectMetis/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v1_MINIAODSIM_NanoAODv1"]        ,
    ["DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10_ext1-v1_MINIAODSIM_NanoAODv1"       , "/hadoop/cms/store/user/namin/NanoAODv1/ProjectMetis/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10_ext1-v1_MINIAODSIM_NanoAODv1"]       ,
    ["DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10_ext1-v2_MINIAODSIM_NanoAODv1"       , "/hadoop/cms/store/user/namin/NanoAODv1/ProjectMetis/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10_ext1-v2_MINIAODSIM_NanoAODv1"]       ,
    ["ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v2_MINIAODSIM_NanoAODv1", "/hadoop/cms/store/user/namin/NanoAODv1/ProjectMetis/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v2_MINIAODSIM_NanoAODv1"],
    ["ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v2_MINIAODSIM_NanoAODv1"    , "/hadoop/cms/store/user/namin/NanoAODv1/ProjectMetis/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v2_MINIAODSIM_NanoAODv1"]    ,
    ["TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v3_MINIAODSIM_NanoAODv1"                    , "/hadoop/cms/store/user/namin/NanoAODv1/ProjectMetis/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v3_MINIAODSIM_NanoAODv1"]                    ,
    ["TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10_ext1-v1_MINIAODSIM_NanoAODv1"                       , "/hadoop/cms/store/user/namin/NanoAODv1/ProjectMetis/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10_ext1-v1_MINIAODSIM_NanoAODv1"]                       ,
    ["WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v1_MINIAODSIM_NanoAODv1"                 , "/hadoop/cms/store/user/namin/NanoAODv1/ProjectMetis/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v1_MINIAODSIM_NanoAODv1"]                 ,
    ["WW_TuneCUETP8M1_13TeV-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v2_MINIAODSIM_NanoAODv1"                                     , "/hadoop/cms/store/user/namin/NanoAODv1/ProjectMetis/WW_TuneCUETP8M1_13TeV-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v2_MINIAODSIM_NanoAODv1"]                                     ,
    ["WZ_TuneCUETP8M1_13TeV-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v2_MINIAODSIM_NanoAODv1"                                     , "/hadoop/cms/store/user/namin/NanoAODv1/ProjectMetis/WZ_TuneCUETP8M1_13TeV-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v2_MINIAODSIM_NanoAODv1"]                                     ,
    ["ZZ_TuneCUETP8M1_13TeV-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v2_MINIAODSIM_NanoAODv1"                                     , "/hadoop/cms/store/user/namin/NanoAODv1/ProjectMetis/ZZ_TuneCUETP8M1_13TeV-pythia8_RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v2_MINIAODSIM_NanoAODv1"]                                     ,

]

total_summary = {}
while True:

    allcomplete = True
    for ds,loc in dslocs:
        task = CondorTask(
                sample = DirectorySample(
                    dataset=ds,
                    location=loc
                    ),
                open_dataset = False,
                flush = True,
                files_per_output = 1,
                output_name = "merged.root",
                tag = job_tag,
                arguments = args,
                executable = exec_path,
                tarfile = targzpath,
                special_dir = hadoop_path,
                condor_submit_params = {"sites" : "UAF,T2_US_UCSD"}
                )
        task.process()
        allcomplete = allcomplete and task.complete()
        # save some information for the dashboard
        total_summary[ds] = task.get_task_summary()
    # parse the total summary and write out the dashboard
    StatsParser(data=total_summary, webdir=metisdashboardpath).do()
    os.system("msummary")
    os.system("chmod -R 755 {}".format(metisdashboardpath))
    if allcomplete:
        print ""
        print "Job={} finished".format(job_tag)
        print ""
        break

    print 'Press Ctrl-C to force update, otherwise will sleep for 300 seconds'
    try:
        for i in range(0,300):
            sleep(1) # could use a backward counter to be preeety :)
    except KeyboardInterrupt:
        raw_input("Press Enter to force update, or Ctrl-C to quit.")
        print "Force updating..."
