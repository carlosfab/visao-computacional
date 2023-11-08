"""Tests for unit functionalities."""

import os
import sys
from pathlib import Path

import pytest


def test_python_version():
    assert sys.version.startswith('3.11.3'), 'A versão do Python não é 3.11.3'
