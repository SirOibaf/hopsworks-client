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
from swagger_client.models.field import Field  # noqa: F401,E501
from swagger_client.models.metadata import Metadata  # noqa: F401,E501
from swagger_client.models.raw_data_pk import RawDataPK  # noqa: F401,E501
from swagger_client.models.tuple_to_file import TupleToFile  # noqa: F401,E501


class RawData(object):
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
        'rawdata_pk': 'RawDataPK',
        'tuple_to_file': 'TupleToFile',
        'metadata': 'list[Metadata]',
        'field': 'Field',
        'id': 'int'
    }

    attribute_map = {
        'rawdata_pk': 'rawdataPK',
        'tuple_to_file': 'tupleToFile',
        'metadata': 'metadata',
        'field': 'field',
        'id': 'id'
    }

    def __init__(self, rawdata_pk=None, tuple_to_file=None, metadata=None, field=None, id=None):  # noqa: E501
        """RawData - a model defined in Swagger"""  # noqa: E501
        self._rawdata_pk = None
        self._tuple_to_file = None
        self._metadata = None
        self._field = None
        self._id = None
        self.discriminator = None
        if rawdata_pk is not None:
            self.rawdata_pk = rawdata_pk
        if tuple_to_file is not None:
            self.tuple_to_file = tuple_to_file
        if metadata is not None:
            self.metadata = metadata
        if field is not None:
            self.field = field
        if id is not None:
            self.id = id

    @property
    def rawdata_pk(self):
        """Gets the rawdata_pk of this RawData.  # noqa: E501


        :return: The rawdata_pk of this RawData.  # noqa: E501
        :rtype: RawDataPK
        """
        return self._rawdata_pk

    @rawdata_pk.setter
    def rawdata_pk(self, rawdata_pk):
        """Sets the rawdata_pk of this RawData.


        :param rawdata_pk: The rawdata_pk of this RawData.  # noqa: E501
        :type: RawDataPK
        """

        self._rawdata_pk = rawdata_pk

    @property
    def tuple_to_file(self):
        """Gets the tuple_to_file of this RawData.  # noqa: E501


        :return: The tuple_to_file of this RawData.  # noqa: E501
        :rtype: TupleToFile
        """
        return self._tuple_to_file

    @tuple_to_file.setter
    def tuple_to_file(self, tuple_to_file):
        """Sets the tuple_to_file of this RawData.


        :param tuple_to_file: The tuple_to_file of this RawData.  # noqa: E501
        :type: TupleToFile
        """

        self._tuple_to_file = tuple_to_file

    @property
    def metadata(self):
        """Gets the metadata of this RawData.  # noqa: E501


        :return: The metadata of this RawData.  # noqa: E501
        :rtype: list[Metadata]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this RawData.


        :param metadata: The metadata of this RawData.  # noqa: E501
        :type: list[Metadata]
        """

        self._metadata = metadata

    @property
    def field(self):
        """Gets the field of this RawData.  # noqa: E501


        :return: The field of this RawData.  # noqa: E501
        :rtype: Field
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this RawData.


        :param field: The field of this RawData.  # noqa: E501
        :type: Field
        """

        self._field = field

    @property
    def id(self):
        """Gets the id of this RawData.  # noqa: E501


        :return: The id of this RawData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RawData.


        :param id: The id of this RawData.  # noqa: E501
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
        if issubclass(RawData, dict):
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
        if not isinstance(other, RawData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other