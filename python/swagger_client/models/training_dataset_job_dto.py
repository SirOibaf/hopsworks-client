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


class TrainingDatasetJobDTO(object):
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
        'features': 'list[str]',
        'sql_query': 'str',
        'training_dataset': 'str',
        'featuregroups_version_dict': 'str',
        'join_key': 'str',
        'description': 'str',
        'featurestore': 'str',
        'data_format': 'str',
        'training_dataset_version': 'int',
        'overwrite': 'bool',
        'jobs': 'list[str]',
        'online': 'bool',
        'descriptive_statistics': 'bool',
        'feature_correlation': 'bool',
        'feature_histograms': 'bool',
        'cluster_analysis': 'bool',
        'stat_columns': 'list[str]',
        'num_bins': 'int',
        'correlation_method': 'str',
        'num_clusters': 'int',
        'fixed': 'bool',
        'sink': 'str',
        'am_cores': 'int',
        'am_memory': 'int',
        'executor_cores': 'int',
        'executor_memory': 'int',
        'max_executors': 'int',
        'path': 'str'
    }

    attribute_map = {
        'features': 'features',
        'sql_query': 'sqlQuery',
        'training_dataset': 'trainingDataset',
        'featuregroups_version_dict': 'featuregroupsVersionDict',
        'join_key': 'joinKey',
        'description': 'description',
        'featurestore': 'featurestore',
        'data_format': 'dataFormat',
        'training_dataset_version': 'trainingDatasetVersion',
        'overwrite': 'overwrite',
        'jobs': 'jobs',
        'online': 'online',
        'descriptive_statistics': 'descriptiveStatistics',
        'feature_correlation': 'featureCorrelation',
        'feature_histograms': 'featureHistograms',
        'cluster_analysis': 'clusterAnalysis',
        'stat_columns': 'statColumns',
        'num_bins': 'numBins',
        'correlation_method': 'correlationMethod',
        'num_clusters': 'numClusters',
        'fixed': 'fixed',
        'sink': 'sink',
        'am_cores': 'amCores',
        'am_memory': 'amMemory',
        'executor_cores': 'executorCores',
        'executor_memory': 'executorMemory',
        'max_executors': 'maxExecutors',
        'path': 'path'
    }

    def __init__(self, features=None, sql_query=None, training_dataset=None, featuregroups_version_dict=None, join_key=None, description=None, featurestore=None, data_format=None, training_dataset_version=None, overwrite=None, jobs=None, online=None, descriptive_statistics=None, feature_correlation=None, feature_histograms=None, cluster_analysis=None, stat_columns=None, num_bins=None, correlation_method=None, num_clusters=None, fixed=None, sink=None, am_cores=None, am_memory=None, executor_cores=None, executor_memory=None, max_executors=None, path=None):  # noqa: E501
        """TrainingDatasetJobDTO - a model defined in Swagger"""  # noqa: E501
        self._features = None
        self._sql_query = None
        self._training_dataset = None
        self._featuregroups_version_dict = None
        self._join_key = None
        self._description = None
        self._featurestore = None
        self._data_format = None
        self._training_dataset_version = None
        self._overwrite = None
        self._jobs = None
        self._online = None
        self._descriptive_statistics = None
        self._feature_correlation = None
        self._feature_histograms = None
        self._cluster_analysis = None
        self._stat_columns = None
        self._num_bins = None
        self._correlation_method = None
        self._num_clusters = None
        self._fixed = None
        self._sink = None
        self._am_cores = None
        self._am_memory = None
        self._executor_cores = None
        self._executor_memory = None
        self._max_executors = None
        self._path = None
        self.discriminator = None
        if features is not None:
            self.features = features
        if sql_query is not None:
            self.sql_query = sql_query
        if training_dataset is not None:
            self.training_dataset = training_dataset
        if featuregroups_version_dict is not None:
            self.featuregroups_version_dict = featuregroups_version_dict
        if join_key is not None:
            self.join_key = join_key
        if description is not None:
            self.description = description
        if featurestore is not None:
            self.featurestore = featurestore
        if data_format is not None:
            self.data_format = data_format
        if training_dataset_version is not None:
            self.training_dataset_version = training_dataset_version
        if overwrite is not None:
            self.overwrite = overwrite
        if jobs is not None:
            self.jobs = jobs
        if online is not None:
            self.online = online
        if descriptive_statistics is not None:
            self.descriptive_statistics = descriptive_statistics
        if feature_correlation is not None:
            self.feature_correlation = feature_correlation
        if feature_histograms is not None:
            self.feature_histograms = feature_histograms
        if cluster_analysis is not None:
            self.cluster_analysis = cluster_analysis
        if stat_columns is not None:
            self.stat_columns = stat_columns
        if num_bins is not None:
            self.num_bins = num_bins
        if correlation_method is not None:
            self.correlation_method = correlation_method
        if num_clusters is not None:
            self.num_clusters = num_clusters
        if fixed is not None:
            self.fixed = fixed
        if sink is not None:
            self.sink = sink
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
        if path is not None:
            self.path = path

    @property
    def features(self):
        """Gets the features of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The features of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this TrainingDatasetJobDTO.


        :param features: The features of this TrainingDatasetJobDTO.  # noqa: E501
        :type: list[str]
        """

        self._features = features

    @property
    def sql_query(self):
        """Gets the sql_query of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The sql_query of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._sql_query

    @sql_query.setter
    def sql_query(self, sql_query):
        """Sets the sql_query of this TrainingDatasetJobDTO.


        :param sql_query: The sql_query of this TrainingDatasetJobDTO.  # noqa: E501
        :type: str
        """

        self._sql_query = sql_query

    @property
    def training_dataset(self):
        """Gets the training_dataset of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The training_dataset of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._training_dataset

    @training_dataset.setter
    def training_dataset(self, training_dataset):
        """Sets the training_dataset of this TrainingDatasetJobDTO.


        :param training_dataset: The training_dataset of this TrainingDatasetJobDTO.  # noqa: E501
        :type: str
        """

        self._training_dataset = training_dataset

    @property
    def featuregroups_version_dict(self):
        """Gets the featuregroups_version_dict of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The featuregroups_version_dict of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._featuregroups_version_dict

    @featuregroups_version_dict.setter
    def featuregroups_version_dict(self, featuregroups_version_dict):
        """Sets the featuregroups_version_dict of this TrainingDatasetJobDTO.


        :param featuregroups_version_dict: The featuregroups_version_dict of this TrainingDatasetJobDTO.  # noqa: E501
        :type: str
        """

        self._featuregroups_version_dict = featuregroups_version_dict

    @property
    def join_key(self):
        """Gets the join_key of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The join_key of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._join_key

    @join_key.setter
    def join_key(self, join_key):
        """Sets the join_key of this TrainingDatasetJobDTO.


        :param join_key: The join_key of this TrainingDatasetJobDTO.  # noqa: E501
        :type: str
        """

        self._join_key = join_key

    @property
    def description(self):
        """Gets the description of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The description of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TrainingDatasetJobDTO.


        :param description: The description of this TrainingDatasetJobDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def featurestore(self):
        """Gets the featurestore of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The featurestore of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._featurestore

    @featurestore.setter
    def featurestore(self, featurestore):
        """Sets the featurestore of this TrainingDatasetJobDTO.


        :param featurestore: The featurestore of this TrainingDatasetJobDTO.  # noqa: E501
        :type: str
        """

        self._featurestore = featurestore

    @property
    def data_format(self):
        """Gets the data_format of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The data_format of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """Sets the data_format of this TrainingDatasetJobDTO.


        :param data_format: The data_format of this TrainingDatasetJobDTO.  # noqa: E501
        :type: str
        """

        self._data_format = data_format

    @property
    def training_dataset_version(self):
        """Gets the training_dataset_version of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The training_dataset_version of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._training_dataset_version

    @training_dataset_version.setter
    def training_dataset_version(self, training_dataset_version):
        """Sets the training_dataset_version of this TrainingDatasetJobDTO.


        :param training_dataset_version: The training_dataset_version of this TrainingDatasetJobDTO.  # noqa: E501
        :type: int
        """

        self._training_dataset_version = training_dataset_version

    @property
    def overwrite(self):
        """Gets the overwrite of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The overwrite of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: bool
        """
        return self._overwrite

    @overwrite.setter
    def overwrite(self, overwrite):
        """Sets the overwrite of this TrainingDatasetJobDTO.


        :param overwrite: The overwrite of this TrainingDatasetJobDTO.  # noqa: E501
        :type: bool
        """

        self._overwrite = overwrite

    @property
    def jobs(self):
        """Gets the jobs of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The jobs of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this TrainingDatasetJobDTO.


        :param jobs: The jobs of this TrainingDatasetJobDTO.  # noqa: E501
        :type: list[str]
        """

        self._jobs = jobs

    @property
    def online(self):
        """Gets the online of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The online of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this TrainingDatasetJobDTO.


        :param online: The online of this TrainingDatasetJobDTO.  # noqa: E501
        :type: bool
        """

        self._online = online

    @property
    def descriptive_statistics(self):
        """Gets the descriptive_statistics of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The descriptive_statistics of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: bool
        """
        return self._descriptive_statistics

    @descriptive_statistics.setter
    def descriptive_statistics(self, descriptive_statistics):
        """Sets the descriptive_statistics of this TrainingDatasetJobDTO.


        :param descriptive_statistics: The descriptive_statistics of this TrainingDatasetJobDTO.  # noqa: E501
        :type: bool
        """

        self._descriptive_statistics = descriptive_statistics

    @property
    def feature_correlation(self):
        """Gets the feature_correlation of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The feature_correlation of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: bool
        """
        return self._feature_correlation

    @feature_correlation.setter
    def feature_correlation(self, feature_correlation):
        """Sets the feature_correlation of this TrainingDatasetJobDTO.


        :param feature_correlation: The feature_correlation of this TrainingDatasetJobDTO.  # noqa: E501
        :type: bool
        """

        self._feature_correlation = feature_correlation

    @property
    def feature_histograms(self):
        """Gets the feature_histograms of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The feature_histograms of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: bool
        """
        return self._feature_histograms

    @feature_histograms.setter
    def feature_histograms(self, feature_histograms):
        """Sets the feature_histograms of this TrainingDatasetJobDTO.


        :param feature_histograms: The feature_histograms of this TrainingDatasetJobDTO.  # noqa: E501
        :type: bool
        """

        self._feature_histograms = feature_histograms

    @property
    def cluster_analysis(self):
        """Gets the cluster_analysis of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The cluster_analysis of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: bool
        """
        return self._cluster_analysis

    @cluster_analysis.setter
    def cluster_analysis(self, cluster_analysis):
        """Sets the cluster_analysis of this TrainingDatasetJobDTO.


        :param cluster_analysis: The cluster_analysis of this TrainingDatasetJobDTO.  # noqa: E501
        :type: bool
        """

        self._cluster_analysis = cluster_analysis

    @property
    def stat_columns(self):
        """Gets the stat_columns of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The stat_columns of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._stat_columns

    @stat_columns.setter
    def stat_columns(self, stat_columns):
        """Sets the stat_columns of this TrainingDatasetJobDTO.


        :param stat_columns: The stat_columns of this TrainingDatasetJobDTO.  # noqa: E501
        :type: list[str]
        """

        self._stat_columns = stat_columns

    @property
    def num_bins(self):
        """Gets the num_bins of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The num_bins of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._num_bins

    @num_bins.setter
    def num_bins(self, num_bins):
        """Sets the num_bins of this TrainingDatasetJobDTO.


        :param num_bins: The num_bins of this TrainingDatasetJobDTO.  # noqa: E501
        :type: int
        """

        self._num_bins = num_bins

    @property
    def correlation_method(self):
        """Gets the correlation_method of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The correlation_method of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._correlation_method

    @correlation_method.setter
    def correlation_method(self, correlation_method):
        """Sets the correlation_method of this TrainingDatasetJobDTO.


        :param correlation_method: The correlation_method of this TrainingDatasetJobDTO.  # noqa: E501
        :type: str
        """

        self._correlation_method = correlation_method

    @property
    def num_clusters(self):
        """Gets the num_clusters of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The num_clusters of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._num_clusters

    @num_clusters.setter
    def num_clusters(self, num_clusters):
        """Sets the num_clusters of this TrainingDatasetJobDTO.


        :param num_clusters: The num_clusters of this TrainingDatasetJobDTO.  # noqa: E501
        :type: int
        """

        self._num_clusters = num_clusters

    @property
    def fixed(self):
        """Gets the fixed of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The fixed of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: bool
        """
        return self._fixed

    @fixed.setter
    def fixed(self, fixed):
        """Sets the fixed of this TrainingDatasetJobDTO.


        :param fixed: The fixed of this TrainingDatasetJobDTO.  # noqa: E501
        :type: bool
        """

        self._fixed = fixed

    @property
    def sink(self):
        """Gets the sink of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The sink of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._sink

    @sink.setter
    def sink(self, sink):
        """Sets the sink of this TrainingDatasetJobDTO.


        :param sink: The sink of this TrainingDatasetJobDTO.  # noqa: E501
        :type: str
        """

        self._sink = sink

    @property
    def am_cores(self):
        """Gets the am_cores of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The am_cores of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._am_cores

    @am_cores.setter
    def am_cores(self, am_cores):
        """Sets the am_cores of this TrainingDatasetJobDTO.


        :param am_cores: The am_cores of this TrainingDatasetJobDTO.  # noqa: E501
        :type: int
        """

        self._am_cores = am_cores

    @property
    def am_memory(self):
        """Gets the am_memory of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The am_memory of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._am_memory

    @am_memory.setter
    def am_memory(self, am_memory):
        """Sets the am_memory of this TrainingDatasetJobDTO.


        :param am_memory: The am_memory of this TrainingDatasetJobDTO.  # noqa: E501
        :type: int
        """

        self._am_memory = am_memory

    @property
    def executor_cores(self):
        """Gets the executor_cores of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The executor_cores of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._executor_cores

    @executor_cores.setter
    def executor_cores(self, executor_cores):
        """Sets the executor_cores of this TrainingDatasetJobDTO.


        :param executor_cores: The executor_cores of this TrainingDatasetJobDTO.  # noqa: E501
        :type: int
        """

        self._executor_cores = executor_cores

    @property
    def executor_memory(self):
        """Gets the executor_memory of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The executor_memory of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._executor_memory

    @executor_memory.setter
    def executor_memory(self, executor_memory):
        """Sets the executor_memory of this TrainingDatasetJobDTO.


        :param executor_memory: The executor_memory of this TrainingDatasetJobDTO.  # noqa: E501
        :type: int
        """

        self._executor_memory = executor_memory

    @property
    def max_executors(self):
        """Gets the max_executors of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The max_executors of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._max_executors

    @max_executors.setter
    def max_executors(self, max_executors):
        """Sets the max_executors of this TrainingDatasetJobDTO.


        :param max_executors: The max_executors of this TrainingDatasetJobDTO.  # noqa: E501
        :type: int
        """

        self._max_executors = max_executors

    @property
    def path(self):
        """Gets the path of this TrainingDatasetJobDTO.  # noqa: E501


        :return: The path of this TrainingDatasetJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this TrainingDatasetJobDTO.


        :param path: The path of this TrainingDatasetJobDTO.  # noqa: E501
        :type: str
        """

        self._path = path

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
        if issubclass(TrainingDatasetJobDTO, dict):
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
        if not isinstance(other, TrainingDatasetJobDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other