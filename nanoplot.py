#!/bin/env python

from plottery import plottery as ply
import ROOT as r

tfile = r.TFile("output.root")

h_mmumu = tfile.Get("Mmumu")

import os
if not os.path.exists("plots"):
        os.makedirs("plots")

ply.plot_hist(bgs=[h_mmumu], options = { "output_name": "plots/Mmumu.pdf", "output_ic": True, })
