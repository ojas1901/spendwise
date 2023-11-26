"""
Tests add command
"""
import time
import unittest
import sys

sys.path.append(r"C:\\Users\\manid\\Desktop\\SE_Project\\spendwise")
print(sys.path)
from src import bot, util
from bot_utils import BotTest


class TestAdd(BotTest):
    """
    Test file for add
    """

    def test_add_wrong_expense_cat(self):
        """
        Tests the add command with an invalid category
        """
        msg = self.create_text_message('/add')
        self.bot.process_new_messages([msg])
        time.sleep(3)

        # assert the message was sent, and text was not changed
        assert msg.chat.id is not None
        assert msg.text == '/add'
        # there should be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 0, \
            "For the /add command, there should be a next step"
        # there should not be any exceptions
        assert self.bot.worker_pool.exception_info is None

        # send the calendar date
        query = self.create_callback_query("2023,10,15", msg)
        self.bot.process_new_callback_query([query])
        time.sleep(3)

        # assert the query was sent
        assert query.chat_instance.id is not None
        # there should be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 1, \
            "For the /add command after date, there should not be a next step"
        # there should not be any exceptions
        assert self.bot.worker_pool.exception_info is None

        # send the category we use
        reply = self.create_text_message(self.user.spend_categories[0])
        self.bot.process_new_messages([reply])
        time.sleep(3)
        # assert the message was sent, and text was not changed
        assert reply.chat.id is not None
        assert reply.text == self.user.spend_categories[0]
        # there should be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 1, \
            "For the reply to add, there should not be a next step"
        # there should not be any exceptions
        assert self.bot.worker_pool.exception_info is None

        # send the category we use
        reply = self.create_text_message("INVALID")
        self.bot.process_new_messages([reply])
        time.sleep(3)
        # assert the message was sent, and text was not changed
        assert reply.chat.id is not None
        assert reply.text == "INVALID"
        # there should be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 0, \
            "For the reply to add with wrong cat, there should not be a next step"
        # there should not be any exceptions
        assert self.bot.worker_pool.exception_info is None

        # send the amount
        reply = self.create_text_message("1.00")
        self.bot.process_new_messages([reply])
        time.sleep(3)
        # assert the message was sent, and text was not changed
        assert reply.chat.id is not None
        assert reply.text == "1.00"
        # there should be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 0, \
            "For the reply to add, there should not be a next step"
        # there should not be any exceptions
        assert self.bot.worker_pool.exception_info is None

        # there should not be any records added
        assert bot.user_list[str(msg.chat.id)].get_number_of_transactions() == 0

    def test_add_wrong_date(self):
        """
        Tests the add command with an invalid value
        """
        msg = self.create_text_message('/add')
        self.bot.process_new_messages([msg])
        time.sleep(3)

        # assert the message was sent, and text was not changed
        assert msg.chat.id is not None
        assert msg.text == '/add'
        # there should be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 0, \
            "For the /add command, there should be a next step"
        # there should not be any exceptions
        assert self.bot.worker_pool.exception_info is None

        # send the calendar date
        query = self.create_callback_query("prev", msg)
        self.bot.process_new_callback_query([query])
        time.sleep(3)

        # assert the query was sent
        assert query.chat_instance.id is not None
        # there should be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 0, \
            "For the /add command after date, there should not be a next step"
        # there should not be any exceptions
        assert self.bot.worker_pool.exception_info is None

        # send the calendar date
        query = self.create_callback_query("", msg)
        self.bot.process_new_callback_query([query])
        time.sleep(3)

        # assert the query was sent
        assert query.chat_instance.id is not None
        # there should be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 0, \
            "For the /add command after date, there should not be a next step"
        # there should not be any exceptions
        assert self.bot.worker_pool.exception_info is None

        # there should not be any records added
        assert bot.user_list[str(msg.chat.id)].get_number_of_transactions() == 0

    def test_add_wrong_cat(self):
        """
        Tests the add command with an invalid category
        """
        msg = self.create_text_message('/add')
        self.bot.process_new_messages([msg])
        time.sleep(3)

        # assert the message was sent, and text was not changed
        assert msg.chat.id is not None
        assert msg.text == '/add'
        # there should be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 0, \
            "For the /add command, there should be a next step"
        # there should not be any exceptions
        assert self.bot.worker_pool.exception_info is None

        # send the calendar date
        query = self.create_callback_query("2023,10,18", msg)
        self.bot.process_new_callback_query([query])
        time.sleep(3)

        # assert the query was sent
        assert query.chat_instance.id is not None
        # there should be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 1, \
            "For the /add command after date, there should not be a next step"
        # there should not be any exceptions
        assert self.bot.worker_pool.exception_info is None

        # send the category we use
        reply = self.create_text_message("INVALID")
        self.bot.process_new_messages([reply])
        time.sleep(3)
        # assert the message was sent, and text was not changed
        assert reply.chat.id is not None
        assert reply.text == "INVALID"
        # there should be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 0, \
            "For the reply to add with wrong cat, there should not be a next step"
        # there should not be any exceptions
        assert self.bot.worker_pool.exception_info is None

        # there should not be any records added
        assert bot.user_list[str(msg.chat.id)].get_number_of_transactions() == 0

    def test_add_wrong_num(self):
        """
        Tests the add command with an invalid value
        """
        msg = self.create_text_message('/add')
        self.bot.process_new_messages([msg])
        time.sleep(3)

        # assert the message was sent, and text was not changed
        assert msg.chat.id is not None
        assert msg.text == '/add'
        # there should be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 0, \
            "For the /add command, there should be a next step"
        # there should not be any exceptions
        assert self.bot.worker_pool.exception_info is None

        # send the calendar date
        query = self.create_callback_query("2023,10,13", msg)
        self.bot.process_new_callback_query([query])
        time.sleep(3)

        # assert the query was sent
        assert query.chat_instance.id is not None
        # there should be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 1, \
            "For the /add command after date, there should be a next step"
        # there should not be any exceptions
        assert self.bot.worker_pool.exception_info is None

        # send the category we use
        reply = self.create_text_message(self.user.spend_categories[0])
        self.bot.process_new_messages([reply])
        time.sleep(3)
        # assert the message was sent, and text was not changed
        assert reply.chat.id is not None
        assert reply.text == self.user.spend_categories[0]
        # there should be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 1, \
            "For the reply to add, there should not be a next step"
        # there should not be any exceptions
        assert self.bot.worker_pool.exception_info is None

        # send the amount we use
        reply = self.create_text_message("-1")
        self.bot.process_new_messages([reply])
        time.sleep(3)
        # assert the message was sent, and text was not changed
        assert reply.chat.id is not None
        assert reply.text == "-1"
        # there should be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 0, \
            "For the reply to add, there should not be a next step"
        # there should not be any exceptions
        assert self.bot.worker_pool.exception_info is None

        # there should not be any records added
        assert bot.user_list[str(msg.chat.id)].get_number_of_transactions() == 0


if __name__ == '__main__':
    unittest.main()
