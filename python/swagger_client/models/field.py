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
from swagger_client.models.field_predefined_value import FieldPredefinedValue  # noqa: F401,E501
from swagger_client.models.field_type import FieldType  # noqa: F401,E501
from swagger_client.models.m_table import MTable  # noqa: F401,E501
from swagger_client.models.raw_data import RawData  # noqa: F401,E501


class Field(object):
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
        'tableid': 'int',
        'field_types': 'FieldType',
        'field_predefined_values': 'list[FieldPredefinedValue]',
        'name': 'str',
        'type': 'str',
        'maxsize': 'int',
        'searchable': 'bool',
        'required': 'bool',
        'description': 'str',
        'position': 'int',
        'field_type_id': 'int',
        'mtable': 'MTable',
        'raw_data': 'list[RawData]'
    }

    attribute_map = {
        'id': 'id',
        'tableid': 'tableid',
        'field_types': 'fieldTypes',
        'field_predefined_values': 'fieldPredefinedValues',
        'name': 'name',
        'type': 'type',
        'maxsize': 'maxsize',
        'searchable': 'searchable',
        'required': 'required',
        'description': 'description',
        'position': 'position',
        'field_type_id': 'fieldTypeId',
        'mtable': 'mtable',
        'raw_data': 'rawData'
    }

    def __init__(self, id=None, tableid=None, field_types=None, field_predefined_values=None, name=None, type=None, maxsize=None, searchable=None, required=None, description=None, position=None, field_type_id=None, mtable=None, raw_data=None):  # noqa: E501
        """Field - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._tableid = None
        self._field_types = None
        self._field_predefined_values = None
        self._name = None
        self._type = None
        self._maxsize = None
        self._searchable = None
        self._required = None
        self._description = None
        self._position = None
        self._field_type_id = None
        self._mtable = None
        self._raw_data = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.tableid = tableid
        if field_types is not None:
            self.field_types = field_types
        if field_predefined_values is not None:
            self.field_predefined_values = field_predefined_values
        self.name = name
        self.type = type
        self.maxsize = maxsize
        self.searchable = searchable
        self.required = required
        self.description = description
        self.position = position
        if field_type_id is not None:
            self.field_type_id = field_type_id
        if mtable is not None:
            self.mtable = mtable
        if raw_data is not None:
            self.raw_data = raw_data

    @property
    def id(self):
        """Gets the id of this Field.  # noqa: E501


        :return: The id of this Field.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Field.


        :param id: The id of this Field.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def tableid(self):
        """Gets the tableid of this Field.  # noqa: E501


        :return: The tableid of this Field.  # noqa: E501
        :rtype: int
        """
        return self._tableid

    @tableid.setter
    def tableid(self, tableid):
        """Sets the tableid of this Field.


        :param tableid: The tableid of this Field.  # noqa: E501
        :type: int
        """
        if tableid is None:
            raise ValueError("Invalid value for `tableid`, must not be `None`")  # noqa: E501

        self._tableid = tableid

    @property
    def field_types(self):
        """Gets the field_types of this Field.  # noqa: E501


        :return: The field_types of this Field.  # noqa: E501
        :rtype: FieldType
        """
        return self._field_types

    @field_types.setter
    def field_types(self, field_types):
        """Sets the field_types of this Field.


        :param field_types: The field_types of this Field.  # noqa: E501
        :type: FieldType
        """

        self._field_types = field_types

    @property
    def field_predefined_values(self):
        """Gets the field_predefined_values of this Field.  # noqa: E501


        :return: The field_predefined_values of this Field.  # noqa: E501
        :rtype: list[FieldPredefinedValue]
        """
        return self._field_predefined_values

    @field_predefined_values.setter
    def field_predefined_values(self, field_predefined_values):
        """Sets the field_predefined_values of this Field.


        :param field_predefined_values: The field_predefined_values of this Field.  # noqa: E501
        :type: list[FieldPredefinedValue]
        """

        self._field_predefined_values = field_predefined_values

    @property
    def name(self):
        """Gets the name of this Field.  # noqa: E501


        :return: The name of this Field.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Field.


        :param name: The name of this Field.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this Field.  # noqa: E501


        :return: The type of this Field.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Field.


        :param type: The type of this Field.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def maxsize(self):
        """Gets the maxsize of this Field.  # noqa: E501


        :return: The maxsize of this Field.  # noqa: E501
        :rtype: int
        """
        return self._maxsize

    @maxsize.setter
    def maxsize(self, maxsize):
        """Sets the maxsize of this Field.


        :param maxsize: The maxsize of this Field.  # noqa: E501
        :type: int
        """
        if maxsize is None:
            raise ValueError("Invalid value for `maxsize`, must not be `None`")  # noqa: E501

        self._maxsize = maxsize

    @property
    def searchable(self):
        """Gets the searchable of this Field.  # noqa: E501


        :return: The searchable of this Field.  # noqa: E501
        :rtype: bool
        """
        return self._searchable

    @searchable.setter
    def searchable(self, searchable):
        """Sets the searchable of this Field.


        :param searchable: The searchable of this Field.  # noqa: E501
        :type: bool
        """
        if searchable is None:
            raise ValueError("Invalid value for `searchable`, must not be `None`")  # noqa: E501

        self._searchable = searchable

    @property
    def required(self):
        """Gets the required of this Field.  # noqa: E501


        :return: The required of this Field.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this Field.


        :param required: The required of this Field.  # noqa: E501
        :type: bool
        """
        if required is None:
            raise ValueError("Invalid value for `required`, must not be `None`")  # noqa: E501

        self._required = required

    @property
    def description(self):
        """Gets the description of this Field.  # noqa: E501


        :return: The description of this Field.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Field.


        :param description: The description of this Field.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def position(self):
        """Gets the position of this Field.  # noqa: E501


        :return: The position of this Field.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Field.


        :param position: The position of this Field.  # noqa: E501
        :type: int
        """
        if position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

    @property
    def field_type_id(self):
        """Gets the field_type_id of this Field.  # noqa: E501


        :return: The field_type_id of this Field.  # noqa: E501
        :rtype: int
        """
        return self._field_type_id

    @field_type_id.setter
    def field_type_id(self, field_type_id):
        """Sets the field_type_id of this Field.


        :param field_type_id: The field_type_id of this Field.  # noqa: E501
        :type: int
        """

        self._field_type_id = field_type_id

    @property
    def mtable(self):
        """Gets the mtable of this Field.  # noqa: E501


        :return: The mtable of this Field.  # noqa: E501
        :rtype: MTable
        """
        return self._mtable

    @mtable.setter
    def mtable(self, mtable):
        """Sets the mtable of this Field.


        :param mtable: The mtable of this Field.  # noqa: E501
        :type: MTable
        """

        self._mtable = mtable

    @property
    def raw_data(self):
        """Gets the raw_data of this Field.  # noqa: E501


        :return: The raw_data of this Field.  # noqa: E501
        :rtype: list[RawData]
        """
        return self._raw_data

    @raw_data.setter
    def raw_data(self, raw_data):
        """Sets the raw_data of this Field.


        :param raw_data: The raw_data of this Field.  # noqa: E501
        :type: list[RawData]
        """

        self._raw_data = raw_data

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
        if issubclass(Field, dict):
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
        if not isinstance(other, Field):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
