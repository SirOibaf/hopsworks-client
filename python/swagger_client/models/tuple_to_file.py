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
from swagger_client.models.raw_data import RawData  # noqa: F401,E501


class TupleToFile(object):
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
        'inode': 'Inode',
        'inode_id': 'int',
        'raw_data': 'list[RawData]',
        'id': 'int'
    }

    attribute_map = {
        'inode': 'inode',
        'inode_id': 'inodeId',
        'raw_data': 'rawData',
        'id': 'id'
    }

    def __init__(self, inode=None, inode_id=None, raw_data=None, id=None):  # noqa: E501
        """TupleToFile - a model defined in Swagger"""  # noqa: E501
        self._inode = None
        self._inode_id = None
        self._raw_data = None
        self._id = None
        self.discriminator = None
        if inode is not None:
            self.inode = inode
        if inode_id is not None:
            self.inode_id = inode_id
        if raw_data is not None:
            self.raw_data = raw_data
        if id is not None:
            self.id = id

    @property
    def inode(self):
        """Gets the inode of this TupleToFile.  # noqa: E501


        :return: The inode of this TupleToFile.  # noqa: E501
        :rtype: Inode
        """
        return self._inode

    @inode.setter
    def inode(self, inode):
        """Sets the inode of this TupleToFile.


        :param inode: The inode of this TupleToFile.  # noqa: E501
        :type: Inode
        """

        self._inode = inode

    @property
    def inode_id(self):
        """Gets the inode_id of this TupleToFile.  # noqa: E501


        :return: The inode_id of this TupleToFile.  # noqa: E501
        :rtype: int
        """
        return self._inode_id

    @inode_id.setter
    def inode_id(self, inode_id):
        """Sets the inode_id of this TupleToFile.


        :param inode_id: The inode_id of this TupleToFile.  # noqa: E501
        :type: int
        """

        self._inode_id = inode_id

    @property
    def raw_data(self):
        """Gets the raw_data of this TupleToFile.  # noqa: E501


        :return: The raw_data of this TupleToFile.  # noqa: E501
        :rtype: list[RawData]
        """
        return self._raw_data

    @raw_data.setter
    def raw_data(self, raw_data):
        """Sets the raw_data of this TupleToFile.


        :param raw_data: The raw_data of this TupleToFile.  # noqa: E501
        :type: list[RawData]
        """

        self._raw_data = raw_data

    @property
    def id(self):
        """Gets the id of this TupleToFile.  # noqa: E501


        :return: The id of this TupleToFile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TupleToFile.


        :param id: The id of this TupleToFile.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(TupleToFile, dict):
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
        if not isinstance(other, TupleToFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
