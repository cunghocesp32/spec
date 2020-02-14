module sdf_annotate ();
  initial
  `ifdef SDFMAX
   $sdf_annotate ("../sdf/BLOCK.scan_setup_wc50_125_typical.sdf.gz", BLOCK_pat_tdf_los_edt_int_parallel_all_v_ctl.BLOCK_inst, ,"sdf_BLOCK_tdf_los_int_parallel_max.log", "maximum");

  `elsif SDFMIN
   $sdf_annotate ("../sdf/BLOCK.scan_hold_bc68_125_typical.sdf.gz",  BLOCK_pat_tdf_los_edt_int_parallel_all_v_ctl.BLOCK_inst, ,"sdf_BLOCK_tdf_los_int_parallel_min.log", "minimum");

  `endif
endmodule