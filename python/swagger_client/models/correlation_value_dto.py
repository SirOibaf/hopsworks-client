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


class CorrelationValueDTO(object):
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
        'feature_name': 'str',
        'correlation': 'float',
        'statistic_type': 'str'
    }

    attribute_map = {
        'feature_name': 'featureName',
        'correlation': 'correlation',
        'statistic_type': 'statisticType'
    }

    def __init__(self, feature_name=None, correlation=None, statistic_type=None):  # noqa: E501
        """CorrelationValueDTO - a model defined in Swagger"""  # noqa: E501
        self._feature_name = None
        self._correlation = None
        self._statistic_type = None
        self.discriminator = None
        if feature_name is not None:
            self.feature_name = feature_name
        if correlation is not None:
            self.correlation = correlation
        if statistic_type is not None:
            self.statistic_type = statistic_type

    @property
    def feature_name(self):
        """Gets the feature_name of this CorrelationValueDTO.  # noqa: E501


        :return: The feature_name of this CorrelationValueDTO.  # noqa: E501
        :rtype: str
        """
        return self._feature_name

    @feature_name.setter
    def feature_name(self, feature_name):
        """Sets the feature_name of this CorrelationValueDTO.


        :param feature_name: The feature_name of this CorrelationValueDTO.  # noqa: E501
        :type: str
        """

        self._feature_name = feature_name

    @property
    def correlation(self):
        """Gets the correlation of this CorrelationValueDTO.  # noqa: E501


        :return: The correlation of this CorrelationValueDTO.  # noqa: E501
        :rtype: float
        """
        return self._correlation

    @correlation.setter
    def correlation(self, correlation):
        """Sets the correlation of this CorrelationValueDTO.


        :param correlation: The correlation of this CorrelationValueDTO.  # noqa: E501
        :type: float
        """

        self._correlation = correlation

    @property
    def statistic_type(self):
        """Gets the statistic_type of this CorrelationValueDTO.  # noqa: E501


        :return: The statistic_type of this CorrelationValueDTO.  # noqa: E501
        :rtype: str
        """
        return self._statistic_type

    @statistic_type.setter
    def statistic_type(self, statistic_type):
        """Sets the statistic_type of this CorrelationValueDTO.


        :param statistic_type: The statistic_type of this CorrelationValueDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["DESCRIPTIVESTATISTICS", "CLUSTERANALYSIS", "FEATUREDISTRIBUTIONS", "FEATURECORRELATIONS"]  # noqa: E501
        if statistic_type not in allowed_values:
            raise ValueError(
                "Invalid value for `statistic_type` ({0}), must be one of {1}"  # noqa: E501
                .format(statistic_type, allowed_values)
            )

        self._statistic_type = statistic_type

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
        if issubclass(CorrelationValueDTO, dict):
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
        if not isinstance(other, CorrelationValueDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other