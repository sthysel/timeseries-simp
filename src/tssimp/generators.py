import math

import numpy as np
import pandas as pd

from .time_series import TimeSeries


def affine(
    start,
    end,
    freq,
    start_y,
    end_y,
):
    index = pd.date_range(start=start, end=end, freq=freq)
    return TimeSeries(index=index, y=np.linspace(start_y, end_y, len(index)))


def constant(
    start,
    end,
    freq,
    value,
):
    return affine(start, end, freq, value, value)


def cosine(
    start,
    end,
    freq,
    amp=1,
    period=1,
):
    index = pd.date_range(start=start, end=end, freq=freq)
    return TimeSeries(
        index=index,
        y=amp * np.cos(np.linspace(0, math.tau * period, num=len(index))),
    )


def sine(
    start,
    end,
    freq,
    period=1,
):
    index = pd.date_range(start=start, end=end, freq=freq)
    return TimeSeries(
        index=index,
        y=np.sin(np.linspace(0, math.tau * period, num=len(index))),
    )
