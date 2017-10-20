# nano

=========================================================================================================


                                       MakeClass script


=========================================================================================================

This script creates CLASSNAME.cc and CLASSNAME.h file.
The generated source C++ codes can be used to read a ROOT's TTree with rest of the TasUtil tool at ease.
The generation of the code relies on:
  > https://github.com/cmstas/Software/blob/master/makeCMS3ClassFiles/makeCMS3ClassFiles.C

Usage:

[32m  > sh makeclass.sh [-f] [-h] [-x] ROOTFILE TTREENAME CLASSNAME [NAMESPACENAME=tas] [CLASSINSTANCENAME=mytree] (B[m


[32m -h (B[m: print this message
[32m -f (B[m: force run this script
[32m -x (B[m: create additional looper template files (i.e. ScanChain.C, doAll.C, compile.sh, run.sh, submit_batch.sh)

[32m ROOTFILE          (B[m= Path to the root file that holds an example TTree that you wish to study.
[32m TREENAME          (B[m= The TTree object TKey name in the ROOTFILE
[32m CLASSNAME         (B[m= The name you want to give to the class you are creating
[32m NAMESPACENAME     (B[m= The name you want to give to the namespace for accessing the ttree
[32m CLASSINSTANCENAME (B[m= The name of the global instance of the class that you are trying to create
                     (defaults to 'mytree')

(B[0;4m[1m[31mNOTE: If no argument is given, it will assume to create a CMS3 looper(B[m(B[m



