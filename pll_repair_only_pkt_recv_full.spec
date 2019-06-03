
        Patterns(MemoryBist_P1_repair_full) {
            tester_period : 80ns;
            ClockPeriods {
                PCIE_REF_CLK_P : 10ns;
                SYNC_CLK : 8ns;
                PCI_DBG_DTA[9] : 10ns;
            }
            SimulationOptions {
                monitor_internal_clock_pins : off;
            }
            TestStep(Mbist_P1_repair_full) {
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
                        enable_memory_list : m3,m8,m1,m4,m7,m5,m6,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_ifb_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST3_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
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
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_pbu_flow_ctrl_u0_pbu_idma_fc_gen_u0_pbu_fc_idmath_ram_u0_pbu_idmath_ram_2rw_141x176_wrapper_u0_ues_gmem_2rw_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST14_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                        test_time_multiplier : ;
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
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST4_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m7,m9,m4,m10,m6,m3,m5,m8,m2,m1 ;
                        freeze_step : 0;
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
                        enable_memory_list : m8,m4,m5,m2,m10,m9,m3,m6,m1,m7 ;
                        freeze_step : 0;
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
                        enable_memory_list : m4,m2,m6,m3,m1,m5 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_wrback_ctrl_u0_pbu_wb_fwft_fifo_64x2048_wrapper_u0_pbu_wb_fifo_64x2048_wrapper_pbu_wb_ram_1r1w_64x2048_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST10_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_pbu_signal_capture_u0_pbu_capture_ram_1rw_64x2048_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST12_NON_REPAIR_BitSlice_158_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_wrback_ctrl_u0_pbu_wb_fwft_fifo_64x2048_wrapper_u0_pbu_wb_fifo_64x2048_wrapper_pbu_wb_ram_1r1w_64x2048_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST13_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_pbu_signal_capture_u0_pbu_capture_ram_1rw_64x2048_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST15_NON_REPAIR_BitSlice_158_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_pbu_flow_ctrl_u0_pbu_idma_fc_gen_u0_pbu_fc_idmath1_ram_u0_pbu_idmath1_ram_1rw_141x176_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST16_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_wrback_ctrl_u0_pbu_wb_fwft_fifo_64x2048_wrapper_u0_pbu_wb_fifo_64x2048_wrapper_pbu_wb_ram_1r1w_64x2048_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST17_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7,m8,m9 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_pbu_flow_ctrl_u0_pbu_idma_fc_gen_u0_pbu_mc_logic_rsp_fifo_64x35_wrapper_u0_pbu_mc_logic_rsp_ram_1r1w_64x35_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST18_NON_REPAIR_BitSlice_36_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_pbu_flow_ctrl_u0_pbu_idma_fc_gen_u0_pbu_mc_logic_req_fwft_fifo_64x38_wrapper_u0_pbu_mc_logic_req_fifo_64x38_wrapper_pbu_mc_logic_req_ram_1r1w_64x38_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST19_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_pbu_flow_ctrl_u0_pbu_mac_fc_gen_u0_pbu_fc_macth1_ram_u0_pbu_macth1_ram_1rw_96x128_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST20_NON_REPAIR_BitSlice_130_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_wrback_ctrl_u0_pbu_wb_fwft_fifo_64x2048_wrapper_u0_pbu_wb_fifo_64x2048_wrapper_pbu_wb_ram_1r1w_64x2048_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST21_NON_REPAIR_BitSlice_160_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_ptr_mngt_u0_pbu_ppu_recy_fifo_64x26_wrapper_u1_pbu_ppu_recy_ram_1r1w_64x26_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST22_NON_REPAIR_BitSlice_28_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_ptr_mngt_u0_pbu_odma_recy1_fifo_128x23_wrapper_u1_pbu_odma_recy1_ram_1r1w_128x23_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST23_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_pbu_stat_u0_pbu_stat_ind_arb_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST24_NON_REPAIR_BitSlice_32_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
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
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_ifb_u0_pbu_reorder_pkt_ram_1r2w_64x2048_wrapper_u0_ues_gmem_1r2w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST25_NON_REPAIR_BitSlice_63_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_ifb_u0_pbu_reorder_pkt_ram_1r2w_64x2048_wrapper_u0_ues_gmem_1r2w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST26_NON_REPAIR_BitSlice_63_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7,m8,m9,m10 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_ifb_u0_pbu_reorder_pkt_ram_1r2w_64x2048_wrapper_u0_ues_gmem_1r2w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST27_NON_REPAIR_BitSlice_63_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_ifb_u0_pbu_rfd_access_block_u0_pbu_se_key_block_fifo_32x69_wrapper_u0_pbu_se_key_block_ram_1r1w_32x69_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST28_NON_REPAIR_BitSlice_70_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
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
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_ifb_u0_pbu_ifbrd_ppu_fwft_fifo_64x22_wrapper_u0_pbu_ifbrd_ppu_fifo_64x22_wrapper_pbu_ifbrd_ppu_ram_1r1w_64x22_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST30_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_ifb_u0_pbu_ifbrd_odma_fwft_fifo_32x36_wrapper_u0_pbu_ifbrd_odma_fifo_32x36_wrapper_pbu_ifbrd_odma_ram_1r1w_32x36_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST31_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
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
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.idma_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST36_NON_REPAIR_BitSlice_32_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
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
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.idma_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST37_NON_REPAIR_BitSlice_26_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_pbu_flow_ctrl_u0_pbu_mac_fc_gen_u0_pbu_fc_macth_ram_u0_pbu_macth_ram_2rw_96x128_wrapper_u0_ues_gmem_2rw_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST42_NON_REPAIR_BitSlice_130_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_pbu_flow_ctrl_u0_pbu_idma_fc_gen_u0_pbu_fc_idmath1_ram_u0_pbu_idmath1_ram_1rw_141x176_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST43_NON_REPAIR_BitSlice_90_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_pbu_flow_ctrl_u0_pbu_idma_fc_gen_u0_pbu_mc_logic_rsp_fifo_64x35_wrapper_u0_pbu_mc_logic_rsp_ram_1r1w_64x35_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST44_NON_REPAIR_BitSlice_36_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_pbu_flow_ctrl_u0_pbu_mac_fc_gen_u0_pbu_fc_macth1_ram_u0_pbu_macth1_ram_1rw_96x128_wrapper_u0_ues_gmem_1rw_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST45_NON_REPAIR_BitSlice_130_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_pbu_flow_ctrl_u0_pbu_idma_fc_gen_u0_pbu_mc_logic_req_fwft_fifo_64x38_wrapper_u0_pbu_mc_logic_req_fifo_64x38_wrapper_pbu_mc_logic_req_ram_1r1w_64x38_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST46_NON_REPAIR_BitSlice_40_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_ptr_mngt_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST47_NON_REPAIR_BitSlice_16_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
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
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_ptr_mngt_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST48_NON_REPAIR_BitSlice_16_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
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
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_ptr_mngt_u0_pbu_ppu_recy_fifo_64x26_wrapper_u0_pbu_ppu_recy_ram_1r1w_64x26_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST49_NON_REPAIR_BitSlice_28_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_ptr_mngt_u0_pbu_odma_recy1_fifo_128x23_wrapper_u0_pbu_odma_recy1_ram_1r1w_128x23_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST50_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_pbu_stat_u0_pbu_stat_ind_arb_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST51_NON_REPAIR_BitSlice_32_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_pbu_stat_u0_pbu_stat_ind_arb_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST52_NON_REPAIR_BitSlice_32_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_pbu_stat_u0_pbu_stat_ind_arb_u0_pbu_fxsch_fc_cnt_u0_pbu_fc_cnt_ram_1r1w_141x32_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST53_NON_REPAIR_BitSlice_32_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_ptr_mngt_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST54_NON_REPAIR_BitSlice_16_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_pbu_stat_u0_pbu_stat_ind_arb_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST55_NON_REPAIR_BitSlice_32_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2,m3,m4 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_ifb_u0_pbu_reorder_pkt_ram_1r2w_64x2048_wrapper_u0_ues_gmem_1r2w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST56_NON_REPAIR_BitSlice_63_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7,m8,m9 ;
                        freeze_step : 0;
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
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_ifb_u0_pbu_ifbrd_odma_fwft_fifo_32x36_wrapper_u0_pbu_ifbrd_odma_fifo_32x36_wrapper_pbu_ifbrd_odma_ram_1r1w_32x36_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST58_NON_REPAIR_BitSlice_38_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_ifb_u0_pbu_rfd_access_block_u0_pbu_se_key_block_fifo_32x69_wrapper_u0_pbu_se_key_block_ram_1r1w_32x69_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST59_NON_REPAIR_BitSlice_70_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_ifb_u0_pbu_ifbrd_ppu_fwft_fifo_64x22_wrapper_u0_pbu_ifbrd_ppu_fifo_64x22_wrapper_pbu_ifbrd_ppu_ram_1r1w_64x22_wrapper_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST60_NON_REPAIR_BitSlice_24_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_ifb_u0_pbu_reorder_pkt_ram_1r2w_64x2048_wrapper_u0_ues_gmem_1r2w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST61_NON_REPAIR_BitSlice_63_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_ifb_u0_pbu_reorder_pkt_ram_1r2w_64x2048_wrapper_u0_ues_gmem_1r2w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST62_NON_REPAIR_BitSlice_63_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_pbu_flow_ctrl_u0_pbu_mac_fc_gen_u0_pbu_fc_macth_ram_u0_pbu_macth_ram_2rw_96x128_wrapper_u0_ues_gmem_2rw_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST64_NON_REPAIR_BitSlice_130_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u1_pbu_stat_u0_pbu_stat_ind_arb_u0_pbu_fxsch_fc_cnt_u0_pbu_fc_cnt_ram_1r1w_141x32_wrapper_u0_ues_gmem_1r1w_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST65_NON_REPAIR_BitSlice_32_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_ptr_mngt_u0_pkt_recv_gate_tessent_mbist_sys_clk_MBIST66_NON_REPAIR_BitSlice_12_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
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
                    
                Controller(u_hcm_nppu_u0_pkt_recv_u0.pbu_u0_pbu_block_u0_pbu_flow_ctrl_u0_pbu_idma_fc_gen_u0_pbu_fc_idmath_ram_u0_pbu_idmath_ram_2rw_141x176_wrapper_u0_ues_gmem_2rw_1clk_mem_wrapper_gmem_pkt_recv_gate_tessent_mbist_sys_clk_MBIST34_REPAIR_BISR_controller_inst) {
                    AdvancedOptions {
                        test_time_multiplier : ;
                        enable_memory_list : m1,m2 ;
                        freeze_step : 0;
                    }
                    RepairOptions {
                        check_repair_status : off ;
                    }
                    DiagnosisOptions {
                        compare_go : on;
                        compare_go_id : on;
                    }
                }
                    
                    } // End full
                } // End TestStep
            } //End Pattern
                
//End