# encoding=utf-8
class Calculator():
    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):

        try:
            return a / b
        except:
            return "Dividend can not be zero"


calc = Calculator()


# 等价类划分：正数，负数，零#
# ------------输入正数-------------#


def test_addPositive():
    result1 = calc.add(3, 4)
    assert result1 == 7


def test_minusPositive():
    result2 = calc.minus(4, 3)
    assert result2 == 1


def test_mulPositive():
    result3 = calc.mul(4, 4)
    assert result3 == 16


def test_divPositive():
    result4 = calc.div(3, 3)
    assert result4 == 1


# ------------输入负数-------------#

def test_addNegative():
    result1 = calc.add(-3, -4)
    assert result1 == -7


def test_minusNegative():
    result2 = calc.minus(-4, -3)
    assert result2 == -1


def test_mulNegative():
    result3 = calc.mul(-4, -4)
    assert result3 == 16


def test_divNegative():
    result4 = calc.div(-3, -3)
    assert result4 == 1


# ------------输入零-------------#
def test_addZero():
    result1 = calc.add(0, 0)
    assert result1 == 0


def test_minusZero():
    result2 = calc.minus(0, 0)
    assert result2 == 0


def test_mulZero():
    result3 = calc.mul(0, 0)
    assert result3 == 0


def test_divZero():
    result4 = calc.div(0, 0)
    assert result4 == 'Dividend can not be zero'
