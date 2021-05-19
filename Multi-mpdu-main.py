import math

import numpy as np
import pandas as pd

from Helpers import *


def generate_output(aggregation_count, MCS_df):
    """Generate empty DF based on payload sizes and MCSs"""
    df = pd.DataFrame(index=aggregation_count, columns=MCS_df['MCS'])
    return df

def get_transmission_time(num_of_agg_ppdu, Rm, Rc):
    """Get the transmission time, given the number of aggregated PPDUs and the MCS."""
    agg_payload_and_header_size_single = HEADER_LEN + get_payload_size( MAX_MPDU_OCTETS, Rm, Rc ) - 64 # Add header and throw away final GI
    payload_size_multi = PREAMBLE_LEN + agg_payload_and_header_size_single * num_of_agg_ppdu + 64 # Add preamble and final GI
    time_ns = payload_size_multi / SYMBOL_RATE_GHZ
    return time_ns


MCS_df = get_relevant_MCS_df()

output_df = generate_output( [*range(100)], MCS_df )

for output_index, _ in output_df.iterrows():

    aggregated_ppdus = output_index + 1

    for _, MCS_row in MCS_df.iterrows():

        (Rm, Rc) = (MCS_row['Modulation_rate'], MCS_row['Code_rate'])
        tmp = get_transmission_time( aggregated_ppdus, Rm, Rc )
        output_df.at[output_index, MCS_row['MCS']] = tmp

output_df.to_csv('Multi-mpdu.csv')
