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
from swagger_client.models.cluster_analysis_dto import ClusterAnalysisDTO  # noqa: F401,E501
from swagger_client.models.descriptive_stats_dto import DescriptiveStatsDTO  # noqa: F401,E501
from swagger_client.models.feature_correlation_matrix_dto import FeatureCorrelationMatrixDTO  # noqa: F401,E501
from swagger_client.models.feature_distributions_dto import FeatureDistributionsDTO  # noqa: F401,E501
from swagger_client.models.feature_dto import FeatureDTO  # noqa: F401,E501
from swagger_client.models.featurestore_job_dto import FeaturestoreJobDTO  # noqa: F401,E501
from swagger_client.models.training_dataset_dto import TrainingDatasetDTO  # noqa: F401,E501


class ExternalTrainingDatasetDTO(TrainingDatasetDTO):
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
        's3_connector_id': 'int',
        's3_connector_name': 'str',
        's3_connector_bucket': 'str'
    }

    attribute_map = {
        's3_connector_id': 's3ConnectorId',
        's3_connector_name': 's3ConnectorName',
        's3_connector_bucket': 's3ConnectorBucket'
    }

    def __init__(self, s3_connector_id=None, s3_connector_name=None, s3_connector_bucket=None):  # noqa: E501
        """ExternalTrainingDatasetDTO - a model defined in Swagger"""  # noqa: E501
        self._s3_connector_id = None
        self._s3_connector_name = None
        self._s3_connector_bucket = None
        self.discriminator = None
        if s3_connector_id is not None:
            self.s3_connector_id = s3_connector_id
        if s3_connector_name is not None:
            self.s3_connector_name = s3_connector_name
        if s3_connector_bucket is not None:
            self.s3_connector_bucket = s3_connector_bucket

    @property
    def s3_connector_id(self):
        """Gets the s3_connector_id of this ExternalTrainingDatasetDTO.  # noqa: E501


        :return: The s3_connector_id of this ExternalTrainingDatasetDTO.  # noqa: E501
        :rtype: int
        """
        return self._s3_connector_id

    @s3_connector_id.setter
    def s3_connector_id(self, s3_connector_id):
        """Sets the s3_connector_id of this ExternalTrainingDatasetDTO.


        :param s3_connector_id: The s3_connector_id of this ExternalTrainingDatasetDTO.  # noqa: E501
        :type: int
        """

        self._s3_connector_id = s3_connector_id

    @property
    def s3_connector_name(self):
        """Gets the s3_connector_name of this ExternalTrainingDatasetDTO.  # noqa: E501


        :return: The s3_connector_name of this ExternalTrainingDatasetDTO.  # noqa: E501
        :rtype: str
        """
        return self._s3_connector_name

    @s3_connector_name.setter
    def s3_connector_name(self, s3_connector_name):
        """Sets the s3_connector_name of this ExternalTrainingDatasetDTO.


        :param s3_connector_name: The s3_connector_name of this ExternalTrainingDatasetDTO.  # noqa: E501
        :type: str
        """

        self._s3_connector_name = s3_connector_name

    @property
    def s3_connector_bucket(self):
        """Gets the s3_connector_bucket of this ExternalTrainingDatasetDTO.  # noqa: E501


        :return: The s3_connector_bucket of this ExternalTrainingDatasetDTO.  # noqa: E501
        :rtype: str
        """
        return self._s3_connector_bucket

    @s3_connector_bucket.setter
    def s3_connector_bucket(self, s3_connector_bucket):
        """Sets the s3_connector_bucket of this ExternalTrainingDatasetDTO.


        :param s3_connector_bucket: The s3_connector_bucket of this ExternalTrainingDatasetDTO.  # noqa: E501
        :type: str
        """

        self._s3_connector_bucket = s3_connector_bucket

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
        if issubclass(ExternalTrainingDatasetDTO, dict):
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
        if not isinstance(other, ExternalTrainingDatasetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
