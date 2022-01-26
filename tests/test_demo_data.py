import pandas as pd
from pandas.testing import assert_frame_equal
import pytest

import drugz as dz


@pytest.fixture
def demo_truth():
    return pd.read_csv("./tests/demo_results.csv", index_col=0)


def test_demo_data(demo_truth):
    class Args:
        infile = "./tests/sgRNA_count.txt"
        drugz_output_file = "/dev/null"
        fc_outfile = "/dev/null"
        control_samples = "T15_A_control,T15_B_control,T15_C_control"
        drug_samples = "T15_A_olaparib,T15_B_olaparib,T15_C_olaparib"
        remove_genes = "LacZ,luciferase,EGFR"
        unpaired = False
        pseudocount = 5
        half_window_size = 5

    result = dz.drugZ_analysis(Args())
    assert_frame_equal(result, demo_truth)
