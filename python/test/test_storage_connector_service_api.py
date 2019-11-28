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
from api.storage_connector_service_api import StorageConnectorServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestStorageConnectorServiceApi(unittest.TestCase):
    """StorageConnectorServiceApi unit test stubs"""

    def setUp(self):
        self.api = api.storage_connector_service_api.StorageConnectorServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_new_storage_connector_with_type(self):
        """Test case for create_new_storage_connector_with_type

        Create a new storage connector for the feature store  # noqa: E501
        """
        pass

    def test_delete_storage_connector_with_type_and_id(self):
        """Test case for delete_storage_connector_with_type_and_id

        Delete storage connector with a specific id and type from a featurestore  # noqa: E501
        """
        pass

    def test_get_online_featurestore_storage_connector(self):
        """Test case for get_online_featurestore_storage_connector

        Get online featurestore storage connector for this feature store  # noqa: E501
        """
        pass

    def test_get_storage_connector_with_id(self):
        """Test case for get_storage_connector_with_id

        Get a storage connector with a specific id and type from a featurestore  # noqa: E501
        """
        pass

    def test_get_storage_connectors(self):
        """Test case for get_storage_connectors

        Get all storage connectors of a feature store  # noqa: E501
        """
        pass

    def test_get_storage_connectors_of_type(self):
        """Test case for get_storage_connectors_of_type

        Get all storage connectors of a specific type of a feature store  # noqa: E501
        """
        pass

    def test_update_storage_connector_with_id(self):
        """Test case for update_storage_connector_with_id

        Get a storage connector with a specific id and type from a featurestore  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
