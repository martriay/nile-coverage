"""Coverage command definition."""

import logging

import click

from nile_coverage import __name__

__author__ = "Eric Nordelo"
__copyright__ = "Eric Nordelo"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


@click.command()
def coverage():
    """Generate coverage report for Cairo Smart Contracts."""
    _logger.info("Generating coverage report")
    _logger.info("Report generated")