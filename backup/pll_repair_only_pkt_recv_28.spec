
        Patterns(MemoryBist_P1_repair_b0) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_P1_repair_b0) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pbu_ifb_ram_bank_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST1_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m3,m6,m4,m2,m5,m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pbu_ifb_ram_bank_u0_pkt_buffer_block0_ram_1r1w_4096x1024_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST2_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m5,m3,m2,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pbu_ifb_ram_bank_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m2,m4,m7,m5,m3,m6,m9,m1,m8,m10 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST33_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m3,m8,m1,m4,m7,m5,m6 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                    } // End b0
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_P1_repair_b1) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_P1_repair_b1) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pbu_ifb_ram_bank_u1_pkt_buffer_block0_ram_1r1w_4096x1024_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST41_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m3,m2,m1,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pbu_ifb_ram_bank_u1_pkt_recv_gate_tessent_mbist_sys_clk_MBIST39_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m3,m6,m4,m7,m5,m1,m2,m8 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pbu_ifb_ram_bank_u1_pkt_buffer_block0_ram_1r1w_4096x1024_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST40_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m5,m1,m4,m3,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pbu_ifb_ram_bank_u1_pkt_recv_gate_tessent_mbist_sys_clk_MBIST38_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m8,m6,m2,m3,m4,m9,m10,m1,m7,m5 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST33_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                    } // End b1
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_P1_repair_b2) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_P1_repair_b2) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pbu_ifb_ram_bank_u2_pkt_recv_gate_tessent_mbist_sys_clk_MBIST6_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m4,m2,m9,m5,m3,m10,m7,m6,m8,m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pbu_ifb_ram_bank_u2_pkt_recv_gate_tessent_mbist_sys_clk_MBIST7_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m2,m8,m6,m1,m7,m4,m5,m3 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST5_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m8,m4,m5,m2,m10,m9 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST8_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m4,m2,m6,m3 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                    } // End b2
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_P1_repair_b3) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_P1_repair_b3) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST4_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m9,m4,m10,m6,m3,m5,m8,m2,m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST5_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m3,m6,m1,m7 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pbu_ifb_ram_bank_u3_pkt_recv_gate_tessent_mbist_sys_clk_MBIST9_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m6,m3,m1,m4,m2,m5 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST8_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m5 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pbu_ifb_ram_bank_u3_pkt_buffer_block1_ram_1r1w_4096x1024_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST11_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m6,m3,m2,m5,m7,m1,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                    } // End b3
                } // End TestStep
            } //End Pattern
                
//End