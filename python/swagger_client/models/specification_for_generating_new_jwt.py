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


class SpecificationForGeneratingNewJWT(object):
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
        'subject': 'str',
        'audiences': 'list[str]',
        'key_name': 'str',
        'expires_at': 'datetime',
        'nbf': 'datetime',
        'renewable': 'bool',
        'exp_leeway': 'int'
    }

    attribute_map = {
        'subject': 'subject',
        'audiences': 'audiences',
        'key_name': 'keyName',
        'expires_at': 'expiresAt',
        'nbf': 'nbf',
        'renewable': 'renewable',
        'exp_leeway': 'expLeeway'
    }

    def __init__(self, subject=None, audiences=None, key_name=None, expires_at=None, nbf=None, renewable=None, exp_leeway=None):  # noqa: E501
        """SpecificationForGeneratingNewJWT - a model defined in Swagger"""  # noqa: E501
        self._subject = None
        self._audiences = None
        self._key_name = None
        self._expires_at = None
        self._nbf = None
        self._renewable = None
        self._exp_leeway = None
        self.discriminator = None
        self.subject = subject
        self.audiences = audiences
        self.key_name = key_name
        if expires_at is not None:
            self.expires_at = expires_at
        if nbf is not None:
            self.nbf = nbf
        self.renewable = renewable
        self.exp_leeway = exp_leeway

    @property
    def subject(self):
        """Gets the subject of this SpecificationForGeneratingNewJWT.  # noqa: E501

        Subject to be encoded in JWT  # noqa: E501

        :return: The subject of this SpecificationForGeneratingNewJWT.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this SpecificationForGeneratingNewJWT.

        Subject to be encoded in JWT  # noqa: E501

        :param subject: The subject of this SpecificationForGeneratingNewJWT.  # noqa: E501
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def audiences(self):
        """Gets the audiences of this SpecificationForGeneratingNewJWT.  # noqa: E501

        Appropriate audience for the JWT  # noqa: E501

        :return: The audiences of this SpecificationForGeneratingNewJWT.  # noqa: E501
        :rtype: list[str]
        """
        return self._audiences

    @audiences.setter
    def audiences(self, audiences):
        """Sets the audiences of this SpecificationForGeneratingNewJWT.

        Appropriate audience for the JWT  # noqa: E501

        :param audiences: The audiences of this SpecificationForGeneratingNewJWT.  # noqa: E501
        :type: list[str]
        """
        if audiences is None:
            raise ValueError("Invalid value for `audiences`, must not be `None`")  # noqa: E501

        self._audiences = audiences

    @property
    def key_name(self):
        """Gets the key_name of this SpecificationForGeneratingNewJWT.  # noqa: E501

        Name of the signing key  # noqa: E501

        :return: The key_name of this SpecificationForGeneratingNewJWT.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this SpecificationForGeneratingNewJWT.

        Name of the signing key  # noqa: E501

        :param key_name: The key_name of this SpecificationForGeneratingNewJWT.  # noqa: E501
        :type: str
        """
        if key_name is None:
            raise ValueError("Invalid value for `key_name`, must not be `None`")  # noqa: E501

        self._key_name = key_name

    @property
    def expires_at(self):
        """Gets the expires_at of this SpecificationForGeneratingNewJWT.  # noqa: E501

        Expiration date of the token  # noqa: E501

        :return: The expires_at of this SpecificationForGeneratingNewJWT.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this SpecificationForGeneratingNewJWT.

        Expiration date of the token  # noqa: E501

        :param expires_at: The expires_at of this SpecificationForGeneratingNewJWT.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def nbf(self):
        """Gets the nbf of this SpecificationForGeneratingNewJWT.  # noqa: E501

        Not-valid-before date  # noqa: E501

        :return: The nbf of this SpecificationForGeneratingNewJWT.  # noqa: E501
        :rtype: datetime
        """
        return self._nbf

    @nbf.setter
    def nbf(self, nbf):
        """Sets the nbf of this SpecificationForGeneratingNewJWT.

        Not-valid-before date  # noqa: E501

        :param nbf: The nbf of this SpecificationForGeneratingNewJWT.  # noqa: E501
        :type: datetime
        """

        self._nbf = nbf

    @property
    def renewable(self):
        """Gets the renewable of this SpecificationForGeneratingNewJWT.  # noqa: E501

        Flag to indicate if the token is auto-renewable  # noqa: E501

        :return: The renewable of this SpecificationForGeneratingNewJWT.  # noqa: E501
        :rtype: bool
        """
        return self._renewable

    @renewable.setter
    def renewable(self, renewable):
        """Sets the renewable of this SpecificationForGeneratingNewJWT.

        Flag to indicate if the token is auto-renewable  # noqa: E501

        :param renewable: The renewable of this SpecificationForGeneratingNewJWT.  # noqa: E501
        :type: bool
        """
        if renewable is None:
            raise ValueError("Invalid value for `renewable`, must not be `None`")  # noqa: E501

        self._renewable = renewable

    @property
    def exp_leeway(self):
        """Gets the exp_leeway of this SpecificationForGeneratingNewJWT.  # noqa: E501

        Number of seconds after the expiration the token is still valid  # noqa: E501

        :return: The exp_leeway of this SpecificationForGeneratingNewJWT.  # noqa: E501
        :rtype: int
        """
        return self._exp_leeway

    @exp_leeway.setter
    def exp_leeway(self, exp_leeway):
        """Sets the exp_leeway of this SpecificationForGeneratingNewJWT.

        Number of seconds after the expiration the token is still valid  # noqa: E501

        :param exp_leeway: The exp_leeway of this SpecificationForGeneratingNewJWT.  # noqa: E501
        :type: int
        """
        if exp_leeway is None:
            raise ValueError("Invalid value for `exp_leeway`, must not be `None`")  # noqa: E501

        self._exp_leeway = exp_leeway

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
        if issubclass(SpecificationForGeneratingNewJWT, dict):
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
        if not isinstance(other, SpecificationForGeneratingNewJWT):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
