import os,re, time
import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
sdf_template = templateEnv.get_template("sdf_annotate.v_template")
system_f_template = templateEnv.get_template("system.f_template")
inter_i_template = templateEnv.get_template("inter.i_template")
run_sim_template = templateEnv.get_template("run_sim.template")
def get_netlist(block, pd_csv):
    ''' This def will get the lasted netlist of block from csv file 
               1. This csv file must be imported from pandas
               2. The column of netlist must be *netlist* 
               3. This def will return netlist path'''
    netlist = pd_csv.loc[block, "netlist"] + "/" + block + ".sv"
    # Check file exist & file size 
    if os.path.exists(netlist) and os.path.getsize(netlist) > 0:
        return netlist
    else :
        print("{} does not exist".format(netlist))
        
def get_tsdb(block, pd_csv):
    ''' This def will get the lasted tsdb of block from csv file 
               1. This csv file must be imported from pandas
               2. The column of netlist must be *tsdb* 
               3. This def will return tuple (dft_mb, outData_mb)'''
    return (pd_csv.loc[block, "tsdb"] + "/dft_mb", pd_csv.loc[block, "tsdb"] + "/outData_mb")

def get_refer_atpg(block, pd_csv):
    ''' This def will get the lasted reference script of block from csv file 
               1. This csv file must be imported from pandas
               2. The column of netlist must be *atpg_ref* 
               3. This def will return tuple (dft_mb, outData_mb)'''
    return pd_csv.loc[block, "atpg_ref"]

def gen_sdf_file(dir_name, block, pat, mode):
    ''' This def generate all sdf format file :
            sdf_annotate '''
    # Generating sdf_annotate.v
    sdf_file_name = dir_name + "/sdf_annotate_" + pat + "_" + mode + ".v"
    print("Generating : {}".format(sdf_file_name))
    with open(sdf_file_name, "w") as f:
        f.write(sdf_template.render(block=block, pat=pat, mode=mode))
    
    #  Generating system.f
    system_file_name = dir_name + "/system_" + pat + "_" + mode + ".f"
    print("Generating : {}".format(system_file_name))
    with open( system_file_name, "w") as f:
        f.write(system_f_template.render(block=block, pat=pat, mode=mode))
    
    #  Generating inter.i
    inter_i_name = dir_name + "/inter_" + pat + "_" + mode + ".i"
    print("Generating : {}".format(inter_i_name))
    with open( inter_i_name, "w") as f:
        f.write(inter_i_template.render(block=block, pat=pat, mode=mode))
    
    # Generating run_sim_sdf
    run_sim_file_name = dir_name + "/run_sim_" + pat + "_" + mode
    print("Generating : {}".format(run_sim_file_name))
    with open( run_sim_file_name, "w") as f:
        f.write(run_sim_template.render(block=block, pat=pat, mode=mode))

