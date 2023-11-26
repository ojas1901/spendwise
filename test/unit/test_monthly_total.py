"""
Tests the monthly_total_method
"""
import unittest

from BaseCase import BaseCase
from datetime import datetime


class TestMonthlyTotal(BaseCase):
    """
    Unit test for monthly total
    """

    def test_one_transaction(self):
        """
        Given one transaction, we expect total to be the value of that transaction
        """
        date = datetime.today()
        value = 12.00
        transaction = self.create_transaction()
        date = datetime.today()
        record = {"Date": date, "Value": value, "Notes": "note"}
        transaction[self.user.spend_categories[0]].append(record)
        for category in transaction:
            # for each record to add
            for record in transaction[category]:
                self.user.add_transaction(record['Date'], category, record['Value'], record['Notes'], 1)
        assert self.user.monthly_total() == value

    def test_multiple_transaction_same_cat(self):
        """
        Given multiple transactions of same category, we expect total to be the sum of all the transactions
        """
        date = datetime.today()
        value = [12.00, 11.00]
        transaction = self.create_transaction()
        date = datetime.today()
        records = [{"Date": date, "Value": value[0], "Notes": "note"},
                   {"Date": date, "Value": value[1], "Notes": "note"}]
        for record in records:
            transaction[self.user.spend_categories[0]].append(record)
        for category in transaction:
            # for each record to add
            for record in transaction[category]:
                self.user.add_transaction(record['Date'], category, record['Value'], record['Notes'], 1)
        assert self.user.monthly_total() == sum(value)

    def test_multiple_transaction_multiple_cat(self):
        """
        Given multiple transactions of different categories, we expect total to be the sum of all the transactions
        """
        date = datetime.today()
        value = [12.00, 11.00, 21.50, 14.25]
        transaction = self.create_transaction()
        date = datetime.today()
        transaction[self.user.spend_categories[0]].append({"Date": date, "Value": value[0], "Notes": "note"})
        transaction[self.user.spend_categories[0]].append({"Date": date, "Value": value[1], "Notes": "note"})
        transaction[self.user.spend_categories[1]].append({"Date": date, "Value": value[2], "Notes": "note"})
        transaction[self.user.spend_categories[1]].append({"Date": date, "Value": value[3], "Notes": "note"})
        for category in transaction:
            # for each record to add
            for record in transaction[category]:
                self.user.add_transaction(record['Date'], category, record['Value'], record['Notes'], 1)
        assert self.user.monthly_total() == sum(value)


if __name__ == '__main__':
    unittest.main()
