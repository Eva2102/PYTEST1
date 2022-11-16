import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 6, 2) == 3

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 8, 3) == 5

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 5, 4) == 9



