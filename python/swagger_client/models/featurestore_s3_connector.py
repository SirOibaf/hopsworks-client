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
from swagger_client.models.featurestore import Featurestore  # noqa: F401,E501


class FeaturestoreS3Connector(object):
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
        'featurestore': 'Featurestore',
        'access_key': 'str',
        'secret_key': 'str',
        'bucket': 'str',
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'featurestore': 'featurestore',
        'access_key': 'accessKey',
        'secret_key': 'secretKey',
        'bucket': 'bucket',
        'description': 'description',
        'name': 'name'
    }

    def __init__(self, id=None, featurestore=None, access_key=None, secret_key=None, bucket=None, description=None, name=None):  # noqa: E501
        """FeaturestoreS3Connector - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._featurestore = None
        self._access_key = None
        self._secret_key = None
        self._bucket = None
        self._description = None
        self._name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if featurestore is not None:
            self.featurestore = featurestore
        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key
        if bucket is not None:
            self.bucket = bucket
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this FeaturestoreS3Connector.  # noqa: E501


        :return: The id of this FeaturestoreS3Connector.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FeaturestoreS3Connector.


        :param id: The id of this FeaturestoreS3Connector.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def featurestore(self):
        """Gets the featurestore of this FeaturestoreS3Connector.  # noqa: E501


        :return: The featurestore of this FeaturestoreS3Connector.  # noqa: E501
        :rtype: Featurestore
        """
        return self._featurestore

    @featurestore.setter
    def featurestore(self, featurestore):
        """Sets the featurestore of this FeaturestoreS3Connector.


        :param featurestore: The featurestore of this FeaturestoreS3Connector.  # noqa: E501
        :type: Featurestore
        """

        self._featurestore = featurestore

    @property
    def access_key(self):
        """Gets the access_key of this FeaturestoreS3Connector.  # noqa: E501


        :return: The access_key of this FeaturestoreS3Connector.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this FeaturestoreS3Connector.


        :param access_key: The access_key of this FeaturestoreS3Connector.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def secret_key(self):
        """Gets the secret_key of this FeaturestoreS3Connector.  # noqa: E501


        :return: The secret_key of this FeaturestoreS3Connector.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this FeaturestoreS3Connector.


        :param secret_key: The secret_key of this FeaturestoreS3Connector.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def bucket(self):
        """Gets the bucket of this FeaturestoreS3Connector.  # noqa: E501


        :return: The bucket of this FeaturestoreS3Connector.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this FeaturestoreS3Connector.


        :param bucket: The bucket of this FeaturestoreS3Connector.  # noqa: E501
        :type: str
        """

        self._bucket = bucket

    @property
    def description(self):
        """Gets the description of this FeaturestoreS3Connector.  # noqa: E501


        :return: The description of this FeaturestoreS3Connector.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FeaturestoreS3Connector.


        :param description: The description of this FeaturestoreS3Connector.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this FeaturestoreS3Connector.  # noqa: E501


        :return: The name of this FeaturestoreS3Connector.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeaturestoreS3Connector.


        :param name: The name of this FeaturestoreS3Connector.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(FeaturestoreS3Connector, dict):
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
        if not isinstance(other, FeaturestoreS3Connector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
