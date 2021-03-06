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


class TrainingDatasetDTO(object):
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
        'featurestore_id': 'int',
        'featurestore_name': 'str',
        'description': 'str',
        'created': 'datetime',
        'creator': 'str',
        'version': 'int',
        'descriptive_statistics': 'DescriptiveStatsDTO',
        'feature_correlation_matrix': 'FeatureCorrelationMatrixDTO',
        'features_histogram': 'FeatureDistributionsDTO',
        'cluster_analysis': 'ClusterAnalysisDTO',
        'name': 'str',
        'id': 'int',
        'features': 'list[FeatureDTO]',
        'location': 'str',
        'jobs': 'list[FeaturestoreJobDTO]',
        'data_format': 'str',
        'training_dataset_type': 'str'
    }

    attribute_map = {
        'featurestore_id': 'featurestoreId',
        'featurestore_name': 'featurestoreName',
        'description': 'description',
        'created': 'created',
        'creator': 'creator',
        'version': 'version',
        'descriptive_statistics': 'descriptiveStatistics',
        'feature_correlation_matrix': 'featureCorrelationMatrix',
        'features_histogram': 'featuresHistogram',
        'cluster_analysis': 'clusterAnalysis',
        'name': 'name',
        'id': 'id',
        'features': 'features',
        'location': 'location',
        'jobs': 'jobs',
        'data_format': 'dataFormat',
        'training_dataset_type': 'trainingDatasetType'
    }

    def __init__(self, featurestore_id=None, featurestore_name=None, description=None, created=None, creator=None, version=None, descriptive_statistics=None, feature_correlation_matrix=None, features_histogram=None, cluster_analysis=None, name=None, id=None, features=None, location=None, jobs=None, data_format=None, training_dataset_type=None):  # noqa: E501
        """TrainingDatasetDTO - a model defined in Swagger"""  # noqa: E501
        self._featurestore_id = None
        self._featurestore_name = None
        self._description = None
        self._created = None
        self._creator = None
        self._version = None
        self._descriptive_statistics = None
        self._feature_correlation_matrix = None
        self._features_histogram = None
        self._cluster_analysis = None
        self._name = None
        self._id = None
        self._features = None
        self._location = None
        self._jobs = None
        self._data_format = None
        self._training_dataset_type = None
        self.discriminator = None
        if featurestore_id is not None:
            self.featurestore_id = featurestore_id
        if featurestore_name is not None:
            self.featurestore_name = featurestore_name
        if description is not None:
            self.description = description
        if created is not None:
            self.created = created
        if creator is not None:
            self.creator = creator
        if version is not None:
            self.version = version
        if descriptive_statistics is not None:
            self.descriptive_statistics = descriptive_statistics
        if feature_correlation_matrix is not None:
            self.feature_correlation_matrix = feature_correlation_matrix
        if features_histogram is not None:
            self.features_histogram = features_histogram
        if cluster_analysis is not None:
            self.cluster_analysis = cluster_analysis
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if features is not None:
            self.features = features
        if location is not None:
            self.location = location
        if jobs is not None:
            self.jobs = jobs
        if data_format is not None:
            self.data_format = data_format
        if training_dataset_type is not None:
            self.training_dataset_type = training_dataset_type

    @property
    def featurestore_id(self):
        """Gets the featurestore_id of this TrainingDatasetDTO.  # noqa: E501


        :return: The featurestore_id of this TrainingDatasetDTO.  # noqa: E501
        :rtype: int
        """
        return self._featurestore_id

    @featurestore_id.setter
    def featurestore_id(self, featurestore_id):
        """Sets the featurestore_id of this TrainingDatasetDTO.


        :param featurestore_id: The featurestore_id of this TrainingDatasetDTO.  # noqa: E501
        :type: int
        """

        self._featurestore_id = featurestore_id

    @property
    def featurestore_name(self):
        """Gets the featurestore_name of this TrainingDatasetDTO.  # noqa: E501


        :return: The featurestore_name of this TrainingDatasetDTO.  # noqa: E501
        :rtype: str
        """
        return self._featurestore_name

    @featurestore_name.setter
    def featurestore_name(self, featurestore_name):
        """Sets the featurestore_name of this TrainingDatasetDTO.


        :param featurestore_name: The featurestore_name of this TrainingDatasetDTO.  # noqa: E501
        :type: str
        """

        self._featurestore_name = featurestore_name

    @property
    def description(self):
        """Gets the description of this TrainingDatasetDTO.  # noqa: E501


        :return: The description of this TrainingDatasetDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TrainingDatasetDTO.


        :param description: The description of this TrainingDatasetDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def created(self):
        """Gets the created of this TrainingDatasetDTO.  # noqa: E501


        :return: The created of this TrainingDatasetDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this TrainingDatasetDTO.


        :param created: The created of this TrainingDatasetDTO.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def creator(self):
        """Gets the creator of this TrainingDatasetDTO.  # noqa: E501


        :return: The creator of this TrainingDatasetDTO.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this TrainingDatasetDTO.


        :param creator: The creator of this TrainingDatasetDTO.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def version(self):
        """Gets the version of this TrainingDatasetDTO.  # noqa: E501


        :return: The version of this TrainingDatasetDTO.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TrainingDatasetDTO.


        :param version: The version of this TrainingDatasetDTO.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def descriptive_statistics(self):
        """Gets the descriptive_statistics of this TrainingDatasetDTO.  # noqa: E501


        :return: The descriptive_statistics of this TrainingDatasetDTO.  # noqa: E501
        :rtype: DescriptiveStatsDTO
        """
        return self._descriptive_statistics

    @descriptive_statistics.setter
    def descriptive_statistics(self, descriptive_statistics):
        """Sets the descriptive_statistics of this TrainingDatasetDTO.


        :param descriptive_statistics: The descriptive_statistics of this TrainingDatasetDTO.  # noqa: E501
        :type: DescriptiveStatsDTO
        """

        self._descriptive_statistics = descriptive_statistics

    @property
    def feature_correlation_matrix(self):
        """Gets the feature_correlation_matrix of this TrainingDatasetDTO.  # noqa: E501


        :return: The feature_correlation_matrix of this TrainingDatasetDTO.  # noqa: E501
        :rtype: FeatureCorrelationMatrixDTO
        """
        return self._feature_correlation_matrix

    @feature_correlation_matrix.setter
    def feature_correlation_matrix(self, feature_correlation_matrix):
        """Sets the feature_correlation_matrix of this TrainingDatasetDTO.


        :param feature_correlation_matrix: The feature_correlation_matrix of this TrainingDatasetDTO.  # noqa: E501
        :type: FeatureCorrelationMatrixDTO
        """

        self._feature_correlation_matrix = feature_correlation_matrix

    @property
    def features_histogram(self):
        """Gets the features_histogram of this TrainingDatasetDTO.  # noqa: E501


        :return: The features_histogram of this TrainingDatasetDTO.  # noqa: E501
        :rtype: FeatureDistributionsDTO
        """
        return self._features_histogram

    @features_histogram.setter
    def features_histogram(self, features_histogram):
        """Sets the features_histogram of this TrainingDatasetDTO.


        :param features_histogram: The features_histogram of this TrainingDatasetDTO.  # noqa: E501
        :type: FeatureDistributionsDTO
        """

        self._features_histogram = features_histogram

    @property
    def cluster_analysis(self):
        """Gets the cluster_analysis of this TrainingDatasetDTO.  # noqa: E501


        :return: The cluster_analysis of this TrainingDatasetDTO.  # noqa: E501
        :rtype: ClusterAnalysisDTO
        """
        return self._cluster_analysis

    @cluster_analysis.setter
    def cluster_analysis(self, cluster_analysis):
        """Sets the cluster_analysis of this TrainingDatasetDTO.


        :param cluster_analysis: The cluster_analysis of this TrainingDatasetDTO.  # noqa: E501
        :type: ClusterAnalysisDTO
        """

        self._cluster_analysis = cluster_analysis

    @property
    def name(self):
        """Gets the name of this TrainingDatasetDTO.  # noqa: E501


        :return: The name of this TrainingDatasetDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrainingDatasetDTO.


        :param name: The name of this TrainingDatasetDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this TrainingDatasetDTO.  # noqa: E501


        :return: The id of this TrainingDatasetDTO.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrainingDatasetDTO.


        :param id: The id of this TrainingDatasetDTO.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def features(self):
        """Gets the features of this TrainingDatasetDTO.  # noqa: E501


        :return: The features of this TrainingDatasetDTO.  # noqa: E501
        :rtype: list[FeatureDTO]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this TrainingDatasetDTO.


        :param features: The features of this TrainingDatasetDTO.  # noqa: E501
        :type: list[FeatureDTO]
        """

        self._features = features

    @property
    def location(self):
        """Gets the location of this TrainingDatasetDTO.  # noqa: E501


        :return: The location of this TrainingDatasetDTO.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this TrainingDatasetDTO.


        :param location: The location of this TrainingDatasetDTO.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def jobs(self):
        """Gets the jobs of this TrainingDatasetDTO.  # noqa: E501


        :return: The jobs of this TrainingDatasetDTO.  # noqa: E501
        :rtype: list[FeaturestoreJobDTO]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this TrainingDatasetDTO.


        :param jobs: The jobs of this TrainingDatasetDTO.  # noqa: E501
        :type: list[FeaturestoreJobDTO]
        """

        self._jobs = jobs

    @property
    def data_format(self):
        """Gets the data_format of this TrainingDatasetDTO.  # noqa: E501


        :return: The data_format of this TrainingDatasetDTO.  # noqa: E501
        :rtype: str
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """Sets the data_format of this TrainingDatasetDTO.


        :param data_format: The data_format of this TrainingDatasetDTO.  # noqa: E501
        :type: str
        """

        self._data_format = data_format

    @property
    def training_dataset_type(self):
        """Gets the training_dataset_type of this TrainingDatasetDTO.  # noqa: E501


        :return: The training_dataset_type of this TrainingDatasetDTO.  # noqa: E501
        :rtype: str
        """
        return self._training_dataset_type

    @training_dataset_type.setter
    def training_dataset_type(self, training_dataset_type):
        """Sets the training_dataset_type of this TrainingDatasetDTO.


        :param training_dataset_type: The training_dataset_type of this TrainingDatasetDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["HOPSFS_TRAINING_DATASET", "EXTERNAL_TRAINING_DATASET"]  # noqa: E501
        if training_dataset_type not in allowed_values:
            raise ValueError(
                "Invalid value for `training_dataset_type` ({0}), must be one of {1}"  # noqa: E501
                .format(training_dataset_type, allowed_values)
            )

        self._training_dataset_type = training_dataset_type

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
        if issubclass(TrainingDatasetDTO, dict):
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
        if not isinstance(other, TrainingDatasetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
