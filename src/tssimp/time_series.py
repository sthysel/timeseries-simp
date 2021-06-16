import numpy as np
import pandas as pd


class TimeSeries:
    def __init__(
        self,
        index: pd.DatetimeUndex,
        y,
    ):
        if not isinstance(index, pd.DatetimeIndex):
            raise TypeError("index should be a pandas.DatetimeIndex")

        self.index = index
        self.y = np.array(y)
        if len(index) != len(y):
            raise ValueError("index and y's shapes do not match")

    def __len__(self):
        return len(self.index)

    def __str__(self):
        return str(self.to_frame())

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, TimeSeries):
            return False

        return (self.index == other.index).all() and (self.y == other.y).all()

    def __add__(self, other):
        if (
            (not isinstance(other, TimeSeries))
            and (not isinstance(other, int))
            and (not isinstance(other, float))
        ):
            raise TypeError("Wrong values")
        if isinstance(other, TimeSeries) and not (self.index == other.index).all():
            raise ValueError("Indexes do not match")

        if isinstance(other, TimeSeries):
            return TimeSeries(index=self.index, y=(self.y + other.y))

        return TimeSeries(index=self.index, y=(self.y + other))

    def to_frame(self):
        return pd.DataFrame({"y": self.y}, index=self.index)

    def plot(self):
        self.to_frame().y.plot()

    def __sub__(self, other):
        if isinstance(other, TimeSeries):
            negative_other = TimeSeries(index=self.index, y=(-1 * other.y))
        else:
            negative_other = -1 * other

        return self + negative_other
