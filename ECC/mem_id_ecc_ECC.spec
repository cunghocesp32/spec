
        Patterns(MemoryBist_ECC_nr_ss_1) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_ECC_nr_ss_1_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_lif_u0_lif0_u0.serdes_s24_u0_serdes_s4_u0_pmem_dmem_wrapper_u0_lif0_gate_tessent_mbist_salina_cpu_clk_MBIST18_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.serdes_s24_u0_serdes_s4_u1_pmem_dmem_wrapper_u0_lif0_gate_tessent_mbist_salina_cpu_clk_MBIST20_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.serdes_s24_u0_serdes_s4_u2_pmem_dmem_wrapper_u0_lif0_gate_tessent_mbist_salina_cpu_clk_MBIST22_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.serdes_s24_u0_serdes_s4_u2_pmem_dmem_wrapper_u0_lif0_gate_tessent_mbist_salina_cpu_clk_MBIST23_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.serdes_s24_u0_serdes_s4_u3_pmem_dmem_wrapper_u0_lif0_gate_tessent_mbist_salina_cpu_clk_MBIST25_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.serdes_s24_u0_serdes_s4_u3_pmem_dmem_wrapper_u0_lif0_gate_tessent_mbist_salina_cpu_clk_MBIST26_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.serdes_s24_u0_serdes_s4_u4_pmem_dmem_wrapper_u0_lif0_gate_tessent_mbist_salina_cpu_clk_MBIST28_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.serdes_s24_u0_serdes_s4_u4_pmem_dmem_wrapper_u0_lif0_gate_tessent_mbist_salina_cpu_clk_MBIST29_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.serdes_s24_u0_serdes_s4_u5_pmem_dmem_wrapper_u0_lif0_gate_tessent_mbist_salina_cpu_clk_MBIST31_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.serdes_s24_u0_serdes_s4_u5_pmem_dmem_wrapper_u0_lif0_gate_tessent_mbist_salina_cpu_clk_MBIST33_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.serdes_s24_u0_serdes_s4_u1_pmem_dmem_wrapper_u0_lif0_gate_tessent_mbist_salina_cpu_clk_MBIST35_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.serdes_s24_u0_serdes_s4_u0_pmem_dmem_wrapper_u0_lif0_gate_tessent_mbist_salina_cpu_clk_MBIST36_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u0_pmem_dmem_wrapper_u0_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST17_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u1_pmem_dmem_wrapper_u0_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST19_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u2_pmem_dmem_wrapper_u0_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST21_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u3_pmem_dmem_wrapper_u0_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST24_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u4_pmem_dmem_wrapper_u0_genvar_data_mem_0__serdes_s4_dmem_ecc_ram_1r1w_4608x8_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST26_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u4_pmem_dmem_wrapper_u0_genvar_data_mem_1__serdes_s4_dmem_ecc_ram_1r1w_4608x8_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST27_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u4_pmem_dmem_wrapper_u0_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST28_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u5_pmem_dmem_wrapper_u0_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST30_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u5_pmem_dmem_wrapper_u0_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST32_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u4_pmem_dmem_wrapper_u0_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST33_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u4_pmem_dmem_wrapper_u0_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST34_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u3_pmem_dmem_wrapper_u0_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST37_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u2_pmem_dmem_wrapper_u0_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST38_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u1_pmem_dmem_wrapper_u0_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST39_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u0_pmem_dmem_wrapper_u0_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST40_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif1_u0.serdes_s24_btm_u0_serdes_s4_u5_pmem_dmem_wrapper_u0_lif1_gate_tessent_mbist_salina_cpu_clk_MBIST15_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_lif_u0_lif1_u0.serdes_s24_btm_u0_serdes_s4_u4_pmem_dmem_wrapper_u0_lif1_gate_tessent_mbist_salina_cpu_clk_MBIST18_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_lif_u0_lif1_u0.serdes_s24_btm_u0_serdes_s4_u3_pmem_dmem_wrapper_u0_lif1_gate_tessent_mbist_salina_cpu_clk_MBIST20_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_lif_u0_lif1_u0.serdes_s24_btm_u0_serdes_s4_u2_pmem_dmem_wrapper_u0_lif1_gate_tessent_mbist_salina_cpu_clk_MBIST22_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_lif_u0_lif1_u0.serdes_s24_btm_u0_serdes_s4_u1_pmem_dmem_wrapper_u0_lif1_gate_tessent_mbist_salina_cpu_clk_MBIST24_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_lif_u0_lif1_u0.serdes_s24_btm_u0_serdes_s4_u0_pmem_dmem_wrapper_u0_lif1_gate_tessent_mbist_salina_cpu_clk_MBIST26_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_lif_u0_lif12_u0.serdes_s24_btm_u0_serdes_s4_u0_pmem_dmem_wrapper_u0_lif12_gate_tessent_mbist_salina_cpu_clk_MBIST19_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif12_u0.serdes_s24_btm_u0_serdes_s4_u0_pmem_dmem_wrapper_u0_lif12_gate_tessent_mbist_salina_cpu_clk_MBIST20_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif12_u0.serdes_s24_btm_u0_serdes_s4_u0_pmem_dmem_wrapper_u0_lif12_gate_tessent_mbist_salina_cpu_clk_MBIST21_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif12_u0.serdes_s24_btm_u0_serdes_s4_u1_pmem_dmem_wrapper_u0_genvar_data_mem_0__serdes_s4_dmem_ecc_ram_1r1w_4608x8_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif12_gate_tessent_mbist_salina_cpu_clk_MBIST23_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif12_u0.serdes_s24_btm_u0_serdes_s4_u1_pmem_dmem_wrapper_u0_lif12_gate_tessent_mbist_salina_cpu_clk_MBIST24_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_lif_u0_lif12_u0.serdes_s24_btm_u0_serdes_s4_u1_pmem_dmem_wrapper_u0_lif12_gate_tessent_mbist_salina_cpu_clk_MBIST25_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_lif_u0_lif12_u0.serdes_s24_btm_u0_serdes_s4_u2_pmem_dmem_wrapper_u0_lif12_gate_tessent_mbist_salina_cpu_clk_MBIST27_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_lif_u0_lif12_u0.serdes_s24_btm_u0_serdes_s4_u3_pmem_dmem_wrapper_u0_lif12_gate_tessent_mbist_salina_cpu_clk_MBIST29_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_lif_u0_lif12_u0.serdes_s24_btm_u0_serdes_s4_u4_pmem_dmem_wrapper_u0_lif12_gate_tessent_mbist_salina_cpu_clk_MBIST31_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_lif_u0_lif12_u0.serdes_s24_btm_u0_serdes_s4_u5_pmem_dmem_wrapper_u0_lif12_gate_tessent_mbist_salina_cpu_clk_MBIST33_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_lif_u0_lif2_u0.serdes_s8_serdes_s4_u0_pmem_dmem_wrapper_u0_lif2_gate_tessent_mbist_salina_cpu_clk_MBIST16_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif2_u0.serdes_s8_serdes_s4_u0_pmem_dmem_wrapper_u0_lif2_gate_tessent_mbist_salina_cpu_clk_MBIST17_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif2_u0.serdes_s8_serdes_s4_u1_pmem_dmem_wrapper_u0_lif2_gate_tessent_mbist_salina_cpu_clk_MBIST19_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_lif_u0_lifcc_u0.serdes_s4_lifc_u0_pmem_dmem_wrapper_u0_lifcc_gate_tessent_mbist_salina_cpu_clk_MBIST11_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.idma_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST37_NON_REPAIR_BitSlice_26_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_cmddeal_u0_cmd_sch_u0_cmdsch_cfgmt_u0_qmu_cmdsch_port_cnt_ram_2r2w_135x18_wrapper_u0_ues_gmem_2r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST11_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_cmddeal_u0_cmd_sch_u0_cmdsch_ram_u0_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST14_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_cmddeal_u0_cmd_sch_u0_cmdsch_ram_u0_qmu_cmdsch_port_cnt_ram_2r2w_135x18_wrapper_u0_ues_gmem_2r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST16_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_cmddeal_u0_cmd_sch_u0_cmdsch_ram_u0_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST17_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.cgavd_u0_cgavd_memory_u0_flow_memory_u0_cgavd_flow_wred_u0_cgavd_flow_wred_para_ram_1r1w_512x78_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST2_NON_REPAIR_BitSlice_86_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_qlist_u0_free_list_man_u0_free_head_tail_man_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST29_NON_REPAIR_BitSlice_25_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.cgavd_u0_cgavd_memory_u0_pp_memory_u0_cgavd_pp_grp_dyen_u0_cgavd_pp_para_ram_1r1w_512x4_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST3_NON_REPAIR_BitSlice_8_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_qlist_u0_free_list_man_u0_qmu_bank_sel_u0_qmu_bdep_ram_2r2w_192x19_wrapper_u0_ues_gmem_2r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST30_NON_REPAIR_BitSlice_25_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.cgavd_u0_cgavd_memory_u0_pp_memory_u0_cgavd_pp_mtd_td_th_u0_cgavd_pp_avg_len_ram_1r1w_512x24_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST4_NON_REPAIR_BitSlice_30_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.cgavd_u0_cgavd_memory_u0_pp_memory_u0_cgavd_pp_q_len_u0_cgavd_pp_q_len_ram_2r2w_512x23_wrapper_u0_ues_gmem_2r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST5_NON_REPAIR_BitSlice_29_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.cgavd_u0_cgavd_memory_u0_pp_memory_u0_cgavd_pp_q_len_u0_cgavd_pp_q_len_ram_2r2w_512x23_wrapper_u0_ues_gmem_2r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST6_NON_REPAIR_BitSlice_29_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_sch_u0_np016_qmu_wlist_u0_wlist_deq_active_ram_1r1w_1024x3_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST63_NON_REPAIR_BitSlice_7_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_sch_u0_np016_qmu_wlist_u0_wlist_enq_active_ram_2r2w_1024x3_wrapper_u0_ues_gmem_2r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST64_NON_REPAIR_BitSlice_7_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_sch_u0_np016_qmu_wlist_u0_wlist_tp_ram_3r2w_8192x16_wrapper_u0_ues_gmem_3r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST65_NON_REPAIR_BitSlice_22_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_sch_u0_np016_qmu_wlist_u0_wlist_tp_ram_3r2w_8192x16_wrapper_u0_ues_gmem_3r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST66_NON_REPAIR_BitSlice_22_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_sch_u0_np016_qmu_wlist_u0_wlist_hp_ram_1r3w_8192x16_wrapper_u0_ues_gmem_1r3w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST69_NON_REPAIR_BitSlice_22_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_qlist_u0_qlist_qdm_u0_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST70_NON_REPAIR_BitSlice_29_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_cmddeal_u0_cmd_sch_u0_cmdsch_cfgmt_u0_qmu_cmdsch_port_cnt_ram_2r2w_135x18_wrapper_u0_ues_gmem_2r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST11_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_cmddeal_u0_cmd_sch_u0_cmdsch_ram_u0_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST14_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_cmddeal_u0_cmd_sch_u0_cmdsch_ram_u0_qmu_cmdsch_port_cnt_ram_2r2w_135x18_wrapper_u0_ues_gmem_2r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST16_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_cmddeal_u0_cmd_sch_u0_cmdsch_ram_u0_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST17_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.cgavd_u0_cgavd_memory_u0_flow_memory_u0_cgavd_flow_wred_u0_cgavd_flow_wred_para_ram_1r1w_512x78_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST2_NON_REPAIR_BitSlice_86_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_qlist_u0_free_list_man_u0_free_head_tail_man_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST29_NON_REPAIR_BitSlice_25_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.cgavd_u0_cgavd_memory_u0_pp_memory_u0_cgavd_pp_grp_dyen_u0_cgavd_pp_para_ram_1r1w_512x4_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST3_NON_REPAIR_BitSlice_8_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_qlist_u0_free_list_man_u0_qmu_bank_sel_u0_qmu_bdep_ram_2r2w_192x19_wrapper_u0_ues_gmem_2r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST30_NON_REPAIR_BitSlice_25_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.cgavd_u0_cgavd_memory_u0_pp_memory_u0_cgavd_pp_mtd_td_th_u0_cgavd_pp_avg_len_ram_1r1w_512x24_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST4_NON_REPAIR_BitSlice_30_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.cgavd_u0_cgavd_memory_u0_pp_memory_u0_cgavd_pp_q_len_u0_cgavd_pp_q_len_ram_2r2w_512x23_wrapper_u0_ues_gmem_2r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST5_NON_REPAIR_BitSlice_29_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.cgavd_u0_cgavd_memory_u0_pp_memory_u0_cgavd_pp_q_len_u0_cgavd_pp_q_len_ram_2r2w_512x23_wrapper_u0_ues_gmem_2r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST6_NON_REPAIR_BitSlice_29_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_np016_qmu_wlist_u0_wlist_deq_active_ram_1r1w_1024x3_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST63_NON_REPAIR_BitSlice_7_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_np016_qmu_wlist_u0_wlist_enq_active_ram_2r2w_1024x3_wrapper_u0_ues_gmem_2r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST64_NON_REPAIR_BitSlice_7_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_np016_qmu_wlist_u0_wlist_tp_ram_3r2w_8192x16_wrapper_u0_ues_gmem_3r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST65_NON_REPAIR_BitSlice_22_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_np016_qmu_wlist_u0_wlist_tp_ram_3r2w_8192x16_wrapper_u0_ues_gmem_3r2w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST66_NON_REPAIR_BitSlice_22_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_np016_qmu_wlist_u0_wlist_hp_ram_1r3w_8192x16_wrapper_u0_ues_gmem_1r3w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST69_NON_REPAIR_BitSlice_22_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
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
                        test_time_multiplier : 150 ;
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
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qsch_wlist_next_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST43_NON_REPAIR_BitSlice_22_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qsch_wlist_next_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST44_NON_REPAIR_BitSlice_22_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qsch_wlist_next_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST45_NON_REPAIR_BitSlice_22_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qsch_wlist_next_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST46_NON_REPAIR_BitSlice_22_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qmu_biu_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST48_NON_REPAIR_BitSlice_10_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qmu_biu_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST49_NON_REPAIR_BitSlice_10_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qmu_biu_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST50_NON_REPAIR_BitSlice_10_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qmu_biu_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST51_NON_REPAIR_BitSlice_10_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qmu_biu_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST52_NON_REPAIR_BitSlice_10_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qmu_biu_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST53_NON_REPAIR_BitSlice_10_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qmu_biu_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST54_NON_REPAIR_BitSlice_10_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qmu_biu_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST55_NON_REPAIR_BitSlice_10_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qmu_biu_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST56_NON_REPAIR_BitSlice_10_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qmu_biu_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST57_NON_REPAIR_BitSlice_10_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qmu_biu_ram_u0_qmu_biu_ram_2r2w_32768x5_wrapper_u7_ues_gmem_2r2w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST58_NON_REPAIR_BitSlice_10_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qsch_wlist_index_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST74_NON_REPAIR_BitSlice_25_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qsch_wlist_index_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST75_NON_REPAIR_BitSlice_25_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qsch_wlist_index_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST76_NON_REPAIR_BitSlice_25_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_mc_mul_fcopy_queue_u0_ram_1w1r_256x60_ram_1r1w_256x60_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST24_NON_REPAIR_BitSlice_68_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_mc_mul_u0_asm_recy_u0_asm_ram_mag_u0_ram_1w1r_12kx21_sa_asm_gate_tessent_mbist_sys_clk_MBIST28_NON_REPAIR_BitSlice_14_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_mc_mul_u0_asm_recy_u0_asm_ram_mag_u0_sa_asm_gate_tessent_mbist_sys_clk_MBIST29_NON_REPAIR_BitSlice_16_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_mc_mul_u0_asm_recy_u0_asm_ram_mag_u0_sa_asm_gate_tessent_mbist_sys_clk_MBIST30_NON_REPAIR_BitSlice_16_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_idle_list_ram_1w1r_1kx10_u0_ram_1r1w_1024x10_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST35_NON_REPAIR_BitSlice_15_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_phm_sa_asm_gate_tessent_mbist_sys_clk_MBIST38_NON_REPAIR_BitSlice_76_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_cell_sort_sa_asm_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_22_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_phm_ram_1w1r_262x4_ram_1r1w_262x20_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST42_NON_REPAIR_BitSlice_26_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_storage_ram_1w1r_1kx48_u4_ram_1r1w_1024x49_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST46_NON_REPAIR_BitSlice_56_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_sa_ip_asm_sm_intf_buf_u0_ram_1w1r_224x72_ram_1r1w_224x78_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST56_NON_REPAIR_BitSlice_86_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_datacell_ch_u0_cgs_datacell_buf_u0_cgs_dc_buf_data_ram_1w1r_384x2074_rxsw_ram_1r1w_384x26_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_xsw_gate_tessent_mbist_sys_clk_MBIST11_NON_REPAIR_BitSlice_16_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_datacell_ch_u0_cgs_datacell_buf_u0_cgs_dc_buf_data_sa_xsw_gate_tessent_mbist_sys_clk_MBIST12_NON_REPAIR_BitSlice_14_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_datacell_ch_u0_cgs_datacell_buf_u0_cgs_dc_buf_tdm_ram_1w1r_384x2074_rxsw_ram_1r1w_384x26_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_xsw_gate_tessent_mbist_sys_clk_MBIST15_NON_REPAIR_BitSlice_16_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_datacell_ch_u0_cgs_datacell_buf_u0_cgs_dc_buf_tdm_sa_xsw_gate_tessent_mbist_sys_clk_MBIST16_NON_REPAIR_BitSlice_14_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_datacell_ch_u0_cgs_datacell_buf_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST17_NON_REPAIR_BitSlice_16_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_datacell_ch_u0_cgs_dst_id_buf_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST22_NON_REPAIR_BitSlice_23_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_datacell_ch_u0_cgs_dst_id_buf_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST23_NON_REPAIR_BitSlice_15_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_txsw_sa_ip_txsw_u0_crp_ctrl_ch_u0_ptal_process_top_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST38_NON_REPAIR_BitSlice_35_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST59_NON_REPAIR_BitSlice_20_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST60_NON_REPAIR_BitSlice_20_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST62_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST63_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST64_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST65_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap0_shap_sg_u0_shap_ram_1r1w_121x22_np_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_shap_gate_tessent_mbist_sys_clk_MBIST70_NON_REPAIR_BitSlice_28_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap0_shap_pp_u0_shap_ram_1r1w_135x23_np_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_shap_gate_tessent_mbist_sys_clk_MBIST71_NON_REPAIR_BitSlice_29_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap1_shap_pp_u0_shap_ram_1r1w_135x23_np_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_shap_gate_tessent_mbist_sys_clk_MBIST80_NON_REPAIR_BitSlice_29_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap1_shap_sg_u0_shap_ram_1r1w_121x22_np_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_shap_gate_tessent_mbist_sys_clk_MBIST81_NON_REPAIR_BitSlice_28_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tm_others_gate_tessent_mbist_sys_clk_MBIST10_NON_REPAIR_BitSlice_89_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tm_others_gate_tessent_mbist_sys_clk_MBIST11_NON_REPAIR_BitSlice_89_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tmmu_module_u1_tmmu_core_u0_tmmu_cache_core_u0_tm_others_gate_tessent_mbist_sys_clk_MBIST12_NON_REPAIR_BitSlice_6_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tmmu_module_u0_tmmu_core_u0_tmmu_cache_core_u0_tmmu_cache_pd_fifo_wrapper_u0_tmmu_cache_pd_fifo_512x64_wrapper_u0_tmmu_cache_pd_ram_1r1w_512x64_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_tm_others_gate_tessent_mbist_sys_clk_MBIST13_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tmmu_module_u0_tmmu_core_u0_tmmu_cache_core_u0_tmmu_emem_pd_fifo_wrapper_u0_tmmu_emem_pd_fifo_256x64_wrapper_u0_tmmu_emem_pd_ram_1r1w_256x64_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_tm_others_gate_tessent_mbist_sys_clk_MBIST14_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tmmu_module_u0_tmmu_core_u0_tmmu_wr_rd_core_u0_tmmu_imem_deq_rd_fifo_wrapper_u0_tmmu_imem_deq_rd_fifo_1024x40_wrapper_u0_tmmu_imem_deq_rd_ram_1r1w_1024x40_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_tm_others_gate_tessent_mbist_sys_clk_MBIST16_NON_REPAIR_BitSlice_47_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tmmu_module_u0_tmmu_core_u0_tmmu_wr_rd_core_u0_tm_others_gate_tessent_mbist_sys_clk_MBIST18_NON_REPAIR_BitSlice_39_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tmmu_module_u0_tmmu_core_u0_tmmu_cache_core_u0_tm_others_gate_tessent_mbist_sys_clk_MBIST22_NON_REPAIR_BitSlice_6_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.olif_u0_tm_others_gate_tessent_mbist_sys_clk_MBIST33_NON_REPAIR_BitSlice_25_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.olif_u0_tm_others_gate_tessent_mbist_sys_clk_MBIST34_NON_REPAIR_BitSlice_25_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tmmu_module_u1_tmmu_core_u0_tmmu_wr_rd_core_u0_tm_others_gate_tessent_mbist_sys_clk_MBIST5_NON_REPAIR_BitSlice_39_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tmmu_module_u1_tmmu_core_u0_tmmu_wr_rd_core_u0_tmmu_imem_deq_rd_fifo_wrapper_u0_tmmu_imem_deq_rd_fifo_1024x40_wrapper_u0_tmmu_imem_deq_rd_ram_1r1w_1024x40_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_tm_others_gate_tessent_mbist_sys_clk_MBIST6_NON_REPAIR_BitSlice_47_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tmmu_module_u1_tmmu_core_u0_tmmu_cache_core_u0_tmmu_emem_pd_fifo_wrapper_u0_tmmu_emem_pd_fifo_256x64_wrapper_u0_tmmu_emem_pd_ram_1r1w_256x64_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_tm_others_gate_tessent_mbist_sys_clk_MBIST7_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tmmu_module_u1_tmmu_core_u0_tmmu_cache_core_u0_tmmu_cache_pd_fifo_wrapper_u0_tmmu_cache_pd_fifo_512x64_wrapper_u0_tmmu_cache_pd_ram_1r1w_512x64_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_tm_others_gate_tessent_mbist_sys_clk_MBIST8_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                    } // End ECC_nr_ss_1
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_ECC_nr_arm_1) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_ECC_nr_arm_1_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_lifc_u0_lif_ctrl_tx_u0_xfi_tx_u0_xfi_mac_tx_u0_uni_mac_tx_across_afifo_32x73_wrapper_u0_uni_mac_tx_across_ram_1r1w_32x73_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST136_NON_REPAIR_BitSlice_74_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_lifc_u0_lif_ctrl_tx_u0_xfi_tx_u1_xfi_mac_tx_u0_uni_mac_tx_across_afifo_32x73_wrapper_u0_uni_mac_tx_across_ram_1r1w_32x73_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST139_NON_REPAIR_BitSlice_74_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_fxsch_pmap_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST81_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_fxsch_pmap_fxsch_pmap_osche_ram_1rw_1160x24_wrapper_ues_gmem_1rw_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST82_NON_REPAIR_BitSlice_30_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_fxsch_pmap_fxsch_pmap_oschi_ram_1rw_416x30_wrapper_ues_gmem_1rw_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST83_NON_REPAIR_BitSlice_37_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u0.hbm_channel_u0_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST1_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u0.hbm_channel_u2_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST11_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u0.hbm_channel_u2_hbm_ctrl_ss_u1_hbm_wr_process_integ_u0_hbm_wcf_afifo_128x30_wrapper_u0_hbm_wcf_ram_1r1w_128x30_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST16_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u0.hbm_channel_u3_hbm_ctrl_ss_u0_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST17_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u0.hbm_channel_u3_hbm_ctrl_ss_u1_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST21_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u0.hbm_channel_u4_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST24_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u0.hbm_channel_u5_hbm_ctrl_ss_u0_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST27_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u0.hbm_channel_u5_hbm_ctrl_ss_u1_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST30_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u0.hbm_channel_u6_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST32_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u0.hbm_channel_u7_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST38_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u0.hbm_channel_u1_hbm_ctrl_ss_u0_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST5_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u0.hbm_channel_u1_hbm_ctrl_ss_u1_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST8_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u2.hbm_channel_u0_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST1_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u2.hbm_channel_u2_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST11_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u2.hbm_channel_u2_hbm_ctrl_ss_u1_hbm_wr_process_integ_u0_hbm_wcf_afifo_128x30_wrapper_u0_hbm_wcf_ram_1r1w_128x30_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST16_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u2.hbm_channel_u3_hbm_ctrl_ss_u0_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST17_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u2.hbm_channel_u3_hbm_ctrl_ss_u1_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST21_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u2.hbm_channel_u4_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST24_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u2.hbm_channel_u5_hbm_ctrl_ss_u0_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST27_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u2.hbm_channel_u5_hbm_ctrl_ss_u1_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST30_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u2.hbm_channel_u6_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST32_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u2.hbm_channel_u7_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST38_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u2.hbm_channel_u1_hbm_ctrl_ss_u0_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST5_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u2.hbm_channel_u1_hbm_ctrl_ss_u1_hbm_octa_channel_v0_gate_tessent_mbist_sys_clk_MBIST8_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u1.hbm_channel_u0_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST1_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u1.hbm_channel_u2_hbm_ctrl_ss_u0_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST12_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u1.hbm_channel_u2_hbm_ctrl_ss_u1_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST16_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u1.hbm_channel_u3_hbm_ctrl_ss_u0_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST19_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u1.hbm_channel_u3_hbm_ctrl_ss_u1_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST23_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u1.hbm_channel_u4_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST26_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u1.hbm_channel_u5_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST29_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u1.hbm_channel_u5_hbm_ctrl_ss_u0_hbm_wr_process_integ_u0_hbm_wcf_afifo_128x30_wrapper_u0_hbm_wcf_ram_1r1w_128x30_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST31_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u1.hbm_channel_u6_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST34_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u1.hbm_channel_u6_hbm_ctrl_ss_u1_hbm_wr_process_integ_u0_hbm_wcf_afifo_128x30_wrapper_u0_hbm_wcf_ram_1r1w_128x30_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST38_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u1.hbm_channel_u7_hbm_ctrl_ss_u0_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST39_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u1.hbm_channel_u7_hbm_ctrl_ss_u1_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST42_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u1.hbm_channel_u1_hbm_ctrl_ss_u0_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST5_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u1.hbm_channel_u1_hbm_ctrl_ss_u1_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST9_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u3.hbm_channel_u0_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST1_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u3.hbm_channel_u2_hbm_ctrl_ss_u0_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST12_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u3.hbm_channel_u2_hbm_ctrl_ss_u1_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST16_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u3.hbm_channel_u3_hbm_ctrl_ss_u0_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST19_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u3.hbm_channel_u3_hbm_ctrl_ss_u1_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST23_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u3.hbm_channel_u4_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST26_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u3.hbm_channel_u5_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST29_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u3.hbm_channel_u5_hbm_ctrl_ss_u0_hbm_wr_process_integ_u0_hbm_wcf_afifo_128x30_wrapper_u0_hbm_wcf_ram_1r1w_128x30_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST31_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u3.hbm_channel_u6_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST34_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u3.hbm_channel_u6_hbm_ctrl_ss_u1_hbm_wr_process_integ_u0_hbm_wcf_afifo_128x30_wrapper_u0_hbm_wcf_ram_1r1w_128x30_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST38_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u3.hbm_channel_u7_hbm_ctrl_ss_u0_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST39_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u3.hbm_channel_u7_hbm_ctrl_ss_u1_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST42_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u3.hbm_channel_u1_hbm_ctrl_ss_u0_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST5_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_hbm_u0_hbm_octa_channel_u3.hbm_channel_u1_hbm_ctrl_ss_u1_hbm_octa_channel_v1_gate_tessent_mbist_sys_clk_MBIST9_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif0_gate_tessent_mbist_CM0_PLL_PHY_0_MBIST7_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif0_gate_tessent_mbist_CM0_PLL_PHY_1_MBIST13_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif0_gate_tessent_mbist_CM0_PLL_PHY_2_MBIST8_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif0_gate_tessent_mbist_CM0_PLL_PHY_2_MBIST9_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif0_gate_tessent_mbist_CM0_PLL_PHY_3_MBIST10_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif0_gate_tessent_mbist_CM0_PLL_PHY_4_MBIST11_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif0_gate_tessent_mbist_CM0_PLL_PHY_5_MBIST12_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif02_gate_tessent_mbist_CM0_PLL_PHY_0_MBIST7_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif02_gate_tessent_mbist_CM0_PLL_PHY_1_MBIST12_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif02_gate_tessent_mbist_CM0_PLL_PHY_2_MBIST8_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif02_gate_tessent_mbist_CM0_PLL_PHY_3_MBIST9_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif02_gate_tessent_mbist_CM0_PLL_PHY_4_MBIST10_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif02_gate_tessent_mbist_CM0_PLL_PHY_5_MBIST11_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif1_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif1_gate_tessent_mbist_CM0_PLL_PHY_0_MBIST6_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif1_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif1_gate_tessent_mbist_CM0_PLL_PHY_1_MBIST5_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif1_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif1_gate_tessent_mbist_CM0_PLL_PHY_2_MBIST3_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif1_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif1_gate_tessent_mbist_CM0_PLL_PHY_3_MBIST7_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif1_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif1_gate_tessent_mbist_CM0_PLL_PHY_4_MBIST4_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif1_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif1_gate_tessent_mbist_CM0_PLL_PHY_5_MBIST2_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif12_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif12_gate_tessent_mbist_CM0_PLL_PHY_0_MBIST9_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif12_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif12_gate_tessent_mbist_CM0_PLL_PHY_1_MBIST14_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif12_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif12_gate_tessent_mbist_CM0_PLL_PHY_2_MBIST10_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif12_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif12_gate_tessent_mbist_CM0_PLL_PHY_3_MBIST11_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif12_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif12_gate_tessent_mbist_CM0_PLL_PHY_4_MBIST12_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif12_u0.itlkn_u0_itlkn_core_u0_itlkn_24lane_tx_lif12_gate_tessent_mbist_CM0_PLL_PHY_5_MBIST13_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lifcc_u0.cfg_cfg_mst_mux_cfg_ahb_async_cfg_ahb_async_afifo_16x32_wrapper_u0_cfg_ahb_async_ram_1r1w_16x32_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_lifcc_gate_tessent_mbist_LIFCC_PLL_CLK_CG_MBIST1_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lifcc_u0.cfg_cfg_mst_mux_cfg_ahb_async_cfg_ahb_async_afifo_16x34_wrapper_u0_cfg_ahb_async_ram_1r1w_16x34_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_lifcc_gate_tessent_mbist_LIFCC_PLL_CLK_CG_MBIST2_NON_REPAIR_BitSlice_42_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lifcc_u0.cfg_cfg_mst_mux_cfg_ahb_async_cfg_ahb_async_afifo_32x72_wrapper_u0_cfg_ahb_async_ram_1r1w_32x72_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_lifcc_gate_tessent_mbist_LIFCC_PLL_CLK_CG_MBIST3_NON_REPAIR_BitSlice_80_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lifcc_u0.cfg_cfg_pcie_top_cfg_pcie_dma_wbuf_cfg_pcie_fifo_32x144_wrapper_u0_cfg_pcie_ram_1r1w_32x144_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lifcc_gate_tessent_mbist_LIFCC_PLL_CLK_CG_MBIST7_NON_REPAIR_BitSlice_154_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lifcc_u0.cfg_cfg_pcie_top_cfg_pcie_dma_tab_down_cfg_pcie_afifo_16x132_wrapper_u0_cfg_pcie_ram_1r1w_16x132_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_lifcc_gate_tessent_mbist_sys_clk_MBIST5_NON_REPAIR_BitSlice_142_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lifcc_u0.cfg_cfg_pcie_top_cfg_pcie_dma_tab_sta_up_cfg_pcie_afifo_256x128_wrapper_u0_cfg_pcie_ram_1r1w_256x128_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_lifcc_gate_tessent_mbist_sys_clk_MBIST6_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_rce_24_ch_u0_falcon_top_v0_u0_pcs_top_v0_u0_pcs.pcs0_tx_pcs_tx_phyvoq_u0_pcs_tx_phyvoq_async_u0_pcs_tx_phyvoq_afifo_32x611_wrapper_u0_pcs_tx_phyvoq_ram_1r1w_32x611_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_pcs_v0_gate_tessent_mbist_sys_clk_MBIST12_NON_REPAIR_BitSlice_154_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_rce_24_ch_u0_falcon_top_v0_u0_pcs_top_v0_u0_pcs.pcs1_tx_pcs_tx_phyvoq_u0_pcs_tx_phyvoq_async_u0_pcs_tx_phyvoq_afifo_32x611_wrapper_u0_pcs_tx_phyvoq_ram_1r1w_32x611_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_pcs_v0_gate_tessent_mbist_sys_clk_MBIST30_NON_REPAIR_BitSlice_154_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_rce_24_ch_u0_falcon_top_v0_u0_pcs_top_v0_u0_pcs.pcs2_tx_pcs_tx_phyvoq_u0_pcs_tx_phyvoq_async_u0_pcs_tx_phyvoq_afifo_32x611_wrapper_u0_pcs_tx_phyvoq_ram_1r1w_32x611_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_pcs_v0_gate_tessent_mbist_sys_clk_MBIST42_NON_REPAIR_BitSlice_154_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_rce_24_ch_u0_falcon_top_v0_u0_pcs_top_v0_u0_pcs.pcs2_tx_pcs_tx_phyvoq_u0_pcs_tx_phyvoq_async_u0_pcs_tx_phyvoq_afifo_32x611_wrapper_u0_pcs_tx_phyvoq_ram_1r1w_32x611_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_pcs_v0_gate_tessent_mbist_sys_clk_MBIST43_NON_REPAIR_BitSlice_154_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_rce_24_ch_1_u0_falcon_top_v1_u0_pcs_top_v1_u0_pcs.pcs0_tx_pcs_tx_phyvoq_u0_pcs_tx_phyvoq_async_u0_pcs_tx_phyvoq_afifo_32x611_wrapper_u0_pcs_tx_phyvoq_ram_1r1w_32x611_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_pcs_v1_gate_tessent_mbist_sys_clk_MBIST11_NON_REPAIR_BitSlice_154_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_rce_24_ch_1_u0_falcon_top_v1_u0_pcs_top_v1_u0_pcs.pcs1_tx_pcs_tx_phyvoq_u0_pcs_tx_phyvoq_async_u0_pcs_tx_phyvoq_afifo_32x611_wrapper_u0_pcs_tx_phyvoq_ram_1r1w_32x611_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_pcs_v1_gate_tessent_mbist_sys_clk_MBIST29_NON_REPAIR_BitSlice_154_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_rce_24_ch_1_u0_falcon_top_v1_u0_pcs_top_v1_u0_pcs.pcs2_tx_pcs_tx_phyvoq_u0_pcs_tx_phyvoq_async_u0_pcs_tx_phyvoq_afifo_32x611_wrapper_u0_pcs_tx_phyvoq_ram_1r1w_32x611_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_pcs_v1_gate_tessent_mbist_sys_clk_MBIST42_NON_REPAIR_BitSlice_154_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_ifb_u0_pbu_ppurd_cmd_ram_1r1w_64x17_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST29_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.idma_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST35_NON_REPAIR_BitSlice_158_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_ifb_u0_pbu_ppurd_cmd_ram_1r1w_64x17_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST57_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.cgavd_u0_cgavd_memory_u0_flow_memory_u0_cgavd_flow_wq_u0_cgavd_flow_wred_grp_ram_1r1w_64x27_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST1_NON_REPAIR_BitSlice_34_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_qlist_u0_free_list_man_u0_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST28_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_qlist_u0_qlist_em_u0_qmu_em_pd_enq_fwft_fifo_128x87_wrapper_u0_qmu_em_pd_enq_fifo_128x87_wrapper_qmu_em_pd_enq_ram_1r1w_128x87_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST36_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.cgavd_u0_cgavd_memory_u0_pp_memory_u0_cgavd_pp_wred_u0_cgavd_pp_wred_para_ram_1r1w_64x78_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST7_NON_REPAIR_BitSlice_86_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.cgavd_u0_cgavd_memory_u0_flow_memory_u0_cgavd_flow_wq_u0_cgavd_flow_wred_grp_ram_1r1w_64x27_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST1_NON_REPAIR_BitSlice_34_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_qlist_u0_free_list_man_u0_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST28_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_qlist_u0_qlist_em_u0_qmu_em_pd_enq_fwft_fifo_128x87_wrapper_u0_qmu_em_pd_enq_fifo_128x87_wrapper_qmu_em_pd_enq_ram_1r1w_128x87_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST36_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.cgavd_u0_cgavd_memory_u0_pp_memory_u0_cgavd_pp_wred_u0_cgavd_pp_wred_para_ram_1r1w_64x78_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST7_NON_REPAIR_BitSlice_86_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_ecgavd_sa_asm_gate_tessent_mbist_sys_clk_MBIST20_NON_REPAIR_BitSlice_13_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_mc_mul_fcopy_queue_u0_mul_1st_mque_mgmt_u0_sa_asm_gate_tessent_mbist_sys_clk_MBIST23_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_mc_mul_u0_asm_info_u0_mulcp_mgmt_u0_ram_1wr_128kx80_sa_asm_gate_tessent_mbist_sys_clk_MBIST26_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_asm_cell_chg_asm_fifo_64x2071_asm_fifo_64x2071_wrapper_asm_ram_1w1r_64x2071_wrapper_asm_ram_1r1w_64x71_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_80_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_pcp_fifo_16x80_fifo_16x80_ram_1w1r_16x80_ram_1r1w_16x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST33_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_sa_ip_asm_sm_intf_buf_u0_sa_asm_gate_tessent_mbist_sys_clk_MBIST57_NON_REPAIR_BitSlice_36_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST1_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u4_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST10_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u5_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST11_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u0_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST12_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST14_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u0_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST2_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST22_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u8_rxmac_u0_afifo_16x64_wrapper_u0_ram_1w1r_16x64_ram_1r1w_16x64_ues_gmem_1r1w_2clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST23_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u8_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST24_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u1_rxmac_u0_afifo_16x64_wrapper_u0_ram_1w1r_16x64_ram_1r1w_16x64_ues_gmem_1r1w_2clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST28_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u1_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST29_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u2_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST31_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u0_rxmac_u0_afifo_16x64_wrapper_u0_ram_1w1r_16x64_ram_1r1w_16x64_ues_gmem_1r1w_2clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST32_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u3_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST33_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u4_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST35_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST37_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u5_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST38_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u6_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST41_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST43_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u7_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST44_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u8_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST47_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u8_rxmac_u0_afifo_16x64_wrapper_u0_ram_1w1r_16x64_ram_1r1w_16x64_ues_gmem_1r1w_2clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST49_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u7_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST50_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u6_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST51_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u3_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST52_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST53_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u2_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST54_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u1_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST55_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u1_rxmac_u0_afifo_16x64_wrapper_u0_ram_1w1r_16x64_ram_1r1w_16x64_ues_gmem_1r1w_2clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST56_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u0_rxmac_u0_afifo_16x64_wrapper_u0_ram_1w1r_16x64_ram_1r1w_16x64_ues_gmem_1r1w_2clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST57_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_sys_clk_MBIST13_NON_REPAIR_BitSlice_140_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_sys_clk_MBIST18_NON_REPAIR_BitSlice_140_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_sys_clk_MBIST25_NON_REPAIR_BitSlice_140_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_140_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u3_sa_mac_top_gate_tessent_mbist_sys_clk_MBIST34_NON_REPAIR_BitSlice_140_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_sys_clk_MBIST40_NON_REPAIR_BitSlice_140_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_sys_clk_MBIST46_NON_REPAIR_BitSlice_140_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u4_sa_mac_top_gate_tessent_mbist_sys_clk_MBIST8_NON_REPAIR_BitSlice_140_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_sys_clk_MBIST9_NON_REPAIR_BitSlice_140_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u0_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_0_MBIST4_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u1_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_1_MBIST30_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u1_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_10_MBIST16_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u2_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_11_MBIST17_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u3_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_12_MBIST19_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u4_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_13_MBIST20_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u5_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_14_MBIST21_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u6_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_15_MBIST5_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u7_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_16_MBIST26_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u8_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_17_MBIST27_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u2_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_2_MBIST6_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u3_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_3_MBIST7_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u4_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_4_MBIST36_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u5_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_5_MBIST39_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u6_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_6_MBIST42_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u7_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_7_MBIST45_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u8_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_8_MBIST48_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u0.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u0_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_9_MBIST15_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST1_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u4_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST10_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u5_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST11_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u0_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST12_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST14_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u0_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST2_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST22_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u8_rxmac_u0_afifo_16x64_wrapper_u0_ram_1w1r_16x64_ram_1r1w_16x64_ues_gmem_1r1w_2clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST23_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u8_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST24_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u1_rxmac_u0_afifo_16x64_wrapper_u0_ram_1w1r_16x64_ram_1r1w_16x64_ues_gmem_1r1w_2clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST28_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u1_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST29_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u2_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST31_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u0_rxmac_u0_afifo_16x64_wrapper_u0_ram_1w1r_16x64_ram_1r1w_16x64_ues_gmem_1r1w_2clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST32_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u3_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST33_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u4_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST35_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST37_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u5_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST38_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u6_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST41_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST43_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u7_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST44_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u8_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST47_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u8_rxmac_u0_afifo_16x64_wrapper_u0_ram_1w1r_16x64_ram_1r1w_16x64_ues_gmem_1r1w_2clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST49_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u7_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST50_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u6_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST51_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u3_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST52_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST53_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u2_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST54_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u1_rxmac_u0_fec_decoder_u0_fec_128x80_wrapper_u0_ram_1w1r_128x80_ram_1r1w_128x80_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST55_NON_REPAIR_BitSlice_88_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u1_rxmac_u0_afifo_16x64_wrapper_u0_ram_1w1r_16x64_ram_1r1w_16x64_ues_gmem_1r1w_2clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST56_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u0_rxmac_u0_afifo_16x64_wrapper_u0_ram_1w1r_16x64_ram_1r1w_16x64_ues_gmem_1r1w_2clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_crm_mac_loc_clk_MBIST57_NON_REPAIR_BitSlice_72_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_sys_clk_MBIST13_NON_REPAIR_BitSlice_140_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_sys_clk_MBIST18_NON_REPAIR_BitSlice_140_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_sys_clk_MBIST25_NON_REPAIR_BitSlice_140_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_140_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u3_sa_mac_top_gate_tessent_mbist_sys_clk_MBIST34_NON_REPAIR_BitSlice_140_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_sys_clk_MBIST40_NON_REPAIR_BitSlice_140_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_sys_clk_MBIST46_NON_REPAIR_BitSlice_140_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u4_sa_mac_top_gate_tessent_mbist_sys_clk_MBIST8_NON_REPAIR_BitSlice_140_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_mac_top_gate_tessent_mbist_sys_clk_MBIST9_NON_REPAIR_BitSlice_140_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u0_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_0_MBIST4_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u1_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_1_MBIST30_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u1_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_10_MBIST16_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u2_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_11_MBIST17_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u3_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_12_MBIST19_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u4_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_13_MBIST20_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u5_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_14_MBIST21_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u6_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_15_MBIST5_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u7_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_16_MBIST26_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u8_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_17_MBIST27_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u2_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_2_MBIST6_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u3_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_3_MBIST7_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u4_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_4_MBIST36_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u5_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_5_MBIST39_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u6_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_6_MBIST42_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u7_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_7_MBIST45_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u0_sa_ip_mac_9lane_u0_sa_one_link_u8_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_8_MBIST48_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_mac_top_u1.sa_mac_u1_sa_ip_mac_9lane_u0_sa_one_link_u0_txmac_u0_fec_encoder_u0_fec_txfifo_64x82_u0_ram_1w1r_64x82_ram_1r1w_64x82_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_mac_top_gate_tessent_mbist_xserdes_mac_ref_clk_9_MBIST15_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_datacell_ch_u0_cgs_datacell_bwc_buf_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST18_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_datacell_ch_u0_cgs_datacell_bwc_buf_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST19_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_datacell_ch_u0_cgs_datacell_lut_buf_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST20_NON_REPAIR_BitSlice_76_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_datacell_ch_u0_cgs_datacell_lut_buf_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST21_NON_REPAIR_BitSlice_74_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_serdes_process_top_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST24_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_serdes_process_top_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST25_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_serdes_process_top_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST26_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_serdes_process_top_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST27_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_serdes_process_top_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST28_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_serdes_process_top_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST29_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_serdes_process_top_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST30_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_serdes_process_top_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST31_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_ctrlcell_ch_u0_cgs_ctrllut_fifo_48x67_wrapper_ram_1w1r_48x67_rxsw_ram_1r1w_48x67_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_xsw_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_76_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_txsw_sa_ip_txsw_u0_crp_data_ch_u0_crp_chan_u0_dc_rcv_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST41_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_txsw_sa_ip_txsw_u0_crp_data_ch_u0_crp_chan_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST42_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_txsw_sa_ip_txsw_u0_crp_data_ch_u0_crp_chan_u0_dc_recon_buf_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST43_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_txsw_sa_ip_txsw_u0_crp_data_ch_u0_crp_chan_u1_dc_rcv_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST44_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_txsw_sa_ip_txsw_u0_crp_data_ch_u0_crp_chan_u1_dc_rcv_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST45_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_txsw_sa_ip_txsw_u0_crp_data_ch_u0_crp_chan_u1_dc_recon_buf_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST46_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_txsw_sa_ip_txsw_u0_crp_data_ch_u0_crp_chan_u2_dc_rcv_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST47_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_txsw_sa_ip_txsw_u0_crp_data_ch_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST48_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_txsw_sa_ip_txsw_u0_crp_data_ch_u0_crp_chan_u3_dc_rcv_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST49_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_txsw_sa_ip_txsw_u0_crp_data_ch_u0_crp_chan_u3_dc_recon_buf_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST50_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_txsw_sa_ip_txsw_u0_crp_data_ch_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST51_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_txsw_sa_ip_txsw_u0_crp_data_ch_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST52_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_txsw_sa_ip_txsw_u0_crp_data_ch_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST53_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_se_ex_u0_se_schd_other_u0.se_schd_u0_se_kschd_u0_se_schd_other_gate_tessent_mbist_sys_clk_MBIST7_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_se_ex_u0_se_schd_other_u0.se_schd_u0_se_kschd_u0_se_schd_other_gate_tessent_mbist_sys_clk_MBIST8_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.smmu1_cash0_inst_cpu_fifo_inst_smmu1_cache_cpu_fifo_16x547_wrapper_smmu1_cache_cpu_ram_1r1w_16x547_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_se_smmu1_gate_tessent_mbist_sys_clk_MBIST25_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.smmu1_cash1_inst_cpu_fifo_inst_smmu1_cache_cpu_fifo_16x547_wrapper_smmu1_cache_cpu_ram_1r1w_16x547_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_se_smmu1_gate_tessent_mbist_sys_clk_MBIST28_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.smmu1_cash2_inst_cpu_fifo_inst_smmu1_cache_cpu_fifo_16x547_wrapper_smmu1_cache_cpu_ram_1r1w_16x547_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_se_smmu1_gate_tessent_mbist_sys_clk_MBIST31_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.smmu1_cash3_inst_cpu_fifo_inst_smmu1_cache_cpu_fifo_16x547_wrapper_smmu1_cache_cpu_ram_1r1w_16x547_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_se_smmu1_gate_tessent_mbist_sys_clk_MBIST34_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.smmu1_cash4_inst_cpu_fifo_inst_smmu1_cache_cpu_fifo_16x547_wrapper_smmu1_cache_cpu_ram_1r1w_16x547_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_se_smmu1_gate_tessent_mbist_sys_clk_MBIST37_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.smmu1_cash5_inst_cpu_fifo_inst_smmu1_cache_cpu_fifo_16x547_wrapper_smmu1_cache_cpu_ram_1r1w_16x547_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_se_smmu1_gate_tessent_mbist_sys_clk_MBIST40_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.smmu1_cash6_inst_cpu_fifo_inst_smmu1_cache_cpu_fifo_16x547_wrapper_smmu1_cache_cpu_ram_1r1w_16x547_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_se_smmu1_gate_tessent_mbist_sys_clk_MBIST43_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.smmu1_cash7_inst_cpu_fifo_inst_smmu1_cache_cpu_fifo_16x547_wrapper_smmu1_cache_cpu_ram_1r1w_16x547_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_se_smmu1_gate_tessent_mbist_sys_clk_MBIST46_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.smmu1_cash8_inst_cpu_fifo_inst_smmu1_cache_cpu_fifo_16x547_wrapper_smmu1_cache_cpu_ram_1r1w_16x547_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_se_smmu1_gate_tessent_mbist_sys_clk_MBIST57_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.smmu1_cash9_inst_cpu_fifo_inst_smmu1_cache_cpu_fifo_16x547_wrapper_smmu1_cache_cpu_ram_1r1w_16x547_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_se_smmu1_gate_tessent_mbist_sys_clk_MBIST60_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.smmu1_cash10_inst_cpu_fifo_inst_smmu1_cache_cpu_fifo_16x547_wrapper_smmu1_cache_cpu_ram_1r1w_16x547_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_se_smmu1_gate_tessent_mbist_sys_clk_MBIST63_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.smmu1_cash11_inst_cpu_fifo_inst_smmu1_cache_cpu_fifo_16x547_wrapper_smmu1_cache_cpu_ram_1r1w_16x547_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_se_smmu1_gate_tessent_mbist_sys_clk_MBIST66_NON_REPAIR_BitSlice_138_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST61_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap0_shap_pp_u0_shap_ram_1rw_135x28_cir_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_shap_gate_tessent_mbist_sys_clk_MBIST72_NON_REPAIR_BitSlice_36_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap0_shap_sg_u0_shap_ram_1rw_121x28_cir_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_shap_gate_tessent_mbist_sys_clk_MBIST73_NON_REPAIR_BitSlice_36_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap0_shap_sg_u0_shap_ram_1rw_121x14_cbs_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_shap_gate_tessent_mbist_sys_clk_MBIST74_NON_REPAIR_BitSlice_20_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap0_shap_pp_u0_shap_ram_1rw_135x14_cbs_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_shap_gate_tessent_mbist_sys_clk_MBIST75_NON_REPAIR_BitSlice_20_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap1_shap_pp_u0_shap_ram_1rw_135x14_cbs_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_shap_gate_tessent_mbist_sys_clk_MBIST76_NON_REPAIR_BitSlice_20_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap1_shap_sg_u0_shap_ram_1rw_121x14_cbs_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_shap_gate_tessent_mbist_sys_clk_MBIST77_NON_REPAIR_BitSlice_20_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap1_shap_sg_u0_shap_ram_1rw_121x28_cir_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_shap_gate_tessent_mbist_sys_clk_MBIST78_NON_REPAIR_BitSlice_36_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap1_shap_pp_u0_shap_ram_1rw_135x28_cir_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_shap_gate_tessent_mbist_sys_clk_MBIST79_NON_REPAIR_BitSlice_36_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tmmu_module_u0_tmmu_core_u0_tm_others_gate_tessent_mbist_sys_clk_MBIST15_NON_REPAIR_BitSlice_68_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tmmu_module_u0_tmmu_core_u0_tmmu_wr_rd_core_u0_tm_others_gate_tessent_mbist_sys_clk_MBIST17_NON_REPAIR_BitSlice_48_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tmmu_module_u1_tmmu_core_u0_tmmu_wr_rd_core_u0_tm_others_gate_tessent_mbist_sys_clk_MBIST3_NON_REPAIR_BitSlice_48_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tmmu_module_u1_tmmu_core_u0_tmmu_wr_rd_core_u0_tmmu_imem_enq_dp_fifo_wrapper_u0_tmmu_imem_enq_dp_fifo_128x60_wrapper_u0_tmmu_imem_enq_dp_ram_1r1w_128x60_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_tm_others_gate_tessent_mbist_sys_clk_MBIST4_NON_REPAIR_BitSlice_68_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tmmu_module_u1_tmmu_core_u0_rd_cmd_fifo_wrapper_u0_tmmu_imem_enq_dp_ram_1r1w_128x60_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_tm_others_gate_tessent_mbist_sys_clk_MBIST9_NON_REPAIR_BitSlice_68_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                    } // End ECC_nr_arm_1
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_ECC_repair_arm_1) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_ECC_repair_arm_1_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_lif_u0_lifcc_u0.cfg_cfg_pcie_top_cfg_pcie_dma_mac_up_cfg_pcie_afifo_256x512_wrapper_u0_cfg_pcie_ram_1r1w_256x512_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_lifcc_gate_tessent_mbist_sys_clk_MBIST4_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_mc_mul_u0_asm_info_u0_index_mgmt_u0_ram_1wr_128kx17_ram_1rw_65536x10_ues_gmem_1rw_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST25_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_ctrlcell_ch_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST5_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m2,m3 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_ctrlcell_ch_u0_cgs_flow_to_queue_tab_ram_1wr_65536x26_rxsw_ram_1rw_65536x25_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_sa_xsw_gate_tessent_mbist_sys_clk_MBIST6_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_ctrlcell_ch_u0_sa_xsw_gate_tessent_mbist_sys_clk_MBIST7_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m2,m3 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap0_shap_gate_tessent_mbist_sys_clk_MBIST13_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap0_shap_mid_u0_shap_gate_tessent_mbist_sys_clk_MBIST14_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap0_shap_flow_u0_shap_gate_tessent_mbist_sys_clk_MBIST15_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap0_shap_ses_u0_shap_gate_tessent_mbist_sys_clk_MBIST16_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap1_shap_ses_u0_shap_gate_tessent_mbist_sys_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap1_shap_flow_u0_shap_gate_tessent_mbist_sys_clk_MBIST27_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap1_shap_mid_u0_shap_gate_tessent_mbist_sys_clk_MBIST28_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap1_shap_gate_tessent_mbist_sys_clk_MBIST29_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST36_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST42_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                    } // End ECC_repair_arm_1
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_ECC_repair_ss_1) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_ECC_repair_ss_1_bp) {
                MemoryBist {
                run_mode : run_time_prog;
                reduced_address_count : off;
                
                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_cfg_ram_1r1w_65536x25_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_cfg_ram_1r1w_65536x25_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST29_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_mid_cfg_ram_1r1w_16384x25_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_cfg_ram_1r1w_65536x25_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST84_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.serdes_s24_u0_serdes_s4_u0_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif0_gate_tessent_mbist_salina_cpu_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.serdes_s24_u0_serdes_s4_u1_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif0_gate_tessent_mbist_salina_cpu_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.serdes_s24_u0_serdes_s4_u2_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif0_gate_tessent_mbist_salina_cpu_clk_MBIST24_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.serdes_s24_u0_serdes_s4_u3_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif0_gate_tessent_mbist_salina_cpu_clk_MBIST27_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.serdes_s24_u0_serdes_s4_u4_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif0_gate_tessent_mbist_salina_cpu_clk_MBIST30_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u0.serdes_s24_u0_serdes_s4_u5_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif0_gate_tessent_mbist_salina_cpu_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u0_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u1_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u2_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u2_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST23_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u3_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST25_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u4_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST29_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif0_u1.serdes_s24_u0_serdes_s4_u5_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif02_gate_tessent_mbist_salina_cpu_clk_MBIST31_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif1_u0.serdes_s24_btm_u0_serdes_s4_u5_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif1_gate_tessent_mbist_salina_cpu_clk_MBIST16_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif1_u0.serdes_s24_btm_u0_serdes_s4_u4_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif1_gate_tessent_mbist_salina_cpu_clk_MBIST17_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif1_u0.serdes_s24_btm_u0_serdes_s4_u3_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif1_gate_tessent_mbist_salina_cpu_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif1_u0.serdes_s24_btm_u0_serdes_s4_u2_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif1_gate_tessent_mbist_salina_cpu_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif1_u0.serdes_s24_btm_u0_serdes_s4_u1_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif1_gate_tessent_mbist_salina_cpu_clk_MBIST23_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif1_u0.serdes_s24_btm_u0_serdes_s4_u0_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif1_gate_tessent_mbist_salina_cpu_clk_MBIST25_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif12_u0.serdes_s24_btm_u0_serdes_s4_u0_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif12_gate_tessent_mbist_salina_cpu_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif12_u0.serdes_s24_btm_u0_serdes_s4_u1_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif12_gate_tessent_mbist_salina_cpu_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif12_u0.serdes_s24_btm_u0_serdes_s4_u2_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif12_gate_tessent_mbist_salina_cpu_clk_MBIST28_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif12_u0.serdes_s24_btm_u0_serdes_s4_u3_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif12_gate_tessent_mbist_salina_cpu_clk_MBIST30_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif12_u0.serdes_s24_btm_u0_serdes_s4_u4_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif12_gate_tessent_mbist_salina_cpu_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif12_u0.serdes_s24_btm_u0_serdes_s4_u5_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif12_gate_tessent_mbist_salina_cpu_clk_MBIST34_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
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
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lif2_u0.serdes_s8_serdes_s4_u1_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lif2_gate_tessent_mbist_salina_cpu_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_lif_u0_lifcc_u0.serdes_s4_lifc_u0_pmem_dmem_wrapper_u0_serdes_s4_imem_ram_1r1w_8192x64_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_lifcc_gate_tessent_mbist_salina_cpu_clk_MBIST12_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_odma_u0.odma_share_ram_access_u0_odma_desc_ram_access_u0_odma_gate_tessent_mbist_sys_clk_MBIST36_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_odma_u0.odma_share_ram_access_u0_odma_gate_tessent_mbist_sys_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_nppu_u0_odma_u0.odma_share_ram_access_u0_odma_ll_ptr_tm_ram_access_interface_u0_odma_gate_tessent_mbist_sys_clk_MBIST38_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_odma_u0.odma_share_ram_access_u0_odma_gate_tessent_mbist_sys_clk_MBIST40_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_odma_u0.odma_share_ram_access_u0_odma_desc_ram_access_u0_odma_gate_tessent_mbist_sys_clk_MBIST41_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_odma_u0.odma_share_ram_access_u0_odma_mfpara1_ram_access_u0_odma_gate_tessent_mbist_sys_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_nppu_u0_odma_u0.odma_share_ram_access_u0_odma_mfpara2_ram_access_u0_odma_gate_tessent_mbist_sys_clk_MBIST44_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_nppu_u0_odma_u0.odma_share_ram_access_u0_odma_gate_tessent_mbist_sys_clk_MBIST45_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_nppu_u0_odma_u0.odma_share_ram_access_u0_odma_mfpara_tm_ram_access_u0_odma_gate_tessent_mbist_sys_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_odma_u0.odma_gate_tessent_mbist_sys_clk_MBIST64_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_nppu_u0_odma_u0.odma_share_ram_access_u0_odma_gate_tessent_mbist_sys_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_nppu_u0_odma_u0.odma_block_u0_odma_quemng_sch_ntm_u0_odma_desc_quemng_ntm_u0_odma_ll_status_ntm_u0_odma_tailptr_ntm_ram_access_u0_odma_tailptr_ntm_ram_1r1w_9600x15_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_odma_gate_tessent_mbist_sys_clk_MBIST76_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_odma_u0.odma_block_u1_odma_quemng_sch_ntm_u0_odma_desc_quemng_ntm_u0_odma_ll_status_ntm_u0_odma_tailptr_ntm_ram_access_u0_odma_tailptr_ntm_ram_1r1w_9600x15_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_odma_gate_tessent_mbist_sys_clk_MBIST84_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_odma_u0.odma_share_ram_access_u0_odma_ll_tm_ram_access_interface_u0_odma_ll_tm_ram_bank_u1_odma_ll_tm_ram_1r1w_8192x14_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_odma_gate_tessent_mbist_sys_clk_MBIST85_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pktrx_u0.pktrx_mpls_label_u0_pktrx_label_tbl_ram_4r1w_131072x24_wrapper_u0_ues_gmem_4r1w_1clk_mem_wrapper_gmem_pktrx_gate_tessent_mbist_sys_clk_MBIST11_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_nppu_u0_pktrx_u0.pktrx_mpls_label_u0_pktrx_label_tbl_ram_4r1w_131072x24_wrapper_u0_ues_gmem_4r1w_1clk_mem_wrapper_gmem_pktrx_gate_tessent_mbist_sys_clk_MBIST12_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_nppu_u0_pktrx_u0.pktrx_mpls_label_u0_pktrx_label_tbl_ram_4r1w_131072x24_wrapper_u0_ues_gmem_4r1w_1clk_mem_wrapper_gmem_pktrx_gate_tessent_mbist_sys_clk_MBIST13_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pktrx_u0.pktrx_mpls_label_u0_pktrx_label_tbl_ram_4r1w_131072x24_wrapper_u0_ues_gmem_4r1w_1clk_mem_wrapper_gmem_pktrx_gate_tessent_mbist_sys_clk_MBIST14_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_nppu_u0_pktrx_u0.pktrx_mpls_label_u0_pktrx_label_tbl_ram_4r1w_131072x24_wrapper_u0_ues_gmem_4r1w_1clk_mem_wrapper_gmem_pktrx_gate_tessent_mbist_sys_clk_MBIST15_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_nppu_u0_pktrx_u0.pktrx_mpls_label_u0_pktrx_label_tbl_ram_4r1w_131072x24_wrapper_u0_ues_gmem_4r1w_1clk_mem_wrapper_gmem_pktrx_gate_tessent_mbist_sys_clk_MBIST16_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_nppu_u0_pktrx_u0.pktrx_mpls_label_u0_pktrx_label_tbl_ram_4r1w_131072x24_wrapper_u0_ues_gmem_4r1w_1clk_mem_wrapper_gmem_pktrx_gate_tessent_mbist_sys_clk_MBIST17_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_nppu_u0_pktrx_u0.pktrx_mpls_label_u0_pktrx_label_tbl_ram_4r1w_131072x24_wrapper_u0_ues_gmem_4r1w_1clk_mem_wrapper_gmem_pktrx_gate_tessent_mbist_sys_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_nppu_u0_pktrx_u0.pktrx_mpls_label_u0_pktrx_label_tbl_ram_4r1w_131072x24_wrapper_u0_ues_gmem_4r1w_1clk_mem_wrapper_gmem_pktrx_gate_tessent_mbist_sys_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_nppu_u0_pktrx_u0.pktrx_mpls_label_u0_pktrx_label_tbl_ram_4r1w_131072x24_wrapper_u0_ues_gmem_4r1w_1clk_mem_wrapper_gmem_pktrx_gate_tessent_mbist_sys_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_nppu_u0_pktrx_u0.pktrx_mpls_label_u0_pktrx_label_tbl_ram_4r1w_131072x24_wrapper_u0_ues_gmem_4r1w_1clk_mem_wrapper_gmem_pktrx_gate_tessent_mbist_sys_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_nppu_u0_pktrx_u0.pktrx_mpls_label_u0_pktrx_label_tbl_ram_4r1w_131072x24_wrapper_u0_ues_gmem_4r1w_1clk_mem_wrapper_gmem_pktrx_gate_tessent_mbist_sys_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_ppu_u0.ppu_reorder_group_u0_ppu_gate_tessent_mbist_sys_clk_MBIST64_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_cmddeal_u0_cmddeal_imem_age_u0_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST24_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_cmddeal_u0_cmddeal_imem_age_u0_qmu_imem_age_hp_chk_map_ram_1r1w_32768x40_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST25_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_cmddeal_u0_cmddeal_imem_age_u0_qmu_imem_age_hp_drop_cnt_ram_1r1w_32768x10_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_np016_qmu_crs_u0_crs_gen_filter_u0_qsch_crs_qnum_fwft_fifo_49152x19_wrapper_u0_qsch_crs_qnum_fifo_49152x19_wrapper_qsch_crs_qnum_ram_1r1w_49152x19_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST51_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
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
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_np016_qmu_crs_u0_crs_gen_send_u0_qsch_crs_destid_ram_1r1w_65536x9_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST55_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_np016_qmu_crs_u0_crs_gen_send_u0_qsch_crs_destid_ram_1r1w_65536x9_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST56_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_np016_qmu_crs_u0_crs_gen_send_u0_qsch_crs_destid_ram_1r1w_65536x9_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_np016_qmu_crs_u0_qsch_crs_indata_fwft_fifo_512x130_wrapper_u0_qsch_crs_indata_fifo_512x130_wrapper_qsch_crs_indata_ram_1r1w_512x130_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST58_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_np016_qmu_wlist_u0_qsch_flow_idle_fifo0_32768x16_wrapper_u0_qsch_flow_idle_ram_1r1w_32768x16_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST59_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_np016_qmu_wlist_u0_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST60_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_np016_qmu_wlist_u0_qsch_flow_idle_fifo1_32768x16_wrapper_u0_qsch_flow_idle_ram_1r1w_32768x16_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_np016_qmu_wlist_u0_qsch_flow_idle_fifo1_32768x16_wrapper_u0_qsch_flow_idle_ram_1r1w_32768x16_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST62_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_sch_u0_qmu_mul_top_u0_auto_credit_process_u0_qsch_qmul_remote_crdt_fifo_fifo_2048x25_wrapper_u0_qsch_qmul_remote_crdt_fifo_ram_1r1w_2048x25_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST67_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_cmddeal_u0_cmddeal_imem_age_u0_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST24_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_cmddeal_u0_cmddeal_imem_age_u0_qmu_imem_age_hp_chk_map_ram_1r1w_32768x40_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST25_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_cmddeal_u0_cmddeal_imem_age_u0_qmu_imem_age_hp_drop_cnt_ram_1r1w_32768x10_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
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
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_sch_u0_np016_qmu_crs_u0_crs_gen_send_u0_qsch_crs_destid_ram_1r1w_65536x9_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST55_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_sch_u0_np016_qmu_crs_u0_crs_gen_send_u0_qsch_crs_destid_ram_1r1w_65536x9_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST56_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_sch_u0_np016_qmu_crs_u0_crs_gen_send_u0_qsch_crs_destid_ram_1r1w_65536x9_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_sch_u0_np016_qmu_crs_u0_qsch_crs_indata_fwft_fifo_512x130_wrapper_u0_qsch_crs_indata_fifo_512x130_wrapper_qsch_crs_indata_ram_1r1w_512x130_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST58_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_sch_u0_np016_qmu_wlist_u0_qsch_flow_idle_fifo0_32768x16_wrapper_u0_qsch_flow_idle_ram_1r1w_32768x16_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST59_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_sch_u0_np016_qmu_wlist_u0_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST60_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_sch_u0_np016_qmu_wlist_u0_qsch_flow_idle_fifo1_32768x16_wrapper_u0_qsch_flow_idle_ram_1r1w_32768x16_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_sch_u0_np016_qmu_wlist_u0_qsch_flow_idle_fifo1_32768x16_wrapper_u0_qsch_flow_idle_ram_1r1w_32768x16_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST62_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_sch_u0_qmu_mul_top_u0_auto_credit_process_u0_qsch_qmul_remote_crdt_fifo_fifo_2048x25_wrapper_u0_qsch_qmul_remote_crdt_fifo_ram_1r1w_2048x25_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST67_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_cmd_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST1_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_cmd_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST10_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST100_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST101_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST102_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST103_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST104_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST105_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST106_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST107_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST108_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST109_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_cmd_ram_u0_qmu_cmdsch_cmd_ram_1r1w_65536x51_wrapper_u3_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST11_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST110_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST111_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_cti_ram_2r1w_65536x4_wrapper_u7_ues_gmem_2r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST112_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_cti_ram_2r1w_65536x4_wrapper_u7_ues_gmem_2r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST113_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cto_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST114_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cto_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST115_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cto_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST116_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cto_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST117_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cto_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST118_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cto_ram_u0_qmu_cto_ram_1r1w_65536x4_wrapper_u4_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST119_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_cmd_ram_u0_qmu_cmdsch_cmd_ram_1r1w_65536x51_wrapper_u3_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST12_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cto_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST120_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cto_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST121_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cto_ram_u0_qmu_cto_ram_1r1w_65536x4_wrapper_u6_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST122_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cto_ram_u0_qmu_cto_ram_1r1w_65536x4_wrapper_u7_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST123_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_cmd_ram_u0_qmu_cmdsch_cmd_ram_1r1w_65536x51_wrapper_u3_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST13_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_free_list_ram_u0_qmu_cmdsch_list_ram_1r1w_65536x18_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST137_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_free_list_ram_u0_qmu_cmdsch_list_ram_1r1w_65536x18_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST138_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_next_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST139_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_free_list_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST14_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_ram_u0_qmu_chk_ram_1r1w_32768x19_wrapper_u6_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST140_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST141_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_ram_u0_qmu_chk_ram_1r1w_32768x19_wrapper_u7_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST142_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cache_index_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST143_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cto_ram_u0_qmu_cto_ram_1r1w_65536x4_wrapper_u3_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST144_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cto_ram_u0_qmu_cto_ram_1r1w_65536x4_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST145_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cache_index_ram_u0_qmu_cache_index_ram_1r1w_65536x12_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST146_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_free_list_ram_u0_qmu_cmdsch_list_ram_1r1w_65536x18_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST15_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cto_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST153_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cto_ram_u0_qmu_cto_ram_1r1w_65536x4_wrapper_u4_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST154_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cto_ram_u0_qmu_cto_ram_1r1w_65536x4_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST158_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_free_list_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST16_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_free_list_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST17_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_free_list_ram_u0_qmu_cmdsch_list_ram_1r1w_65536x18_wrapper_u2_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_free_list_ram_u0_qmu_cmdsch_list_ram_1r1w_65536x18_wrapper_u2_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_cmd_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST2_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_next_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_next_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_next_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_next_ram_u0_qmu_cmdsch_list_ram_1r1w_65536x18_wrapper_u2_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST23_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_cmd_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST3_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST39_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_cmd_ram_u0_qmu_cmdsch_cmd_ram_1r1w_65536x51_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST4_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST40_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_ram_u0_qmu_chk_ram_1r1w_32768x19_wrapper_u4_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST41_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_ram_u0_qmu_chk_ram_1r1w_32768x19_wrapper_u5_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST42_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_cmd_ram_u0_qmu_cmdsch_cmd_ram_1r1w_65536x51_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST5_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qmu_free_list_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST59_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_cmd_ram_u0_qmu_cmdsch_cmd_ram_1r1w_65536x51_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST6_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qmu_free_list_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST60_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qmu_free_list_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qmu_free_list_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST62_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qmu_free_list_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST63_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qmu_free_list_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST64_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_cmd_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST7_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cache_index_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_cmd_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST8_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cache_index_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST80_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cache_index_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST81_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cache_index_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST82_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cache_index_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST83_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cache_index_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST84_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cache_index_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST85_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cache_index_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST86_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cache_index_ram_u0_qmu_cache_index_ram_1r1w_16384x12_wrapper_u9_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST87_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cache_index_ram_u0_qmu_cache_index_ram_1r1w_65536x12_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST88_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cache_index_ram_u0_qmu_cache_index_ram_1r1w_65536x12_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST89_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_cmdsch_cmd_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST9_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cache_index_ram_u0_qmu_cache_index_ram_1r1w_65536x12_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST90_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST91_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST93_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_cti_ram_2r1w_65536x4_wrapper_u0_ues_gmem_2r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST94_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST95_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST96_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_cti_ram_2r1w_65536x4_wrapper_u0_ues_gmem_2r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST97_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST98_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_cti_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST99_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_cell_sort_asm_cs_ocf_all_u0_sa_asm_gate_tessent_mbist_sys_clk_MBIST10_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_cell_sort_asm_cs_ocf_all_u0_asm_cs_ocf_u1_sa_asm_gate_tessent_mbist_sys_clk_MBIST11_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_cell_sort_asm_cs_ocf_all_u0_sa_asm_gate_tessent_mbist_sys_clk_MBIST12_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_cell_sort_asm_cs_ocf_all_u0_asm_cs_ocf_u1_sa_asm_gate_tessent_mbist_sys_clk_MBIST13_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_cell_sort_asm_cs_ocf_all_u0_sa_asm_gate_tessent_mbist_sys_clk_MBIST14_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_etm_asm_etm_burst_man_u0_asm_etm_burst_man_l2_u0_ram_1w1r_6861x16_ram_1r1w_6861x15_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST15_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_etm_asm_etm_burst_man_u0_asm_etm_burst_man_l1_u0_ram_1w1r_2859x16_ram_1r1w_2859x15_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST17_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_mc_mul_u0_asm_que_mgmt_u0_que_list_u0_ram_1w1r_512x105_ram_1r1w_512x106_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST27_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_pc_asm_pc_queue_ram_1w1r_26kx63_sa_asm_gate_tessent_mbist_sys_clk_MBIST31_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_pc_asm_pc_queue_ram_1w1r_26kx63_sa_asm_gate_tessent_mbist_sys_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_storage_sa_asm_gate_tessent_mbist_sys_clk_MBIST36_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_idle_list_sa_asm_gate_tessent_mbist_sys_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_etm_asm_etm_burst_man_u0_asm_etm_data_inf_ram_u0_ram_1w1r_49152x41_ram_1r1w_24576x46_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST41_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_storage_sa_asm_gate_tessent_mbist_sys_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_mc_mul_u0_asm_info_u0_wr_store_u0_ram_1w1r_4kx97_ram_1r1w_4096x97_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST45_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_cell_sort_asm_cs_ocf_all_u0_sa_asm_gate_tessent_mbist_sys_clk_MBIST5_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_storage_sa_asm_gate_tessent_mbist_sys_clk_MBIST53_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_etm_asm_etm_burst_man_u0_asm_etm_burst_man_l1_u0_sa_asm_gate_tessent_mbist_sys_clk_MBIST59_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_cell_sort_asm_cs_ocf_all_u0_sa_asm_gate_tessent_mbist_sys_clk_MBIST6_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_etm_asm_etm_burst_man_u0_asm_etm_burst_man_l2_u0_sa_asm_gate_tessent_mbist_sys_clk_MBIST60_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_cell_sort_asm_cs_ocf_all_u0_asm_cs_ocf_u0_sa_asm_gate_tessent_mbist_sys_clk_MBIST7_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_etm_asm_etm_burst_man_u0_asm_etm_burst_man_l1_u0_ram_1w1r_49152x43_ram_1r1w_24576x43_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST8_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_etm_asm_etm_burst_man_u0_asm_etm_burst_man_l1_u0_asm_etm_idle_list_u0_ram_1w1r_49152x16_ram_1r1w_24576x15_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST9_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST1_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST10_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST11_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST12_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST2_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST3_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST38_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST39_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST4_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST40_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST41_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST44_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST45_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST46_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST48_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST49_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST5_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST50_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST51_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST53_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST54_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST55_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST56_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST58_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST6_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_qmu_shap_share_ram5_ram_1r1w_32768x19_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_shap_gate_tessent_mbist_sys_clk_MBIST66_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST67_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST68_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_gate_tessent_mbist_sys_clk_MBIST69_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST7_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST8_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST9_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
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
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u16_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST1_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u20_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST10_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u21_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST11_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u21_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST12_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u22_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST13_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u22_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST14_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u24_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u16_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST2_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u24_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u23_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u23_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u25_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST23_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u27_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST24_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u28_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST25_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_16384x135_wrapper_u29_0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_16384x135_wrapper_u30_0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST27_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_16384x135_wrapper_u30_1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST28_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_stat_gate_tessent_mbist_sys_clk_MBIST29_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u18_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST3_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_stat_gate_tessent_mbist_sys_clk_MBIST30_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_16384x135_wrapper_u29_1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST31_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u28_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u26_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST33_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u27_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST34_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u25_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST35_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u26_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST36_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u18_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST4_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u17_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST5_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u17_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST6_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u19_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST7_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u19_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST8_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_se_u0_stat_u0.stat_smmu0_u0_smmu0_ctrl_ram_1r1w_32768x135_wrapper_u20_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST9_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 150 ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                    } // End ECC_repair_ss_1
                } // End TestStep
            } //End Pattern
                
//End