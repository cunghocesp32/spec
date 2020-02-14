import pandas as pd
import os.path, datetime
import dft_def
import jinja2
import block_action

BLOCK = block_action.BLOCK
lasted_data = pd.read_csv('lasted_data.csv', index_col='block', delimiter=",")


def task_run_review():
    def gen_data(review, mode, targets):
        with open(targets[0], 'a') as output:
            output.write("{b},{log},{m},{t},{cv},{tp},{tt},{sce},{lg}\n".format(
                           b=review.get_block_name(), log=review.get_log_file(), m=mode, t=datetime.datetime.now(),
                           cv=review.get_test_coverage(), tp=review.get_test_pattern(),
                           tt=review.get_test_atpg_time(), sce=review.get_scan_cells(),
                           lg=review.get_longest_chain_length()
            ))
    for block in BLOCK:
        dir_name = os.path.dirname(dft_def.get_refer_atpg(block,lasted_data))
        base_name = os.path.basename(dft_def.get_refer_atpg(block,lasted_data))
        for mode in ['dcsa_edt.ext', 'dcsa_edt.int', 'tdf_loc_edt.int', 'tdf_los_edt.int'] : 
            review = dft_def.DFT_REVIEW_ATPG(block, dir_name+"/"+base_name+"/atpg/log/log.atpg_"+mode)
            yield {
                'name' : 'run_review_' + block + '_' + mode,
                'file_dep' : ["lasted_data.csv", "block_action.py"],
                'actions' : [(gen_data, [review, mode])],
                'targets' : ["review_log/make_review_"+block+ "_" +mode +".log"]
            }

def task_run_clock_checking():
    def gen_data(review, targets):
        pass

    for block in BLOCK:
        dir_name = os.path.dirname(dft_def.get_refer_atpg(block,lasted_data))
        base_name = os.path.basename(dft_def.get_refer_atpg(block,lasted_data))
        
