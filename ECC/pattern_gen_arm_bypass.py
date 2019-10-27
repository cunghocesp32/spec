import pandas as pd
import jinja2

#controller = pd.read_csv('controller.csv', index_col='controller', delimiter=",")
block = "zx222016"
groups = ["rf_2pA_nr_1", "rf_2pA_nr_2", "rf_2pA_nr_3", "rf_2pA_nr_4", "rf_2pA_nr_5", "rf_2pA_nr_6",
          "rf_spA_nr_1", "rf_spA_nr_2", "rf_2pA_repair_1", "sram_nr_1", "sram_repair_1"]
groups = ["ss_nr_1", "ss_nr_2", "ss_repair_1", "ss_repair_2"]
groups = ["ECC_nr_ss_1", "ECC_nr_arm_1", "ECC_repair_arm_1" , "ECC_repair_ss_1"]
groups = ["rf_2pA_nr_1", "rf_2pA_nr_8", "rf_2pA_nr_4", "rf_2pA_nr_5", "rf_2pA_nr_7"]
groups = ["rf_2pA_nr_1", "rf_2pA_nr_4", "rf_2pA_nr_cluster_u10"]
groups = ["rf_2pA_nr_1", "rf_2pA_nr_1_v0", "rf_2pA_nr_1_v1", "rf_2pA_nr_4", "rf_2pA_nr_7"]
groups = ["rf_2pA_nr_9", "rf_2pA_nr_10"]
groups = ["rf_2pA_nr_1", "rf_2pA_nr_1_oh_v1"]


#groups = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
#full_controller = pd.merge(data.reset_index(),controller.reset_index(), on="block", how="outer").set_index(['controller', 'icl'])
#full_controller = pd.merge(data.reset_index(),controller.reset_index(), on="block", how="outer")
icl = pd.read_csv('icl.csv', index_col='icl', delimiter=",")

"""
    NOTE THAT ONLY USE mem_id.csv FOR MEM PLL REPAIR
        190305 : pass group r1-r6
"""
file_target = "mem_id_ecc"
type_ecc = "noECC_rf_191014"
mem_id  = pd.read_csv(file_target+ '.csv', delimiter=",")
#full_controller[full_controller.repair][full_controller.block == "sa_asm"]
#full_controller[full_controller.repair == True][full_controller.block == "cluster"]['controller_inst']
outSpec = ""
pattern_header = jinja2.Template('''
        Patterns(MemoryBist_{{group}}) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_{{group}}_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                ''')
pattern_footer = jinja2.Template('''
                    } // End {{group}}
                } // End TestStep
            } //End Pattern
                ''')
controller_body = jinja2.Template('''
                Controller({{icl_id}}.{{controller}}) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : {{mem_en}} ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    ''')
with open(file_target + "_" + type_ecc+ ".tcl", 'w') as tcl:
    for gr in groups :
        tcl.write("set OCC_CLK_GATE({})  {} \n".format(gr, "{"))
        group = mem_id[mem_id.group == gr]
        print("Group {} has {} memories ".format(gr, len(group)))
        #templateLoader = jinja2.FileSystemLoader(searchpath="./")
        #templateEnv = jinja2.Environment(loader=templateLoader)
        #template = templateEnv.get_template("template.spec")
        #outSpec = template.render(group=gr, controller_list=group.iterrows())
        for i in group['icl'].unique():
            tcl.write("    {}.{}_gate_tessent_tdr_SCAN_TDR_inst.OCC_CLK_GATE_EN \n".format(i, icl.loc[i]["block"]))
        tcl.write("{} \n".format("}"))

with open(file_target + "_" + type_ecc + ".spec", 'w') as full:
    for gr in groups :
        outSpec = pattern_header.render(group=gr)

        group_id = mem_id[mem_id.group == gr]
        for icl_id in group_id.icl.unique():
            group_icl = group_id[group_id.icl == icl_id]
            for controller in group_icl.controller_inst.unique():
                group_controller  = group_icl[group_icl.controller_inst == controller]
                #print("{icl} + {controller}".format(icl=icl_id, controller=controller))
                #print("          {mem_id}".format(mem_id=",".join(list(group_controller.mem_id))))
                outSpec = outSpec + controller_body.render(icl_id=icl_id, controller=controller,
                                 mem_en=",".join(list(group_controller.mem_id)))
        outSpec = outSpec + pattern_footer.render(group=gr)
        full.write(outSpec)   
    full.write("\n//End")