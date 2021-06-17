import click
import emoji

from tssimp.generators import sine


@click.command(context_settings=dict(max_content_width=120))
@click.option(
    "-s",
    "--start",
    default=0,
    help="When does the time series start",
    show_default=True,
)
@click.option(
    "-e",
    "--end",
    default=60,
    help="When does the time series end",
    show_default=True,
)
@click.option(
    "-f",
    "--frequency",
    default="1s",
    help="Time series period",
    show_default=True,
)
@click.option(
    "-p",
    "--period",
    default=1,
    help="Time series period",
    show_default=True,
)
@click.version_option()
def cli(
    start,
    end,
    period,
    frequency,
):
    """
    Product Variability Canary
    """
    print(emoji.emojize("Time Series Simp :pleading_face:"))
    s = sine(start=start, end=end, period=period, freq=frequency)
    s.plot()
