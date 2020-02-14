import pandas as pd
import os.path, datetime
import dft_def
import block_action

BLOCK = block_action.BLOCK
lasted_data = pd.read_csv('lasted_data.csv', index_col='block', delimiter=",")

''' DEFINE GLOBAL VARIABLE '''
CARINA_SDF_DIR = "/scratch/carina_pddft/carina_ce/DFT/final"
    
def task_make_env():
    '''THIS TASK WILL CREATE ENV FOR ATPG & SIMULATION '''
    def gen_target(dir_name, lasted_name, targets):
        with open(targets[0],"a") as output :
            output.write("{} : {}\n".format(datetime.datetime.now(), dir_name + "/" + lasted_name))
    def process_sdf(atpg_folder, block):
        dft_def.gen_sdf_file(atpg_folder +"/sim_sdf/dcsa", block, "dcsa", "int_parallel")
        dft_def.gen_sdf_file(atpg_folder +"/sim_sdf/dcsa", block, "dcsa", "int_serial")
        dft_def.gen_sdf_file(atpg_folder +"/sim_sdf/dcsa", block, "dcsa", "ext_parallel")
        dft_def.gen_sdf_file(atpg_folder +"/sim_sdf/dcsa", block, "dcsa", "ext_serial")
        dft_def.gen_sdf_file(atpg_folder +"/sim_sdf/los", block, "tdf_los", "int_parallel")
        dft_def.gen_sdf_file(atpg_folder +"/sim_sdf/los", block, "tdf_los", "int_serial")
        dft_def.gen_sdf_file(atpg_folder +"/sim_sdf/los", block, "tdf_loc", "int_parallel")
        dft_def.gen_sdf_file(atpg_folder +"/sim_sdf/los", block, "tdf_loc", "int_serial")
    
    for block in BLOCK:
        dir_name = os.path.dirname(dft_def.get_refer_atpg(block,lasted_data))
        base_name = os.path.basename(dft_def.get_refer_atpg(block,lasted_data))
        netlist_dir = dft_def.get_netlist(block,lasted_data)
        lasted_name = "20200212_tiep_" + base_name

        yield {
            'name' : 'make_env_' + block,
            'file_dep' : ["lasted_data.csv", "block_action.py"],
            'actions' : ["cd {dir_name}; mkdir -p {pnr}; mkdir -p {pnr}/outData; cp -r {current}/atpg {pnr}/atpg; \
                          ln -ns {netlist_dir}/{block}.sv {pnr}/outData/{block}_scan_edt.v; \
                          ln -ns {netlist_dir}/{block}*sdf* {pnr}/atpg/sim_sdf/sdf; \
                          sed -i 's/canopus/carina/g'  atpg/run* atpg/override/* ;\
                          sed -i 's/carina_A/carina_ce/g' atpg/run* atpg/override/* ;\
                          ".format(dir_name=dir_name, current=base_name, pnr=lasted_name), 
                          (process_sdf, [dir_name + "/" + lasted_name + "/atpg", block])]
        }

def task_make_run_sdf():
    '''THIS TASK WILL GENERATE SDF RUN FILE'''
    ''' avaiable pat = dcsa, tdf_loc, tdf_los
                 mode = int_parallel, int_serial, ext_parallel, ext_serial'''
    for block in BLOCK:
        dir_name = os.path.dirname(dft_def.get_refer_atpg(block,lasted_data))
        base_name = os.path.basename(dft_def.get_refer_atpg(block,lasted_data))
        lasted_name = "20200208_tiep_" + base_name

        yield {
            'name' : 'make_sdf_' + block,
            'file_dep' : ["lasted_data.csv","block_target.csv"],
            'actions' : ["cd {dir_name}/{lasted_name}/atpg/sim_sdf; ".format(dir_name=dir_name, lasted_name=lasted_name),
                          (gen_target, [dir_name, lasted_name])],
            'targets' : ["make_env.log"]
        }
def task_run_dcsa():
    '''THIS TASK RUN ALL DCSA FOR TARGET BLOCK'''
    def gen_dcsa_log():
        with open(targets[0], "a") as output:
            output.write("\n")
    
    for block in BLOCK:
        dir_name = os.path.dirname(dft_def.get_refer_atpg(block,lasted_data))
        base_name = os.path.basename(dft_def.get_refer_atpg(block,lasted_data))
        lasted_name = "20200208_tiep_" + base_name

        yield {
            'name' : 'make_run_dcsa' + block,
            'file_dep' : ["lasted_data.csv"],
            'actions' : ["cd {dir_name}/{lasted_name}; cd -".format(dir_name=dir_name,lasted_name=lasted_name),
                          (gen_dcsa_log, [dir_name, lasted_name])],
            'targets' : ["make_run_dcsa.log"]
        }    
def task_copy_ref():
    """THIS TASK WILL COPY REFER DOFILE"""
    return {
        'actions' : [print("Block {}".format(BLOCK))],
    }