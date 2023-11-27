"""
Tests income command
"""
import time
import unittest
from src import bot
from bot_utils import BotTest


class Testincome(BotTest):
    """
    Test file for income
    """

    def test_income_command(self):
        """
        Tests the income command
        """
        msg = self.create_text_message('/income')
        self.bot.process_new_messages([msg])
        time.sleep(3)

        # assert the message was sent, and text was not changed
        assert msg.chat.id is not None
        assert msg.text == '/income'
        # there should be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 1, \
            "For the /income command, there should be a next step"
        # there should not be any exceptions
        # assert self.bot.worker_pool.exception_info is None

        # send the income amount
        reply = self.create_text_message("150.00")
        self.bot.process_new_messages([reply])
        time.sleep(3)
        # assert the message was sent, and text was not changed
        assert reply.chat.id is not None
        assert reply.text == "150.00"
        # there should not be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 0, \
            "For the reply to income, there should not be a next step"
        # there should not be any exceptions
        assert self.bot.worker_pool.exception_info is None

        # assert the income was added to the user
        chat_id = str(reply.chat.id)
        assert chat_id in bot.user_list
        user_income = bot.user_list[chat_id].monthly_income
        assert user_income == 120.00

    def test_income_command_invalid(self):
        """
        Tests the income command for invalid income
        """
        msg = self.create_text_message('/income')
        self.bot.process_new_messages([msg])
        time.sleep(3)

        # assert the message was sent, and text was not changed
        assert msg.chat.id is not None
        assert msg.text == '/income'
        # there should be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 1, \
            "For the /income command, there should be a next step"
        # there should not be any exceptions
        # assert self.bot.worker_pool.exception_info is None

        # send the income amount
        reply = self.create_text_message("-19.00")
        self.bot.process_new_messages([reply])
        time.sleep(3)
        # assert the message was sent, and text was not changed
        assert reply.chat.id is not None
        assert reply.text == "-19.00"
        # there should not be a next step handler
        assert len(self.bot.next_step_backend.handlers) == 0, \
            "For the reply to income, there should not be a next step"
        # # there should not be any exceptions
        # assert self.bot.worker_pool.exception_info is None

        # assert the income was not changed for the user
        chat_id = str(reply.chat.id)
        assert chat_id in bot.user_list
        user_income = bot.user_list[chat_id].monthly_income
        assert user_income != -19.00
