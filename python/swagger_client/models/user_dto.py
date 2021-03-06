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
from swagger_client.models.user_dto import UserDTO  # noqa: F401,E501


class UserDTO(object):
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
        'items': 'list[UserDTO]',
        'count': 'int',
        'firstname': 'str',
        'lastname': 'str',
        'email': 'str',
        'username': 'str'
    }

    attribute_map = {
        'href': 'href',
        'items': 'items',
        'count': 'count',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'email': 'email',
        'username': 'username'
    }

    def __init__(self, href=None, items=None, count=None, firstname=None, lastname=None, email=None, username=None):  # noqa: E501
        """UserDTO - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._items = None
        self._count = None
        self._firstname = None
        self._lastname = None
        self._email = None
        self._username = None
        self.discriminator = None
        if href is not None:
            self.href = href
        if items is not None:
            self.items = items
        if count is not None:
            self.count = count
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if email is not None:
            self.email = email
        if username is not None:
            self.username = username

    @property
    def href(self):
        """Gets the href of this UserDTO.  # noqa: E501


        :return: The href of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this UserDTO.


        :param href: The href of this UserDTO.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def items(self):
        """Gets the items of this UserDTO.  # noqa: E501


        :return: The items of this UserDTO.  # noqa: E501
        :rtype: list[UserDTO]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this UserDTO.


        :param items: The items of this UserDTO.  # noqa: E501
        :type: list[UserDTO]
        """

        self._items = items

    @property
    def count(self):
        """Gets the count of this UserDTO.  # noqa: E501


        :return: The count of this UserDTO.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this UserDTO.


        :param count: The count of this UserDTO.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def firstname(self):
        """Gets the firstname of this UserDTO.  # noqa: E501


        :return: The firstname of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this UserDTO.


        :param firstname: The firstname of this UserDTO.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this UserDTO.  # noqa: E501


        :return: The lastname of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this UserDTO.


        :param lastname: The lastname of this UserDTO.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def email(self):
        """Gets the email of this UserDTO.  # noqa: E501


        :return: The email of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserDTO.


        :param email: The email of this UserDTO.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def username(self):
        """Gets the username of this UserDTO.  # noqa: E501


        :return: The username of this UserDTO.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserDTO.


        :param username: The username of this UserDTO.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(UserDTO, dict):
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
        if not isinstance(other, UserDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
