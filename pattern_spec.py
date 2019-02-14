import pandas as pd
import jinja2



icl = pd.read_csv('icl.csv', index_col='icl', delimiter=",")
#controller = pd.read_csv('controller.csv', index_col='controller', delimiter=",")
block = "zx222016"
groups = ["r1", "r2", "r3", "r4"]
groups = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
full_spec = ""
#full_controller = pd.merge(data.reset_index(),controller.reset_index(), on="block", how="outer").set_index(['controller', 'icl'])
#full_controller = pd.merge(data.reset_index(),controller.reset_index(), on="block", how="outer")

full_controller  = pd.read_csv('controller.csv', index_col='controller', delimiter=",")
#full_controller[full_controller.repair][full_controller.block == "sa_asm"]
#full_controller[full_controller.repair == True][full_controller.block == "cluster"]['controller_inst']
with open("group.tcl", 'w') as tcl:
    for gr in groups :
        tcl.write("set OCC_CLK_GATE({})  {} \n".format(gr, "{"))
        group = full_controller[full_controller.group == gr]
        print("Group {} has {} controllers ".format(gr, len(group)))
        templateLoader = jinja2.FileSystemLoader(searchpath="./")
        templateEnv = jinja2.Environment(loader=templateLoader)
        template = templateEnv.get_template("template.spec")
        outSpec = template.render(group=gr, controller_list=group.iterrows())
        for i in group['icl'].unique():
            tcl.write("    {}.{}_gate_tessent_tdr_SCAN_TDR_inst.OCC_CLK_GATE_EN \n".format(i, icl.loc[i]["block"]))
        tcl.write("{} \n".format("}"))
        with open('{}_teststep.spec'.format(gr), 'w') as f :
            f.write(outSpec)
        full_spec = full_spec + outSpec

with open("full.spec", 'w') as full:
    full.write(full_spec)
