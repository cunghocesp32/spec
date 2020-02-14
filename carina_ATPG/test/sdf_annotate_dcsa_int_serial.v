module sdf_annotate ();
  initial 
  `ifdef SDFMAX
   $sdf_annotate ("../sdf/BLOCK.scan_setup_wc50_125_typical.sdf.gz", BLOCK_pat_dcsa_edt_int_serial_sample_v_ctl.BLOCK_inst, ,"sdf_BLOCK_dcsa_int_serial_max.log", "maximum");

  `elsif SDFMIN
   $sdf_annotate ("../sdf/BLOCK.scan_hold_bc68_125_typical.sdf.gz",  BLOCK_pat_dcsa_edt_int_serial_sample_v_ctl.BLOCK_inst, ,"sdf_BLOCK_dcsa_int_serial_min.log", "minimum");

  `endif
endmodule