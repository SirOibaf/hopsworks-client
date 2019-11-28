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
from swagger_client.models.inode import Inode  # noqa: F401,E501
from swagger_client.models.m_table import MTable  # noqa: F401,E501


class Template(object):
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
        'name': 'str',
        'inodes': 'list[Inode]',
        'mtables': 'list[MTable]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'inodes': 'inodes',
        'mtables': 'mtables'
    }

    def __init__(self, id=None, name=None, inodes=None, mtables=None):  # noqa: E501
        """Template - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._inodes = None
        self._mtables = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        if inodes is not None:
            self.inodes = inodes
        if mtables is not None:
            self.mtables = mtables

    @property
    def id(self):
        """Gets the id of this Template.  # noqa: E501


        :return: The id of this Template.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Template.


        :param id: The id of this Template.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Template.  # noqa: E501


        :return: The name of this Template.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Template.


        :param name: The name of this Template.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def inodes(self):
        """Gets the inodes of this Template.  # noqa: E501


        :return: The inodes of this Template.  # noqa: E501
        :rtype: list[Inode]
        """
        return self._inodes

    @inodes.setter
    def inodes(self, inodes):
        """Sets the inodes of this Template.


        :param inodes: The inodes of this Template.  # noqa: E501
        :type: list[Inode]
        """

        self._inodes = inodes

    @property
    def mtables(self):
        """Gets the mtables of this Template.  # noqa: E501


        :return: The mtables of this Template.  # noqa: E501
        :rtype: list[MTable]
        """
        return self._mtables

    @mtables.setter
    def mtables(self, mtables):
        """Sets the mtables of this Template.


        :param mtables: The mtables of this Template.  # noqa: E501
        :type: list[MTable]
        """

        self._mtables = mtables

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
        if issubclass(Template, dict):
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
        if not isinstance(other, Template):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
