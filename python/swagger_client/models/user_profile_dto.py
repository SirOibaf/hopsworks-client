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


class UserProfileDTO(object):
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
        'username': 'str',
        'phone_number': 'str',
        'account_type': 'str',
        'two_factor': 'bool',
        'tours_state': 'int',
        'status': 'int',
        'max_num_projects': 'int',
        'num_created_projects': 'int',
        'num_active_projects': 'int'
    }

    attribute_map = {
        'href': 'href',
        'items': 'items',
        'count': 'count',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'email': 'email',
        'username': 'username',
        'phone_number': 'phoneNumber',
        'account_type': 'accountType',
        'two_factor': 'twoFactor',
        'tours_state': 'toursState',
        'status': 'status',
        'max_num_projects': 'maxNumProjects',
        'num_created_projects': 'numCreatedProjects',
        'num_active_projects': 'numActiveProjects'
    }

    def __init__(self, href=None, items=None, count=None, firstname=None, lastname=None, email=None, username=None, phone_number=None, account_type=None, two_factor=None, tours_state=None, status=None, max_num_projects=None, num_created_projects=None, num_active_projects=None):  # noqa: E501
        """UserProfileDTO - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._items = None
        self._count = None
        self._firstname = None
        self._lastname = None
        self._email = None
        self._username = None
        self._phone_number = None
        self._account_type = None
        self._two_factor = None
        self._tours_state = None
        self._status = None
        self._max_num_projects = None
        self._num_created_projects = None
        self._num_active_projects = None
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
        if phone_number is not None:
            self.phone_number = phone_number
        if account_type is not None:
            self.account_type = account_type
        if two_factor is not None:
            self.two_factor = two_factor
        if tours_state is not None:
            self.tours_state = tours_state
        if status is not None:
            self.status = status
        if max_num_projects is not None:
            self.max_num_projects = max_num_projects
        if num_created_projects is not None:
            self.num_created_projects = num_created_projects
        if num_active_projects is not None:
            self.num_active_projects = num_active_projects

    @property
    def href(self):
        """Gets the href of this UserProfileDTO.  # noqa: E501


        :return: The href of this UserProfileDTO.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this UserProfileDTO.


        :param href: The href of this UserProfileDTO.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def items(self):
        """Gets the items of this UserProfileDTO.  # noqa: E501


        :return: The items of this UserProfileDTO.  # noqa: E501
        :rtype: list[UserDTO]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this UserProfileDTO.


        :param items: The items of this UserProfileDTO.  # noqa: E501
        :type: list[UserDTO]
        """

        self._items = items

    @property
    def count(self):
        """Gets the count of this UserProfileDTO.  # noqa: E501


        :return: The count of this UserProfileDTO.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this UserProfileDTO.


        :param count: The count of this UserProfileDTO.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def firstname(self):
        """Gets the firstname of this UserProfileDTO.  # noqa: E501


        :return: The firstname of this UserProfileDTO.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this UserProfileDTO.


        :param firstname: The firstname of this UserProfileDTO.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this UserProfileDTO.  # noqa: E501


        :return: The lastname of this UserProfileDTO.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this UserProfileDTO.


        :param lastname: The lastname of this UserProfileDTO.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def email(self):
        """Gets the email of this UserProfileDTO.  # noqa: E501


        :return: The email of this UserProfileDTO.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserProfileDTO.


        :param email: The email of this UserProfileDTO.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def username(self):
        """Gets the username of this UserProfileDTO.  # noqa: E501


        :return: The username of this UserProfileDTO.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserProfileDTO.


        :param username: The username of this UserProfileDTO.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def phone_number(self):
        """Gets the phone_number of this UserProfileDTO.  # noqa: E501


        :return: The phone_number of this UserProfileDTO.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this UserProfileDTO.


        :param phone_number: The phone_number of this UserProfileDTO.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def account_type(self):
        """Gets the account_type of this UserProfileDTO.  # noqa: E501


        :return: The account_type of this UserProfileDTO.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this UserProfileDTO.


        :param account_type: The account_type of this UserProfileDTO.  # noqa: E501
        :type: str
        """

        self._account_type = account_type

    @property
    def two_factor(self):
        """Gets the two_factor of this UserProfileDTO.  # noqa: E501


        :return: The two_factor of this UserProfileDTO.  # noqa: E501
        :rtype: bool
        """
        return self._two_factor

    @two_factor.setter
    def two_factor(self, two_factor):
        """Sets the two_factor of this UserProfileDTO.


        :param two_factor: The two_factor of this UserProfileDTO.  # noqa: E501
        :type: bool
        """

        self._two_factor = two_factor

    @property
    def tours_state(self):
        """Gets the tours_state of this UserProfileDTO.  # noqa: E501


        :return: The tours_state of this UserProfileDTO.  # noqa: E501
        :rtype: int
        """
        return self._tours_state

    @tours_state.setter
    def tours_state(self, tours_state):
        """Sets the tours_state of this UserProfileDTO.


        :param tours_state: The tours_state of this UserProfileDTO.  # noqa: E501
        :type: int
        """

        self._tours_state = tours_state

    @property
    def status(self):
        """Gets the status of this UserProfileDTO.  # noqa: E501


        :return: The status of this UserProfileDTO.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserProfileDTO.


        :param status: The status of this UserProfileDTO.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def max_num_projects(self):
        """Gets the max_num_projects of this UserProfileDTO.  # noqa: E501


        :return: The max_num_projects of this UserProfileDTO.  # noqa: E501
        :rtype: int
        """
        return self._max_num_projects

    @max_num_projects.setter
    def max_num_projects(self, max_num_projects):
        """Sets the max_num_projects of this UserProfileDTO.


        :param max_num_projects: The max_num_projects of this UserProfileDTO.  # noqa: E501
        :type: int
        """

        self._max_num_projects = max_num_projects

    @property
    def num_created_projects(self):
        """Gets the num_created_projects of this UserProfileDTO.  # noqa: E501


        :return: The num_created_projects of this UserProfileDTO.  # noqa: E501
        :rtype: int
        """
        return self._num_created_projects

    @num_created_projects.setter
    def num_created_projects(self, num_created_projects):
        """Sets the num_created_projects of this UserProfileDTO.


        :param num_created_projects: The num_created_projects of this UserProfileDTO.  # noqa: E501
        :type: int
        """

        self._num_created_projects = num_created_projects

    @property
    def num_active_projects(self):
        """Gets the num_active_projects of this UserProfileDTO.  # noqa: E501


        :return: The num_active_projects of this UserProfileDTO.  # noqa: E501
        :rtype: int
        """
        return self._num_active_projects

    @num_active_projects.setter
    def num_active_projects(self, num_active_projects):
        """Sets the num_active_projects of this UserProfileDTO.


        :param num_active_projects: The num_active_projects of this UserProfileDTO.  # noqa: E501
        :type: int
        """

        self._num_active_projects = num_active_projects

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
        if issubclass(UserProfileDTO, dict):
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
        if not isinstance(other, UserProfileDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other