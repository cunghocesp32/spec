
        Patterns(MemoryBist_opro_sr_211_uhs) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_opro_sr_211_uhs_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST49_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST53_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST65_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7,m8 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST69_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST73_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST51_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST55_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST59_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST63_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST67_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST56_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST60_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST64_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST68_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST72_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST50_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST54_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST58_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST62_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST66_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST70_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST74_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                    } // End opro_sr_211_uhs
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_qmu_rfinst_4096x29x16) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_qmu_rfinst_4096x29x16_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_qlist_u0_qlist_qdm_u0_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST70_NON_REPAIR_BitSlice_29_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_qlist_u0_qlist_qdm_u0_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST71_NON_REPAIR_BitSlice_29_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_qlist_u0_qlist_qdm_u0_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST70_NON_REPAIR_BitSlice_29_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_qlist_u0_qlist_qdm_u0_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST71_NON_REPAIR_BitSlice_29_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                    } // End qmu_rfinst_4096x29x16
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_cluster_rf_spA_128x122) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_cluster_rf_spA_128x122_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST23_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST28_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST34_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST39_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST40_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u1_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST45_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u1_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST49_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u1_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST54_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u1_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST59_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u2_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST63_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST68_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u2_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST73_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u2_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST77_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u3_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST81_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u3_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST85_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u3_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST90_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u3_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST94_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST23_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST28_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST34_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST39_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST40_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u1_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST45_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u1_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST49_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u1_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST54_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u1_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST59_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u2_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST63_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST68_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u2_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST73_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u2_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST77_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u3_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST81_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u3_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST85_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u3_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST90_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u3_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST94_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST23_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST28_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST34_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST39_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST40_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u1_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST45_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u1_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST49_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u1_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST54_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u1_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST59_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u2_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST63_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST68_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u2_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST73_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u2_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST77_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u3_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST81_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u3_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST85_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u3_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST90_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u3_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST94_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST23_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST28_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST34_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST39_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST40_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u1_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST45_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u1_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST49_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u1_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST54_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u1_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST59_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u2_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST63_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST68_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u2_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST73_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u2_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST77_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u3_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST81_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u3_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST85_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u3_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST90_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u3_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST94_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST23_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST28_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST34_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST39_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST40_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u1_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST45_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u1_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST49_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u1_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST54_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u1_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST59_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u2_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST63_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST68_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u2_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST73_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u2_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST77_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u3_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST81_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u3_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST85_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u3_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST90_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u3_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST94_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST23_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST28_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST34_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST39_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST40_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u1_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST45_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u1_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST49_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u1_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST54_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u1_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST59_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u2_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST63_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST68_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u2_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST73_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u2_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST77_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u3_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST81_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u3_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST85_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u3_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST90_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u3_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST94_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST23_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST28_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST34_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST39_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST40_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u1_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST45_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u1_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST49_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u1_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST54_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u1_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST59_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u2_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST63_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST68_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u2_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST73_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u2_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST77_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u3_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST81_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u3_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST85_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u3_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST90_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u3_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST94_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST23_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST28_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST34_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST39_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST40_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u1_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST45_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u1_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST49_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u1_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST54_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u1_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST59_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u2_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST63_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST68_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u2_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST73_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u2_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST77_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u3_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST81_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u3_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST85_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u3_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST90_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u3_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST94_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST23_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST28_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST34_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST39_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST40_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u1_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST45_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u1_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST49_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u1_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST54_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u1_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST59_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u2_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST63_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST68_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u2_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST73_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u2_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST77_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u3_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST81_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u3_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST85_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u3_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST90_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u3_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST94_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST23_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST28_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST34_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST39_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST40_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u1_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST45_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u1_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST49_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u1_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST54_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u1_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST59_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u2_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST63_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST68_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u2_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST73_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u2_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST77_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u3_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST81_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u3_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST85_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u3_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST90_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u3_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST94_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST23_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST28_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST34_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST39_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST40_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u1_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST45_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u1_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST49_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u1_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST54_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u1_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST59_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u2_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST63_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST68_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u2_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST73_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u2_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST77_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u3_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST81_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u3_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST85_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u3_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST90_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u3_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST94_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST23_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST28_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST34_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST39_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST40_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u1_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST45_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u1_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST49_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u1_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST54_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u1_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST59_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u2_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST63_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST68_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u2_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST73_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u2_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST77_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u3_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST81_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u3_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST85_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u3_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST90_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u3_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST94_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST23_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST28_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST34_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST39_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST40_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u1_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST45_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u1_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST49_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u1_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST54_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u1_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST59_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u2_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST63_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST68_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u2_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST73_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u2_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST77_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u3_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST81_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u3_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST85_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u3_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST90_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u3_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST94_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST23_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST28_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST34_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST39_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST40_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u1_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST45_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u1_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST49_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u1_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST54_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u1_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST59_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u2_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST63_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST68_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u2_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST73_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u2_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST77_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u3_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST81_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u3_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST85_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u3_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST90_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u3_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST94_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST23_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST28_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST34_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST39_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST40_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u1_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST45_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u1_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST49_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u1_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST54_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u1_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST59_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u2_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST63_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST68_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u2_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST73_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u2_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST77_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u3_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST81_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u3_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST85_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u3_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST90_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u3_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST94_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST23_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST28_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST34_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST39_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST40_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u1_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST45_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u1_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST49_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u1_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST54_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u1_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST59_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u2_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST63_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST68_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4,m5 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u2_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST73_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u2_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST77_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u3_me_u0_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST81_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u3_me_u1_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST85_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u3_me_u2_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST90_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u3_me_u3_me_cache_u0_ppu_me_cache_ram_1rw_128x487_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST94_NON_REPAIR_BitSlice_122_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                    } // End cluster_rf_spA_128x122
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_cluster_sram_spA_2048x80) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_cluster_sram_spA_2048x80_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_ppu_u0.cluster_u0.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20 ;
                        enable_memory_list : m1,m2,m3,m4 ;
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
                    
                    } // End cluster_sram_spA_2048x80
                } // End TestStep
            } //End Pattern
                
//End