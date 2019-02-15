import pandas as pd

icl = pd.read_csv("full_mem.csv")
icl.controller = icl.block + "_gate_tessent_mbist_" + icl.controller + "_controller"
data = pd.read_csv("icl.csv")

full_controller = pd.merge(data.reset_index(),icl.reset_index(), on="block", how="outer")
#full_controller.to_csv("full_icl.csv")
A = full_controller.groupby(['icl','controller'])['mem_instance'].count()