class DFT_REVIEW_ATPG():
    def __init__(self,block, log_file):
        '''447055 scan cells have been identified in 1497 scan chains.'''
        self.start_time = time.time()
        # For scan chain
        self.scan_cells = 0
        self.scan_chains = 0
        self.longest_chain = 0
        # For ATPG
        self.test_coverage = 0
        self.test_pattern = 0
        self.test_atpg_time = 0
        # For clock 
        self.clock_list = {}

        self.chain_identified = re.compile(r"(?P<scan_cells>\d+) scan cells have been identified in (?P<scan_chains>\d+) scan chains.")
        self.longest_chain_length = re.compile(r"Longest scan chain has (?P<longes_scan_lenght>\d+) scan cells.")
        self.test_coverage_re = re.compile(r"test_coverage\s+([\d.%]+)")
        self.test_pattern_re = re.compile(r"#test_patterns\s+(?P<test_pattern>\d+)")
        self.test_atpg_time_re = re.compile(r"CPU_time \(secs\)\s+(?P<cpu_time>[\d.]+)")
        self.clock_domain_re = re.compile(r"command: add_clocks [01] (?P<clock_name>[\S]+)  -period (?P<clock_period>[\d.]+)")
        print("Processing logfile : {}".format(log_file))
        with open(log_file, "r") as f:
            for line in f:
                if  self.chain_identified.search(line):
                    self.scan_cells = int(self.chain_identified.search(line).group("scan_cells"))
                    self.scan_chains = int(self.chain_identified.search(line).group("scan_chains"))
                
                if  self.longest_chain_length.search(line):
                    self.longest_chain = int(self.longest_chain_length.search(line).group("longes_scan_lenght"))
                
                if self.test_coverage_re.search(line):
                    _tc = re.findall(r'[\d.]+', line)
                    self.test_coverage = float(_tc[-1])
                
                if self.test_pattern_re.search(line):
                    self.test_pattern = int(self.test_pattern_re.search(line).group("test_pattern"))
                
                if self.test_atpg_time_re.search(line):
                    self.test_atpg_time = float(self.test_atpg_time_re.search(line).group("cpu_time"))
                
                if self.clock_domain_re.search(line):
                    _cd = self.clock_domain_re.search(line)
                    self.clock_list[_cd.group("clock_name")] = float(_cd.group("clock_period"))

        print("Script done after {} sec ".format(time.time()-self.start_time))
    def get_scan_cells(self):
        return self.scan_cells
    
    def get_scan_chain(self):
        return self.scan_chains

    def get_longest_chain_length(self):
        return self.longest_chain

    def get_test_coverage(self):
        return self.test_coverage
    
    def get_test_pattern(self):
        return self.test_pattern

    def get_test_aptg_time(self):
        return self.test_atpg_time

    def get_clock_domain(self):
        return self.clock_list

def test_review_scan_chain():
    test_loc_int = DFT_REVIEW_ATPG("test","log.atpg_tdf_loc_edt.int")
    assert test_loc_int.get_scan_cells() == 106283
    assert test_loc_int.get_scan_chain() == 360
    assert test_loc_int.get_longest_chain_length() == 302
    assert test_loc_int.get_test_coverage() == 70.28
    assert test_loc_int.get_test_pattern() == 8312
    assert test_loc_int.get_test_aptg_time() == 3129.9
    assert test_loc_int.get_clock_domain()["i_clock"] == 5

    test_los_int = DFT_REVIEW_ATPG("test","log.atpg_tdf_los_edt.int")
    assert test_los_int.get_scan_cells() == 106283
    assert test_los_int.get_scan_chain() == 360
    assert test_los_int.get_longest_chain_length() == 302
    assert test_los_int.get_test_coverage() == 76.34
    assert test_los_int.get_test_pattern() == 12509
    assert test_los_int.get_test_aptg_time() == 6530.0

    test_dcsa_int = DFT_REVIEW_ATPG("test","log.atpg_dcsa_edt.int")
    assert test_dcsa_int.get_scan_cells() == 106283
    assert test_dcsa_int.get_scan_chain() == 360
    assert test_dcsa_int.get_longest_chain_length() == 302
    assert test_dcsa_int.get_test_coverage() == 99.28
    assert test_dcsa_int.get_test_pattern() == 1634
    assert test_dcsa_int.get_test_aptg_time() == 431.3

    test_dcsa_ext = DFT_REVIEW_ATPG("test","log.atpg_dcsa_edt.ext")
    assert test_dcsa_ext.get_scan_cells() == 6250
    assert test_dcsa_ext.get_scan_chain() == 25
    assert test_dcsa_ext.get_longest_chain_length() == 282
    assert test_dcsa_ext.get_test_coverage() == 78.61
    assert test_dcsa_ext.get_test_pattern() == 55
    assert test_dcsa_ext.get_test_aptg_time() == 148.1

if  __name__ == "__main__":
   gen_sdf_file("test", "BLOCK", "int_serial") 
   gen_sdf_file("test", "BLOCK", "int_parallel")