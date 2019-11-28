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
from api.machine_types_resource_api import MachineTypesResourceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMachineTypesResourceApi(unittest.TestCase):
    """MachineTypesResourceApi unit test stubs"""

    def setUp(self):
        self.api = api.machine_types_resource_api.MachineTypesResourceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_machine_type(self):
        """Test case for get_machine_type

        Get number of machines for a machine type  # noqa: E501
        """
        pass

    def test_get_machine_types(self):
        """Test case for get_machine_types

        Get all types of machines for conda  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()