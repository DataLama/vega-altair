"""Visualize the multiple line-chart with vega-altair."""
from typing import List
import pandas as pd
import altair as alt

def plot_hcc_line(
    df:pd.DataFrame,
    xcol:str,
    ycols:List[str],
    catecol:str
):
    """Plot Horizontal Concatenated Chart with line chart.
    
    Args:
        df: pivoted dataframe.
        xcol: column name for xaxis
        ycols: list of column name for yaxis
        catecol: nominal column witch discrete the lines by color.
    """
    dmin = round(df.loc[:,ycols].values.min() - 0.01, 2)
    dmax = round(df.loc[:,ycols].values.max() + 0.01, 2)
    y_scale = alt.Scale(domainMin=dmin, domainMax=dmax)
    sub_df = df.loc[:,[catecol, xcol, *ycols]]
    
    chart = alt.Chart(sub_df).mark_line().encode(
        alt.X(alt.repeat("row"), type='quantitative'),
        alt.Y(alt.repeat("column"), type='quantitative', scale=y_scale),
        color=f"{catecol}:N"
    ).properties(
        width=200,
        height=200
    ).repeat(
        row=[xcol],
        column=ycols
    )
    return chart