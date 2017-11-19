# -*- coding: utf-8 -*-
"""bootstrap.

テストコードで使用するモジュールの共通処理

"""

import pytest


def pytest_report_header(config):
    """ テストレポートヘッダ
    """
    return "サンプル テストCb"

@pytest.fixture(scope='session')
def e():
    return 2


@pytest.fixture(scope='session')
def f():
    return 2


@pytest.fixture(scope='session')
def ef(e, f):
    return e * f

