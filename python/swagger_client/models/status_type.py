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


class StatusType(object):
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
        'reason_phrase': 'str',
        'status_code': 'int',
        'family': 'str'
    }

    attribute_map = {
        'reason_phrase': 'reasonPhrase',
        'status_code': 'statusCode',
        'family': 'family'
    }

    def __init__(self, reason_phrase=None, status_code=None, family=None):  # noqa: E501
        """StatusType - a model defined in Swagger"""  # noqa: E501
        self._reason_phrase = None
        self._status_code = None
        self._family = None
        self.discriminator = None
        if reason_phrase is not None:
            self.reason_phrase = reason_phrase
        if status_code is not None:
            self.status_code = status_code
        if family is not None:
            self.family = family

    @property
    def reason_phrase(self):
        """Gets the reason_phrase of this StatusType.  # noqa: E501


        :return: The reason_phrase of this StatusType.  # noqa: E501
        :rtype: str
        """
        return self._reason_phrase

    @reason_phrase.setter
    def reason_phrase(self, reason_phrase):
        """Sets the reason_phrase of this StatusType.


        :param reason_phrase: The reason_phrase of this StatusType.  # noqa: E501
        :type: str
        """

        self._reason_phrase = reason_phrase

    @property
    def status_code(self):
        """Gets the status_code of this StatusType.  # noqa: E501


        :return: The status_code of this StatusType.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this StatusType.


        :param status_code: The status_code of this StatusType.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def family(self):
        """Gets the family of this StatusType.  # noqa: E501


        :return: The family of this StatusType.  # noqa: E501
        :rtype: str
        """
        return self._family

    @family.setter
    def family(self, family):
        """Sets the family of this StatusType.


        :param family: The family of this StatusType.  # noqa: E501
        :type: str
        """
        allowed_values = ["INFORMATIONAL", "SUCCESSFUL", "REDIRECTION", "CLIENT_ERROR", "SERVER_ERROR", "OTHER"]  # noqa: E501
        if family not in allowed_values:
            raise ValueError(
                "Invalid value for `family` ({0}), must be one of {1}"  # noqa: E501
                .format(family, allowed_values)
            )

        self._family = family

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
        if issubclass(StatusType, dict):
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
        if not isinstance(other, StatusType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other