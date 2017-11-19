# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope='class', autouse=True)
def scope_class():
    # class 事前処理
    pass

    # class 実施
    yield "必要であれば値を渡せる"

    # class 事後処理
    pass


@pytest.fixture(scope='function', autouse=True)
def scope_function(scope_class):
    # function 事前処理
    pass

    # function 実施
    yield 3

    # function 事後処理
    pass


class TestA(object):
    def test_1(self):
        a = 1
        b = 1
        assert a == b

    def test_2(self, scope_function):
        a = 1
        b = 2
        assert a + b == scope_function

    def test_3(self, a, b, ab):
        assert a + b == ab

    @pytest.mark.parametrize(['x', 'y', 'ans'], [
        (1, 1, 3),
        (2, 2, 5),
        (3, 3, 7),
    ])
    def test_4(self, x, y, ans, a):
        assert x + y + a == ans
