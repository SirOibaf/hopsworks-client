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
from api.elastic_service_api import ElasticServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestElasticServiceApi(unittest.TestCase):
    """ElasticServiceApi unit test stubs"""

    def setUp(self):
        self.api = api.elastic_service_api.ElasticServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_dataset_search(self):
        """Test case for dataset_search

        """
        pass

    def test_global_search(self):
        """Test case for global_search

        """
        pass

    def test_project_search(self):
        """Test case for project_search

        """
        pass


if __name__ == '__main__':
    unittest.main()