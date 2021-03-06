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


class ClusterAddressDTO(object):
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
        'cluster_id': 'str',
        'dela_transfer_address': 'str',
        'dela_cluster_address': 'str'
    }

    attribute_map = {
        'cluster_id': 'clusterId',
        'dela_transfer_address': 'delaTransferAddress',
        'dela_cluster_address': 'delaClusterAddress'
    }

    def __init__(self, cluster_id=None, dela_transfer_address=None, dela_cluster_address=None):  # noqa: E501
        """ClusterAddressDTO - a model defined in Swagger"""  # noqa: E501
        self._cluster_id = None
        self._dela_transfer_address = None
        self._dela_cluster_address = None
        self.discriminator = None
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if dela_transfer_address is not None:
            self.dela_transfer_address = dela_transfer_address
        if dela_cluster_address is not None:
            self.dela_cluster_address = dela_cluster_address

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ClusterAddressDTO.  # noqa: E501


        :return: The cluster_id of this ClusterAddressDTO.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ClusterAddressDTO.


        :param cluster_id: The cluster_id of this ClusterAddressDTO.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def dela_transfer_address(self):
        """Gets the dela_transfer_address of this ClusterAddressDTO.  # noqa: E501


        :return: The dela_transfer_address of this ClusterAddressDTO.  # noqa: E501
        :rtype: str
        """
        return self._dela_transfer_address

    @dela_transfer_address.setter
    def dela_transfer_address(self, dela_transfer_address):
        """Sets the dela_transfer_address of this ClusterAddressDTO.


        :param dela_transfer_address: The dela_transfer_address of this ClusterAddressDTO.  # noqa: E501
        :type: str
        """

        self._dela_transfer_address = dela_transfer_address

    @property
    def dela_cluster_address(self):
        """Gets the dela_cluster_address of this ClusterAddressDTO.  # noqa: E501


        :return: The dela_cluster_address of this ClusterAddressDTO.  # noqa: E501
        :rtype: str
        """
        return self._dela_cluster_address

    @dela_cluster_address.setter
    def dela_cluster_address(self, dela_cluster_address):
        """Sets the dela_cluster_address of this ClusterAddressDTO.


        :param dela_cluster_address: The dela_cluster_address of this ClusterAddressDTO.  # noqa: E501
        :type: str
        """

        self._dela_cluster_address = dela_cluster_address

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
        if issubclass(ClusterAddressDTO, dict):
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
        if not isinstance(other, ClusterAddressDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
