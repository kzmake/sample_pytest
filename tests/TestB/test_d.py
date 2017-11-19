# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope='function', autouse=True)
def scope_function(scope_class):
    # function 事前処理
    pass

    # function 実施
    yield 7

    # function 事後処理
    pass


class TestB(object):
    def test_1(self, scope_function):
        a = 2
        b = 4
        assert a + b == scope_function

    def test_2(self, c, d, cd):
        assert c + d == cd + 1
