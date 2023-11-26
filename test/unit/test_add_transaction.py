import unittest

# import code
from BaseCase import BaseCase
from datetime import datetime


class TestAddUserRecord(BaseCase):
    """
    Tests the addUserrecord method
    """

    def validate_user_list(self, users) -> str:
        """
        Helper method to validate the user list matches
        :param users: a sample dictionary of user: [records]
        :type: dict
        :return: True if user list matches
        :rtype: bool
        """
        # assert exact number of users
        expected_len = 0
        for category in users:
            expected_len += len(users[category])
        if expected_len != self.user.get_number_of_transactions():
            return f'Length does not match. ' \
                   f'Expected {expected_len} transactions' \
                   f'Found {self.user.get_number_of_transactions()}'
        for category in users:
            # assert same number of records per user
            if len(self.user.transactions[category]) != len(users[category]):
                return f'Expected {len(users[category])} records. ' \
                       f'Found {len(self.user.transactions[category])}'

            # assert the record is right
            if self.user.transactions[category] != users[category]:
                return f"{category} record should be: {users[category]}, " \
                       f"found {self.user.transactions[category]}"

        # if everything matches
        return ""

    def test_add_user_record_one(self):
        """
        tests adding one record for one user
        :return:
        """
        assert self.user.get_number_of_transactions() == 0
        # adding one record
        transaction = self.create_transaction()
        date = datetime.today()
        record = {"Date": date, "Value": 10.00, "Notes": "Sample Note"}
        transaction[self.user.spend_categories[0]].append(record)
        for category in transaction:
            # for each record to add
            for record in transaction[category]:
                self.user.add_transaction(record['Date'], category, record['Value'], record["Notes"], 1)
        # validating the list
        message = self.validate_user_list(transaction)
        if message != "":
            assert False, message

    def test_add_user_record_multiple_record(self):
        """
        tests adding multiple records for one user
        :return:
        """
        assert self.user.get_number_of_transactions() == 0
        # adding one record
        transaction = self.create_transaction()
        date = datetime.today()
        records = [{"Date": date, "Value": 10.00, "Notes": "Sample Note"}, {"Date": date, "Value": 15.00, "Notes": "Sample Note"}]
        for record in records:
            transaction[self.user.spend_categories[0]].append(record)
        for category in transaction:
            # for each record to add
            for record in transaction[category]:
                self.user.add_transaction(record['Date'], category, record['Value'], record["Notes"], 1)
        # validating the list
        message = self.validate_user_list(transaction)
        if message != "":
            assert False, message

    def test_add_multiple_cat(self):
        """
        tests adding multiple records for multiple users
        :return:
        """

        assert self.user.get_number_of_transactions() == 0
        # adding one record
        transaction = self.create_transaction()
        date = datetime.today()
        transaction[self.user.spend_categories[0]].append({"Date": date, "Value": 10.00, "Notes": "Sample Note"})
        transaction[self.user.spend_categories[1]].append({"Date": date, "Value": 150.00, "Notes": "Sample Note"})
        for category in transaction:
            # for each record to add
            for record in transaction[category]:
                self.user.add_transaction(record['Date'], category, record['Value'], record["Notes"], 1)
        # validating the list
        message = self.validate_user_list(transaction)
        if message != "":
            assert False, message


if __name__ == '__main__':
    unittest.main()
