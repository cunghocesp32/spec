
        Patterns(MemoryBist_ARM_nr_2pA_192x128) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_ARM_nr_2pA_192x128_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST25_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST31_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST36_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST42_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST46_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST51_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST55_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST56_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST60_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST65_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST70_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST74_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST78_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST83_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST87_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST91_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST95_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST25_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST31_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST36_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST42_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST46_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST51_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST55_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST56_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST60_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST65_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST70_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST74_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST78_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST83_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST87_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST91_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST95_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST25_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST31_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST36_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST42_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST46_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST51_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST55_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST56_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST60_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST65_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST70_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST74_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST78_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST83_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST87_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST91_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST95_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST25_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST31_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST36_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST42_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST46_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST51_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST55_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST56_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST60_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST65_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST70_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST74_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST78_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST83_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST87_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST91_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST95_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST25_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST31_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST36_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST42_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST46_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST51_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST55_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST56_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST60_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST65_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST70_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST74_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST78_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST83_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST87_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST91_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST95_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST25_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST31_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST36_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST42_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST46_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST51_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST55_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST56_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST60_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST65_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST70_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST74_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST78_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST83_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST87_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST91_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST95_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST25_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST31_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST36_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST42_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST46_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST51_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST55_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST56_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST60_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST65_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST70_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST74_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST78_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST83_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST87_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST91_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST95_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST25_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST31_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST36_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST42_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST46_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST51_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST55_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST56_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST60_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST65_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST70_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST74_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST78_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST83_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST87_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST91_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST95_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST25_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST31_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST36_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST42_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST46_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST51_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST55_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST56_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST60_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST65_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST70_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST74_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST78_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST83_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST87_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST91_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST95_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST25_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST31_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST36_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST42_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST46_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST51_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST55_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST56_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST60_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST65_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST70_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST74_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST78_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST83_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST87_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST91_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST95_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST25_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST31_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST36_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST42_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST46_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST51_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST55_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST56_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST60_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST65_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST70_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST74_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST78_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST83_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST87_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST91_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST95_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST25_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST31_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST36_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST42_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST46_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST51_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST55_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST56_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST60_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST65_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST70_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST74_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST78_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST83_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST87_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST91_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST95_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST25_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST31_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST36_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST42_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST46_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST51_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST55_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST56_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST60_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST65_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST70_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST74_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST78_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST83_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST87_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST91_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST95_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST25_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST31_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST36_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST42_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST46_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST51_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST55_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST56_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST60_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST65_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST70_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST74_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST78_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST83_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST87_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST91_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST95_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST25_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST31_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST36_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST42_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST46_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST51_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST55_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST56_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST60_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST65_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST70_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST74_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST78_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST83_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST87_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST91_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST95_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST25_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST31_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST36_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST42_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST46_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST51_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST55_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_ppu_me_pkt_ram_1r1w_192x128_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST56_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST60_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST65_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST70_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST74_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST78_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST83_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST87_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST91_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_pkt_ram_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST95_NON_REPAIR_BitSlice_128_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                    } // End ARM_nr_2pA_192x128
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_ESI_nr_211_512x30) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_ESI_nr_211_512x30_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_decoder_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST29_NON_REPAIR_BitSlice_30_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_decoder_u0_st_rd_ram_1r1w_512x29_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST84_NON_REPAIR_BitSlice_30_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_decoder_u0_st_rd_ram_1r1w_512x29_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST109_NON_REPAIR_BitSlice_30_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_wr_pack_u0.st_mmu_wr_u0_st_mmu_wr_decoder_u0_st_mmu_wr_pack_gate_tessent_mbist_sys_clk_MBIST11_NON_REPAIR_BitSlice_30_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                    } // End ESI_nr_211_512x30
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_ESI_nr_422_4096x18) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_ESI_nr_422_4096x18_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_qlist_u0_qlist_qdm_u0_ql_enq_deq_pipepkcnt_man_u0_deq_pipepkcnt_ram_3r2w_4096x12_wrapper_u0_ues_gmem_3r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST41_NON_REPAIR_BitSlice_18_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_qlist_u0_qlist_qdm_u0_ql_enq_deq_pipepkcnt_man_u0_deq_pipepkcnt_ram_3r2w_4096x12_wrapper_u0_ues_gmem_3r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST42_NON_REPAIR_BitSlice_18_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_qlist_u0_qlist_qdm_u0_ql_enq_deq_pipepkcnt_man_u0_deq_pipepkcnt_ram_3r2w_4096x12_wrapper_u0_ues_gmem_3r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST41_NON_REPAIR_BitSlice_18_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_qlist_u0_qlist_qdm_u0_ql_enq_deq_pipepkcnt_man_u0_deq_pipepkcnt_ram_3r2w_4096x12_wrapper_u0_ues_gmem_3r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST42_NON_REPAIR_BitSlice_18_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                    } // End ESI_nr_422_4096x18
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_ESI_repair_211_8192x20) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_ESI_repair_211_8192x20_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_spi_mid_wfqfq_link_ram_1r1w_524288x19_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST91_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_spi_mid_wfqfq_link_ram_1r1w_524288x19_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST95_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_tm_u0_crdt_u0.crdt_gate_tessent_mbist_sys_clk_MBIST60_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_spi_mid_wfqfq_link_ram_1r1w_524288x19_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST90_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_spi_mid_wfqfq_link_ram_1r1w_524288x19_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST94_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_spi_mid_wfqfq_link_ram_1r1w_524288x19_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST88_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_spi_mid_wfqfq_link_ram_1r1w_524288x19_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_spi_mid_wfqfq_link_ram_1r1w_524288x19_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST96_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_tm_u0_crdt_u0.crdt_gate_tessent_mbist_sys_clk_MBIST59_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_spi_mid_wfqfq_link_ram_1r1w_524288x19_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST89_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_spi_mid_wfqfq_link_ram_1r1w_524288x19_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST93_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                    } // End ESI_repair_211_8192x20
                } // End TestStep
            } //End Pattern
                
//End