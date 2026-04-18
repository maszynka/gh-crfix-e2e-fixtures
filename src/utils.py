"""Utility functions."""

import os
import json


def load_config(path):
    """Load configuration from a JSON file."""
    with open(path, "r") as f:
        return json.load(f)


def format_name(first_name, last_name):
    """Format a full name."""
    return f"{first_name} {last_name}"


def calculate_total(prices):
    """Calculate total from a list of prices."""
    return sum(prices)


def clamp(value, min_val, max_val):
    """Clamp value to [min_val, max_val]."""
    return max(min_val, min(max_val, value))
