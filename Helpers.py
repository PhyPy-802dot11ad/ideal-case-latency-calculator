import math

import pandas as pd


PREAMBLE_LEN = 3328
HEADER_LEN = 1024
SYMBOL_RATE_GHZ = 1.76
MAX_MPDU_OCTETS = 262_143
N_CBPB = [448, 896, 1792, 2688]

def get_payload_size(MPDU_length_bytes, modulation_rate, code_rate):

    N_cw = MPDU_length_bytes * 8 / (672 * code_rate)
    N_data_pad = N_cw * 672 * code_rate - MPDU_length_bytes * 8

    N_cbpb = N_CBPB[ int(modulation_rate/2) ]
    N_blks = math.ceil( N_cw * 672 / N_cbpb )
    N_blk_pad = N_blks * N_cbpb - N_cw * 672

    payload_size_symbols = N_blks * 512 + 64

    return payload_size_symbols


def get_relevant_MCS_df():
    df = pd.read_csv('MCS_table.csv')
    df = df.drop( df.index[df['Repetition'] != 1] )
    df = df.drop( df.index[df['Code_rate'] == 0.8125] )
    return df
