# -*- coding: utf-8 -*-
"""bootstrap.

テストコードで使用するモジュールの共通処理

"""

import pytest

import sys
import os
sys.path.append(os.path.dirname(__file__))
from TestCb_fixtures import *


def pytest_report_header(config):
    """ テストレポートヘッダ
    """
    return "サンプル テストCa"

