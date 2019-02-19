import pandas as pd

icl = pd.read_csv("full_mem.csv")
icl.controller = icl.block + "_gate_tessent_mbist_" + icl.controller + "_controller"
controller = pd.read_csv("controller.csv")

full_controller = pd.merge(icl.reset_index(),controller.reset_index(), on="controller", how="outer")
#full_controller.to_csv("full_icl.csv")
A = full_controller.groupby(['icl','controller'])['mem_instance'].count()

full_controller = pd.read_csv("full_controller.csv")
temp = pd.read_csv("temp.csv")
mem_id = pd.merge(full_controller.reset_index(), temp.reset_index(), on=["controller", "mem_instance"], how="outer")
#id = pd.read_csv("mem_id.csv")