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
from swagger_client.models.python_dep import PythonDep  # noqa: F401,E501


class AnacondaRepo(object):
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
        'url': 'str',
        'python_dep_collection': 'list[PythonDep]'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'python_dep_collection': 'pythonDepCollection'
    }

    def __init__(self, id=None, url=None, python_dep_collection=None):  # noqa: E501
        """AnacondaRepo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._url = None
        self._python_dep_collection = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.url = url
        if python_dep_collection is not None:
            self.python_dep_collection = python_dep_collection

    @property
    def id(self):
        """Gets the id of this AnacondaRepo.  # noqa: E501


        :return: The id of this AnacondaRepo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AnacondaRepo.


        :param id: The id of this AnacondaRepo.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this AnacondaRepo.  # noqa: E501


        :return: The url of this AnacondaRepo.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AnacondaRepo.


        :param url: The url of this AnacondaRepo.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def python_dep_collection(self):
        """Gets the python_dep_collection of this AnacondaRepo.  # noqa: E501


        :return: The python_dep_collection of this AnacondaRepo.  # noqa: E501
        :rtype: list[PythonDep]
        """
        return self._python_dep_collection

    @python_dep_collection.setter
    def python_dep_collection(self, python_dep_collection):
        """Sets the python_dep_collection of this AnacondaRepo.


        :param python_dep_collection: The python_dep_collection of this AnacondaRepo.  # noqa: E501
        :type: list[PythonDep]
        """

        self._python_dep_collection = python_dep_collection

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
        if issubclass(AnacondaRepo, dict):
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
        if not isinstance(other, AnacondaRepo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other