
        Patterns(MemoryBist_cluster_rf_2pA_32x160) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_cluster_rf_2pA_32x160_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST7_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST8_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST9_NON_REPAIR_BitSlice_160_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST10_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST7_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST8_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST9_NON_REPAIR_BitSlice_160_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST10_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST7_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST8_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST9_NON_REPAIR_BitSlice_160_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST10_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST7_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST8_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST9_NON_REPAIR_BitSlice_160_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST10_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST7_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST8_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST9_NON_REPAIR_BitSlice_160_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST10_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST7_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST8_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST9_NON_REPAIR_BitSlice_160_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST10_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST7_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST8_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST9_NON_REPAIR_BitSlice_160_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST10_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST7_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST8_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST9_NON_REPAIR_BitSlice_160_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST10_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST7_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST8_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST9_NON_REPAIR_BitSlice_160_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST10_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST7_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST8_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST9_NON_REPAIR_BitSlice_160_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST10_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST7_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST8_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST9_NON_REPAIR_BitSlice_160_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST10_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST7_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST8_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST9_NON_REPAIR_BitSlice_160_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST10_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST7_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST8_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST9_NON_REPAIR_BitSlice_160_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST10_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST7_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST8_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST9_NON_REPAIR_BitSlice_160_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST10_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST7_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST8_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST9_NON_REPAIR_BitSlice_160_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST10_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST7_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST8_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST9_NON_REPAIR_BitSlice_160_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_mex_u0_cluster_mf_in_u0_ppu_cluster_mf_in_afifo_32x2048_wrapper_u0_ppu_cluster_mf_in_ram_1r1w_32x2048_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST10_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                    } // End cluster_rf_2pA_32x160
                } // End TestStep
            } //End Pattern
                
//End