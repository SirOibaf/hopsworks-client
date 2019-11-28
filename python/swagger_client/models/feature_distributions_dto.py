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
from swagger_client.models.feature_distribution_dto import FeatureDistributionDTO  # noqa: F401,E501


class FeatureDistributionsDTO(object):
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
        'feature_distributions': 'list[FeatureDistributionDTO]'
    }

    attribute_map = {
        'feature_distributions': 'featureDistributions'
    }

    def __init__(self, feature_distributions=None):  # noqa: E501
        """FeatureDistributionsDTO - a model defined in Swagger"""  # noqa: E501
        self._feature_distributions = None
        self.discriminator = None
        if feature_distributions is not None:
            self.feature_distributions = feature_distributions

    @property
    def feature_distributions(self):
        """Gets the feature_distributions of this FeatureDistributionsDTO.  # noqa: E501


        :return: The feature_distributions of this FeatureDistributionsDTO.  # noqa: E501
        :rtype: list[FeatureDistributionDTO]
        """
        return self._feature_distributions

    @feature_distributions.setter
    def feature_distributions(self, feature_distributions):
        """Sets the feature_distributions of this FeatureDistributionsDTO.


        :param feature_distributions: The feature_distributions of this FeatureDistributionsDTO.  # noqa: E501
        :type: list[FeatureDistributionDTO]
        """

        self._feature_distributions = feature_distributions

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
        if issubclass(FeatureDistributionsDTO, dict):
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
        if not isinstance(other, FeatureDistributionsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other