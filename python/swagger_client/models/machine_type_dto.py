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
from swagger_client.models.machine_type_dto import MachineTypeDTO  # noqa: F401,E501


class MachineTypeDTO(object):
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
        'items': 'list[MachineTypeDTO]',
        'count': 'int',
        'machine_type': 'str',
        'num_machines': 'int'
    }

    attribute_map = {
        'href': 'href',
        'items': 'items',
        'count': 'count',
        'machine_type': 'machineType',
        'num_machines': 'numMachines'
    }

    def __init__(self, href=None, items=None, count=None, machine_type=None, num_machines=None):  # noqa: E501
        """MachineTypeDTO - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._items = None
        self._count = None
        self._machine_type = None
        self._num_machines = None
        self.discriminator = None
        if href is not None:
            self.href = href
        if items is not None:
            self.items = items
        if count is not None:
            self.count = count
        if machine_type is not None:
            self.machine_type = machine_type
        if num_machines is not None:
            self.num_machines = num_machines

    @property
    def href(self):
        """Gets the href of this MachineTypeDTO.  # noqa: E501


        :return: The href of this MachineTypeDTO.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this MachineTypeDTO.


        :param href: The href of this MachineTypeDTO.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def items(self):
        """Gets the items of this MachineTypeDTO.  # noqa: E501


        :return: The items of this MachineTypeDTO.  # noqa: E501
        :rtype: list[MachineTypeDTO]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this MachineTypeDTO.


        :param items: The items of this MachineTypeDTO.  # noqa: E501
        :type: list[MachineTypeDTO]
        """

        self._items = items

    @property
    def count(self):
        """Gets the count of this MachineTypeDTO.  # noqa: E501


        :return: The count of this MachineTypeDTO.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this MachineTypeDTO.


        :param count: The count of this MachineTypeDTO.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def machine_type(self):
        """Gets the machine_type of this MachineTypeDTO.  # noqa: E501


        :return: The machine_type of this MachineTypeDTO.  # noqa: E501
        :rtype: str
        """
        return self._machine_type

    @machine_type.setter
    def machine_type(self, machine_type):
        """Sets the machine_type of this MachineTypeDTO.


        :param machine_type: The machine_type of this MachineTypeDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALL", "CPU", "GPU"]  # noqa: E501
        if machine_type not in allowed_values:
            raise ValueError(
                "Invalid value for `machine_type` ({0}), must be one of {1}"  # noqa: E501
                .format(machine_type, allowed_values)
            )

        self._machine_type = machine_type

    @property
    def num_machines(self):
        """Gets the num_machines of this MachineTypeDTO.  # noqa: E501


        :return: The num_machines of this MachineTypeDTO.  # noqa: E501
        :rtype: int
        """
        return self._num_machines

    @num_machines.setter
    def num_machines(self, num_machines):
        """Sets the num_machines of this MachineTypeDTO.


        :param num_machines: The num_machines of this MachineTypeDTO.  # noqa: E501
        :type: int
        """

        self._num_machines = num_machines

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
        if issubclass(MachineTypeDTO, dict):
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
        if not isinstance(other, MachineTypeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
