
        Patterns(MemoryBist_rf_2pA_128x10) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_rf_2pA_128x10_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_lif_u0_rce_24_ch_u0_falcon_top_v0_u0_pcs_top_v0_u0_pcs.pcs_v0_gate_tessent_mbist_pcs_clk_MBIST18_NON_REPAIR_BitSlice_10_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 50 ;
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
                    
                Controller(u_hcm_lif_u0_rce_24_ch_u0_falcon_top_v0_u0_pcs_top_v0_u0_pcs.pcs2_tx_pcs_tx_phyvoq_u0_pcs_tx_phyvoq_qmu_u0_pcs_tx_phyvoq_dat_queue_pro_u0_pcs_tx_phyvoq_dat_queue_ptr_u0_pcs_v0_gate_tessent_mbist_pcs_clk_MBIST48_NON_REPAIR_BitSlice_10_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 50 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_rce_24_ch_1_u0_falcon_top_v1_u0_pcs_top_v1_u0_pcs.pcs0_tx_pcs_tx_phyvoq_u0_pcs_tx_phyvoq_qmu_u0_pcs_tx_phyvoq_dat_queue_pro_u0_pcs_tx_phyvoq_dat_queue_ptr_u0_pcs_v1_gate_tessent_mbist_pcs_clk_MBIST17_NON_REPAIR_BitSlice_10_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 50 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_rce_24_ch_1_u0_falcon_top_v1_u0_pcs_top_v1_u0_pcs.pcs1_tx_pcs_tx_phyvoq_u0_pcs_tx_phyvoq_qmu_u0_pcs_tx_phyvoq_dat_queue_pro_u0_pcs_tx_phyvoq_dat_queue_ptr_u0_pcs_v1_gate_tessent_mbist_pcs_clk_MBIST33_NON_REPAIR_BitSlice_10_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 50 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_rce_24_ch_1_u0_falcon_top_v1_u0_pcs_top_v1_u0_pcs.pcs2_tx_pcs_tx_phyvoq_u0_pcs_tx_phyvoq_qmu_u0_pcs_tx_phyvoq_dat_queue_pro_u0_pcs_tx_phyvoq_dat_queue_ptr_u0_pcs_v1_gate_tessent_mbist_pcs_clk_MBIST46_NON_REPAIR_BitSlice_10_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 50 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                    } // End rf_2pA_128x10
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_rf_2pA_120x11) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_rf_2pA_120x11_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_lif_u0_rce_24_ch_u0_falcon_top_v0_u0_flexe_v0_u0_flexe_tx_v0_u0_flexe_tx_wrapper_01_v0_u0.flexe_tx_wrapper_0_u0_flexe_tx_cfg_u0_flexe_tx_wrapper_01_v0_gate_tessent_mbist_sys_clk_MBIST1_NON_REPAIR_BitSlice_11_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 50 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_rce_24_ch_1_u0_falcon_top_v1_u0_flexe_v1_u0_flexe_tx_v1_u0_flexe_tx_wrapper_01_v1_u0.flexe_tx_wrapper_0_u0_flexe_tx_cfg_u0_flexe_tx_wrapper_01_v1_gate_tessent_mbist_sys_clk_MBIST1_NON_REPAIR_BitSlice_11_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 50 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                    } // End rf_2pA_120x11
                } // End TestStep
            } //End Pattern
                
//End