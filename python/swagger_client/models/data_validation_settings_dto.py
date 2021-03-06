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


class DataValidationSettingsDTO(object):
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
        'validation_rules_path': 'str',
        'executable_path': 'str',
        'executable_main_class': 'str'
    }

    attribute_map = {
        'validation_rules_path': 'validationRulesPath',
        'executable_path': 'executablePath',
        'executable_main_class': 'executableMainClass'
    }

    def __init__(self, validation_rules_path=None, executable_path=None, executable_main_class=None):  # noqa: E501
        """DataValidationSettingsDTO - a model defined in Swagger"""  # noqa: E501
        self._validation_rules_path = None
        self._executable_path = None
        self._executable_main_class = None
        self.discriminator = None
        if validation_rules_path is not None:
            self.validation_rules_path = validation_rules_path
        if executable_path is not None:
            self.executable_path = executable_path
        if executable_main_class is not None:
            self.executable_main_class = executable_main_class

    @property
    def validation_rules_path(self):
        """Gets the validation_rules_path of this DataValidationSettingsDTO.  # noqa: E501


        :return: The validation_rules_path of this DataValidationSettingsDTO.  # noqa: E501
        :rtype: str
        """
        return self._validation_rules_path

    @validation_rules_path.setter
    def validation_rules_path(self, validation_rules_path):
        """Sets the validation_rules_path of this DataValidationSettingsDTO.


        :param validation_rules_path: The validation_rules_path of this DataValidationSettingsDTO.  # noqa: E501
        :type: str
        """

        self._validation_rules_path = validation_rules_path

    @property
    def executable_path(self):
        """Gets the executable_path of this DataValidationSettingsDTO.  # noqa: E501


        :return: The executable_path of this DataValidationSettingsDTO.  # noqa: E501
        :rtype: str
        """
        return self._executable_path

    @executable_path.setter
    def executable_path(self, executable_path):
        """Sets the executable_path of this DataValidationSettingsDTO.


        :param executable_path: The executable_path of this DataValidationSettingsDTO.  # noqa: E501
        :type: str
        """

        self._executable_path = executable_path

    @property
    def executable_main_class(self):
        """Gets the executable_main_class of this DataValidationSettingsDTO.  # noqa: E501


        :return: The executable_main_class of this DataValidationSettingsDTO.  # noqa: E501
        :rtype: str
        """
        return self._executable_main_class

    @executable_main_class.setter
    def executable_main_class(self, executable_main_class):
        """Sets the executable_main_class of this DataValidationSettingsDTO.


        :param executable_main_class: The executable_main_class of this DataValidationSettingsDTO.  # noqa: E501
        :type: str
        """

        self._executable_main_class = executable_main_class

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
        if issubclass(DataValidationSettingsDTO, dict):
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
        if not isinstance(other, DataValidationSettingsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
