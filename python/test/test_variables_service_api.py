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
from api.variables_service_api import VariablesServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestVariablesServiceApi(unittest.TestCase):
    """VariablesServiceApi unit test stubs"""

    def setUp(self):
        self.api = api.variables_service_api.VariablesServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_auth_status(self):
        """Test case for get_auth_status

        """
        pass

    def test_get_conda_default_repo(self):
        """Test case for get_conda_default_repo

        """
        pass

    def test_get_ldap_auth_status(self):
        """Test case for get_ldap_auth_status

        """
        pass

    def test_get_security_questions(self):
        """Test case for get_security_questions

        """
        pass

    def test_get_twofactor(self):
        """Test case for get_twofactor

        """
        pass

    def test_get_var(self):
        """Test case for get_var

        """
        pass

    def test_get_versions(self):
        """Test case for get_versions

        """
        pass


if __name__ == '__main__':
    unittest.main()
