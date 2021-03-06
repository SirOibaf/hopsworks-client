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


class FeaturegroupDTO(object):
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
        'featuregroup_type': 'str',
        'desc_stats_enabled': 'bool',
        'feat_corr_enabled': 'bool',
        'feat_hist_enabled': 'bool',
        'cluster_analysis_enabled': 'bool',
        'statistic_columns': 'list[str]',
        'num_bins': 'int',
        'num_clusters': 'int',
        'corr_method': 'str'
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
        'featuregroup_type': 'featuregroupType',
        'desc_stats_enabled': 'descStatsEnabled',
        'feat_corr_enabled': 'featCorrEnabled',
        'feat_hist_enabled': 'featHistEnabled',
        'cluster_analysis_enabled': 'clusterAnalysisEnabled',
        'statistic_columns': 'statisticColumns',
        'num_bins': 'numBins',
        'num_clusters': 'numClusters',
        'corr_method': 'corrMethod'
    }

    def __init__(self, featurestore_id=None, featurestore_name=None, description=None, created=None, creator=None, version=None, descriptive_statistics=None, feature_correlation_matrix=None, features_histogram=None, cluster_analysis=None, name=None, id=None, features=None, location=None, jobs=None, featuregroup_type=None, desc_stats_enabled=None, feat_corr_enabled=None, feat_hist_enabled=None, cluster_analysis_enabled=None, statistic_columns=None, num_bins=None, num_clusters=None, corr_method=None):  # noqa: E501
        """FeaturegroupDTO - a model defined in Swagger"""  # noqa: E501
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
        self._featuregroup_type = None
        self._desc_stats_enabled = None
        self._feat_corr_enabled = None
        self._feat_hist_enabled = None
        self._cluster_analysis_enabled = None
        self._statistic_columns = None
        self._num_bins = None
        self._num_clusters = None
        self._corr_method = None
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
        if featuregroup_type is not None:
            self.featuregroup_type = featuregroup_type
        if desc_stats_enabled is not None:
            self.desc_stats_enabled = desc_stats_enabled
        if feat_corr_enabled is not None:
            self.feat_corr_enabled = feat_corr_enabled
        if feat_hist_enabled is not None:
            self.feat_hist_enabled = feat_hist_enabled
        if cluster_analysis_enabled is not None:
            self.cluster_analysis_enabled = cluster_analysis_enabled
        if statistic_columns is not None:
            self.statistic_columns = statistic_columns
        if num_bins is not None:
            self.num_bins = num_bins
        if num_clusters is not None:
            self.num_clusters = num_clusters
        if corr_method is not None:
            self.corr_method = corr_method

    @property
    def featurestore_id(self):
        """Gets the featurestore_id of this FeaturegroupDTO.  # noqa: E501


        :return: The featurestore_id of this FeaturegroupDTO.  # noqa: E501
        :rtype: int
        """
        return self._featurestore_id

    @featurestore_id.setter
    def featurestore_id(self, featurestore_id):
        """Sets the featurestore_id of this FeaturegroupDTO.


        :param featurestore_id: The featurestore_id of this FeaturegroupDTO.  # noqa: E501
        :type: int
        """

        self._featurestore_id = featurestore_id

    @property
    def featurestore_name(self):
        """Gets the featurestore_name of this FeaturegroupDTO.  # noqa: E501


        :return: The featurestore_name of this FeaturegroupDTO.  # noqa: E501
        :rtype: str
        """
        return self._featurestore_name

    @featurestore_name.setter
    def featurestore_name(self, featurestore_name):
        """Sets the featurestore_name of this FeaturegroupDTO.


        :param featurestore_name: The featurestore_name of this FeaturegroupDTO.  # noqa: E501
        :type: str
        """

        self._featurestore_name = featurestore_name

    @property
    def description(self):
        """Gets the description of this FeaturegroupDTO.  # noqa: E501


        :return: The description of this FeaturegroupDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FeaturegroupDTO.


        :param description: The description of this FeaturegroupDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def created(self):
        """Gets the created of this FeaturegroupDTO.  # noqa: E501


        :return: The created of this FeaturegroupDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this FeaturegroupDTO.


        :param created: The created of this FeaturegroupDTO.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def creator(self):
        """Gets the creator of this FeaturegroupDTO.  # noqa: E501


        :return: The creator of this FeaturegroupDTO.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this FeaturegroupDTO.


        :param creator: The creator of this FeaturegroupDTO.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def version(self):
        """Gets the version of this FeaturegroupDTO.  # noqa: E501


        :return: The version of this FeaturegroupDTO.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FeaturegroupDTO.


        :param version: The version of this FeaturegroupDTO.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def descriptive_statistics(self):
        """Gets the descriptive_statistics of this FeaturegroupDTO.  # noqa: E501


        :return: The descriptive_statistics of this FeaturegroupDTO.  # noqa: E501
        :rtype: DescriptiveStatsDTO
        """
        return self._descriptive_statistics

    @descriptive_statistics.setter
    def descriptive_statistics(self, descriptive_statistics):
        """Sets the descriptive_statistics of this FeaturegroupDTO.


        :param descriptive_statistics: The descriptive_statistics of this FeaturegroupDTO.  # noqa: E501
        :type: DescriptiveStatsDTO
        """

        self._descriptive_statistics = descriptive_statistics

    @property
    def feature_correlation_matrix(self):
        """Gets the feature_correlation_matrix of this FeaturegroupDTO.  # noqa: E501


        :return: The feature_correlation_matrix of this FeaturegroupDTO.  # noqa: E501
        :rtype: FeatureCorrelationMatrixDTO
        """
        return self._feature_correlation_matrix

    @feature_correlation_matrix.setter
    def feature_correlation_matrix(self, feature_correlation_matrix):
        """Sets the feature_correlation_matrix of this FeaturegroupDTO.


        :param feature_correlation_matrix: The feature_correlation_matrix of this FeaturegroupDTO.  # noqa: E501
        :type: FeatureCorrelationMatrixDTO
        """

        self._feature_correlation_matrix = feature_correlation_matrix

    @property
    def features_histogram(self):
        """Gets the features_histogram of this FeaturegroupDTO.  # noqa: E501


        :return: The features_histogram of this FeaturegroupDTO.  # noqa: E501
        :rtype: FeatureDistributionsDTO
        """
        return self._features_histogram

    @features_histogram.setter
    def features_histogram(self, features_histogram):
        """Sets the features_histogram of this FeaturegroupDTO.


        :param features_histogram: The features_histogram of this FeaturegroupDTO.  # noqa: E501
        :type: FeatureDistributionsDTO
        """

        self._features_histogram = features_histogram

    @property
    def cluster_analysis(self):
        """Gets the cluster_analysis of this FeaturegroupDTO.  # noqa: E501


        :return: The cluster_analysis of this FeaturegroupDTO.  # noqa: E501
        :rtype: ClusterAnalysisDTO
        """
        return self._cluster_analysis

    @cluster_analysis.setter
    def cluster_analysis(self, cluster_analysis):
        """Sets the cluster_analysis of this FeaturegroupDTO.


        :param cluster_analysis: The cluster_analysis of this FeaturegroupDTO.  # noqa: E501
        :type: ClusterAnalysisDTO
        """

        self._cluster_analysis = cluster_analysis

    @property
    def name(self):
        """Gets the name of this FeaturegroupDTO.  # noqa: E501


        :return: The name of this FeaturegroupDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeaturegroupDTO.


        :param name: The name of this FeaturegroupDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this FeaturegroupDTO.  # noqa: E501


        :return: The id of this FeaturegroupDTO.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FeaturegroupDTO.


        :param id: The id of this FeaturegroupDTO.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def features(self):
        """Gets the features of this FeaturegroupDTO.  # noqa: E501


        :return: The features of this FeaturegroupDTO.  # noqa: E501
        :rtype: list[FeatureDTO]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this FeaturegroupDTO.


        :param features: The features of this FeaturegroupDTO.  # noqa: E501
        :type: list[FeatureDTO]
        """

        self._features = features

    @property
    def location(self):
        """Gets the location of this FeaturegroupDTO.  # noqa: E501


        :return: The location of this FeaturegroupDTO.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this FeaturegroupDTO.


        :param location: The location of this FeaturegroupDTO.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def jobs(self):
        """Gets the jobs of this FeaturegroupDTO.  # noqa: E501


        :return: The jobs of this FeaturegroupDTO.  # noqa: E501
        :rtype: list[FeaturestoreJobDTO]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this FeaturegroupDTO.


        :param jobs: The jobs of this FeaturegroupDTO.  # noqa: E501
        :type: list[FeaturestoreJobDTO]
        """

        self._jobs = jobs

    @property
    def featuregroup_type(self):
        """Gets the featuregroup_type of this FeaturegroupDTO.  # noqa: E501


        :return: The featuregroup_type of this FeaturegroupDTO.  # noqa: E501
        :rtype: str
        """
        return self._featuregroup_type

    @featuregroup_type.setter
    def featuregroup_type(self, featuregroup_type):
        """Sets the featuregroup_type of this FeaturegroupDTO.


        :param featuregroup_type: The featuregroup_type of this FeaturegroupDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["CACHED_FEATURE_GROUP", "ON_DEMAND_FEATURE_GROUP"]  # noqa: E501
        if featuregroup_type not in allowed_values:
            raise ValueError(
                "Invalid value for `featuregroup_type` ({0}), must be one of {1}"  # noqa: E501
                .format(featuregroup_type, allowed_values)
            )

        self._featuregroup_type = featuregroup_type

    @property
    def desc_stats_enabled(self):
        """Gets the desc_stats_enabled of this FeaturegroupDTO.  # noqa: E501


        :return: The desc_stats_enabled of this FeaturegroupDTO.  # noqa: E501
        :rtype: bool
        """
        return self._desc_stats_enabled

    @desc_stats_enabled.setter
    def desc_stats_enabled(self, desc_stats_enabled):
        """Sets the desc_stats_enabled of this FeaturegroupDTO.


        :param desc_stats_enabled: The desc_stats_enabled of this FeaturegroupDTO.  # noqa: E501
        :type: bool
        """

        self._desc_stats_enabled = desc_stats_enabled

    @property
    def feat_corr_enabled(self):
        """Gets the feat_corr_enabled of this FeaturegroupDTO.  # noqa: E501


        :return: The feat_corr_enabled of this FeaturegroupDTO.  # noqa: E501
        :rtype: bool
        """
        return self._feat_corr_enabled

    @feat_corr_enabled.setter
    def feat_corr_enabled(self, feat_corr_enabled):
        """Sets the feat_corr_enabled of this FeaturegroupDTO.


        :param feat_corr_enabled: The feat_corr_enabled of this FeaturegroupDTO.  # noqa: E501
        :type: bool
        """

        self._feat_corr_enabled = feat_corr_enabled

    @property
    def feat_hist_enabled(self):
        """Gets the feat_hist_enabled of this FeaturegroupDTO.  # noqa: E501


        :return: The feat_hist_enabled of this FeaturegroupDTO.  # noqa: E501
        :rtype: bool
        """
        return self._feat_hist_enabled

    @feat_hist_enabled.setter
    def feat_hist_enabled(self, feat_hist_enabled):
        """Sets the feat_hist_enabled of this FeaturegroupDTO.


        :param feat_hist_enabled: The feat_hist_enabled of this FeaturegroupDTO.  # noqa: E501
        :type: bool
        """

        self._feat_hist_enabled = feat_hist_enabled

    @property
    def cluster_analysis_enabled(self):
        """Gets the cluster_analysis_enabled of this FeaturegroupDTO.  # noqa: E501


        :return: The cluster_analysis_enabled of this FeaturegroupDTO.  # noqa: E501
        :rtype: bool
        """
        return self._cluster_analysis_enabled

    @cluster_analysis_enabled.setter
    def cluster_analysis_enabled(self, cluster_analysis_enabled):
        """Sets the cluster_analysis_enabled of this FeaturegroupDTO.


        :param cluster_analysis_enabled: The cluster_analysis_enabled of this FeaturegroupDTO.  # noqa: E501
        :type: bool
        """

        self._cluster_analysis_enabled = cluster_analysis_enabled

    @property
    def statistic_columns(self):
        """Gets the statistic_columns of this FeaturegroupDTO.  # noqa: E501


        :return: The statistic_columns of this FeaturegroupDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._statistic_columns

    @statistic_columns.setter
    def statistic_columns(self, statistic_columns):
        """Sets the statistic_columns of this FeaturegroupDTO.


        :param statistic_columns: The statistic_columns of this FeaturegroupDTO.  # noqa: E501
        :type: list[str]
        """

        self._statistic_columns = statistic_columns

    @property
    def num_bins(self):
        """Gets the num_bins of this FeaturegroupDTO.  # noqa: E501


        :return: The num_bins of this FeaturegroupDTO.  # noqa: E501
        :rtype: int
        """
        return self._num_bins

    @num_bins.setter
    def num_bins(self, num_bins):
        """Sets the num_bins of this FeaturegroupDTO.


        :param num_bins: The num_bins of this FeaturegroupDTO.  # noqa: E501
        :type: int
        """

        self._num_bins = num_bins

    @property
    def num_clusters(self):
        """Gets the num_clusters of this FeaturegroupDTO.  # noqa: E501


        :return: The num_clusters of this FeaturegroupDTO.  # noqa: E501
        :rtype: int
        """
        return self._num_clusters

    @num_clusters.setter
    def num_clusters(self, num_clusters):
        """Sets the num_clusters of this FeaturegroupDTO.


        :param num_clusters: The num_clusters of this FeaturegroupDTO.  # noqa: E501
        :type: int
        """

        self._num_clusters = num_clusters

    @property
    def corr_method(self):
        """Gets the corr_method of this FeaturegroupDTO.  # noqa: E501


        :return: The corr_method of this FeaturegroupDTO.  # noqa: E501
        :rtype: str
        """
        return self._corr_method

    @corr_method.setter
    def corr_method(self, corr_method):
        """Sets the corr_method of this FeaturegroupDTO.


        :param corr_method: The corr_method of this FeaturegroupDTO.  # noqa: E501
        :type: str
        """

        self._corr_method = corr_method

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
        if issubclass(FeaturegroupDTO, dict):
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
        if not isinstance(other, FeaturegroupDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
