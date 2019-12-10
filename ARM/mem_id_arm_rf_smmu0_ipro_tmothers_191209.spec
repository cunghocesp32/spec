
        Patterns(MemoryBist_smmu0_sram_spA_4096x136) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_smmu0_sram_spA_4096x136_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x135_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST16_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x135_wrapper_u3_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST20_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x135_wrapper_u5_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST56_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x135_wrapper_u7_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST64_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x135_wrapper_u1_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST15_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x135_wrapper_u2_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST19_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x135_wrapper_u5_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST55_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x135_wrapper_u7_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST63_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x135_wrapper_u3_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST13_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x135_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST17_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x135_wrapper_u4_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST49_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x135_wrapper_u6_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST57_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x135_wrapper_u2_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST14_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x135_wrapper_u1_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST18_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x135_wrapper_u4_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST50_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x135_wrapper_u6_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST58_REPAIR_BISR_controller_inst) {
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
                    
                    } // End smmu0_sram_spA_4096x136
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_ipro_rf_2pA_96x160) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_ipro_rf_2pA_96x160_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_fxsch_pre_lif1h_width_inc_lif1_rx_width_ram_1r1w_96x1114_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST103_NON_REPAIR_BitSlice_160_controller_inst) {
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_fxsch_pre_lif1h_width_inc_lif1_rx_width_ram_1r1w_96x1114_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST104_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_fxsch_pre_lif1l_width_inc_lif1_rx_width_ram_1r1w_96x1114_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST105_NON_REPAIR_BitSlice_160_controller_inst) {
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
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_fxsch_pre_lif1l_width_inc_lif1_rx_width_ram_1r1w_96x1114_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST106_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1500 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                    } // End ipro_rf_2pA_96x160
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_tm_others_256x206) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_tm_others_256x206_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_tm_u0_tm_others_u0.olif_u0_olif_module_u0_ie_pkt_order_u0_tmolif_emem_data_fifo_256x2067_wrapper_u0_tmolif_emem_data_fifo_256x2048_wrapper_u0_tmolif_emem_data_ram_1r1w_256x2048_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_tm_others_gate_tessent_mbist_sys_clk_MBIST1_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_tm_u0_tm_others_u0.olif_u0_olif_module_u1_ie_pkt_order_u0_tmolif_emem_data_fifo_256x2067_wrapper_u0_tmolif_emem_data_fifo_256x2048_wrapper_u0_tmolif_emem_data_ram_1r1w_256x2048_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_tm_others_gate_tessent_mbist_sys_clk_MBIST26_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_tm_u0_tm_others_u0.olif_u0_olif_module_u0_ie_pkt_order_u0_tmolif_emem_data_fifo_256x2067_wrapper_u0_tmolif_emem_data_fifo_256x2048_wrapper_u0_tmolif_emem_data_ram_1r1w_256x2048_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_tm_others_gate_tessent_mbist_sys_clk_MBIST2_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_tm_u0_tm_others_u0.olif_u0_olif_module_u1_ie_pkt_order_u0_tmolif_emem_data_fifo_256x2067_wrapper_u0_tmolif_emem_data_fifo_256x2048_wrapper_u0_tmolif_emem_data_ram_1r1w_256x2048_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_tm_others_gate_tessent_mbist_sys_clk_MBIST27_REPAIR_BISR_controller_inst) {
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
                    
                    } // End tm_others_256x206
                } // End TestStep
            } //End Pattern
                
//End