# -*- coding: utf-8 -*-
"""scopes.

テストコードで使用するスコープ毎の共通処理

"""

import pytest


@pytest.fixture(scope='session', autouse=True)
def scope_session():
    # session 事前準備
    pass

    # session 実施
    yield

    # session 事後処理
    pass


@pytest.fixture(scope='class', autouse=True)
def scope_class():
    # class 事前処理
    pass

    # class 実施
    yield

    # class 事後処理
    pass


@pytest.fixture(scope='function', autouse=True)
def scope_function(scope_class):
    # function 事前処理
    pass

    # function 実施
    yield

    # function 事後処理
    pass
