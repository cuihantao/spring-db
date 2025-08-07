from __future__ import annotations

import importlib.metadata

import spring_db as m


def test_version():
    assert importlib.metadata.version("spring_db") == m.__version__
