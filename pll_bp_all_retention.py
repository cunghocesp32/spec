import pandas as pd
import jinja2



icl = pd.read_csv('icl.csv', index_col='icl', delimiter=",")
#controller = pd.read_csv('controller.csv', index_col='controller', delimiter=",")
block = "zx222016"
#groups = ["r1", "r2", "r3", "r4"]
groups = ["1","2"]
full_spec = ""
#full_controller = pd.merge(data.reset_index(),controller.reset_index(), on="block", how="outer").set_index(['controller', 'icl'])
#full_controller = pd.merge(data.reset_index(),controller.reset_index(), on="block", how="outer")

full_controller  = pd.read_csv('controller_retention.csv', delimiter=",")

pattern_header = jinja2.Template('''
        Patterns(p_zx016_mbist_pll_bp_retention_all) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(p_zx016_mbist_pll_bp_retention_all) {
                MemoryBist {
                run_mode : hw_default;
                reduced_address_count : off;
                parallel_retention_time : 50ms;
                ''')
pattern_footer = jinja2.Template('''
                    } // End {{group}}
                } // End TestStep
            } //End Pattern
                ''')
controller_body = jinja2.Template('''
                Controller({{icl_id}}.{{controller}}) {
                    parallel_retention_group : 1;
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : off;
                        compare_go_id : off;
                    }
                }
                    ''')

with open("pll_bp_retention_all_group.tcl", 'w') as tcl:
    for gr in groups :
        tcl.write("set OCC_CLK_GATE({})  {} \n".format(gr, "{"))
        print("TEST : ", full_controller[full_controller.group])
        group = full_controller[full_controller.group == gr]
        #print("Group {} has {} controllers ".format(gr, len(group)))
        outSpec = pattern_header.render(group=gr)
        for index, row in group.iterrows():
            outSpec += controller_body.render(icl_id=row.icl, controller=row.controller_inst)
        
        for i in group['icl'].unique():
            tcl.write("    {}.{}_gate_tessent_tdr_SCAN_TDR_inst.OCC_CLK_GATE_EN \n".format(i, icl.loc[i]["block"]))
        tcl.write("{} \n".format("}"))
        
        outSpec += pattern_footer.render(group=gr)
        full_spec = full_spec + outSpec

with open("pll_bp_rentention_all.spec", 'w') as full:
    full.write(full_spec)