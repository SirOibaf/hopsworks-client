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
from swagger_client.models.acl_dto import AclDTO  # noqa: F401,E501


class AclDTO(object):
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
        'items': 'list[AclDTO]',
        'count': 'int',
        'id': 'int',
        'project_name': 'str',
        'user_email': 'str',
        'permission_type': 'str',
        'operation_type': 'str',
        'host': 'str',
        'role': 'str'
    }

    attribute_map = {
        'href': 'href',
        'items': 'items',
        'count': 'count',
        'id': 'id',
        'project_name': 'projectName',
        'user_email': 'userEmail',
        'permission_type': 'permissionType',
        'operation_type': 'operationType',
        'host': 'host',
        'role': 'role'
    }

    def __init__(self, href=None, items=None, count=None, id=None, project_name=None, user_email=None, permission_type=None, operation_type=None, host=None, role=None):  # noqa: E501
        """AclDTO - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._items = None
        self._count = None
        self._id = None
        self._project_name = None
        self._user_email = None
        self._permission_type = None
        self._operation_type = None
        self._host = None
        self._role = None
        self.discriminator = None
        if href is not None:
            self.href = href
        if items is not None:
            self.items = items
        if count is not None:
            self.count = count
        if id is not None:
            self.id = id
        if project_name is not None:
            self.project_name = project_name
        if user_email is not None:
            self.user_email = user_email
        if permission_type is not None:
            self.permission_type = permission_type
        if operation_type is not None:
            self.operation_type = operation_type
        if host is not None:
            self.host = host
        if role is not None:
            self.role = role

    @property
    def href(self):
        """Gets the href of this AclDTO.  # noqa: E501


        :return: The href of this AclDTO.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AclDTO.


        :param href: The href of this AclDTO.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def items(self):
        """Gets the items of this AclDTO.  # noqa: E501


        :return: The items of this AclDTO.  # noqa: E501
        :rtype: list[AclDTO]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this AclDTO.


        :param items: The items of this AclDTO.  # noqa: E501
        :type: list[AclDTO]
        """

        self._items = items

    @property
    def count(self):
        """Gets the count of this AclDTO.  # noqa: E501


        :return: The count of this AclDTO.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this AclDTO.


        :param count: The count of this AclDTO.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def id(self):
        """Gets the id of this AclDTO.  # noqa: E501


        :return: The id of this AclDTO.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AclDTO.


        :param id: The id of this AclDTO.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def project_name(self):
        """Gets the project_name of this AclDTO.  # noqa: E501


        :return: The project_name of this AclDTO.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this AclDTO.


        :param project_name: The project_name of this AclDTO.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def user_email(self):
        """Gets the user_email of this AclDTO.  # noqa: E501


        :return: The user_email of this AclDTO.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this AclDTO.


        :param user_email: The user_email of this AclDTO.  # noqa: E501
        :type: str
        """

        self._user_email = user_email

    @property
    def permission_type(self):
        """Gets the permission_type of this AclDTO.  # noqa: E501


        :return: The permission_type of this AclDTO.  # noqa: E501
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        """Sets the permission_type of this AclDTO.


        :param permission_type: The permission_type of this AclDTO.  # noqa: E501
        :type: str
        """

        self._permission_type = permission_type

    @property
    def operation_type(self):
        """Gets the operation_type of this AclDTO.  # noqa: E501


        :return: The operation_type of this AclDTO.  # noqa: E501
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this AclDTO.


        :param operation_type: The operation_type of this AclDTO.  # noqa: E501
        :type: str
        """

        self._operation_type = operation_type

    @property
    def host(self):
        """Gets the host of this AclDTO.  # noqa: E501


        :return: The host of this AclDTO.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this AclDTO.


        :param host: The host of this AclDTO.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def role(self):
        """Gets the role of this AclDTO.  # noqa: E501


        :return: The role of this AclDTO.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this AclDTO.


        :param role: The role of this AclDTO.  # noqa: E501
        :type: str
        """

        self._role = role

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
        if issubclass(AclDTO, dict):
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
        if not isinstance(other, AclDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
