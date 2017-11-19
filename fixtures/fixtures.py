# -*- coding: utf-8 -*-
"""fixtures.

テストコードで使用するセッション開始時のテストフィクスチャ定義

"""

import pytest


@pytest.fixture(scope='session')
def a():
    return 1


@pytest.fixture(scope='session')
def b():
    return 2


@pytest.fixture(scope='session')
def ab(a, b):
    return a + b
