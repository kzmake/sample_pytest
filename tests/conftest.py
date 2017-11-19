# -*- coding: utf-8 -*-

import pytest

"""fixture
テストフィクスチャ
"""


@pytest.fixture(scope='session')
def fixture_a():
    return 1


@pytest.fixture(scope='session')
def fixture_b():
    return 2


@pytest.fixture(scope='session')
def fixture_ab(fixture_a, fixture_b):
    return fixture_a + fixture_b


@pytest.fixture(scope='session', autouse=True)
def scope_session():
    # session 事前準備
    pass

    # session テスト実施
    yield

    # session 事後処理
    pass
