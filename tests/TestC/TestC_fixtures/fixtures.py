# -*- coding: utf-8 -*-
"""fixtures.

テストコードで使用するセッション開始時のテストフィクスチャ定義

"""

import pytest


@pytest.fixture(scope='session')
def e():
    return 1


@pytest.fixture(scope='session')
def f():
    return 1


@pytest.fixture(scope='session')
def ef(e, f):
    return e + f
