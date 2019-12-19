import pandas as pd
import jinja2

icl = pd.read_csv('icl.csv', index_col='icl', delimiter=",")
#controller = pd.read_csv('controller.csv', index_col='controller', delimiter=",")
block = "zx222016"
groups = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
groups = ["14", "14_mac_tx_v0"]
groups = ["6", "7", "10", "15"]
# Trial for u_scan_937 -191210
groups = ["1", "1_pll937"]
# Update for 15groups exclude u_scan_937
groups = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
groups = ["pll_937"]
date = "191210_uscan937"
date = "191210_exclude_uscan937"
date = "191212_uscan937"
full_spec = ""
#full_controller = pd.merge(data.reset_index(),controller.reset_index(), on="block", how="outer").set_index(['controller', 'icl'])
#full_controller = pd.merge(data.reset_index(),controller.reset_index(), on="block", how="outer")

full_controller  = pd.read_csv('controller.csv', index_col='controller', delimiter=",")

pattern_header = jinja2.Template('''
        Patterns(MemoryBist_P1_pll_{{group}}) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_P1_{{group}}) {
                MemoryBist {
                run_mode : hw_default;
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
                        test_time_multiplier : 5;
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
with open("pll_nonrepair_group_" + date + ".tcl", 'w') as tcl:
    for gr in groups :
        tcl.write("set OCC_CLK_GATE({})  {} \n".format(gr, "{"))
        group = full_controller[full_controller.group == gr]
        print("Group {} has {} controllers ".format(gr, len(group)))
        outSpec = pattern_header.render(group=gr)
        for index, row in group.iterrows():
            outSpec += controller_body.render(icl_id=row.icl, controller=row.controller_inst)
        
        for i in group['icl'].unique():
            tcl.write("    {}.{}_gate_tessent_tdr_SCAN_TDR_inst.OCC_CLK_GATE_EN \n".format(i, icl.loc[i]["block"]))
        tcl.write("{} \n".format("}"))
        
        outSpec += pattern_footer.render(group=gr)
        full_spec = full_spec + outSpec

with open("pll_nonrepair_full_" + date + ".spec", 'w') as full:
    full.write(full_spec)
