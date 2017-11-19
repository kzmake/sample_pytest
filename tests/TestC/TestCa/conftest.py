# -*- coding: utf-8 -*-
"""bootstrap.

テストコードで使用するモジュールの共通処理

"""

import pytest


def pytest_report_header(config):
    """ テストレポートヘッダ
    """
    return "サンプル テストCa"

