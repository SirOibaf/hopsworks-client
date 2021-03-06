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


class RepresentConfigurationForServingUI(object):
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
        'max_num_instances': 'int',
        'kafka_topic_schema': 'str',
        'kafka_topic_schema_version': 'int'
    }

    attribute_map = {
        'max_num_instances': 'maxNumInstances',
        'kafka_topic_schema': 'kafkaTopicSchema',
        'kafka_topic_schema_version': 'kafkaTopicSchemaVersion'
    }

    def __init__(self, max_num_instances=None, kafka_topic_schema=None, kafka_topic_schema_version=None):  # noqa: E501
        """RepresentConfigurationForServingUI - a model defined in Swagger"""  # noqa: E501
        self._max_num_instances = None
        self._kafka_topic_schema = None
        self._kafka_topic_schema_version = None
        self.discriminator = None
        if max_num_instances is not None:
            self.max_num_instances = max_num_instances
        if kafka_topic_schema is not None:
            self.kafka_topic_schema = kafka_topic_schema
        if kafka_topic_schema_version is not None:
            self.kafka_topic_schema_version = kafka_topic_schema_version

    @property
    def max_num_instances(self):
        """Gets the max_num_instances of this RepresentConfigurationForServingUI.  # noqa: E501

        Max number of serving instances of model  # noqa: E501

        :return: The max_num_instances of this RepresentConfigurationForServingUI.  # noqa: E501
        :rtype: int
        """
        return self._max_num_instances

    @max_num_instances.setter
    def max_num_instances(self, max_num_instances):
        """Sets the max_num_instances of this RepresentConfigurationForServingUI.

        Max number of serving instances of model  # noqa: E501

        :param max_num_instances: The max_num_instances of this RepresentConfigurationForServingUI.  # noqa: E501
        :type: int
        """

        self._max_num_instances = max_num_instances

    @property
    def kafka_topic_schema(self):
        """Gets the kafka_topic_schema of this RepresentConfigurationForServingUI.  # noqa: E501

        Schema name for the Kafka topic used for logging  # noqa: E501

        :return: The kafka_topic_schema of this RepresentConfigurationForServingUI.  # noqa: E501
        :rtype: str
        """
        return self._kafka_topic_schema

    @kafka_topic_schema.setter
    def kafka_topic_schema(self, kafka_topic_schema):
        """Sets the kafka_topic_schema of this RepresentConfigurationForServingUI.

        Schema name for the Kafka topic used for logging  # noqa: E501

        :param kafka_topic_schema: The kafka_topic_schema of this RepresentConfigurationForServingUI.  # noqa: E501
        :type: str
        """

        self._kafka_topic_schema = kafka_topic_schema

    @property
    def kafka_topic_schema_version(self):
        """Gets the kafka_topic_schema_version of this RepresentConfigurationForServingUI.  # noqa: E501

        Schema version for the Kafka topic used for logging  # noqa: E501

        :return: The kafka_topic_schema_version of this RepresentConfigurationForServingUI.  # noqa: E501
        :rtype: int
        """
        return self._kafka_topic_schema_version

    @kafka_topic_schema_version.setter
    def kafka_topic_schema_version(self, kafka_topic_schema_version):
        """Sets the kafka_topic_schema_version of this RepresentConfigurationForServingUI.

        Schema version for the Kafka topic used for logging  # noqa: E501

        :param kafka_topic_schema_version: The kafka_topic_schema_version of this RepresentConfigurationForServingUI.  # noqa: E501
        :type: int
        """

        self._kafka_topic_schema_version = kafka_topic_schema_version

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
        if issubclass(RepresentConfigurationForServingUI, dict):
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
        if not isinstance(other, RepresentConfigurationForServingUI):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
