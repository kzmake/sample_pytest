# -*- coding: utf-8 -*-
"""fixtures.

テストコードで使用するセッション開始時のテストフィクスチャ定義

"""

import pytest


@pytest.fixture(scope='session')
def e():
    return 2


@pytest.fixture(scope='session')
def f():
    return 2


@pytest.fixture(scope='session')
def ef(e, f):
    return e * f * 2
