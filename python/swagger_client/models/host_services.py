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
from swagger_client.models.hosts import Hosts  # noqa: F401,E501


class HostServices(object):
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
        'pid': 'int',
        'group': 'str',
        'service': 'str',
        'status': 'str',
        'uptime': 'int',
        'start_time': 'int',
        'stop_time': 'int',
        'host': 'Hosts',
        'health': 'str'
    }

    attribute_map = {
        'id': 'id',
        'pid': 'pid',
        'group': 'group',
        'service': 'service',
        'status': 'status',
        'uptime': 'uptime',
        'start_time': 'startTime',
        'stop_time': 'stopTime',
        'host': 'host',
        'health': 'health'
    }

    def __init__(self, id=None, pid=None, group=None, service=None, status=None, uptime=None, start_time=None, stop_time=None, host=None, health=None):  # noqa: E501
        """HostServices - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._pid = None
        self._group = None
        self._service = None
        self._status = None
        self._uptime = None
        self._start_time = None
        self._stop_time = None
        self._host = None
        self._health = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if pid is not None:
            self.pid = pid
        self.group = group
        self.service = service
        self.status = status
        if uptime is not None:
            self.uptime = uptime
        if start_time is not None:
            self.start_time = start_time
        if stop_time is not None:
            self.stop_time = stop_time
        if host is not None:
            self.host = host
        if health is not None:
            self.health = health

    @property
    def id(self):
        """Gets the id of this HostServices.  # noqa: E501


        :return: The id of this HostServices.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HostServices.


        :param id: The id of this HostServices.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def pid(self):
        """Gets the pid of this HostServices.  # noqa: E501


        :return: The pid of this HostServices.  # noqa: E501
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this HostServices.


        :param pid: The pid of this HostServices.  # noqa: E501
        :type: int
        """

        self._pid = pid

    @property
    def group(self):
        """Gets the group of this HostServices.  # noqa: E501


        :return: The group of this HostServices.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this HostServices.


        :param group: The group of this HostServices.  # noqa: E501
        :type: str
        """
        if group is None:
            raise ValueError("Invalid value for `group`, must not be `None`")  # noqa: E501

        self._group = group

    @property
    def service(self):
        """Gets the service of this HostServices.  # noqa: E501


        :return: The service of this HostServices.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this HostServices.


        :param service: The service of this HostServices.  # noqa: E501
        :type: str
        """
        if service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501

        self._service = service

    @property
    def status(self):
        """Gets the status of this HostServices.  # noqa: E501


        :return: The status of this HostServices.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this HostServices.


        :param status: The status of this HostServices.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["Started", "Stopped", "Failed", "TimedOut", "None"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def uptime(self):
        """Gets the uptime of this HostServices.  # noqa: E501


        :return: The uptime of this HostServices.  # noqa: E501
        :rtype: int
        """
        return self._uptime

    @uptime.setter
    def uptime(self, uptime):
        """Sets the uptime of this HostServices.


        :param uptime: The uptime of this HostServices.  # noqa: E501
        :type: int
        """

        self._uptime = uptime

    @property
    def start_time(self):
        """Gets the start_time of this HostServices.  # noqa: E501


        :return: The start_time of this HostServices.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this HostServices.


        :param start_time: The start_time of this HostServices.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def stop_time(self):
        """Gets the stop_time of this HostServices.  # noqa: E501


        :return: The stop_time of this HostServices.  # noqa: E501
        :rtype: int
        """
        return self._stop_time

    @stop_time.setter
    def stop_time(self, stop_time):
        """Sets the stop_time of this HostServices.


        :param stop_time: The stop_time of this HostServices.  # noqa: E501
        :type: int
        """

        self._stop_time = stop_time

    @property
    def host(self):
        """Gets the host of this HostServices.  # noqa: E501


        :return: The host of this HostServices.  # noqa: E501
        :rtype: Hosts
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this HostServices.


        :param host: The host of this HostServices.  # noqa: E501
        :type: Hosts
        """

        self._host = host

    @property
    def health(self):
        """Gets the health of this HostServices.  # noqa: E501


        :return: The health of this HostServices.  # noqa: E501
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this HostServices.


        :param health: The health of this HostServices.  # noqa: E501
        :type: str
        """
        allowed_values = ["Good", "Bad"]  # noqa: E501
        if health not in allowed_values:
            raise ValueError(
                "Invalid value for `health` ({0}), must be one of {1}"  # noqa: E501
                .format(health, allowed_values)
            )

        self._health = health

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
        if issubclass(HostServices, dict):
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
        if not isinstance(other, HostServices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other