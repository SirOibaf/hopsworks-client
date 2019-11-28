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


class AirflowOperatorDTO(object):
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
        'name': 'str',
        'id': 'str',
        'job_name': 'str',
        'wait': 'bool',
        'depends_on': 'list[str]',
        'feature_group_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'job_name': 'jobName',
        'wait': 'wait',
        'depends_on': 'dependsOn',
        'feature_group_name': 'featureGroupName'
    }

    def __init__(self, name=None, id=None, job_name=None, wait=None, depends_on=None, feature_group_name=None):  # noqa: E501
        """AirflowOperatorDTO - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._id = None
        self._job_name = None
        self._wait = None
        self._depends_on = None
        self._feature_group_name = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if job_name is not None:
            self.job_name = job_name
        if wait is not None:
            self.wait = wait
        if depends_on is not None:
            self.depends_on = depends_on
        if feature_group_name is not None:
            self.feature_group_name = feature_group_name

    @property
    def name(self):
        """Gets the name of this AirflowOperatorDTO.  # noqa: E501


        :return: The name of this AirflowOperatorDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AirflowOperatorDTO.


        :param name: The name of this AirflowOperatorDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this AirflowOperatorDTO.  # noqa: E501


        :return: The id of this AirflowOperatorDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AirflowOperatorDTO.


        :param id: The id of this AirflowOperatorDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def job_name(self):
        """Gets the job_name of this AirflowOperatorDTO.  # noqa: E501


        :return: The job_name of this AirflowOperatorDTO.  # noqa: E501
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this AirflowOperatorDTO.


        :param job_name: The job_name of this AirflowOperatorDTO.  # noqa: E501
        :type: str
        """

        self._job_name = job_name

    @property
    def wait(self):
        """Gets the wait of this AirflowOperatorDTO.  # noqa: E501


        :return: The wait of this AirflowOperatorDTO.  # noqa: E501
        :rtype: bool
        """
        return self._wait

    @wait.setter
    def wait(self, wait):
        """Sets the wait of this AirflowOperatorDTO.


        :param wait: The wait of this AirflowOperatorDTO.  # noqa: E501
        :type: bool
        """

        self._wait = wait

    @property
    def depends_on(self):
        """Gets the depends_on of this AirflowOperatorDTO.  # noqa: E501


        :return: The depends_on of this AirflowOperatorDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._depends_on

    @depends_on.setter
    def depends_on(self, depends_on):
        """Sets the depends_on of this AirflowOperatorDTO.


        :param depends_on: The depends_on of this AirflowOperatorDTO.  # noqa: E501
        :type: list[str]
        """

        self._depends_on = depends_on

    @property
    def feature_group_name(self):
        """Gets the feature_group_name of this AirflowOperatorDTO.  # noqa: E501


        :return: The feature_group_name of this AirflowOperatorDTO.  # noqa: E501
        :rtype: str
        """
        return self._feature_group_name

    @feature_group_name.setter
    def feature_group_name(self, feature_group_name):
        """Sets the feature_group_name of this AirflowOperatorDTO.


        :param feature_group_name: The feature_group_name of this AirflowOperatorDTO.  # noqa: E501
        :type: str
        """

        self._feature_group_name = feature_group_name

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
        if issubclass(AirflowOperatorDTO, dict):
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
        if not isinstance(other, AirflowOperatorDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other