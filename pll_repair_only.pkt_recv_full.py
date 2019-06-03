import pandas as pd
import jinja2

#controller = pd.read_csv('controller.csv', index_col='controller', delimiter=",")
block = "zx222016"
groups = ["full"]
#groups = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
#full_controller = pd.merge(data.reset_index(),controller.reset_index(), on="block", how="outer").set_index(['controller', 'icl'])
#full_controller = pd.merge(data.reset_index(),controller.reset_index(), on="block", how="outer")
icl = pd.read_csv('icl.csv', index_col='icl', delimiter=",")

"""
    NOTE THAT ONLY USE mem_id.csv FOR MEM PLL REPAIR
        190305 : pass group r1-r6
"""
mem_id  = pd.read_csv('mem_id_pkt_recv.csv', delimiter=",")
#full_controller[full_controller.repair][full_controller.block == "sa_asm"]
#full_controller[full_controller.repair == True][full_controller.block == "cluster"]['controller_inst']
outSpec = ""
pattern_header = jinja2.Template('''
        Patterns(MemoryBist_P1_repair_{{group}}) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_P1_repair_{{group}}) {
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
                        test_time_multiplier : ;
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
with open("pll_repair_group.tcl", 'w') as tcl:
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

with open("pll_repair_only_pkt_recv_full.spec", 'w') as full:
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
