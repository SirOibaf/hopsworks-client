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
from api.python_environment_library_resource_api import PythonEnvironmentLibraryResourceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPythonEnvironmentLibraryResourceApi(unittest.TestCase):
    """PythonEnvironmentLibraryResourceApi unit test stubs"""

    def setUp(self):
        self.api = api.python_environment_library_resource_api.PythonEnvironmentLibraryResourceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete1(self):
        """Test case for delete1

        Delete commands for this library  # noqa: E501
        """
        pass

    def test_get1(self):
        """Test case for get1

        Get all commands for this library  # noqa: E501
        """
        pass

    def test_get2(self):
        """Test case for get2

        Get the python libraries installed in this environment  # noqa: E501
        """
        pass

    def test_get_by_name1(self):
        """Test case for get_by_name1

        Get command by id  # noqa: E501
        """
        pass

    def test_get_by_name2(self):
        """Test case for get_by_name2

        Get the a python library installed in this environment  # noqa: E501
        """
        pass

    def test_install(self):
        """Test case for install

        Install a python library in the environment  # noqa: E501
        """
        pass

    def test_search(self):
        """Test case for search

        Search for libraries using conda or pip package managers  # noqa: E501
        """
        pass

    def test_uninstall(self):
        """Test case for uninstall

        Uninstall a python library from the environment  # noqa: E501
        """
        pass

    def test_update(self):
        """Test case for update

        Update commands for this library  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()