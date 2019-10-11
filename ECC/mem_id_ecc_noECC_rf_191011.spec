
        Patterns(MemoryBist_rf_2pA_nr_9) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_rf_2pA_nr_9_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST1_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_afifo_64x77_wrapper_u0_ppu_coprocess_rsp_ram_1r1w_64x77_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST11_NON_REPAIR_BitSlice_78_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_fwft_fifo_128x78_wrapper_u0_ppu_coprocess_rsp_fifo_128x78_wrapper_ppu_coprocess_rsp_ram_1r1w_128x78_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST12_NON_REPAIR_BitSlice_80_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_afifo_64x272_wrapper_u0_ppu_ese_rsp_ram_1r1w_64x272_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST13_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_ram_1w1r_128x272_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST14_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_afifo_64x143_wrapper_u0_ppu_srh0_rsp_ram_1r1w_64x143_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST15_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_ram_1w1r_128x143_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST16_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_afifo_64x144_wrapper_u0_ppu_srh1_rsp_ram_1r1w_64x144_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST17_NON_REPAIR_BitSlice_146_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST2_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST24_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST27_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_gate_tessent_mbist_me_core_clk_MBIST29_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST30_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST33_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST35_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST38_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_gate_tessent_mbist_me_core_clk_MBIST41_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST44_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST48_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh0_u0_key_send_to_srh0_u0_ppu_srh0_key_afifo_16x54_wrapper_u0_ppu_srh0_key_ram_1r1w_16x54_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST5_NON_REPAIR_BitSlice_56_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u1_cluster_gate_tessent_mbist_me_core_clk_MBIST50_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST53_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST58_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh1_u0_key_send_to_srh1_u0_ppu_srh1_key_afifo_16x109_wrapper_u0_ppu_srh1_key_ram_1r1w_16x109_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST6_NON_REPAIR_BitSlice_110_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST62_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST64_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST67_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_gate_tessent_mbist_me_core_clk_MBIST69_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST72_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST76_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST80_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST82_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST84_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST86_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST89_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST93_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST97_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u0.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST1_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_afifo_64x77_wrapper_u0_ppu_coprocess_rsp_ram_1r1w_64x77_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST11_NON_REPAIR_BitSlice_78_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_fwft_fifo_128x78_wrapper_u0_ppu_coprocess_rsp_fifo_128x78_wrapper_ppu_coprocess_rsp_ram_1r1w_128x78_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST12_NON_REPAIR_BitSlice_80_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_afifo_64x272_wrapper_u0_ppu_ese_rsp_ram_1r1w_64x272_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST13_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_ram_1w1r_128x272_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST14_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_afifo_64x143_wrapper_u0_ppu_srh0_rsp_ram_1r1w_64x143_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST15_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_ram_1w1r_128x143_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST16_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_afifo_64x144_wrapper_u0_ppu_srh1_rsp_ram_1r1w_64x144_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST17_NON_REPAIR_BitSlice_146_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST2_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST24_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST27_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_gate_tessent_mbist_me_core_clk_MBIST29_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST30_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST33_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST35_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST38_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_gate_tessent_mbist_me_core_clk_MBIST41_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST44_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST48_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh0_u0_key_send_to_srh0_u0_ppu_srh0_key_afifo_16x54_wrapper_u0_ppu_srh0_key_ram_1r1w_16x54_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST5_NON_REPAIR_BitSlice_56_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u1_cluster_gate_tessent_mbist_me_core_clk_MBIST50_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST53_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST58_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh1_u0_key_send_to_srh1_u0_ppu_srh1_key_afifo_16x109_wrapper_u0_ppu_srh1_key_ram_1r1w_16x109_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST6_NON_REPAIR_BitSlice_110_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST62_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST64_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST67_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_gate_tessent_mbist_me_core_clk_MBIST69_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST72_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST76_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST80_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST82_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST84_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST86_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST89_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST93_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST97_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u10.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST1_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_afifo_64x77_wrapper_u0_ppu_coprocess_rsp_ram_1r1w_64x77_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST11_NON_REPAIR_BitSlice_78_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_fwft_fifo_128x78_wrapper_u0_ppu_coprocess_rsp_fifo_128x78_wrapper_ppu_coprocess_rsp_ram_1r1w_128x78_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST12_NON_REPAIR_BitSlice_80_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_afifo_64x272_wrapper_u0_ppu_ese_rsp_ram_1r1w_64x272_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST13_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_ram_1w1r_128x272_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST14_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_afifo_64x143_wrapper_u0_ppu_srh0_rsp_ram_1r1w_64x143_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST15_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_ram_1w1r_128x143_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST16_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_afifo_64x144_wrapper_u0_ppu_srh1_rsp_ram_1r1w_64x144_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST17_NON_REPAIR_BitSlice_146_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST2_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST24_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST27_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_gate_tessent_mbist_me_core_clk_MBIST29_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST30_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST33_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST35_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST38_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_gate_tessent_mbist_me_core_clk_MBIST41_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST44_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST48_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh0_u0_key_send_to_srh0_u0_ppu_srh0_key_afifo_16x54_wrapper_u0_ppu_srh0_key_ram_1r1w_16x54_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST5_NON_REPAIR_BitSlice_56_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u1_cluster_gate_tessent_mbist_me_core_clk_MBIST50_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST53_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST58_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh1_u0_key_send_to_srh1_u0_ppu_srh1_key_afifo_16x109_wrapper_u0_ppu_srh1_key_ram_1r1w_16x109_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST6_NON_REPAIR_BitSlice_110_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST62_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST64_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST67_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_gate_tessent_mbist_me_core_clk_MBIST69_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST72_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST76_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST80_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST82_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST84_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST86_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST89_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST93_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST97_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u12.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST1_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_afifo_64x77_wrapper_u0_ppu_coprocess_rsp_ram_1r1w_64x77_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST11_NON_REPAIR_BitSlice_78_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_fwft_fifo_128x78_wrapper_u0_ppu_coprocess_rsp_fifo_128x78_wrapper_ppu_coprocess_rsp_ram_1r1w_128x78_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST12_NON_REPAIR_BitSlice_80_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_afifo_64x272_wrapper_u0_ppu_ese_rsp_ram_1r1w_64x272_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST13_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_ram_1w1r_128x272_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST14_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_afifo_64x143_wrapper_u0_ppu_srh0_rsp_ram_1r1w_64x143_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST15_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_ram_1w1r_128x143_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST16_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_afifo_64x144_wrapper_u0_ppu_srh1_rsp_ram_1r1w_64x144_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST17_NON_REPAIR_BitSlice_146_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST2_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST24_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST27_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_gate_tessent_mbist_me_core_clk_MBIST29_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST30_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST33_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST35_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST38_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_gate_tessent_mbist_me_core_clk_MBIST41_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST44_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST48_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh0_u0_key_send_to_srh0_u0_ppu_srh0_key_afifo_16x54_wrapper_u0_ppu_srh0_key_ram_1r1w_16x54_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST5_NON_REPAIR_BitSlice_56_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u1_cluster_gate_tessent_mbist_me_core_clk_MBIST50_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST53_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST58_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh1_u0_key_send_to_srh1_u0_ppu_srh1_key_afifo_16x109_wrapper_u0_ppu_srh1_key_ram_1r1w_16x109_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST6_NON_REPAIR_BitSlice_110_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST62_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST64_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST67_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_gate_tessent_mbist_me_core_clk_MBIST69_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST72_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST76_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST80_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST82_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST84_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST86_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST89_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST93_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST97_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u14.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST1_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_afifo_64x77_wrapper_u0_ppu_coprocess_rsp_ram_1r1w_64x77_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST11_NON_REPAIR_BitSlice_78_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_fwft_fifo_128x78_wrapper_u0_ppu_coprocess_rsp_fifo_128x78_wrapper_ppu_coprocess_rsp_ram_1r1w_128x78_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST12_NON_REPAIR_BitSlice_80_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_afifo_64x272_wrapper_u0_ppu_ese_rsp_ram_1r1w_64x272_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST13_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_ram_1w1r_128x272_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST14_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_afifo_64x143_wrapper_u0_ppu_srh0_rsp_ram_1r1w_64x143_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST15_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_ram_1w1r_128x143_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST16_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_afifo_64x144_wrapper_u0_ppu_srh1_rsp_ram_1r1w_64x144_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST17_NON_REPAIR_BitSlice_146_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST2_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST24_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST27_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_gate_tessent_mbist_me_core_clk_MBIST29_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST30_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST33_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST35_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST38_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_gate_tessent_mbist_me_core_clk_MBIST41_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST44_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST48_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh0_u0_key_send_to_srh0_u0_ppu_srh0_key_afifo_16x54_wrapper_u0_ppu_srh0_key_ram_1r1w_16x54_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST5_NON_REPAIR_BitSlice_56_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u1_cluster_gate_tessent_mbist_me_core_clk_MBIST50_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST53_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST58_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh1_u0_key_send_to_srh1_u0_ppu_srh1_key_afifo_16x109_wrapper_u0_ppu_srh1_key_ram_1r1w_16x109_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST6_NON_REPAIR_BitSlice_110_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST62_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST64_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST67_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_gate_tessent_mbist_me_core_clk_MBIST69_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST72_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST76_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST80_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST82_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST84_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST86_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST89_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST93_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST97_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u2.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST1_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_afifo_64x77_wrapper_u0_ppu_coprocess_rsp_ram_1r1w_64x77_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST11_NON_REPAIR_BitSlice_78_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_fwft_fifo_128x78_wrapper_u0_ppu_coprocess_rsp_fifo_128x78_wrapper_ppu_coprocess_rsp_ram_1r1w_128x78_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST12_NON_REPAIR_BitSlice_80_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_afifo_64x272_wrapper_u0_ppu_ese_rsp_ram_1r1w_64x272_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST13_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_ram_1w1r_128x272_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST14_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_afifo_64x143_wrapper_u0_ppu_srh0_rsp_ram_1r1w_64x143_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST15_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_ram_1w1r_128x143_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST16_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_afifo_64x144_wrapper_u0_ppu_srh1_rsp_ram_1r1w_64x144_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST17_NON_REPAIR_BitSlice_146_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST2_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST24_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST27_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_gate_tessent_mbist_me_core_clk_MBIST29_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST30_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST33_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST35_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST38_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_gate_tessent_mbist_me_core_clk_MBIST41_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST44_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST48_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh0_u0_key_send_to_srh0_u0_ppu_srh0_key_afifo_16x54_wrapper_u0_ppu_srh0_key_ram_1r1w_16x54_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST5_NON_REPAIR_BitSlice_56_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u1_cluster_gate_tessent_mbist_me_core_clk_MBIST50_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST53_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST58_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh1_u0_key_send_to_srh1_u0_ppu_srh1_key_afifo_16x109_wrapper_u0_ppu_srh1_key_ram_1r1w_16x109_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST6_NON_REPAIR_BitSlice_110_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST62_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST64_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST67_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_gate_tessent_mbist_me_core_clk_MBIST69_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST72_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST76_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST80_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST82_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST84_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST86_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST89_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST93_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST97_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u4.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST1_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_afifo_64x77_wrapper_u0_ppu_coprocess_rsp_ram_1r1w_64x77_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST11_NON_REPAIR_BitSlice_78_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_fwft_fifo_128x78_wrapper_u0_ppu_coprocess_rsp_fifo_128x78_wrapper_ppu_coprocess_rsp_ram_1r1w_128x78_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST12_NON_REPAIR_BitSlice_80_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_afifo_64x272_wrapper_u0_ppu_ese_rsp_ram_1r1w_64x272_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST13_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_ram_1w1r_128x272_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST14_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_afifo_64x143_wrapper_u0_ppu_srh0_rsp_ram_1r1w_64x143_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST15_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_ram_1w1r_128x143_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST16_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_afifo_64x144_wrapper_u0_ppu_srh1_rsp_ram_1r1w_64x144_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST17_NON_REPAIR_BitSlice_146_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST2_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST24_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST27_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_gate_tessent_mbist_me_core_clk_MBIST29_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST30_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST33_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST35_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST38_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_gate_tessent_mbist_me_core_clk_MBIST41_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST44_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST48_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh0_u0_key_send_to_srh0_u0_ppu_srh0_key_afifo_16x54_wrapper_u0_ppu_srh0_key_ram_1r1w_16x54_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST5_NON_REPAIR_BitSlice_56_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u1_cluster_gate_tessent_mbist_me_core_clk_MBIST50_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST53_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST58_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh1_u0_key_send_to_srh1_u0_ppu_srh1_key_afifo_16x109_wrapper_u0_ppu_srh1_key_ram_1r1w_16x109_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST6_NON_REPAIR_BitSlice_110_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST62_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST64_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST67_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_gate_tessent_mbist_me_core_clk_MBIST69_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST72_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST76_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST80_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST82_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST84_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST86_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST89_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST93_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST97_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u6.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST1_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_afifo_64x77_wrapper_u0_ppu_coprocess_rsp_ram_1r1w_64x77_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST11_NON_REPAIR_BitSlice_78_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_fwft_fifo_128x78_wrapper_u0_ppu_coprocess_rsp_fifo_128x78_wrapper_ppu_coprocess_rsp_ram_1r1w_128x78_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST12_NON_REPAIR_BitSlice_80_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_afifo_64x272_wrapper_u0_ppu_ese_rsp_ram_1r1w_64x272_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST13_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_ram_1w1r_128x272_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST14_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_afifo_64x143_wrapper_u0_ppu_srh0_rsp_ram_1r1w_64x143_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST15_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_ram_1w1r_128x143_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST16_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_afifo_64x144_wrapper_u0_ppu_srh1_rsp_ram_1r1w_64x144_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST17_NON_REPAIR_BitSlice_146_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST2_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST24_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST27_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_gate_tessent_mbist_me_core_clk_MBIST29_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST30_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST33_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST35_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST38_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_gate_tessent_mbist_me_core_clk_MBIST41_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST44_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST48_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh0_u0_key_send_to_srh0_u0_ppu_srh0_key_afifo_16x54_wrapper_u0_ppu_srh0_key_ram_1r1w_16x54_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST5_NON_REPAIR_BitSlice_56_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u1_cluster_gate_tessent_mbist_me_core_clk_MBIST50_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST53_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST58_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh1_u0_key_send_to_srh1_u0_ppu_srh1_key_afifo_16x109_wrapper_u0_ppu_srh1_key_ram_1r1w_16x109_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST6_NON_REPAIR_BitSlice_110_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST62_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST64_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST67_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_gate_tessent_mbist_me_core_clk_MBIST69_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST72_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST76_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST80_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST82_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST84_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST86_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST89_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST93_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST97_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u8.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                    } // End rf_2pA_nr_9
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_rf_2pA_nr_10) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_rf_2pA_nr_10_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST1_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_afifo_64x77_wrapper_u0_ppu_coprocess_rsp_ram_1r1w_64x77_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST11_NON_REPAIR_BitSlice_78_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_fwft_fifo_128x78_wrapper_u0_ppu_coprocess_rsp_fifo_128x78_wrapper_ppu_coprocess_rsp_ram_1r1w_128x78_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST12_NON_REPAIR_BitSlice_80_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_afifo_64x272_wrapper_u0_ppu_ese_rsp_ram_1r1w_64x272_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST13_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_ram_1w1r_128x272_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST14_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_afifo_64x143_wrapper_u0_ppu_srh0_rsp_ram_1r1w_64x143_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST15_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_ram_1w1r_128x143_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST16_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_afifo_64x144_wrapper_u0_ppu_srh1_rsp_ram_1r1w_64x144_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST17_NON_REPAIR_BitSlice_146_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST2_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST24_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST27_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_gate_tessent_mbist_me_core_clk_MBIST29_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST30_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST33_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST35_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST38_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_gate_tessent_mbist_me_core_clk_MBIST41_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST44_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST48_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh0_u0_key_send_to_srh0_u0_ppu_srh0_key_afifo_16x54_wrapper_u0_ppu_srh0_key_ram_1r1w_16x54_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST5_NON_REPAIR_BitSlice_56_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u1_cluster_gate_tessent_mbist_me_core_clk_MBIST50_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST53_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST58_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh1_u0_key_send_to_srh1_u0_ppu_srh1_key_afifo_16x109_wrapper_u0_ppu_srh1_key_ram_1r1w_16x109_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST6_NON_REPAIR_BitSlice_110_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST62_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST64_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST67_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_gate_tessent_mbist_me_core_clk_MBIST69_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST72_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST76_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST80_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST82_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST84_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST86_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST89_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST93_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST97_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u1.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST1_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_afifo_64x77_wrapper_u0_ppu_coprocess_rsp_ram_1r1w_64x77_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST11_NON_REPAIR_BitSlice_78_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_fwft_fifo_128x78_wrapper_u0_ppu_coprocess_rsp_fifo_128x78_wrapper_ppu_coprocess_rsp_ram_1r1w_128x78_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST12_NON_REPAIR_BitSlice_80_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_afifo_64x272_wrapper_u0_ppu_ese_rsp_ram_1r1w_64x272_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST13_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_ram_1w1r_128x272_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST14_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_afifo_64x143_wrapper_u0_ppu_srh0_rsp_ram_1r1w_64x143_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST15_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_ram_1w1r_128x143_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST16_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_afifo_64x144_wrapper_u0_ppu_srh1_rsp_ram_1r1w_64x144_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST17_NON_REPAIR_BitSlice_146_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST2_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST24_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST27_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_gate_tessent_mbist_me_core_clk_MBIST29_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST30_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST33_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST35_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST38_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_gate_tessent_mbist_me_core_clk_MBIST41_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST44_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST48_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh0_u0_key_send_to_srh0_u0_ppu_srh0_key_afifo_16x54_wrapper_u0_ppu_srh0_key_ram_1r1w_16x54_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST5_NON_REPAIR_BitSlice_56_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u1_cluster_gate_tessent_mbist_me_core_clk_MBIST50_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST53_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST58_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh1_u0_key_send_to_srh1_u0_ppu_srh1_key_afifo_16x109_wrapper_u0_ppu_srh1_key_ram_1r1w_16x109_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST6_NON_REPAIR_BitSlice_110_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST62_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST64_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST67_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_gate_tessent_mbist_me_core_clk_MBIST69_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST72_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST76_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST80_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST82_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST84_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST86_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST89_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST93_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST97_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u11.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST1_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_afifo_64x77_wrapper_u0_ppu_coprocess_rsp_ram_1r1w_64x77_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST11_NON_REPAIR_BitSlice_78_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_fwft_fifo_128x78_wrapper_u0_ppu_coprocess_rsp_fifo_128x78_wrapper_ppu_coprocess_rsp_ram_1r1w_128x78_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST12_NON_REPAIR_BitSlice_80_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_afifo_64x272_wrapper_u0_ppu_ese_rsp_ram_1r1w_64x272_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST13_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_ram_1w1r_128x272_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST14_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_afifo_64x143_wrapper_u0_ppu_srh0_rsp_ram_1r1w_64x143_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST15_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_ram_1w1r_128x143_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST16_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_afifo_64x144_wrapper_u0_ppu_srh1_rsp_ram_1r1w_64x144_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST17_NON_REPAIR_BitSlice_146_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST2_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST24_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST27_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_gate_tessent_mbist_me_core_clk_MBIST29_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST30_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST33_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST35_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST38_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_gate_tessent_mbist_me_core_clk_MBIST41_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST44_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST48_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh0_u0_key_send_to_srh0_u0_ppu_srh0_key_afifo_16x54_wrapper_u0_ppu_srh0_key_ram_1r1w_16x54_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST5_NON_REPAIR_BitSlice_56_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u1_cluster_gate_tessent_mbist_me_core_clk_MBIST50_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST53_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST58_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh1_u0_key_send_to_srh1_u0_ppu_srh1_key_afifo_16x109_wrapper_u0_ppu_srh1_key_ram_1r1w_16x109_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST6_NON_REPAIR_BitSlice_110_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST62_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST64_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST67_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_gate_tessent_mbist_me_core_clk_MBIST69_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST72_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST76_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST80_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST82_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST84_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST86_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST89_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST93_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST97_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u13.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST1_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_afifo_64x77_wrapper_u0_ppu_coprocess_rsp_ram_1r1w_64x77_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST11_NON_REPAIR_BitSlice_78_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_fwft_fifo_128x78_wrapper_u0_ppu_coprocess_rsp_fifo_128x78_wrapper_ppu_coprocess_rsp_ram_1r1w_128x78_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST12_NON_REPAIR_BitSlice_80_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_afifo_64x272_wrapper_u0_ppu_ese_rsp_ram_1r1w_64x272_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST13_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_ram_1w1r_128x272_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST14_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_afifo_64x143_wrapper_u0_ppu_srh0_rsp_ram_1r1w_64x143_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST15_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_ram_1w1r_128x143_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST16_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_afifo_64x144_wrapper_u0_ppu_srh1_rsp_ram_1r1w_64x144_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST17_NON_REPAIR_BitSlice_146_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST2_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST24_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST27_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_gate_tessent_mbist_me_core_clk_MBIST29_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST30_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST33_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST35_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST38_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_gate_tessent_mbist_me_core_clk_MBIST41_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST44_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST48_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh0_u0_key_send_to_srh0_u0_ppu_srh0_key_afifo_16x54_wrapper_u0_ppu_srh0_key_ram_1r1w_16x54_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST5_NON_REPAIR_BitSlice_56_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u1_cluster_gate_tessent_mbist_me_core_clk_MBIST50_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST53_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST58_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh1_u0_key_send_to_srh1_u0_ppu_srh1_key_afifo_16x109_wrapper_u0_ppu_srh1_key_ram_1r1w_16x109_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST6_NON_REPAIR_BitSlice_110_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST62_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST64_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST67_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_gate_tessent_mbist_me_core_clk_MBIST69_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST72_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST76_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST80_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST82_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST84_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST86_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST89_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST93_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST97_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u15.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST1_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_afifo_64x77_wrapper_u0_ppu_coprocess_rsp_ram_1r1w_64x77_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST11_NON_REPAIR_BitSlice_78_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_fwft_fifo_128x78_wrapper_u0_ppu_coprocess_rsp_fifo_128x78_wrapper_ppu_coprocess_rsp_ram_1r1w_128x78_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST12_NON_REPAIR_BitSlice_80_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_afifo_64x272_wrapper_u0_ppu_ese_rsp_ram_1r1w_64x272_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST13_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_ram_1w1r_128x272_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST14_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_afifo_64x143_wrapper_u0_ppu_srh0_rsp_ram_1r1w_64x143_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST15_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_ram_1w1r_128x143_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST16_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_afifo_64x144_wrapper_u0_ppu_srh1_rsp_ram_1r1w_64x144_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST17_NON_REPAIR_BitSlice_146_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST2_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST24_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST27_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_gate_tessent_mbist_me_core_clk_MBIST29_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST30_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST33_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST35_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST38_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_gate_tessent_mbist_me_core_clk_MBIST41_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST44_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST48_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh0_u0_key_send_to_srh0_u0_ppu_srh0_key_afifo_16x54_wrapper_u0_ppu_srh0_key_ram_1r1w_16x54_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST5_NON_REPAIR_BitSlice_56_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u1_cluster_gate_tessent_mbist_me_core_clk_MBIST50_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST53_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST58_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh1_u0_key_send_to_srh1_u0_ppu_srh1_key_afifo_16x109_wrapper_u0_ppu_srh1_key_ram_1r1w_16x109_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST6_NON_REPAIR_BitSlice_110_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST62_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST64_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST67_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_gate_tessent_mbist_me_core_clk_MBIST69_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST72_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST76_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST80_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST82_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST84_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST86_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST89_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST93_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST97_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u3.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST1_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_afifo_64x77_wrapper_u0_ppu_coprocess_rsp_ram_1r1w_64x77_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST11_NON_REPAIR_BitSlice_78_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_fwft_fifo_128x78_wrapper_u0_ppu_coprocess_rsp_fifo_128x78_wrapper_ppu_coprocess_rsp_ram_1r1w_128x78_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST12_NON_REPAIR_BitSlice_80_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_afifo_64x272_wrapper_u0_ppu_ese_rsp_ram_1r1w_64x272_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST13_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_ram_1w1r_128x272_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST14_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_afifo_64x143_wrapper_u0_ppu_srh0_rsp_ram_1r1w_64x143_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST15_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_ram_1w1r_128x143_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST16_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_afifo_64x144_wrapper_u0_ppu_srh1_rsp_ram_1r1w_64x144_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST17_NON_REPAIR_BitSlice_146_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST2_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST24_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST27_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_gate_tessent_mbist_me_core_clk_MBIST29_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST30_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST33_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST35_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST38_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_gate_tessent_mbist_me_core_clk_MBIST41_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST44_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST48_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh0_u0_key_send_to_srh0_u0_ppu_srh0_key_afifo_16x54_wrapper_u0_ppu_srh0_key_ram_1r1w_16x54_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST5_NON_REPAIR_BitSlice_56_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u1_cluster_gate_tessent_mbist_me_core_clk_MBIST50_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST53_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST58_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh1_u0_key_send_to_srh1_u0_ppu_srh1_key_afifo_16x109_wrapper_u0_ppu_srh1_key_ram_1r1w_16x109_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST6_NON_REPAIR_BitSlice_110_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST62_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST64_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST67_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_gate_tessent_mbist_me_core_clk_MBIST69_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST72_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST76_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST80_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST82_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST84_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST86_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST89_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST93_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST97_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u5.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST1_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_afifo_64x77_wrapper_u0_ppu_coprocess_rsp_ram_1r1w_64x77_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST11_NON_REPAIR_BitSlice_78_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_fwft_fifo_128x78_wrapper_u0_ppu_coprocess_rsp_fifo_128x78_wrapper_ppu_coprocess_rsp_ram_1r1w_128x78_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST12_NON_REPAIR_BitSlice_80_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_afifo_64x272_wrapper_u0_ppu_ese_rsp_ram_1r1w_64x272_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST13_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_ram_1w1r_128x272_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST14_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_afifo_64x143_wrapper_u0_ppu_srh0_rsp_ram_1r1w_64x143_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST15_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_ram_1w1r_128x143_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST16_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_afifo_64x144_wrapper_u0_ppu_srh1_rsp_ram_1r1w_64x144_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST17_NON_REPAIR_BitSlice_146_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST2_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST24_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST27_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_gate_tessent_mbist_me_core_clk_MBIST29_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST30_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST33_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST35_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST38_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_gate_tessent_mbist_me_core_clk_MBIST41_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST44_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST48_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh0_u0_key_send_to_srh0_u0_ppu_srh0_key_afifo_16x54_wrapper_u0_ppu_srh0_key_ram_1r1w_16x54_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST5_NON_REPAIR_BitSlice_56_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u1_cluster_gate_tessent_mbist_me_core_clk_MBIST50_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST53_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST58_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh1_u0_key_send_to_srh1_u0_ppu_srh1_key_afifo_16x109_wrapper_u0_ppu_srh1_key_ram_1r1w_16x109_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST6_NON_REPAIR_BitSlice_110_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST62_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST64_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST67_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_gate_tessent_mbist_me_core_clk_MBIST69_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST72_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST76_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST80_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST82_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST84_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST86_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST89_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST93_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST97_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u7.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST1_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_afifo_64x77_wrapper_u0_ppu_coprocess_rsp_ram_1r1w_64x77_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST11_NON_REPAIR_BitSlice_78_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_mex_u0_rsp_handle_u0_coprocess_rsp_handle_u0_ppu_coprocess_rsp_fwft_fifo_128x78_wrapper_u0_ppu_coprocess_rsp_fifo_128x78_wrapper_ppu_coprocess_rsp_ram_1r1w_128x78_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST12_NON_REPAIR_BitSlice_80_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_afifo_64x272_wrapper_u0_ppu_ese_rsp_ram_1r1w_64x272_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST13_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_mex_u0_rsp_handle_u0_ese_rsp_handle_u0_ppu_ese_rsp_ram_1w1r_128x272_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST14_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_afifo_64x143_wrapper_u0_ppu_srh0_rsp_ram_1r1w_64x143_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST15_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_mex_u0_rsp_handle_u0_srh0_rsp_handle_u0_ppu_srh0_rsp_ram_1w1r_128x143_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST16_NON_REPAIR_BitSlice_144_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_afifo_64x144_wrapper_u0_ppu_srh1_rsp_ram_1r1w_64x144_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST17_NON_REPAIR_BitSlice_146_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_afifo_16x665_wrapper_u0_ppu_ese_key_ram_1r1w_16x665_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST2_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST24_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST27_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_gate_tessent_mbist_me_core_clk_MBIST29_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST30_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST33_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_key_ram_u0_ppu_me_key_ram_1r1w_129x161_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST35_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST38_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_gate_tessent_mbist_me_core_clk_MBIST41_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST44_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST48_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh0_u0_key_send_to_srh0_u0_ppu_srh0_key_afifo_16x54_wrapper_u0_ppu_srh0_key_ram_1r1w_16x54_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST5_NON_REPAIR_BitSlice_56_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u1_cluster_gate_tessent_mbist_me_core_clk_MBIST50_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST53_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST58_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_srh1_u0_key_send_to_srh1_u0_ppu_srh1_key_afifo_16x109_wrapper_u0_ppu_srh1_key_ram_1r1w_16x109_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST6_NON_REPAIR_BitSlice_110_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST62_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u2_cluster_gate_tessent_mbist_me_core_clk_MBIST64_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST67_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_gate_tessent_mbist_me_core_clk_MBIST69_NON_REPAIR_BitSlice_82_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u2_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST72_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST76_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u2_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST80_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST82_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u3_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST84_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u3_cluster_gate_tessent_mbist_me_core_clk_MBIST86_NON_REPAIR_BitSlice_82_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST89_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST93_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_ppu_me_rsp_ram_1r1w_160x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST97_NON_REPAIR_BitSlice_64_controller_inst) {
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_134_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
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
                    
                Controller(u_hcm_ppu_u0.cluster_u9.cluster_mex_u0_cluster_mex_key_send_u0_cluster_key_send_to_ese_u0_key_send_to_se_u0_ppu_ese_key_out_fwft_fifo_32x664_wrapper_u0_ppu_ese_key_out_fifo_32x664_wrapper_ppu_ese_key_out_ram_1r1w_32x664_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_134_controller_inst) {
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
                    
                    } // End rf_2pA_nr_10
                } // End TestStep
            } //End Pattern
                
//End