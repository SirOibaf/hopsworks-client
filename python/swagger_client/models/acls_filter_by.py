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


class AclsFilterBy(object):
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
        'param': 'str',
        'sql': 'str',
        'value': 'str',
        'field': 'str'
    }

    attribute_map = {
        'param': 'param',
        'sql': 'sql',
        'value': 'value',
        'field': 'field'
    }

    def __init__(self, param=None, sql=None, value=None, field=None):  # noqa: E501
        """AclsFilterBy - a model defined in Swagger"""  # noqa: E501
        self._param = None
        self._sql = None
        self._value = None
        self._field = None
        self.discriminator = None
        if param is not None:
            self.param = param
        if sql is not None:
            self.sql = sql
        if value is not None:
            self.value = value
        if field is not None:
            self.field = field

    @property
    def param(self):
        """Gets the param of this AclsFilterBy.  # noqa: E501


        :return: The param of this AclsFilterBy.  # noqa: E501
        :rtype: str
        """
        return self._param

    @param.setter
    def param(self, param):
        """Sets the param of this AclsFilterBy.


        :param param: The param of this AclsFilterBy.  # noqa: E501
        :type: str
        """

        self._param = param

    @property
    def sql(self):
        """Gets the sql of this AclsFilterBy.  # noqa: E501


        :return: The sql of this AclsFilterBy.  # noqa: E501
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        """Sets the sql of this AclsFilterBy.


        :param sql: The sql of this AclsFilterBy.  # noqa: E501
        :type: str
        """

        self._sql = sql

    @property
    def value(self):
        """Gets the value of this AclsFilterBy.  # noqa: E501


        :return: The value of this AclsFilterBy.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AclsFilterBy.


        :param value: The value of this AclsFilterBy.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def field(self):
        """Gets the field of this AclsFilterBy.  # noqa: E501


        :return: The field of this AclsFilterBy.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this AclsFilterBy.


        :param field: The field of this AclsFilterBy.  # noqa: E501
        :type: str
        """

        self._field = field

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
        if issubclass(AclsFilterBy, dict):
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
        if not isinstance(other, AclsFilterBy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
