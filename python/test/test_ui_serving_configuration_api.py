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
from api.ui_serving_configuration_api import UIServingConfigurationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUIServingConfigurationApi(unittest.TestCase):
    """UIServingConfigurationApi unit test stubs"""

    def setUp(self):
        self.api = api.ui_serving_configuration_api.UIServingConfigurationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_configuration(self):
        """Test case for get_configuration

        Get UI configuration for serving  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
