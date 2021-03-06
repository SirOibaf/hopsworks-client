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


class FeaturegroupImportJobDTO(object):
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
        'type': 'str',
        'storage_connector': 'str',
        'path': 'str',
        'featuregroup': 'str',
        'primary_key': 'list[str]',
        'description': 'str',
        'featurestore': 'str',
        'featuregroup_version': 'int',
        'jobs': 'str',
        'descriptive_statistics': 'bool',
        'feature_correlation': 'bool',
        'feature_histograms': 'bool',
        'cluster_analysis': 'bool',
        'stats_column': 'list[str]',
        'num_bins': 'int',
        'corr_method': 'str',
        'num_clusters': 'int',
        'partition_by': 'list[str]',
        'data_format': 'str',
        'online': 'bool',
        'online_types': 'dict(str, str)',
        'offline': 'bool',
        'am_cores': 'int',
        'am_memory': 'int',
        'executor_cores': 'int',
        'executor_memory': 'int',
        'max_executors': 'int'
    }

    attribute_map = {
        'type': 'type',
        'storage_connector': 'storageConnector',
        'path': 'path',
        'featuregroup': 'featuregroup',
        'primary_key': 'primaryKey',
        'description': 'description',
        'featurestore': 'featurestore',
        'featuregroup_version': 'featuregroupVersion',
        'jobs': 'jobs',
        'descriptive_statistics': 'descriptiveStatistics',
        'feature_correlation': 'featureCorrelation',
        'feature_histograms': 'featureHistograms',
        'cluster_analysis': 'clusterAnalysis',
        'stats_column': 'statsColumn',
        'num_bins': 'numBins',
        'corr_method': 'corrMethod',
        'num_clusters': 'num_clusters',
        'partition_by': 'partitionBy',
        'data_format': 'dataFormat',
        'online': 'online',
        'online_types': 'onlineTypes',
        'offline': 'offline',
        'am_cores': 'amCores',
        'am_memory': 'amMemory',
        'executor_cores': 'executorCores',
        'executor_memory': 'executorMemory',
        'max_executors': 'maxExecutors'
    }

    def __init__(self, type=None, storage_connector=None, path=None, featuregroup=None, primary_key=None, description=None, featurestore=None, featuregroup_version=None, jobs=None, descriptive_statistics=None, feature_correlation=None, feature_histograms=None, cluster_analysis=None, stats_column=None, num_bins=None, corr_method=None, num_clusters=None, partition_by=None, data_format=None, online=None, online_types=None, offline=None, am_cores=None, am_memory=None, executor_cores=None, executor_memory=None, max_executors=None):  # noqa: E501
        """FeaturegroupImportJobDTO - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._storage_connector = None
        self._path = None
        self._featuregroup = None
        self._primary_key = None
        self._description = None
        self._featurestore = None
        self._featuregroup_version = None
        self._jobs = None
        self._descriptive_statistics = None
        self._feature_correlation = None
        self._feature_histograms = None
        self._cluster_analysis = None
        self._stats_column = None
        self._num_bins = None
        self._corr_method = None
        self._num_clusters = None
        self._partition_by = None
        self._data_format = None
        self._online = None
        self._online_types = None
        self._offline = None
        self._am_cores = None
        self._am_memory = None
        self._executor_cores = None
        self._executor_memory = None
        self._max_executors = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if storage_connector is not None:
            self.storage_connector = storage_connector
        if path is not None:
            self.path = path
        if featuregroup is not None:
            self.featuregroup = featuregroup
        if primary_key is not None:
            self.primary_key = primary_key
        if description is not None:
            self.description = description
        if featurestore is not None:
            self.featurestore = featurestore
        if featuregroup_version is not None:
            self.featuregroup_version = featuregroup_version
        if jobs is not None:
            self.jobs = jobs
        if descriptive_statistics is not None:
            self.descriptive_statistics = descriptive_statistics
        if feature_correlation is not None:
            self.feature_correlation = feature_correlation
        if feature_histograms is not None:
            self.feature_histograms = feature_histograms
        if cluster_analysis is not None:
            self.cluster_analysis = cluster_analysis
        if stats_column is not None:
            self.stats_column = stats_column
        if num_bins is not None:
            self.num_bins = num_bins
        if corr_method is not None:
            self.corr_method = corr_method
        if num_clusters is not None:
            self.num_clusters = num_clusters
        if partition_by is not None:
            self.partition_by = partition_by
        if data_format is not None:
            self.data_format = data_format
        if online is not None:
            self.online = online
        if online_types is not None:
            self.online_types = online_types
        if offline is not None:
            self.offline = offline
        if am_cores is not None:
            self.am_cores = am_cores
        if am_memory is not None:
            self.am_memory = am_memory
        if executor_cores is not None:
            self.executor_cores = executor_cores
        if executor_memory is not None:
            self.executor_memory = executor_memory
        if max_executors is not None:
            self.max_executors = max_executors

    @property
    def type(self):
        """Gets the type of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The type of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FeaturegroupImportJobDTO.


        :param type: The type of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["S3", "REDSHIFT"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def storage_connector(self):
        """Gets the storage_connector of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The storage_connector of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._storage_connector

    @storage_connector.setter
    def storage_connector(self, storage_connector):
        """Sets the storage_connector of this FeaturegroupImportJobDTO.


        :param storage_connector: The storage_connector of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: str
        """

        self._storage_connector = storage_connector

    @property
    def path(self):
        """Gets the path of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The path of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this FeaturegroupImportJobDTO.


        :param path: The path of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def featuregroup(self):
        """Gets the featuregroup of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The featuregroup of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._featuregroup

    @featuregroup.setter
    def featuregroup(self, featuregroup):
        """Sets the featuregroup of this FeaturegroupImportJobDTO.


        :param featuregroup: The featuregroup of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: str
        """

        self._featuregroup = featuregroup

    @property
    def primary_key(self):
        """Gets the primary_key of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The primary_key of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        """Sets the primary_key of this FeaturegroupImportJobDTO.


        :param primary_key: The primary_key of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: list[str]
        """

        self._primary_key = primary_key

    @property
    def description(self):
        """Gets the description of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The description of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FeaturegroupImportJobDTO.


        :param description: The description of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def featurestore(self):
        """Gets the featurestore of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The featurestore of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._featurestore

    @featurestore.setter
    def featurestore(self, featurestore):
        """Sets the featurestore of this FeaturegroupImportJobDTO.


        :param featurestore: The featurestore of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: str
        """

        self._featurestore = featurestore

    @property
    def featuregroup_version(self):
        """Gets the featuregroup_version of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The featuregroup_version of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._featuregroup_version

    @featuregroup_version.setter
    def featuregroup_version(self, featuregroup_version):
        """Sets the featuregroup_version of this FeaturegroupImportJobDTO.


        :param featuregroup_version: The featuregroup_version of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: int
        """

        self._featuregroup_version = featuregroup_version

    @property
    def jobs(self):
        """Gets the jobs of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The jobs of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this FeaturegroupImportJobDTO.


        :param jobs: The jobs of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: str
        """

        self._jobs = jobs

    @property
    def descriptive_statistics(self):
        """Gets the descriptive_statistics of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The descriptive_statistics of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: bool
        """
        return self._descriptive_statistics

    @descriptive_statistics.setter
    def descriptive_statistics(self, descriptive_statistics):
        """Sets the descriptive_statistics of this FeaturegroupImportJobDTO.


        :param descriptive_statistics: The descriptive_statistics of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: bool
        """

        self._descriptive_statistics = descriptive_statistics

    @property
    def feature_correlation(self):
        """Gets the feature_correlation of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The feature_correlation of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: bool
        """
        return self._feature_correlation

    @feature_correlation.setter
    def feature_correlation(self, feature_correlation):
        """Sets the feature_correlation of this FeaturegroupImportJobDTO.


        :param feature_correlation: The feature_correlation of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: bool
        """

        self._feature_correlation = feature_correlation

    @property
    def feature_histograms(self):
        """Gets the feature_histograms of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The feature_histograms of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: bool
        """
        return self._feature_histograms

    @feature_histograms.setter
    def feature_histograms(self, feature_histograms):
        """Sets the feature_histograms of this FeaturegroupImportJobDTO.


        :param feature_histograms: The feature_histograms of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: bool
        """

        self._feature_histograms = feature_histograms

    @property
    def cluster_analysis(self):
        """Gets the cluster_analysis of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The cluster_analysis of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: bool
        """
        return self._cluster_analysis

    @cluster_analysis.setter
    def cluster_analysis(self, cluster_analysis):
        """Sets the cluster_analysis of this FeaturegroupImportJobDTO.


        :param cluster_analysis: The cluster_analysis of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: bool
        """

        self._cluster_analysis = cluster_analysis

    @property
    def stats_column(self):
        """Gets the stats_column of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The stats_column of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._stats_column

    @stats_column.setter
    def stats_column(self, stats_column):
        """Sets the stats_column of this FeaturegroupImportJobDTO.


        :param stats_column: The stats_column of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: list[str]
        """

        self._stats_column = stats_column

    @property
    def num_bins(self):
        """Gets the num_bins of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The num_bins of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._num_bins

    @num_bins.setter
    def num_bins(self, num_bins):
        """Sets the num_bins of this FeaturegroupImportJobDTO.


        :param num_bins: The num_bins of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: int
        """

        self._num_bins = num_bins

    @property
    def corr_method(self):
        """Gets the corr_method of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The corr_method of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._corr_method

    @corr_method.setter
    def corr_method(self, corr_method):
        """Sets the corr_method of this FeaturegroupImportJobDTO.


        :param corr_method: The corr_method of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: str
        """

        self._corr_method = corr_method

    @property
    def num_clusters(self):
        """Gets the num_clusters of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The num_clusters of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._num_clusters

    @num_clusters.setter
    def num_clusters(self, num_clusters):
        """Sets the num_clusters of this FeaturegroupImportJobDTO.


        :param num_clusters: The num_clusters of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: int
        """

        self._num_clusters = num_clusters

    @property
    def partition_by(self):
        """Gets the partition_by of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The partition_by of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._partition_by

    @partition_by.setter
    def partition_by(self, partition_by):
        """Sets the partition_by of this FeaturegroupImportJobDTO.


        :param partition_by: The partition_by of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: list[str]
        """

        self._partition_by = partition_by

    @property
    def data_format(self):
        """Gets the data_format of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The data_format of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """Sets the data_format of this FeaturegroupImportJobDTO.


        :param data_format: The data_format of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: str
        """

        self._data_format = data_format

    @property
    def online(self):
        """Gets the online of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The online of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this FeaturegroupImportJobDTO.


        :param online: The online of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: bool
        """

        self._online = online

    @property
    def online_types(self):
        """Gets the online_types of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The online_types of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._online_types

    @online_types.setter
    def online_types(self, online_types):
        """Sets the online_types of this FeaturegroupImportJobDTO.


        :param online_types: The online_types of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._online_types = online_types

    @property
    def offline(self):
        """Gets the offline of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The offline of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: bool
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """Sets the offline of this FeaturegroupImportJobDTO.


        :param offline: The offline of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: bool
        """

        self._offline = offline

    @property
    def am_cores(self):
        """Gets the am_cores of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The am_cores of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._am_cores

    @am_cores.setter
    def am_cores(self, am_cores):
        """Sets the am_cores of this FeaturegroupImportJobDTO.


        :param am_cores: The am_cores of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: int
        """

        self._am_cores = am_cores

    @property
    def am_memory(self):
        """Gets the am_memory of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The am_memory of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._am_memory

    @am_memory.setter
    def am_memory(self, am_memory):
        """Sets the am_memory of this FeaturegroupImportJobDTO.


        :param am_memory: The am_memory of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: int
        """

        self._am_memory = am_memory

    @property
    def executor_cores(self):
        """Gets the executor_cores of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The executor_cores of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._executor_cores

    @executor_cores.setter
    def executor_cores(self, executor_cores):
        """Sets the executor_cores of this FeaturegroupImportJobDTO.


        :param executor_cores: The executor_cores of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: int
        """

        self._executor_cores = executor_cores

    @property
    def executor_memory(self):
        """Gets the executor_memory of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The executor_memory of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._executor_memory

    @executor_memory.setter
    def executor_memory(self, executor_memory):
        """Sets the executor_memory of this FeaturegroupImportJobDTO.


        :param executor_memory: The executor_memory of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: int
        """

        self._executor_memory = executor_memory

    @property
    def max_executors(self):
        """Gets the max_executors of this FeaturegroupImportJobDTO.  # noqa: E501


        :return: The max_executors of this FeaturegroupImportJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._max_executors

    @max_executors.setter
    def max_executors(self, max_executors):
        """Sets the max_executors of this FeaturegroupImportJobDTO.


        :param max_executors: The max_executors of this FeaturegroupImportJobDTO.  # noqa: E501
        :type: int
        """

        self._max_executors = max_executors

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
        if issubclass(FeaturegroupImportJobDTO, dict):
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
        if not isinstance(other, FeaturegroupImportJobDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
