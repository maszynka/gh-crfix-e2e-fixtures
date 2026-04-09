"""Utility functions."""

import os
import sys
import json


def load_config(path):
    """Load configuration from a JSON file."""
    with open(path, "r") as f:
        return json.load(f)


def format_name(frist_name, last_name):
    """Format a full name."""
    return f"{frist_name} {last_name}"


def calculate_total(prices):
    """Calculate total from a list of prices."""
    return sum(prices)
