# coding: utf-8

"""
    Hopsworks api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.1.0-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.message_service_api import MessageServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMessageServiceApi(unittest.TestCase):
    """MessageServiceApi unit test stubs"""

    def setUp(self):
        self.api = api.message_service_api.MessageServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_count_unread_messages_by_user(self):
        """Test case for count_unread_messages_by_user

        """
        pass

    def test_delete_message(self):
        """Test case for delete_message

        """
        pass

    def test_empty_trash(self):
        """Test case for empty_trash

        """
        pass

    def test_get_all_deleted_messages_by_user(self):
        """Test case for get_all_deleted_messages_by_user

        """
        pass

    def test_get_all_messages_by_user(self):
        """Test case for get_all_messages_by_user

        """
        pass

    def test_mark_as_read(self):
        """Test case for mark_as_read

        """
        pass

    def test_move_to_trash(self):
        """Test case for move_to_trash

        """
        pass

    def test_reply(self):
        """Test case for reply

        """
        pass

    def test_restore_from_trash(self):
        """Test case for restore_from_trash

        """
        pass


if __name__ == '__main__':
    unittest.main()
