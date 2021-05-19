import math

import numpy as np
import pandas as pd

from Helpers import *


def generate_output(payload_sizes, MCS_df):
    """Generate empty DF based on payload sizes and MCSs"""
    df = pd.DataFrame(index=payload_sizes, columns=MCS_df['MCS'])
    return df

def get_transmission_time(size, Rm, Rc):
    """Get the transmission time, given the size and MCS."""
    payload_size = get_payload_size( size, Rm, Rc )
    time_ns = (PREAMBLE_LEN + HEADER_LEN + payload_size) / SYMBOL_RATE_GHZ
    return time_ns


MCS_df = get_relevant_MCS_df()

output_df = generate_output( [*range(int(MAX_MPDU_OCTETS/1000-1))], MCS_df )

for output_index, _ in output_df.iterrows():

    size = (output_index + 1) * 1000

    for _, MCS_row in MCS_df.iterrows():

        (Rm, Rc) = (MCS_row['Modulation_rate'], MCS_row['Code_rate'])
        tmp = get_transmission_time( size, Rm, Rc )
        output_df.at[output_index, MCS_row['MCS']] = tmp

output_df.to_csv('Single-mpdu.csv')
