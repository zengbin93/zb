# -*- coding: utf-8 -*-

import pandas as pd


def count_nans(df):
    """
    Count the total number of NaNs in every column

    Parameters
    --------------------
        df    pd.DataFrame

    Returns
    --------------------
        nas_df    pd.DataFrame

    """
    cols = df.columns
    res = []
    for col in cols:
        length = len(df[col])
        not_nas = len(df[col].dropna())
        nas = length - not_nas
        rate = round(nas/length, 4)
        # add unique value
        uv = len(df[col].unique())
        res_ = (col, nas, not_nas, rate, uv)
        res.append(res_)
    nas_df = pd.DataFrame(res, columns=['Column', 'NaNs', 'Not_NaNs',
                                        'Rate', 'UV'])
    return nas_df

