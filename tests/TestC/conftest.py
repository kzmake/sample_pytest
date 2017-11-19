# -*- coding: utf-8 -*-
"""bootstrap.

テストコードで使用するモジュールの共通処理

"""

import pytest


def pytest_report_header(config):
    """ テストレポートヘッダ
    """
    return "サンプル テストC"


@pytest.fixture(scope='session')
def e():
    return 1


@pytest.fixture(scope='session')
def f():
    return 1


@pytest.fixture(scope='session')
def ef(e, f):
    return e + f
