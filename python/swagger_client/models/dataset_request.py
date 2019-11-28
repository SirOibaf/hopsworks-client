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
from swagger_client.models.dataset import Dataset  # noqa: F401,E501
from swagger_client.models.message import Message  # noqa: F401,E501
from swagger_client.models.project_team import ProjectTeam  # noqa: F401,E501


class DatasetRequest(object):
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
        'id': 'int',
        'requested': 'datetime',
        'message_content': 'str',
        'dataset': 'Dataset',
        'project_team': 'ProjectTeam',
        'message': 'Message'
    }

    attribute_map = {
        'id': 'id',
        'requested': 'requested',
        'message_content': 'messageContent',
        'dataset': 'dataset',
        'project_team': 'projectTeam',
        'message': 'message'
    }

    def __init__(self, id=None, requested=None, message_content=None, dataset=None, project_team=None, message=None):  # noqa: E501
        """DatasetRequest - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._requested = None
        self._message_content = None
        self._dataset = None
        self._project_team = None
        self._message = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.requested = requested
        if message_content is not None:
            self.message_content = message_content
        if dataset is not None:
            self.dataset = dataset
        if project_team is not None:
            self.project_team = project_team
        if message is not None:
            self.message = message

    @property
    def id(self):
        """Gets the id of this DatasetRequest.  # noqa: E501


        :return: The id of this DatasetRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatasetRequest.


        :param id: The id of this DatasetRequest.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def requested(self):
        """Gets the requested of this DatasetRequest.  # noqa: E501


        :return: The requested of this DatasetRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._requested

    @requested.setter
    def requested(self, requested):
        """Sets the requested of this DatasetRequest.


        :param requested: The requested of this DatasetRequest.  # noqa: E501
        :type: datetime
        """
        if requested is None:
            raise ValueError("Invalid value for `requested`, must not be `None`")  # noqa: E501

        self._requested = requested

    @property
    def message_content(self):
        """Gets the message_content of this DatasetRequest.  # noqa: E501


        :return: The message_content of this DatasetRequest.  # noqa: E501
        :rtype: str
        """
        return self._message_content

    @message_content.setter
    def message_content(self, message_content):
        """Sets the message_content of this DatasetRequest.


        :param message_content: The message_content of this DatasetRequest.  # noqa: E501
        :type: str
        """

        self._message_content = message_content

    @property
    def dataset(self):
        """Gets the dataset of this DatasetRequest.  # noqa: E501


        :return: The dataset of this DatasetRequest.  # noqa: E501
        :rtype: Dataset
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this DatasetRequest.


        :param dataset: The dataset of this DatasetRequest.  # noqa: E501
        :type: Dataset
        """

        self._dataset = dataset

    @property
    def project_team(self):
        """Gets the project_team of this DatasetRequest.  # noqa: E501


        :return: The project_team of this DatasetRequest.  # noqa: E501
        :rtype: ProjectTeam
        """
        return self._project_team

    @project_team.setter
    def project_team(self, project_team):
        """Sets the project_team of this DatasetRequest.


        :param project_team: The project_team of this DatasetRequest.  # noqa: E501
        :type: ProjectTeam
        """

        self._project_team = project_team

    @property
    def message(self):
        """Gets the message of this DatasetRequest.  # noqa: E501


        :return: The message of this DatasetRequest.  # noqa: E501
        :rtype: Message
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DatasetRequest.


        :param message: The message of this DatasetRequest.  # noqa: E501
        :type: Message
        """

        self._message = message

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
        if issubclass(DatasetRequest, dict):
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
        if not isinstance(other, DatasetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
