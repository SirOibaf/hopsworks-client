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
from swagger_client.models.project import Project  # noqa: F401,E501


class JupyterProject(object):
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
        'pid': 'int',
        'port': 'int',
        'created': 'datetime',
        'expires': 'datetime',
        'secret': 'str',
        'token': 'str',
        'project_id': 'Project',
        'hdfs_user_id': 'int',
        'minutes_until_expiration': 'int'
    }

    attribute_map = {
        'pid': 'pid',
        'port': 'port',
        'created': 'created',
        'expires': 'expires',
        'secret': 'secret',
        'token': 'token',
        'project_id': 'projectId',
        'hdfs_user_id': 'hdfsUserId',
        'minutes_until_expiration': 'minutesUntilExpiration'
    }

    def __init__(self, pid=None, port=None, created=None, expires=None, secret=None, token=None, project_id=None, hdfs_user_id=None, minutes_until_expiration=None):  # noqa: E501
        """JupyterProject - a model defined in Swagger"""  # noqa: E501
        self._pid = None
        self._port = None
        self._created = None
        self._expires = None
        self._secret = None
        self._token = None
        self._project_id = None
        self._hdfs_user_id = None
        self._minutes_until_expiration = None
        self.discriminator = None
        self.pid = pid
        self.port = port
        self.created = created
        self.expires = expires
        self.secret = secret
        self.token = token
        if project_id is not None:
            self.project_id = project_id
        self.hdfs_user_id = hdfs_user_id
        if minutes_until_expiration is not None:
            self.minutes_until_expiration = minutes_until_expiration

    @property
    def pid(self):
        """Gets the pid of this JupyterProject.  # noqa: E501


        :return: The pid of this JupyterProject.  # noqa: E501
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this JupyterProject.


        :param pid: The pid of this JupyterProject.  # noqa: E501
        :type: int
        """
        if pid is None:
            raise ValueError("Invalid value for `pid`, must not be `None`")  # noqa: E501

        self._pid = pid

    @property
    def port(self):
        """Gets the port of this JupyterProject.  # noqa: E501


        :return: The port of this JupyterProject.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this JupyterProject.


        :param port: The port of this JupyterProject.  # noqa: E501
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def created(self):
        """Gets the created of this JupyterProject.  # noqa: E501


        :return: The created of this JupyterProject.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this JupyterProject.


        :param created: The created of this JupyterProject.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def expires(self):
        """Gets the expires of this JupyterProject.  # noqa: E501


        :return: The expires of this JupyterProject.  # noqa: E501
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this JupyterProject.


        :param expires: The expires of this JupyterProject.  # noqa: E501
        :type: datetime
        """
        if expires is None:
            raise ValueError("Invalid value for `expires`, must not be `None`")  # noqa: E501

        self._expires = expires

    @property
    def secret(self):
        """Gets the secret of this JupyterProject.  # noqa: E501


        :return: The secret of this JupyterProject.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this JupyterProject.


        :param secret: The secret of this JupyterProject.  # noqa: E501
        :type: str
        """
        if secret is None:
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def token(self):
        """Gets the token of this JupyterProject.  # noqa: E501


        :return: The token of this JupyterProject.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this JupyterProject.


        :param token: The token of this JupyterProject.  # noqa: E501
        :type: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def project_id(self):
        """Gets the project_id of this JupyterProject.  # noqa: E501


        :return: The project_id of this JupyterProject.  # noqa: E501
        :rtype: Project
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this JupyterProject.


        :param project_id: The project_id of this JupyterProject.  # noqa: E501
        :type: Project
        """

        self._project_id = project_id

    @property
    def hdfs_user_id(self):
        """Gets the hdfs_user_id of this JupyterProject.  # noqa: E501


        :return: The hdfs_user_id of this JupyterProject.  # noqa: E501
        :rtype: int
        """
        return self._hdfs_user_id

    @hdfs_user_id.setter
    def hdfs_user_id(self, hdfs_user_id):
        """Sets the hdfs_user_id of this JupyterProject.


        :param hdfs_user_id: The hdfs_user_id of this JupyterProject.  # noqa: E501
        :type: int
        """
        if hdfs_user_id is None:
            raise ValueError("Invalid value for `hdfs_user_id`, must not be `None`")  # noqa: E501

        self._hdfs_user_id = hdfs_user_id

    @property
    def minutes_until_expiration(self):
        """Gets the minutes_until_expiration of this JupyterProject.  # noqa: E501


        :return: The minutes_until_expiration of this JupyterProject.  # noqa: E501
        :rtype: int
        """
        return self._minutes_until_expiration

    @minutes_until_expiration.setter
    def minutes_until_expiration(self, minutes_until_expiration):
        """Sets the minutes_until_expiration of this JupyterProject.


        :param minutes_until_expiration: The minutes_until_expiration of this JupyterProject.  # noqa: E501
        :type: int
        """

        self._minutes_until_expiration = minutes_until_expiration

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
        if issubclass(JupyterProject, dict):
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
        if not isinstance(other, JupyterProject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
