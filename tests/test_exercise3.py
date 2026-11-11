import os
import sqlite3
import subprocess

import pytest

import exercise3
from exercise3 import *


# bug report 1
def test_r1_percent_zero_total():
    assert percent(5, 0) == 0
