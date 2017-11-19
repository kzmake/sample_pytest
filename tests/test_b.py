# -*- coding: utf-8 -*-

import pytest
import time
from parameterized import parameterized


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
    yield 4

    # function 事後処理
    pass


class TestB(object):
    def test_1(self):
        a = 1
        b = 2
        assert a == b

    def test_2(self, scope_function):
        a = 1
        b = 2
        assert a + b == scope_function

    def test_3(self, fixture_a, fixture_b, fixture_ab):
        assert fixture_a + fixture_b == fixture_ab + 1

    def test_4(self):
        time.sleep(10)
        assert True

    @parameterized([
        (2, 3, 4),
        (1, 1, 3),
        (3, -1, 2),
    ])
    def test_5(self, a, b, ans):
        assert a + b == ans
