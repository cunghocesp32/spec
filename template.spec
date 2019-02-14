        #####
        TestStep(Mbist_P1_hw_default_nonrepair_{{group}}) {
            MemoryBist {
                run_mode : hw_default;
                reduced_address_count : off;
                {% for index, row in controller_list %}
                Controller({{row['icl'] + '.' + row['controller_inst']}}) {
                    AdvancedOptions {
                        test_time_multiplier : 1.2;
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
        #####
