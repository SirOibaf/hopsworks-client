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


class FeaturestoreJobDTO(object):
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
        'job_id': 'int',
        'job_name': 'str',
        'last_computed': 'datetime',
        'job_status': 'str',
        'featurestore_id': 'int',
        'featuregroup_id': 'int',
        'training_dataset_id': 'int'
    }

    attribute_map = {
        'job_id': 'jobId',
        'job_name': 'jobName',
        'last_computed': 'lastComputed',
        'job_status': 'jobStatus',
        'featurestore_id': 'featurestoreId',
        'featuregroup_id': 'featuregroupId',
        'training_dataset_id': 'trainingDatasetId'
    }

    def __init__(self, job_id=None, job_name=None, last_computed=None, job_status=None, featurestore_id=None, featuregroup_id=None, training_dataset_id=None):  # noqa: E501
        """FeaturestoreJobDTO - a model defined in Swagger"""  # noqa: E501
        self._job_id = None
        self._job_name = None
        self._last_computed = None
        self._job_status = None
        self._featurestore_id = None
        self._featuregroup_id = None
        self._training_dataset_id = None
        self.discriminator = None
        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if last_computed is not None:
            self.last_computed = last_computed
        if job_status is not None:
            self.job_status = job_status
        if featurestore_id is not None:
            self.featurestore_id = featurestore_id
        if featuregroup_id is not None:
            self.featuregroup_id = featuregroup_id
        if training_dataset_id is not None:
            self.training_dataset_id = training_dataset_id

    @property
    def job_id(self):
        """Gets the job_id of this FeaturestoreJobDTO.  # noqa: E501


        :return: The job_id of this FeaturestoreJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this FeaturestoreJobDTO.


        :param job_id: The job_id of this FeaturestoreJobDTO.  # noqa: E501
        :type: int
        """

        self._job_id = job_id

    @property
    def job_name(self):
        """Gets the job_name of this FeaturestoreJobDTO.  # noqa: E501


        :return: The job_name of this FeaturestoreJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this FeaturestoreJobDTO.


        :param job_name: The job_name of this FeaturestoreJobDTO.  # noqa: E501
        :type: str
        """

        self._job_name = job_name

    @property
    def last_computed(self):
        """Gets the last_computed of this FeaturestoreJobDTO.  # noqa: E501


        :return: The last_computed of this FeaturestoreJobDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_computed

    @last_computed.setter
    def last_computed(self, last_computed):
        """Sets the last_computed of this FeaturestoreJobDTO.


        :param last_computed: The last_computed of this FeaturestoreJobDTO.  # noqa: E501
        :type: datetime
        """

        self._last_computed = last_computed

    @property
    def job_status(self):
        """Gets the job_status of this FeaturestoreJobDTO.  # noqa: E501


        :return: The job_status of this FeaturestoreJobDTO.  # noqa: E501
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this FeaturestoreJobDTO.


        :param job_status: The job_status of this FeaturestoreJobDTO.  # noqa: E501
        :type: str
        """

        self._job_status = job_status

    @property
    def featurestore_id(self):
        """Gets the featurestore_id of this FeaturestoreJobDTO.  # noqa: E501


        :return: The featurestore_id of this FeaturestoreJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._featurestore_id

    @featurestore_id.setter
    def featurestore_id(self, featurestore_id):
        """Sets the featurestore_id of this FeaturestoreJobDTO.


        :param featurestore_id: The featurestore_id of this FeaturestoreJobDTO.  # noqa: E501
        :type: int
        """

        self._featurestore_id = featurestore_id

    @property
    def featuregroup_id(self):
        """Gets the featuregroup_id of this FeaturestoreJobDTO.  # noqa: E501


        :return: The featuregroup_id of this FeaturestoreJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._featuregroup_id

    @featuregroup_id.setter
    def featuregroup_id(self, featuregroup_id):
        """Sets the featuregroup_id of this FeaturestoreJobDTO.


        :param featuregroup_id: The featuregroup_id of this FeaturestoreJobDTO.  # noqa: E501
        :type: int
        """

        self._featuregroup_id = featuregroup_id

    @property
    def training_dataset_id(self):
        """Gets the training_dataset_id of this FeaturestoreJobDTO.  # noqa: E501


        :return: The training_dataset_id of this FeaturestoreJobDTO.  # noqa: E501
        :rtype: int
        """
        return self._training_dataset_id

    @training_dataset_id.setter
    def training_dataset_id(self, training_dataset_id):
        """Sets the training_dataset_id of this FeaturestoreJobDTO.


        :param training_dataset_id: The training_dataset_id of this FeaturestoreJobDTO.  # noqa: E501
        :type: int
        """

        self._training_dataset_id = training_dataset_id

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
        if issubclass(FeaturestoreJobDTO, dict):
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
        if not isinstance(other, FeaturestoreJobDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
