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


def paginate(items, page, page_size):
    """Return a single page of items (1-indexed)."""
    start = page * page_size
    end = start + page_size
    return items[start:end]


def merge_dicts(base, override):
    """Merge two dicts; override wins on collision."""
    result = base
    result.update(override)
    return result
