
        Patterns(MemoryBist_P1_bp_r1) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_P1_r1) {
                MemoryBist {
                run_mode : hw_default;
                reduced_address_count : off;
                

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_fxsch_iosch_fxsch_buffer_odma0_fxsch_buffer_odma_queue_u0_fxsch_ipro_buf_odma_ram_1r1w_384x2160_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_fxsch_iosch_fxsch_buffer_odma1_fxsch_buffer_odma1_queue_u0_fxsch_ipro_buf_odma_ram_1r1w_384x2160_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST24_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_fxsch_iosch_tdm_arbi_u0_flex_lif0_data_fifo_20x2160_wrapper_u0_flex_tdm_data_fifo_20x2160_wrapper_flex_tdm_data_ram_1r1w_20x2160_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_lifc_u0_lifc_tx_sch_lifc_tx_sch_buf_lifc_tx_sch_buf_fifo_256x1035_wrapper_u0_lifc_tx_sch_buf_ram_1r1w_256x1035_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST154_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_evoq_fxsch_evoq_qmu_fxsch_evoq_dat_queue_pro_fxsch_evoq_dat_ram_1r1w_4608x2088_wrapper0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST49_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_ivoq_fxsch_ivoq_qmu_fxsch_ivoq_dat_queue_pro_dnif_tx_voq_dat_ram_1r1w_1280x2088_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST77_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_ivoq_fxsch_ivoq_qmu_fxsch_ivoq_dat_queue_pro_dnif_tx_voq_dat_ram_1r1w_1280x2088_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST81_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_rce_24_ch_u0_falcon_top_v0_u0_pcs_top_v0_u0_pcs.pcs_v0_gate_tessent_mbist_pcs_clk_MBIST34_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u1_st_rd_ram_1r1w_1024x2050_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST2_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u1_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST6_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST10_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_management_u0_mmu_pk_rd_split_top_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST24_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u1_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_management_u0_mmu_pk_rd_split_top_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST53_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u1_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u0_st_rd_ram_1r1w_1024x2050_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_management_u0_mmu_pk_rd_split_top_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST77_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_wr_pack_u0.st_mmu_wr_u0_st_mmu_wr_buf_u0_st_mmu_wr_pack_gate_tessent_mbist_sys_clk_MBIST2_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_wr_pack_u0.st_mmu_wr_u0_st_mmu_wr_management_u0_st_mmu_wr_data_ctrl_u1_st_wr_ram_1r1w_1024x2084_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_wr_pack_gate_tessent_mbist_sys_clk_MBIST46_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_wr_pack_u0.st_mmu_wr_u0_st_mmu_wr_management_u0_st_mmu_wr_data_ctrl_u0_st_wr_ram_1r1w_1024x2084_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_wr_pack_gate_tessent_mbist_sys_clk_MBIST50_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_isu_u0.isu_block_u0_isu_gate_tessent_mbist_sys_clk_MBIST2_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_odma_u0.oam_u0_oam_2544_u0_odma_gate_tessent_mbist_sys_clk_MBIST3_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_odma_u0.odma_block_u0_odma_slice_mng_u0_odma_dat_tail_ram_u0_odma_dat_tail_ram_1r1w_156x2048_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_odma_gate_tessent_mbist_sys_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_odma_u0.odma_block_u1_odma_slice_mng_u0_odma_dat_tail_ram_u0_odma_dat_tail_ram_1r1w_156x2048_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_odma_gate_tessent_mbist_sys_clk_MBIST63_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_odma_u0.oam_u0_oam_tst_u0_oam_tst_tx_u0_tstpkt_fwft_fifo_256x2058_wrapper_u0_tstpkt_fifo_256x2058_wrapper_tstpkt_ram_1r1w_256x2058_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_odma_gate_tessent_mbist_sys_clk_MBIST80_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pbu_ifb_ram_bank_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST1_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u0.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_ram_1w1r_128x145_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u0.instrmem_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u0.cluster_gate_tessent_mbist_me_core_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST66_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u1.cluster_gate_tessent_mbist_me_core_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST96_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u10.cluster_gate_tessent_mbist_me_core_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST88_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u11.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_ram_1w1r_128x145_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u11.cluster_gate_tessent_mbist_me_core_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST66_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u12.cluster_gate_tessent_mbist_me_core_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST96_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u13.cluster_gate_tessent_mbist_me_core_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST88_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u14.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_ram_1w1r_128x145_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u14.cluster_gate_tessent_mbist_me_core_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST66_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u15.cluster_gate_tessent_mbist_me_core_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST96_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u2.cluster_gate_tessent_mbist_me_core_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST88_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u3.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_ram_1w1r_128x145_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u3.cluster_gate_tessent_mbist_me_core_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST66_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u4.cluster_gate_tessent_mbist_me_core_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST96_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u5.cluster_gate_tessent_mbist_me_core_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST88_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u6.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_ram_1w1r_128x145_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u6.cluster_gate_tessent_mbist_me_core_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST66_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u7.cluster_gate_tessent_mbist_me_core_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST96_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u8.cluster_gate_tessent_mbist_me_core_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST88_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u9.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_ram_1w1r_128x145_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u9.cluster_gate_tessent_mbist_me_core_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_pc_asm_pc_queue_asm_pc_que_err_ram_1w1r_4096x16_ram_1r1w_4096x15_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_phm_sa_asm_gate_tessent_mbist_sys_clk_MBIST40_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_storage_sa_asm_gate_tessent_mbist_sys_clk_MBIST50_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_storage_ram_1w1r_6kx2048_u2_ram_1r1w_3072x2064_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST54_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_datacell_ch_u0_cgs_datacell_buf_u0_cgs_dc_buf_data_ram_1w1r_384x2074_rxsw_ram_1r1w_384x2064_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_xsw_gate_tessent_mbist_sys_clk_MBIST9_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_txsw_sa_ip_txsw_u0_crp_ctrl_ch_u0_ptal_process_top_u0_ptal_process_u0_ram_1wr_65536x10_txsw_ram_1rw_65536x10_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_sa_xsw_gate_tessent_mbist_sys_clk_MBIST39_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_alg_top_u0_alg_altro_inst.alg_inst_alg_hash_cmp_inst2_alg_root_cmp_inst_hash_int_rsp_fifo_inst_hash_int_rsp_ram_1r1w_1024x258_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_alg_altro_gate_tessent_mbist_alg_clk_MBIST3_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_alg_top_u0_alg_altro_inst.alg_inst_alg_hash_cmp_inst1_alg_root_cmp_inst_hash_root_info_fifo_inst_hash_root_info_ram_1r1w_1024x546_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_alg_altro_gate_tessent_mbist_alg_clk_MBIST14_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_alg_top_u0_alg_altro_inst.alg_inst_alg_altro_gate_tessent_mbist_alg_clk_MBIST36_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_schd_other_u0.se_other_u0_se_cmmu_u0_alu_hbm_u0_hbm_opr_sel_u0_cmmu_alu_calc_ram_1r1w_512x512_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_se_schd_other_gate_tessent_mbist_sys_clk_MBIST49_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.smmu1_rschd_inst_se_smmu1_gate_tessent_mbist_sys_clk_MBIST73_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.se_smmu1_gate_tessent_mbist_sys_clk_MBIST104_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u0.zx222016_1024x640_tcam_u1_etcam_egroup_v0_gate_tessent_mbist_sys_clk_MBIST3_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u0.zx222016_1024x640_tcam_u3_etcam_egroup_v0_gate_tessent_mbist_sys_clk_MBIST7_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u1.zx222016_1024x640_tcam_u1_etcam_egroup_v1_gate_tessent_mbist_sys_clk_MBIST3_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u1.zx222016_1024x640_tcam_u3_etcam_egroup_v1_gate_tessent_mbist_sys_clk_MBIST7_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u2.zx222016_1024x640_tcam_u3_etcam_egroup_h_gate_tessent_mbist_sys_clk_MBIST3_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u2.zx222016_1024x640_tcam_u1_etcam_egroup_h_gate_tessent_mbist_sys_clk_MBIST7_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u3.zx222016_1024x640_tcam_u3_etcam_egroup_h_gate_tessent_mbist_sys_clk_MBIST3_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u3.zx222016_1024x640_tcam_u1_etcam_egroup_h_gate_tessent_mbist_sys_clk_MBIST7_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x128_wrapper_u9_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST23_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x128_wrapper_u10_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST27_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x128_wrapper_u12_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST51_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x128_wrapper_u14_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST59_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_stat_u0.plcr_u0_plcr_memory_inst0_plcr_ram_1r1w_1024x108_wrapper_inst0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_stat_gate_tessent_mbist_sys_clk_MBIST16_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_cfg_se_ram_1rw_524288x4_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_que_num_ram_1r1w_131072x6_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST23_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_mid_sch_ram_1r1w_16384x17_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST35_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_map_ram_1r1w_65536x21_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_htptr_dci_ram_1r1w_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST103_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_htptr_dci_ram_1r1w_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST107_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_mid_wfq_link_ram_1r1w_229376x36_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST111_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_htptr_dci_ram_1r1w_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST115_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_up_down_ptr_ram_1r1w_524288x12_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST139_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_up_down_ptr_ram_1r1w_524288x12_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST143_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_up_down_ptr_ram_1r1w_524288x12_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST147_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_up_down_ptr_ram_1r1w_524288x12_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST151_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_up_down_ptr_ram_1r1w_131072x36_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST159_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_cmddeal_u0_cmd_sw_u0_qmu_cmdsw_nsop_fwft_fifo_1024x71_wrapper_u0_qmu_cmdsw_nsop_fifo_1024x71_wrapper_qmu_cmdsw_nsop_ram_1r1w_1024x71_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_qlist_u0_qlist_em_u0_qmu_em_enq_rpt_fwft_fifo_2048x56_wrapper_u0_qmu_em_enq_rpt_fifo_2048x56_wrapper_qmu_em_enq_rpt_ram_1r1w_2048x56_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST35_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_qlist_u0_qlist_em_u0_qmu_em_pds_enq_fwft_fifo_256x129_wrapper_u0_qmu_em_pds_enq_fifo_256x129_wrapper_qmu_em_pds_enq_ram_1r1w_256x129_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST38_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_cmddeal_u0_cmd_sw_u0_qmu_cmdsw_nsop_fwft_fifo_1024x71_wrapper_u0_qmu_cmdsw_nsop_fifo_1024x71_wrapper_qmu_cmdsw_nsop_ram_1r1w_1024x71_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_qlist_u0_qlist_em_u0_qmu_em_enq_rpt_fwft_fifo_2048x56_wrapper_u0_qmu_em_enq_rpt_fifo_2048x56_wrapper_qmu_em_enq_rpt_ram_1r1w_2048x56_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST35_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_qlist_u0_qlist_em_u0_qmu_em_pds_enq_fwft_fifo_256x129_wrapper_u0_qmu_em_pds_enq_fifo_256x129_wrapper_qmu_em_pds_enq_ram_1r1w_256x129_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST38_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST17_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_qmu_shap_share_ram1_ram_1r1w_32768x18_wrapper_u3_ues_gmem_1r1w_1clk_mem_wrapper_gmem_shap_gate_tessent_mbist_sys_clk_MBIST25_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST33_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_tm_others_u0.olif_u0_olif_module_u0_ie_pkt_order_u0_tmolif_imem_data_fifo_512x2067_wrapper_u0_tmolif_imem_data_fifo_512x2048_wrapper_u0_tmolif_imem_data_ram_1r1w_512x2048_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_tm_others_gate_tessent_mbist_sys_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                    } // End r1
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_P1_bp_r2) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_P1_r2) {
                MemoryBist {
                run_mode : hw_default;
                reduced_address_count : off;
                

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_fxsch_iosch_fxsch_buffer_odma0_fxsch_buffer_odma_queue_u0_fxsch_ipro_buf_odma_ram_1r1w_384x2160_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_fxsch_iosch_fxsch_buffer_odma1_fxsch_buffer_odma1_queue_u0_fxsch_ipro_buf_odma_ram_1r1w_384x2160_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST25_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_fxsch_iosch_tdm_arbi_u0_flex_lif0_data_fifo_20x2160_wrapper_u0_flex_tdm_data_fifo_20x2160_wrapper_flex_tdm_data_ram_1r1w_20x2160_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST72_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_lifc_u0_lifc_tx_sch_lifc_tx_sch_buf_lifc_tx_sch_buf_fifo_256x1035_wrapper_u0_lifc_tx_sch_buf_ram_1r1w_256x1035_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST155_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_ivoq_fxsch_ivoq_qmu_fxsch_ivoq_dat_queue_pro_dnif_tx_voq_dat_ram_1r1w_1280x2088_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST78_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_ivoq_fxsch_ivoq_qmu_fxsch_ivoq_dat_queue_pro_dnif_tx_voq_dat_ram_1r1w_1280x2088_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST82_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_rce_24_ch_1_u0_falcon_top_v1_u0_pcs_top_v1_u0_pcs.pcs_v1_gate_tessent_mbist_pcs_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_s_mmu_u0.s_mmu_wr_u0_s_mmu_wr_port_u1_s_mmu_wr_deli_u0_s_wr_fwft_fifo_256x284_wrapper_u0_s_wr_fifo_256x284_wrapper_s_wr_ram_1r1w_256x284_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_s_mmu_gate_tessent_mbist_sys_clk_MBIST1_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u1_st_rd_ram_1r1w_1024x2050_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST3_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST7_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST11_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_management_u0_mmu_pk_rd_split_top_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST25_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_management_u0_mmu_pk_rd_split_top_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST40_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u1_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST46_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST54_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST58_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u0_st_rd_ram_1r1w_1024x2050_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST62_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_management_u0_mmu_pk_rd_split_top_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST82_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_wr_pack_u0.st_mmu_wr_u0_st_mmu_wr_buf_u0_st_mmu_wr_pack_gate_tessent_mbist_sys_clk_MBIST3_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_wr_pack_u0.st_mmu_wr_u0_st_mmu_wr_management_u0_st_mmu_wr_data_ctrl_u1_st_wr_ram_1r1w_1024x2084_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_wr_pack_gate_tessent_mbist_sys_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_wr_pack_u0.st_mmu_wr_u0_st_mmu_wr_management_u0_st_mmu_wr_data_ctrl_u0_st_wr_ram_1r1w_1024x2084_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_wr_pack_gate_tessent_mbist_sys_clk_MBIST51_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_isu_u0.isu_block_u1_isu_para_ram_1r1w_2048x107_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_isu_gate_tessent_mbist_sys_clk_MBIST5_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_odma_u0.oam_u0_oam_pktrx_txsch_u0_odma_gate_tessent_mbist_sys_clk_MBIST4_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_odma_u0.odma_oam_sch_u0_odma_gate_tessent_mbist_sys_clk_MBIST23_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_odma_u0.oam_u0_odma_gate_tessent_mbist_sys_clk_MBIST77_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_odma_u0.odma_block_u1_odma_slice_mng_u0_odma_dat_tail_ram_u0_odma_dat_tail_ram_1r1w_156x2048_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_odma_gate_tessent_mbist_sys_clk_MBIST83_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pbu_ifb_ram_bank_u2_pkt_recv_gate_tessent_mbist_sys_clk_MBIST6_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_pbu_flow_ctrl_u0_pbu_idma_fc_gen_u0_pbu_fc_idmath_ram_u0_pbu_idmath_ram_2rw_141x176_wrapper_u0_ues_gmem_2rw_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST34_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_ifb_ram_access_u0_pbu_ifb_ram_bank_u1_pkt_buffer_block0_ram_1r1w_4096x1024_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST41_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST66_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u0.cluster_gate_tessent_mbist_me_core_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST96_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u1.cluster_gate_tessent_mbist_me_core_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST88_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u10.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_ram_1w1r_128x145_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u10.cluster_gate_tessent_mbist_me_core_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST66_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u11.cluster_gate_tessent_mbist_me_core_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST96_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u12.cluster_gate_tessent_mbist_me_core_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST88_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u13.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_ram_1w1r_128x145_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u13.cluster_gate_tessent_mbist_me_core_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST66_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u14.cluster_gate_tessent_mbist_me_core_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST96_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u15.cluster_gate_tessent_mbist_me_core_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST88_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u2.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_ram_1w1r_128x145_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u2.cluster_gate_tessent_mbist_me_core_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST66_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u3.cluster_gate_tessent_mbist_me_core_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST96_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u4.cluster_gate_tessent_mbist_me_core_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST88_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u5.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_ram_1w1r_128x145_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u5.cluster_gate_tessent_mbist_me_core_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST66_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u6.cluster_gate_tessent_mbist_me_core_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST96_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u7.cluster_gate_tessent_mbist_me_core_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST88_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u8.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_ram_1w1r_128x145_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u8.cluster_gate_tessent_mbist_me_core_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST66_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u9.cluster_gate_tessent_mbist_me_core_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST96_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_storage_sa_asm_gate_tessent_mbist_sys_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_storage_ram_1w1r_6kx2048_u3_ram_1r1w_3072x2064_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST55_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_datacell_ch_u0_cgs_datacell_buf_u0_cgs_dc_buf_data_ram_1w1r_384x2074_rxsw_ram_1r1w_384x2064_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_xsw_gate_tessent_mbist_sys_clk_MBIST10_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_txsw_sa_ip_txsw_u0_crp_ctrl_ch_u0_ptal_process_top_u0_ptal_process_u0_ram_1wr_65536x10_txsw_ram_1rw_65536x10_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_sa_xsw_gate_tessent_mbist_sys_clk_MBIST40_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_alg_top_u0_alg_altro_inst.alg_inst_alg_hash_cmp_inst2_alg_root_cmp_inst_hash_root_info_fifo_inst_hash_root_info_ram_1r1w_1024x546_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_alg_altro_gate_tessent_mbist_alg_clk_MBIST5_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_alg_top_u0_alg_altro_inst.alg_inst_alg_hash_cmp_inst3_alg_root_cmp_inst_hash_root_info_fifo_inst_hash_root_info_ram_1r1w_1024x546_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_alg_altro_gate_tessent_mbist_alg_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_alg_top_u0_alg_altro_inst.alg_inst_alg_hash_cmp_inst0_alg_chain_cmp_inst_chash_kinfo_fifo_inst_chash_kinfo_fifo_1024x401_wrapper_chash_kinfo_ram_1r1w_1024x401_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_alg_altro_gate_tessent_mbist_alg_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.smmu1_rschd_inst_se_smmu1_gate_tessent_mbist_sys_clk_MBIST70_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.smmu1_rschd_inst_smmu1_rschd_dma_ram_inst_ues_gmem_1r1w_1clk_mem_wrapper_gmem_se_smmu1_gate_tessent_mbist_sys_clk_MBIST74_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.se_smmu1_gate_tessent_mbist_sys_clk_MBIST105_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u0.zx222016_1024x640_tcam_u1_etcam_egroup_v0_gate_tessent_mbist_sys_clk_MBIST4_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u0.zx222016_1024x640_tcam_u3_etcam_egroup_v0_gate_tessent_mbist_sys_clk_MBIST8_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u1.zx222016_1024x640_tcam_u1_etcam_egroup_v1_gate_tessent_mbist_sys_clk_MBIST4_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u1.zx222016_1024x640_tcam_u3_etcam_egroup_v1_gate_tessent_mbist_sys_clk_MBIST8_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u2.zx222016_1024x640_tcam_u3_etcam_egroup_h_gate_tessent_mbist_sys_clk_MBIST4_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u2.zx222016_1024x640_tcam_u1_etcam_egroup_h_gate_tessent_mbist_sys_clk_MBIST8_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u3.zx222016_1024x640_tcam_u3_etcam_egroup_h_gate_tessent_mbist_sys_clk_MBIST4_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u3.zx222016_1024x640_tcam_u1_etcam_egroup_h_gate_tessent_mbist_sys_clk_MBIST8_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x135_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST16_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x128_wrapper_u8_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST24_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x128_wrapper_u11_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST28_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x128_wrapper_u12_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x128_wrapper_u14_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST60_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_cfg_se_ram_1rw_524288x4_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_mid_fq_link_ram_1r1w_98304x36_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST24_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_gate_tessent_mbist_sys_clk_MBIST30_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_weight_ram_1rw_65536x14_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST36_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_htptr_dci_ram_1r1w_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST63_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_map_ram_1r1w_65536x21_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_mid_ptr_ram_1r1w_32768x36_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST85_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_spi_mid_wfqfq_link_ram_1r1w_524288x19_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST91_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_htptr_dci_ram_1r1w_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST104_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_htptr_dci_ram_1r1w_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST108_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_mid_wfq_link_ram_1r1w_229376x36_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST112_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_htptr_dci_ram_1r1w_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST116_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_up_down_ptr_ram_1r1w_524288x12_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST140_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_up_down_ptr_ram_1r1w_524288x12_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST144_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_up_down_ptr_ram_1r1w_524288x12_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST148_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_up_down_ptr_ram_1r1w_524288x12_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST152_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_htptr_dci_ram_1r1w_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST156_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_up_down_ptr_ram_1r1w_131072x36_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST160_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u0.qmu_qlist_u0_qlist_em_u0_qmu_em_pd_enq_pre_fwft_fifo_512x87_wrapper_u0_qmu_em_pd_enq_pre_fifo_512x87_wrapper_qmu_em_pd_enq_pre_ram_1r1w_512x87_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_u1.qmu_qlist_u0_qlist_em_u0_qmu_em_pd_enq_pre_fwft_fifo_512x87_wrapper_u0_qmu_em_pd_enq_pre_fifo_512x87_wrapper_qmu_em_pd_enq_pre_ram_1r1w_512x87_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_gate_tessent_mbist_qmu_sys_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST30_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST34_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_tm_others_u0.olif_u0_olif_module_u0_ie_pkt_order_u0_tmolif_emem_data_fifo_256x2067_wrapper_u0_tmolif_emem_data_fifo_256x2048_wrapper_u0_tmolif_emem_data_ram_1r1w_256x2048_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_tm_others_gate_tessent_mbist_sys_clk_MBIST1_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tmmu_module_u0_tmmu_core_u0_tmmu_wr_rd_core_u0_tmmu_dma_data_fifo_wrapper_u0_tmmu_dma_data_fifo_512x2048_wrapper_u0_tmmu_dma_data_ram_1r1w_512x2048_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_tm_others_gate_tessent_mbist_sys_clk_MBIST23_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                    } // End r2
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_P1_bp_r3) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_P1_r3) {
                MemoryBist {
                run_mode : hw_default;
                reduced_address_count : off;
                

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_fxsch_iosch_fxsch_buffer_odma0_fxsch_buffer_odma_queue_u0_fxsch_ipro_buf_odma_ram_1r1w_384x2160_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_fxsch_iosch_fxsch_buffer_odma1_fxsch_buffer_odma1_queue_u0_fxsch_ipro_buf_odma_ram_1r1w_384x2160_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_fxsch_iosch_tdm_arbi_u0_flex_lif0_data_fifo_20x2160_wrapper_u0_flex_tdm_data_fifo_20x2160_wrapper_flex_tdm_data_ram_1r1w_20x2160_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST73_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_lifc_u0_lifc_tx_sch_lifc_tx_sch_buf_lifc_tx_sch_buf_fifo_256x1035_wrapper_u1_lifc_tx_sch_buf_ram_1r1w_256x1035_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST156_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_ivoq_fxsch_ivoq_qmu_fxsch_ivoq_dat_queue_pro_dnif_tx_voq_dat_ram_1r1w_1280x2088_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_rce_24_ch_1_u0_falcon_top_v1_u0_pcs_top_v1_u0_pcs.pcs2_tx_pcs_tx_phyvoq_u0_pcs_tx_phyvoq_qmu_u0_pcs_tx_phyvoq_dat_queue_pro_u0_pcs_tx_phyvoq_dat_ram_1r1w_512x608_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pcs_v1_gate_tessent_mbist_pcs_clk_MBIST48_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u1_st_rd_ram_1r1w_1024x2050_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST4_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST8_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST12_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_management_u0_mmu_pk_rd_split_top_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_management_u0_mmu_pk_rd_split_top_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST41_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST55_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST59_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u0_st_rd_ram_1r1w_1024x2050_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST63_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_management_u0_mmu_pk_rd_split_top_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST83_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_wr_pack_u0.st_mmu_wr_u0_st_mmu_wr_buf_u0_st_wr_fifo_256x2058_wrapper_u1_st_wr_ram_1r1w_256x2058_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_wr_pack_gate_tessent_mbist_sys_clk_MBIST4_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_wr_pack_u0.st_mmu_wr_u0_st_mmu_wr_management_u0_st_mmu_wr_data_ctrl_u1_st_wr_ram_1r1w_1024x2084_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_wr_pack_gate_tessent_mbist_sys_clk_MBIST48_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_wr_pack_u0.st_mmu_wr_u0_st_mmu_wr_management_u0_st_mmu_wr_data_ctrl_u0_st_wr_ram_1r1w_1024x2084_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_wr_pack_gate_tessent_mbist_sys_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_isu_u0.isu_block_u1_isu_qmu_u0_isu_tptr_ram_1r1w_13344x11_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_isu_gate_tessent_mbist_sys_clk_MBIST8_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_odma_u0.oam_u0_oam_timing_u0_odma_gate_tessent_mbist_sys_clk_MBIST6_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_odma_u0.odma_block_u0_odma_slice_mng_u0_odma_dat_tail_ram_u0_odma_dat_tail_ram_1r1w_156x2048_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_odma_gate_tessent_mbist_sys_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_odma_u0.odma_block_u1_odma_slice_mng_u0_odma_dat_tail_ram_u0_odma_dat_tail_ram_1r1w_156x2048_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_odma_gate_tessent_mbist_sys_clk_MBIST65_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_odma_u0.oam_u0_oam_tx_prepro_u0_oam_pkt_fwft_fifo_512x256_wrapper_u0_oam_pkt_fifo_512x256_wrapper_oam_pkt_ram_1r1w_512x256_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_odma_gate_tessent_mbist_sys_clk_MBIST78_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_ifb_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST3_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_pbu_flow_ctrl_u0_pbu_idma_fc_gen_u0_pbu_fc_idmath_ram_u0_pbu_idmath_ram_2rw_141x176_wrapper_u0_ues_gmem_2rw_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST14_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_ifb_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST63_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_pktrx_u0.pktrx_gmem_tcam_u0_tcm0_tcam0_width_ygm_0__xgm_0__tcam0_pktrx_gate_tessent_mbist_sys_clk_MBIST5_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_pktrx_u0.pktrx_gmem_tcam_u0_tcm1_tcam0_width_ygm_0__xgm_0__tcam0_tcamsel_tc64x64_pbce_inst_pktrx_gate_tessent_mbist_sys_clk_MBIST28_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u0.cluster_gate_tessent_mbist_me_core_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u0.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST88_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u1.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_ram_1w1r_128x145_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u1.cluster_gate_tessent_mbist_me_core_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u1.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST66_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u10.cluster_gate_tessent_mbist_me_core_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u10.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST96_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u11.cluster_gate_tessent_mbist_me_core_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u11.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST88_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u12.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_ram_1w1r_128x145_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u12.cluster_gate_tessent_mbist_me_core_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u12.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST66_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u13.cluster_gate_tessent_mbist_me_core_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u13.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST96_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u14.cluster_gate_tessent_mbist_me_core_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u14.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST88_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u15.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_ram_1w1r_128x145_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u15.cluster_gate_tessent_mbist_me_core_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u15.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST66_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u2.cluster_gate_tessent_mbist_me_core_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u2.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST96_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u3.cluster_gate_tessent_mbist_me_core_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u3.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST88_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u4.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_ram_1w1r_128x145_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u4.cluster_gate_tessent_mbist_me_core_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u4.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST66_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u5.cluster_gate_tessent_mbist_me_core_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u5.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST96_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u6.cluster_gate_tessent_mbist_me_core_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u6.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST88_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u7.cluster_mex_u0_rsp_handle_u0_srh1_rsp_handle_u0_ppu_srh1_rsp_ram_1w1r_128x145_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST18_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u7.cluster_gate_tessent_mbist_me_core_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u1_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST47_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u1_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u2_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u7.me_group_u3_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_ppu_me_rf_ram_1r1w_320x64_wrapper_u1_ues_gmem_1r1w_1clk_mem_wrapper_gmem_cluster_gate_tessent_mbist_me_core_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u0_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u1_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u2_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST66_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u8.cluster_gate_tessent_mbist_me_core_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u8.me_group_u3_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST96_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u0_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u0_me_u3_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST43_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u1_me_u2_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST57_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u9.cluster_gate_tessent_mbist_me_core_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.cluster_u9.me_group_u3_me_u1_me_mc_u0_me_context_u0_me_rf_u0_me_rfram_generic_u0_me_rf_ram_u0_me_rf_1w2r_320x64_wrapper_u0_cluster_gate_tessent_mbist_me_core_clk_MBIST88_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_ecgavd_asm_ecgavd_que_man_sa_ip_asm_ecgavd_th_ram_1w1r_4kx16_ram_1r1w_4096x15_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST16_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_storage_sa_asm_gate_tessent_mbist_sys_clk_MBIST48_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_storage_ram_1w1r_6kx2048_u1_ram_1r1w_3072x2064_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_datacell_ch_u0_cgs_datacell_buf_u0_cgs_dc_buf_tdm_ram_1w1r_384x2074_rxsw_ram_1r1w_384x2064_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_xsw_gate_tessent_mbist_sys_clk_MBIST13_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_alg_top_u0_alg_altro_inst.alg_inst_alg_hash_cmp_inst0_alg_root_cmp_inst_hash_int_rsp_fifo_inst_hash_int_rsp_ram_1r1w_1024x258_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_alg_altro_gate_tessent_mbist_alg_clk_MBIST1_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_alg_top_u0_alg_altro_inst.alg_inst_alg_hash_cmp_inst1_alg_chain_cmp_inst_chash_kinfo_fifo_inst_chash_kinfo_fifo_1024x401_wrapper_chash_kinfo_ram_1r1w_1024x401_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_alg_altro_gate_tessent_mbist_alg_clk_MBIST12_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_alg_top_u0_alg_altro_inst.alg_inst_alg_hash_cmp_inst3_alg_root_cmp_inst_hash_int_rsp_fifo_inst_hash_int_rsp_ram_1r1w_1024x258_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_alg_altro_gate_tessent_mbist_alg_clk_MBIST27_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_alg_top_u0_alg_altro_inst.alg_inst_alg_hash_cmp_inst0_alg_root_cmp_inst_hash_root_info_fifo_inst_hash_root_info_ram_1r1w_1024x546_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_alg_altro_gate_tessent_mbist_alg_clk_MBIST44_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.smmu1_rschd_inst_se_smmu1_gate_tessent_mbist_sys_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.se_smmu1_gate_tessent_mbist_sys_clk_MBIST75_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u0.zx222016_1024x640_tcam_u0_etcam_egroup_v0_gate_tessent_mbist_sys_clk_MBIST1_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u0.zx222016_1024x640_tcam_u2_etcam_egroup_v0_gate_tessent_mbist_sys_clk_MBIST5_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u1.zx222016_1024x640_tcam_u0_etcam_egroup_v1_gate_tessent_mbist_sys_clk_MBIST1_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u1.zx222016_1024x640_tcam_u2_etcam_egroup_v1_gate_tessent_mbist_sys_clk_MBIST5_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u2.zx222016_1024x640_tcam_u0_etcam_egroup_h_gate_tessent_mbist_sys_clk_MBIST1_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u2.zx222016_1024x640_tcam_u2_etcam_egroup_h_gate_tessent_mbist_sys_clk_MBIST5_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u3.zx222016_1024x640_tcam_u0_etcam_egroup_h_gate_tessent_mbist_sys_clk_MBIST1_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u3.zx222016_1024x640_tcam_u2_etcam_egroup_h_gate_tessent_mbist_sys_clk_MBIST5_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x128_wrapper_u11_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x128_wrapper_u8_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST25_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x128_wrapper_u13_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST53_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x128_wrapper_u15_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST61_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_cfg_se_ram_1rw_524288x4_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_mid_fq_link_ram_1r1w_98304x36_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST25_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_gate_tessent_mbist_sys_clk_MBIST31_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_mid_wfq_que_cnt_stat_ram_1r1w_32768x14_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_htptr_dci_ram_1r1w_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST64_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_sch_ram_1r1w_16384x17_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST78_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_htptr_dci_ram_1r1w_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST105_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_htptr_dci_ram_1r1w_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST109_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_htptr_dci_ram_1r1w_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST113_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_htptr_dci_ram_1r1w_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST132_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_up_down_ptr_ram_1r1w_524288x12_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST141_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_up_down_ptr_ram_1r1w_524288x12_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST145_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_up_down_ptr_ram_1r1w_524288x12_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST149_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_up_down_ptr_ram_1r1w_524288x12_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST153_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_htptr_dci_ram_1r1w_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST157_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_up_down_ptr_ram_1r1w_131072x36_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST161_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_eop_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST25_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_eop_ram_u0_qmu_chk_eop_ram_2r1w_32768x16_wrapper_u1_ues_gmem_2r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST27_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_eop_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST29_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_eop_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST31_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_eop_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST33_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_eop_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST35_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_eop_ram_u0_qmu_chk_eop_ram_2r1w_32768x16_wrapper_u6_ues_gmem_2r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST37_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qsch_crs_renew_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST68_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qsch_crs_send_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST71_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_pkt_age_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST155_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_pkt_age_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST157_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST23_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST31_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tm_others_gate_tessent_mbist_sys_clk_MBIST24_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                    } // End r3
                } // End TestStep
            } //End Pattern
                
        Patterns(MemoryBist_P1_bp_r4) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_P1_r4) {
                MemoryBist {
                run_mode : hw_default;
                reduced_address_count : off;
                

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_fxsch_iosch_fxsch_buffer_odma0_fxsch_buffer_odma_queue_u0_fxsch_ipro_buf_odma_ram_1r1w_384x2160_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST21_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_fxsch_iosch_fxsch_buffer_odma1_fxsch_buffer_odma1_queue_u0_fxsch_ipro_buf_odma_ram_1r1w_384x2160_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST27_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_lifc_u0_lifc_tx_sch_lifc_tx_sch_buf_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST153_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_ipro_crm_top_u0.fxsch_ipro_u0_lifc_u0_lifc_tx_sch_lifc_tx_sch_buf_lifc_tx_sch_buf_fifo_256x1035_wrapper_u1_lifc_tx_sch_buf_ram_1r1w_256x1035_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_ipro_crm_top_gate_tessent_mbist_lif_sys_clk_MBIST157_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_ivoq_fxsch_ivoq_qmu_fxsch_ivoq_dat_queue_pro_dnif_tx_voq_dat_ram_1r1w_1280x2088_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST76_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_fxsch_u0_fxsch_opro_top_u0.fxsch_opro_fxsch_ivoq_fxsch_ivoq_qmu_fxsch_ivoq_dat_queue_pro_dnif_tx_voq_dat_ram_1r1w_1280x2088_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_fxsch_opro_top_gate_tessent_mbist_lif_sys_clk_MBIST80_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_lifcc_u0.cfg_cfg_pcie_top_cfg_pcie_dma_mac_up_cfg_pcie_afifo_256x512_wrapper_u0_cfg_pcie_ram_1r1w_256x512_wrapper_ues_gmem_1r1w_2clk_mem_wrapper_gmem_lifcc_gate_tessent_mbist_sys_clk_MBIST4_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_lif_u0_rce_24_ch_u0_falcon_top_v0_u0_pcs_top_v0_u0_pcs.pcs0_tx_pcs_tx_phyvoq_u0_pcs_tx_phyvoq_qmu_u0_pcs_tx_phyvoq_dat_queue_pro_u0_pcs_tx_phyvoq_dat_ram_1r1w_512x608_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pcs_v0_gate_tessent_mbist_pcs_clk_MBIST19_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_s_mmu_u0.s_mmu_wr_u0_s_mmu_wr_port_u0_s_mmu_wr_deli_u0_s_wr_fwft_fifo_256x284_wrapper_u0_s_wr_fifo_256x284_wrapper_s_wr_ram_1r1w_256x284_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_s_mmu_gate_tessent_mbist_sys_clk_MBIST5_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u1_st_rd_ram_1r1w_1024x2050_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST1_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u1_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST5_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST9_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_management_u0_mmu_pk_rd_split_top_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST23_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST36_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_management_u0_mmu_pk_rd_split_top_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST42_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST52_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u1_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST56_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_data_in_u0_st_mmu_rd_pk_share_u0_st_rd_ram_1r1w_1024x2050_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST60_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_rd_pack_u0.st_mmu_rd_u0_st_mmu_rd_management_u0_mmu_pk_rd_split_top_u0_st_mmu_rd_pack_gate_tessent_mbist_sys_clk_MBIST76_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_wr_pack_u0.st_mmu_wr_u0_st_mmu_wr_buf_u0_st_mmu_wr_pack_gate_tessent_mbist_sys_clk_MBIST1_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_wr_pack_u0.st_mmu_wr_u0_st_mmu_wr_management_u0_st_mmu_wr_data_ctrl_u1_st_wr_ram_1r1w_1024x2084_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_wr_pack_gate_tessent_mbist_sys_clk_MBIST45_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_wr_pack_u0.st_mmu_wr_u0_st_mmu_wr_management_u0_st_mmu_wr_data_ctrl_u0_st_wr_ram_1r1w_1024x2084_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_st_mmu_wr_pack_gate_tessent_mbist_sys_clk_MBIST49_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_mmu_u0_st_mmu_u0_st_mmu_wr_pack_u0.st_mmu_wr_u0_st_mmu_wr_management_u0_st_mmu_wr_pack_gate_tessent_mbist_sys_clk_MBIST53_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_odma_u0.oam_u0_oam_2544_u0_oam_2544_pkt_ram_access_u0_oam_2544_pkt_ram_1rw_2500x512_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_odma_gate_tessent_mbist_sys_clk_MBIST1_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_odma_u0.oam_u0_oam_chk_int_u0_odma_gate_tessent_mbist_sys_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_odma_u0.oam_u0_odma_gate_tessent_mbist_sys_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST4_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_pktrx_u0.pkt_parser_u0_hdu1_u0_icu_tcam_tbl_u0_tcm_tcam0_width_ygm_0__xgm_0__tcam0_pktrx_gate_tessent_mbist_sys_clk_MBIST2_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_nppu_u0_pktrx_u0.pkt_parser_u1_hdu1_u0_icu_tcam_tbl_u0_tcm_tcam0_width_ygm_0__xgm_0__tcam0_tcamsel_tc128x121_pbce_inst_pktrx_gate_tessent_mbist_sys_clk_MBIST27_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.ppu_mf_in_group_u0_ppu_mf_in_schedule_u0_ppu_gate_tessent_mbist_sys_clk_MBIST35_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_ppu_u0.ppu_reorder_group_u0_ppu_gate_tessent_mbist_sys_clk_MBIST60_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_phm_sa_asm_gate_tessent_mbist_sys_clk_MBIST39_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_storage_ram_1w1r_1kx2048_u4_ram_1r1w_1024x2064_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST44_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_asm_u0.sa_ip_asm_u0_asm_epu_asm_sm_asm_sm_storage_ram_1w1r_6kx2048_u0_ram_1r1w_3072x2064_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_asm_gate_tessent_mbist_sys_clk_MBIST49_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_datacell_ch_u0_cgs_datacell_buf_u0_cgs_dc_buf_data_ram_1w1r_384x2074_rxsw_ram_1r1w_384x2064_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_xsw_gate_tessent_mbist_sys_clk_MBIST8_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_sa_u0_sa_xsw_u0.sa_rxsw_rxsw_u0_cgs_u0_cgs_datacell_ch_u0_cgs_datacell_buf_u0_cgs_dc_buf_tdm_ram_1w1r_384x2074_rxsw_ram_1r1w_384x2064_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_sa_xsw_gate_tessent_mbist_sys_clk_MBIST14_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_alg_top_u0_alg_altro_inst.alg_inst_alg_hash_cmp_inst2_alg_chain_cmp_inst_chash_kinfo_fifo_inst_chash_kinfo_fifo_1024x401_wrapper_chash_kinfo_ram_1r1w_1024x401_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_alg_altro_gate_tessent_mbist_alg_clk_MBIST2_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_alg_top_u0_alg_altro_inst.alg_inst_alg_hash_cmp_inst1_alg_root_cmp_inst_hash_int_rsp_fifo_inst_hash_int_rsp_ram_1r1w_1024x258_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_alg_altro_gate_tessent_mbist_alg_clk_MBIST13_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_alg_top_u0_alg_altro_inst.alg_inst_alg_hash_cmp_inst3_alg_chain_cmp_inst_chash_kinfo_fifo_inst_chash_kinfo_fifo_1024x401_wrapper_chash_kinfo_ram_1r1w_1024x401_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_alg_altro_gate_tessent_mbist_alg_clk_MBIST28_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_schd_other_u0.se_other_u0_se_schd_other_gate_tessent_mbist_sys_clk_MBIST48_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.smmu1_rschd_inst_se_smmu1_gate_tessent_mbist_sys_clk_MBIST72_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_ex_u0_se_smmu1_u0.se_smmu1_gate_tessent_mbist_sys_clk_MBIST92_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u0.zx222016_1024x640_tcam_u0_etcam_egroup_v0_gate_tessent_mbist_sys_clk_MBIST2_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u0.zx222016_1024x640_tcam_u2_etcam_egroup_v0_gate_tessent_mbist_sys_clk_MBIST6_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u1.zx222016_1024x640_tcam_u0_etcam_egroup_v1_gate_tessent_mbist_sys_clk_MBIST2_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u1.zx222016_1024x640_tcam_u2_etcam_egroup_v1_gate_tessent_mbist_sys_clk_MBIST6_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u2.zx222016_1024x640_tcam_u0_etcam_egroup_h_gate_tessent_mbist_sys_clk_MBIST2_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u2.zx222016_1024x640_tcam_u2_etcam_egroup_h_gate_tessent_mbist_sys_clk_MBIST6_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u3.zx222016_1024x640_tcam_u0_etcam_egroup_h_gate_tessent_mbist_sys_clk_MBIST2_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_se_tcam_u0_etcam_egroup_u3.zx222016_1024x640_tcam_u2_etcam_egroup_h_gate_tessent_mbist_sys_clk_MBIST6_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x128_wrapper_u10_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x128_wrapper_u9_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x128_wrapper_u13_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST54_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_se_u0_smmu0_u0.smmu0_ctrl_ram_1rw_32768x128_wrapper_u15_ues_gmem_1rw_1clk_mem_wrapper_gmem_smmu0_gate_tessent_mbist_sys_clk_MBIST62_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_mid_sch_hptr_ram_1r1w_131072x36_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST1_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_cfg_se_ram_1rw_524288x4_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST22_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_cfg_ram_1r1w_65536x25_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_mid_map_ram_1r1w_16384x23_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST68_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_wfq_que_cnt_stat_ram_1r1w_32768x14_u0_crdt_gate_tessent_mbist_sys_clk_MBIST79_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_htptr_dci_ram_1r1w_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST102_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_htptr_dci_ram_1r1w_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST106_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_htptr_dci_ram_1r1w_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST110_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_htptr_dci_ram_1r1w_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST114_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_up_down_ptr_ram_1r1w_524288x12_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST133_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_up_down_ptr_ram_1r1w_524288x12_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST142_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_up_down_ptr_ram_1r1w_524288x12_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST146_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_up_down_ptr_ram_1r1w_524288x12_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST150_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_flow_up_down_ptr_ram_1r1w_524288x12_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST154_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_crdt_u0.ram_manage_u0_crdt_ses_up_down_ptr_ram_1r1w_131072x36_wrapper_u0_crdt_gate_tessent_mbist_sys_clk_MBIST158_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_eop_ram_u0_qmu_chk_eop_ram_2r1w_32768x16_wrapper_u0_ues_gmem_2r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST24_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_eop_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST26_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_eop_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST28_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_eop_ram_u0_qmu_chk_eop_ram_2r1w_32768x16_wrapper_u1_ues_gmem_2r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST30_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_eop_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_eop_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST34_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_eop_ram_u0_qmu_chk_eop_ram_2r1w_32768x16_wrapper_u6_ues_gmem_2r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST36_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem0_u0_qmu_chk_eop_ram_u0_qmu_chk_eop_ram_2r1w_32768x16_wrapper_u7_ues_gmem_2r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST38_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qsch_crs_renew_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST69_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qsch_crs_send_ram_u0_qsch_crs_send_ram_1r1w_8192x8_wrapper_u7_ues_gmem_1r1w_1clk_mem_wrapper_gmem_qmu_top_gate_tessent_mbist_sys_clk_MBIST72_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem1_u0_qsch_crs_send_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST151_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_qmu_top_u0.qmu_share_mem_u0_qmu_share_mem2_u0_qmu_pkt_age_ram_u0_qmu_top_gate_tessent_mbist_sys_clk_MBIST156_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST24_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_shap_u0.shap_share_ram_man_u0_shap_flow_512k_wrapper_u0_shap_gate_tessent_mbist_sys_clk_MBIST32_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
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
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_tm_others_u0.tmmu_u0_tm_others_gate_tessent_mbist_sys_clk_MBIST20_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    

                Controller(u_hcm_tm_u0_tm_others_u0.tm_others_gate_tessent_mbist_sys_clk_MBIST25_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : 20;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                    } // End r4
                } // End TestStep
            } //End Pattern
                