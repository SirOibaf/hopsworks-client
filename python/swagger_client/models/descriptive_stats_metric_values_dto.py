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
from swagger_client.models.descriptive_stats_metric_value_dto import DescriptiveStatsMetricValueDTO  # noqa: F401,E501


class DescriptiveStatsMetricValuesDTO(object):
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
        'metric_values': 'list[DescriptiveStatsMetricValueDTO]',
        'statistic_type': 'str'
    }

    attribute_map = {
        'feature_name': 'featureName',
        'metric_values': 'metricValues',
        'statistic_type': 'statisticType'
    }

    def __init__(self, feature_name=None, metric_values=None, statistic_type=None):  # noqa: E501
        """DescriptiveStatsMetricValuesDTO - a model defined in Swagger"""  # noqa: E501
        self._feature_name = None
        self._metric_values = None
        self._statistic_type = None
        self.discriminator = None
        if feature_name is not None:
            self.feature_name = feature_name
        if metric_values is not None:
            self.metric_values = metric_values
        if statistic_type is not None:
            self.statistic_type = statistic_type

    @property
    def feature_name(self):
        """Gets the feature_name of this DescriptiveStatsMetricValuesDTO.  # noqa: E501


        :return: The feature_name of this DescriptiveStatsMetricValuesDTO.  # noqa: E501
        :rtype: str
        """
        return self._feature_name

    @feature_name.setter
    def feature_name(self, feature_name):
        """Sets the feature_name of this DescriptiveStatsMetricValuesDTO.


        :param feature_name: The feature_name of this DescriptiveStatsMetricValuesDTO.  # noqa: E501
        :type: str
        """

        self._feature_name = feature_name

    @property
    def metric_values(self):
        """Gets the metric_values of this DescriptiveStatsMetricValuesDTO.  # noqa: E501


        :return: The metric_values of this DescriptiveStatsMetricValuesDTO.  # noqa: E501
        :rtype: list[DescriptiveStatsMetricValueDTO]
        """
        return self._metric_values

    @metric_values.setter
    def metric_values(self, metric_values):
        """Sets the metric_values of this DescriptiveStatsMetricValuesDTO.


        :param metric_values: The metric_values of this DescriptiveStatsMetricValuesDTO.  # noqa: E501
        :type: list[DescriptiveStatsMetricValueDTO]
        """

        self._metric_values = metric_values

    @property
    def statistic_type(self):
        """Gets the statistic_type of this DescriptiveStatsMetricValuesDTO.  # noqa: E501


        :return: The statistic_type of this DescriptiveStatsMetricValuesDTO.  # noqa: E501
        :rtype: str
        """
        return self._statistic_type

    @statistic_type.setter
    def statistic_type(self, statistic_type):
        """Sets the statistic_type of this DescriptiveStatsMetricValuesDTO.


        :param statistic_type: The statistic_type of this DescriptiveStatsMetricValuesDTO.  # noqa: E501
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
        if issubclass(DescriptiveStatsMetricValuesDTO, dict):
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
        if not isinstance(other, DescriptiveStatsMetricValuesDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
