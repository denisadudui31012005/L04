import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_check_admin():
    assert check_admin("admin123") == True
    assert check_admin("wrongpassword") == False
