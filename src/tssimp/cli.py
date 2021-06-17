import click
import emoji
from loguru import logger


@click.command(context_settings=dict(max_content_width=120))
@click.option(
    "--aws-profile",
    help="AWS Profile",
    default="bhp_pv_np",
)
@click.option(
    "-v",
    "--verbosity",
    default=0,
    count=True,
    help="Log verbosity",
    show_default=True,
)
@click.version_option()
def cli():
    """
    Product Variability Canary
    """
    logger.info(emoji.emojize(":baby_chick: Product Variability data canary"))
