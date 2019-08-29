import pandas as pd
import jinja2

icl = pd.read_csv('icl.csv', index_col='icl', delimiter=",")
#controller = pd.read_csv('controller.csv', index_col='controller', delimiter=",")
block = "zx222016"
groups = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]

#groups = ["6", "7", "10", "15"]
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
                        test_time_multiplier : 2;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                        StopOnErrorOptions {
                            failure_limit : auto_increment ;
                        }
                    }
                }
                    ''')
with open("pll_nonrepair_group.tcl", 'w') as tcl:
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

with open("pll_nonrepair_full.spec", 'w') as full:
    full.write(full_spec)