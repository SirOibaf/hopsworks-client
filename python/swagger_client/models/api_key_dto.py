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
from swagger_client.models.api_key_dto import ApiKeyDTO  # noqa: F401,E501


class ApiKeyDTO(object):
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
        'items': 'list[ApiKeyDTO]',
        'count': 'int',
        'key': 'str',
        'name': 'str',
        'prefix': 'str',
        'created': 'datetime',
        'modified': 'datetime',
        'scope': 'list[str]'
    }

    attribute_map = {
        'href': 'href',
        'items': 'items',
        'count': 'count',
        'key': 'key',
        'name': 'name',
        'prefix': 'prefix',
        'created': 'created',
        'modified': 'modified',
        'scope': 'scope'
    }

    def __init__(self, href=None, items=None, count=None, key=None, name=None, prefix=None, created=None, modified=None, scope=None):  # noqa: E501
        """ApiKeyDTO - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._items = None
        self._count = None
        self._key = None
        self._name = None
        self._prefix = None
        self._created = None
        self._modified = None
        self._scope = None
        self.discriminator = None
        if href is not None:
            self.href = href
        if items is not None:
            self.items = items
        if count is not None:
            self.count = count
        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if prefix is not None:
            self.prefix = prefix
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if scope is not None:
            self.scope = scope

    @property
    def href(self):
        """Gets the href of this ApiKeyDTO.  # noqa: E501


        :return: The href of this ApiKeyDTO.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ApiKeyDTO.


        :param href: The href of this ApiKeyDTO.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def items(self):
        """Gets the items of this ApiKeyDTO.  # noqa: E501


        :return: The items of this ApiKeyDTO.  # noqa: E501
        :rtype: list[ApiKeyDTO]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ApiKeyDTO.


        :param items: The items of this ApiKeyDTO.  # noqa: E501
        :type: list[ApiKeyDTO]
        """

        self._items = items

    @property
    def count(self):
        """Gets the count of this ApiKeyDTO.  # noqa: E501


        :return: The count of this ApiKeyDTO.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ApiKeyDTO.


        :param count: The count of this ApiKeyDTO.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def key(self):
        """Gets the key of this ApiKeyDTO.  # noqa: E501


        :return: The key of this ApiKeyDTO.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ApiKeyDTO.


        :param key: The key of this ApiKeyDTO.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this ApiKeyDTO.  # noqa: E501


        :return: The name of this ApiKeyDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiKeyDTO.


        :param name: The name of this ApiKeyDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def prefix(self):
        """Gets the prefix of this ApiKeyDTO.  # noqa: E501


        :return: The prefix of this ApiKeyDTO.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this ApiKeyDTO.


        :param prefix: The prefix of this ApiKeyDTO.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def created(self):
        """Gets the created of this ApiKeyDTO.  # noqa: E501


        :return: The created of this ApiKeyDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ApiKeyDTO.


        :param created: The created of this ApiKeyDTO.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this ApiKeyDTO.  # noqa: E501


        :return: The modified of this ApiKeyDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this ApiKeyDTO.


        :param modified: The modified of this ApiKeyDTO.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def scope(self):
        """Gets the scope of this ApiKeyDTO.  # noqa: E501


        :return: The scope of this ApiKeyDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ApiKeyDTO.


        :param scope: The scope of this ApiKeyDTO.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["JOB", "DATASET_VIEW", "DATASET_CREATE", "DATASET_DELETE", "INFERENCE", "FEATURESTORE", "PROJECT"]  # noqa: E501
        if not set(scope).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `scope` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(scope) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._scope = scope

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
        if issubclass(ApiKeyDTO, dict):
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
        if not isinstance(other, ApiKeyDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
