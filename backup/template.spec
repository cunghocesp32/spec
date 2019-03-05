    
    Patterns(MemoryBist_P1_repair_{{group}}) {
        tester_period : 80ns;
        SimulationOptions {
            monitor_internal_clock_pins : off;
       }
        TestStep(Mbist_P1_repair_{{group}}) {
            MemoryBist {
                run_mode : run_time_proc;
                reduced_address_count : off;
                {% for index, row in controller_list %}
                Controller({{row['icl'] + '.' + row['controller_inst']}}) {
                    AdvancedOptions {
                        test_time_multiplier : 1.5;
                        enable_memory_list : row['mem_en'] ;
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
                {% endfor %}
            }
        }
    }
        ////////////////////
