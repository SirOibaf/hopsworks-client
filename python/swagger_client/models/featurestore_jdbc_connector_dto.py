# coding: utf-8

"""
    Hopsworks api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.1.0-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.featurestore_storage_connector_dto import FeaturestoreStorageConnectorDTO  # noqa: F401,E501


class FeaturestoreJdbcConnectorDTO(FeaturestoreStorageConnectorDTO):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'connection_string': 'str',
        'arguments': 'str'
    }

    attribute_map = {
        'connection_string': 'connectionString',
        'arguments': 'arguments'
    }

    def __init__(self, connection_string=None, arguments=None):  # noqa: E501
        """FeaturestoreJdbcConnectorDTO - a model defined in Swagger"""  # noqa: E501
        self._connection_string = None
        self._arguments = None
        self.discriminator = None
        if connection_string is not None:
            self.connection_string = connection_string
        if arguments is not None:
            self.arguments = arguments

    @property
    def connection_string(self):
        """Gets the connection_string of this FeaturestoreJdbcConnectorDTO.  # noqa: E501


        :return: The connection_string of this FeaturestoreJdbcConnectorDTO.  # noqa: E501
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """Sets the connection_string of this FeaturestoreJdbcConnectorDTO.


        :param connection_string: The connection_string of this FeaturestoreJdbcConnectorDTO.  # noqa: E501
        :type: str
        """

        self._connection_string = connection_string

    @property
    def arguments(self):
        """Gets the arguments of this FeaturestoreJdbcConnectorDTO.  # noqa: E501


        :return: The arguments of this FeaturestoreJdbcConnectorDTO.  # noqa: E501
        :rtype: str
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this FeaturestoreJdbcConnectorDTO.


        :param arguments: The arguments of this FeaturestoreJdbcConnectorDTO.  # noqa: E501
        :type: str
        """

        self._arguments = arguments

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FeaturestoreJdbcConnectorDTO, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FeaturestoreJdbcConnectorDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
