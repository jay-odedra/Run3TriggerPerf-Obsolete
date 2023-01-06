import awkward as ak
import numpy as np
import time
import uproot as uproot
import json
import bisect
import pandas as pd

name_input = "/vols/cms/jo3717/slimming/Run3TriggerPerf/commissioning/input/ntuples/2022Oct12/ntuple_2022Dec15_Run2022Dv1.root"+":tree"
with uproot.open(name_input,
                    file_handler=uproot.MultithreadedFileSource,
                    num_workers=100) as file_input:

            print(" Available branches",file_input.keys())
