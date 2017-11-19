# -*- coding: utf-8 -*-
"""bootstrap.

テストコードで使用するモジュールの共通処理

"""

import pytest
from fixtures import *


def pytest_report_header(config):
    """ テストレポートヘッダ
    """
    return "サンプル テスト"
