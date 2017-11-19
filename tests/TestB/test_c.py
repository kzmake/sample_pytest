# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope='function', autouse=True)
def scope_function(scope_class):
    # function 事前処理
    pass

    # function 実施
    yield 6

    # function 事後処理
    pass


class TestA(object):
    def test_1(self, scope_function):
        a = 2
        b = 4
        assert a + b == scope_function

    def test_2(self, c, d, cd):
        assert c + d == cd

    @pytest.mark.parametrize(['x', 'y', 'ans'], [
        (1, 1, 4),
        (2, 2, 6),
        (3, 3, 8),
    ])
    def test_3(self, x, y, ans, c):
        assert x + y + c == ans
