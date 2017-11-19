# -*- coding: utf-8 -*-
"""bootstrap.

テストコードで使用するモジュールの共通処理

"""

import pytest


def pytest_report_header(config):
    """ テストレポートヘッダ
    """
    return "サンプル テストB"

@pytest.fixture(scope='session')
def c():
    return 2


@pytest.fixture(scope='session')
def d():
    return 4


@pytest.fixture(scope='session')
def cd(c, d):
    return c + d

