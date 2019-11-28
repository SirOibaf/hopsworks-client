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
from swagger_client.models.column_value_query_result import ColumnValueQueryResult  # noqa: F401,E501


class RowValueQueryResult(object):
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
        'columns': 'list[ColumnValueQueryResult]'
    }

    attribute_map = {
        'columns': 'columns'
    }

    def __init__(self, columns=None):  # noqa: E501
        """RowValueQueryResult - a model defined in Swagger"""  # noqa: E501
        self._columns = None
        self.discriminator = None
        if columns is not None:
            self.columns = columns

    @property
    def columns(self):
        """Gets the columns of this RowValueQueryResult.  # noqa: E501


        :return: The columns of this RowValueQueryResult.  # noqa: E501
        :rtype: list[ColumnValueQueryResult]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this RowValueQueryResult.


        :param columns: The columns of this RowValueQueryResult.  # noqa: E501
        :type: list[ColumnValueQueryResult]
        """

        self._columns = columns

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
        if issubclass(RowValueQueryResult, dict):
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
        if not isinstance(other, RowValueQueryResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other