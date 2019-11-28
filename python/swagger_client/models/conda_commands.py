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
from swagger_client.models.project import Project  # noqa: F401,E501


class CondaCommands(object):
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
        'user': 'str',
        'proj': 'str',
        'channel_url': 'str',
        'arg': 'str',
        'lib': 'str',
        'version': 'str',
        'op': 'str',
        'status': 'str',
        'install_type': 'str',
        'machine_type': 'str',
        'created': 'datetime',
        'project_id': 'Project',
        'host_id': 'Hosts',
        'environment_yml': 'str',
        'install_jupyter': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'proj': 'proj',
        'channel_url': 'channelUrl',
        'arg': 'arg',
        'lib': 'lib',
        'version': 'version',
        'op': 'op',
        'status': 'status',
        'install_type': 'installType',
        'machine_type': 'machineType',
        'created': 'created',
        'project_id': 'projectId',
        'host_id': 'hostId',
        'environment_yml': 'environmentYml',
        'install_jupyter': 'installJupyter'
    }

    def __init__(self, id=None, user=None, proj=None, channel_url=None, arg=None, lib=None, version=None, op=None, status=None, install_type=None, machine_type=None, created=None, project_id=None, host_id=None, environment_yml=None, install_jupyter=None):  # noqa: E501
        """CondaCommands - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._user = None
        self._proj = None
        self._channel_url = None
        self._arg = None
        self._lib = None
        self._version = None
        self._op = None
        self._status = None
        self._install_type = None
        self._machine_type = None
        self._created = None
        self._project_id = None
        self._host_id = None
        self._environment_yml = None
        self._install_jupyter = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.user = user
        self.proj = proj
        if channel_url is not None:
            self.channel_url = channel_url
        if arg is not None:
            self.arg = arg
        if lib is not None:
            self.lib = lib
        if version is not None:
            self.version = version
        self.op = op
        self.status = status
        self.install_type = install_type
        self.machine_type = machine_type
        self.created = created
        if project_id is not None:
            self.project_id = project_id
        if host_id is not None:
            self.host_id = host_id
        if environment_yml is not None:
            self.environment_yml = environment_yml
        if install_jupyter is not None:
            self.install_jupyter = install_jupyter

    @property
    def id(self):
        """Gets the id of this CondaCommands.  # noqa: E501


        :return: The id of this CondaCommands.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CondaCommands.


        :param id: The id of this CondaCommands.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def user(self):
        """Gets the user of this CondaCommands.  # noqa: E501


        :return: The user of this CondaCommands.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this CondaCommands.


        :param user: The user of this CondaCommands.  # noqa: E501
        :type: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def proj(self):
        """Gets the proj of this CondaCommands.  # noqa: E501


        :return: The proj of this CondaCommands.  # noqa: E501
        :rtype: str
        """
        return self._proj

    @proj.setter
    def proj(self, proj):
        """Sets the proj of this CondaCommands.


        :param proj: The proj of this CondaCommands.  # noqa: E501
        :type: str
        """
        if proj is None:
            raise ValueError("Invalid value for `proj`, must not be `None`")  # noqa: E501

        self._proj = proj

    @property
    def channel_url(self):
        """Gets the channel_url of this CondaCommands.  # noqa: E501


        :return: The channel_url of this CondaCommands.  # noqa: E501
        :rtype: str
        """
        return self._channel_url

    @channel_url.setter
    def channel_url(self, channel_url):
        """Sets the channel_url of this CondaCommands.


        :param channel_url: The channel_url of this CondaCommands.  # noqa: E501
        :type: str
        """

        self._channel_url = channel_url

    @property
    def arg(self):
        """Gets the arg of this CondaCommands.  # noqa: E501


        :return: The arg of this CondaCommands.  # noqa: E501
        :rtype: str
        """
        return self._arg

    @arg.setter
    def arg(self, arg):
        """Sets the arg of this CondaCommands.


        :param arg: The arg of this CondaCommands.  # noqa: E501
        :type: str
        """

        self._arg = arg

    @property
    def lib(self):
        """Gets the lib of this CondaCommands.  # noqa: E501


        :return: The lib of this CondaCommands.  # noqa: E501
        :rtype: str
        """
        return self._lib

    @lib.setter
    def lib(self, lib):
        """Sets the lib of this CondaCommands.


        :param lib: The lib of this CondaCommands.  # noqa: E501
        :type: str
        """

        self._lib = lib

    @property
    def version(self):
        """Gets the version of this CondaCommands.  # noqa: E501


        :return: The version of this CondaCommands.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CondaCommands.


        :param version: The version of this CondaCommands.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def op(self):
        """Gets the op of this CondaCommands.  # noqa: E501


        :return: The op of this CondaCommands.  # noqa: E501
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this CondaCommands.


        :param op: The op of this CondaCommands.  # noqa: E501
        :type: str
        """
        if op is None:
            raise ValueError("Invalid value for `op`, must not be `None`")  # noqa: E501
        allowed_values = ["CLONE", "CREATE", "BACKUP", "REMOVE", "LIST", "INSTALL", "UNINSTALL", "UPGRADE", "CLEAN", "YML"]  # noqa: E501
        if op not in allowed_values:
            raise ValueError(
                "Invalid value for `op` ({0}), must be one of {1}"  # noqa: E501
                .format(op, allowed_values)
            )

        self._op = op

    @property
    def status(self):
        """Gets the status of this CondaCommands.  # noqa: E501


        :return: The status of this CondaCommands.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CondaCommands.


        :param status: The status of this CondaCommands.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["NEW", "SUCCESS", "ONGOING", "FAILED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def install_type(self):
        """Gets the install_type of this CondaCommands.  # noqa: E501


        :return: The install_type of this CondaCommands.  # noqa: E501
        :rtype: str
        """
        return self._install_type

    @install_type.setter
    def install_type(self, install_type):
        """Sets the install_type of this CondaCommands.


        :param install_type: The install_type of this CondaCommands.  # noqa: E501
        :type: str
        """
        if install_type is None:
            raise ValueError("Invalid value for `install_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ENVIRONMENT", "CONDA", "PIP"]  # noqa: E501
        if install_type not in allowed_values:
            raise ValueError(
                "Invalid value for `install_type` ({0}), must be one of {1}"  # noqa: E501
                .format(install_type, allowed_values)
            )

        self._install_type = install_type

    @property
    def machine_type(self):
        """Gets the machine_type of this CondaCommands.  # noqa: E501


        :return: The machine_type of this CondaCommands.  # noqa: E501
        :rtype: str
        """
        return self._machine_type

    @machine_type.setter
    def machine_type(self, machine_type):
        """Sets the machine_type of this CondaCommands.


        :param machine_type: The machine_type of this CondaCommands.  # noqa: E501
        :type: str
        """
        if machine_type is None:
            raise ValueError("Invalid value for `machine_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ALL", "CPU", "GPU"]  # noqa: E501
        if machine_type not in allowed_values:
            raise ValueError(
                "Invalid value for `machine_type` ({0}), must be one of {1}"  # noqa: E501
                .format(machine_type, allowed_values)
            )

        self._machine_type = machine_type

    @property
    def created(self):
        """Gets the created of this CondaCommands.  # noqa: E501


        :return: The created of this CondaCommands.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CondaCommands.


        :param created: The created of this CondaCommands.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def project_id(self):
        """Gets the project_id of this CondaCommands.  # noqa: E501


        :return: The project_id of this CondaCommands.  # noqa: E501
        :rtype: Project
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CondaCommands.


        :param project_id: The project_id of this CondaCommands.  # noqa: E501
        :type: Project
        """

        self._project_id = project_id

    @property
    def host_id(self):
        """Gets the host_id of this CondaCommands.  # noqa: E501


        :return: The host_id of this CondaCommands.  # noqa: E501
        :rtype: Hosts
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this CondaCommands.


        :param host_id: The host_id of this CondaCommands.  # noqa: E501
        :type: Hosts
        """

        self._host_id = host_id

    @property
    def environment_yml(self):
        """Gets the environment_yml of this CondaCommands.  # noqa: E501


        :return: The environment_yml of this CondaCommands.  # noqa: E501
        :rtype: str
        """
        return self._environment_yml

    @environment_yml.setter
    def environment_yml(self, environment_yml):
        """Sets the environment_yml of this CondaCommands.


        :param environment_yml: The environment_yml of this CondaCommands.  # noqa: E501
        :type: str
        """

        self._environment_yml = environment_yml

    @property
    def install_jupyter(self):
        """Gets the install_jupyter of this CondaCommands.  # noqa: E501


        :return: The install_jupyter of this CondaCommands.  # noqa: E501
        :rtype: bool
        """
        return self._install_jupyter

    @install_jupyter.setter
    def install_jupyter(self, install_jupyter):
        """Sets the install_jupyter of this CondaCommands.


        :param install_jupyter: The install_jupyter of this CondaCommands.  # noqa: E501
        :type: bool
        """

        self._install_jupyter = install_jupyter

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
        if issubclass(CondaCommands, dict):
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
        if not isinstance(other, CondaCommands):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other