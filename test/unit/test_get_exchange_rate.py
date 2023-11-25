from BaseCase import BaseCase
import unittest
from src import util


class TestExchangeRate(BaseCase):
    """
    Unit test to check exchange rate
    """

    def test_get_exchange_rate(self):
        """
        Asserts if exchange API is working fine
        """
        assert type(util.real_time_currency_convert("USD", "INR")) == float
        assert util.real_time_currency_convert('USD', 'INR') > 0
