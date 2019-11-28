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
from api.api_key_resource_api import ApiKeyResourceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestApiKeyResourceApi(unittest.TestCase):
    """ApiKeyResourceApi unit test stubs"""

    def setUp(self):
        self.api = api.api_key_resource_api.ApiKeyResourceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_session(self):
        """Test case for check_session

        Check api key session.  # noqa: E501
        """
        pass

    def test_create(self):
        """Test case for create

        Create an api key.  # noqa: E501
        """
        pass

    def test_delete_all(self):
        """Test case for delete_all

        Delete all api keys.  # noqa: E501
        """
        pass

    def test_delete_by_name(self):
        """Test case for delete_by_name

        Delete api key by name.  # noqa: E501
        """
        pass

    def test_get4(self):
        """Test case for get4

        Get all api keys.  # noqa: E501
        """
        pass

    def test_get_by_key(self):
        """Test case for get_by_key

        Find api key by name.  # noqa: E501
        """
        pass

    def test_get_by_name3(self):
        """Test case for get_by_name3

        Find api key by name.  # noqa: E501
        """
        pass

    def test_get_scopes(self):
        """Test case for get_scopes

        Get all api keys scopes.  # noqa: E501
        """
        pass

    def test_update1(self):
        """Test case for update1

        Update an api key.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()