
        Patterns(MemoryBist_qmu_esi_8192x25) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_qmu_esi_8192x25_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_np016_qmu_crs_u0_crs_gen_filter_u0_qsch_crs_qnum_fwft_fifo_49152x19_wrapper_u0_qsch_crs_qnum_fifo_49152x19_wrapper_qsch_crs_qnum_ram_1r1w_49152x19_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST51_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_np016_qmu_crs_u0_crs_gen_filter_u0_qsch_crs_qnum_fwft_fifo_49152x19_wrapper_u1_qsch_crs_qnum_fifo_49152x19_wrapper_qsch_crs_qnum_ram_1r1w_49152x19_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST53_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 50 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_np016_qmu_crs_u0_crs_gen_filter_u0_qsch_crs_qnum_fwft_fifo_49152x19_wrapper_u0_qsch_crs_qnum_fifo_49152x19_wrapper_qsch_crs_qnum_ram_1r1w_49152x19_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 50 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_np016_qmu_crs_u0_crs_gen_filter_u0_qsch_crs_qnum_fwft_fifo_49152x19_wrapper_u1_qsch_crs_qnum_fifo_49152x19_wrapper_qsch_crs_qnum_ram_1r1w_49152x19_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST54_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_sch_u0_np016_qmu_crs_u0_crs_gen_filter_u0_qsch_crs_qnum_fwft_fifo_49152x19_wrapper_u0_qsch_crs_qnum_fifo_49152x19_wrapper_qsch_crs_qnum_ram_1r1w_49152x19_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST51_REPAIR_BISR_controller_inst) {
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_sch_u0_np016_qmu_crs_u0_crs_gen_filter_u0_qsch_crs_qnum_fwft_fifo_49152x19_wrapper_u1_qsch_crs_qnum_fifo_49152x19_wrapper_qsch_crs_qnum_ram_1r1w_49152x19_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST53_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 50 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_sch_u0_np016_qmu_crs_u0_crs_gen_filter_u0_qsch_crs_qnum_fwft_fifo_49152x19_wrapper_u0_qsch_crs_qnum_fifo_49152x19_wrapper_qsch_crs_qnum_ram_1r1w_49152x19_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 50 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_sch_u0_np016_qmu_crs_u0_crs_gen_filter_u0_qsch_crs_qnum_fwft_fifo_49152x19_wrapper_u1_qsch_crs_qnum_fifo_49152x19_wrapper_qsch_crs_qnum_ram_1r1w_49152x19_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST54_REPAIR_BISR_controller_inst) {
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
                    
                    } // End qmu_esi_8192x25
                } // End TestStep
            } //End Pattern
                
//End