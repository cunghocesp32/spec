
        Patterns(MemoryBist_P1_repair_r1_140220) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_P1_repair_r1_140220) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_ppu_u0.cluster_u9.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1.5;
                        enable_memory_list : m4 ;
                        freeze_step : 0;
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
                        test_time_multiplier : 1.5;
                        enable_memory_list : m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_gate_tessent_mbist_sys_clk_MBIST155_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1.5;
                        enable_memory_list : m6 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                    } // End r1_140220
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_P1_repair_r2_140220) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_P1_repair_r2_140220) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u25_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST23_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1.5;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_storage_ram_1w1r_6kx2048_u1_ram_1r1w_3072x2064_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST51_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1.5;
                        enable_memory_list : m7 ;
                        freeze_step : 0;
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
                        test_time_multiplier : 1.5;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif2_u0.serdes_s8_serdes_s4_u0_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif2_gate_tessent_mbist_salina_cpu_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 1.5;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                    } // End r2_140220
                } // End TestStep
            } //End Pattern
                
//End