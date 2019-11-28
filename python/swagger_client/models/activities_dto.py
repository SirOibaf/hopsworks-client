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
from swagger_client.models.activities_dto import ActivitiesDTO  # noqa: F401,E501
from swagger_client.models.user_dto import UserDTO  # noqa: F401,E501


class ActivitiesDTO(object):
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
        'href': 'str',
        'items': 'list[ActivitiesDTO]',
        'count': 'int',
        'activity': 'str',
        'timestamp': 'datetime',
        'project_name': 'str',
        'flag': 'str',
        'user': 'UserDTO'
    }

    attribute_map = {
        'href': 'href',
        'items': 'items',
        'count': 'count',
        'activity': 'activity',
        'timestamp': 'timestamp',
        'project_name': 'projectName',
        'flag': 'flag',
        'user': 'user'
    }

    def __init__(self, href=None, items=None, count=None, activity=None, timestamp=None, project_name=None, flag=None, user=None):  # noqa: E501
        """ActivitiesDTO - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._items = None
        self._count = None
        self._activity = None
        self._timestamp = None
        self._project_name = None
        self._flag = None
        self._user = None
        self.discriminator = None
        if href is not None:
            self.href = href
        if items is not None:
            self.items = items
        if count is not None:
            self.count = count
        if activity is not None:
            self.activity = activity
        if timestamp is not None:
            self.timestamp = timestamp
        if project_name is not None:
            self.project_name = project_name
        if flag is not None:
            self.flag = flag
        if user is not None:
            self.user = user

    @property
    def href(self):
        """Gets the href of this ActivitiesDTO.  # noqa: E501


        :return: The href of this ActivitiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ActivitiesDTO.


        :param href: The href of this ActivitiesDTO.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def items(self):
        """Gets the items of this ActivitiesDTO.  # noqa: E501


        :return: The items of this ActivitiesDTO.  # noqa: E501
        :rtype: list[ActivitiesDTO]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ActivitiesDTO.


        :param items: The items of this ActivitiesDTO.  # noqa: E501
        :type: list[ActivitiesDTO]
        """

        self._items = items

    @property
    def count(self):
        """Gets the count of this ActivitiesDTO.  # noqa: E501


        :return: The count of this ActivitiesDTO.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ActivitiesDTO.


        :param count: The count of this ActivitiesDTO.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def activity(self):
        """Gets the activity of this ActivitiesDTO.  # noqa: E501


        :return: The activity of this ActivitiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this ActivitiesDTO.


        :param activity: The activity of this ActivitiesDTO.  # noqa: E501
        :type: str
        """

        self._activity = activity

    @property
    def timestamp(self):
        """Gets the timestamp of this ActivitiesDTO.  # noqa: E501


        :return: The timestamp of this ActivitiesDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ActivitiesDTO.


        :param timestamp: The timestamp of this ActivitiesDTO.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def project_name(self):
        """Gets the project_name of this ActivitiesDTO.  # noqa: E501


        :return: The project_name of this ActivitiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ActivitiesDTO.


        :param project_name: The project_name of this ActivitiesDTO.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def flag(self):
        """Gets the flag of this ActivitiesDTO.  # noqa: E501


        :return: The flag of this ActivitiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this ActivitiesDTO.


        :param flag: The flag of this ActivitiesDTO.  # noqa: E501
        :type: str
        """

        self._flag = flag

    @property
    def user(self):
        """Gets the user of this ActivitiesDTO.  # noqa: E501


        :return: The user of this ActivitiesDTO.  # noqa: E501
        :rtype: UserDTO
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ActivitiesDTO.


        :param user: The user of this ActivitiesDTO.  # noqa: E501
        :type: UserDTO
        """

        self._user = user

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
        if issubclass(ActivitiesDTO, dict):
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
        if not isinstance(other, ActivitiesDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
