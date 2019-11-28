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
from swagger_client.models.featurestore_hopsfs_connector import FeaturestoreHopsfsConnector  # noqa: F401,E501
from swagger_client.models.featurestore_jdbc_connector import FeaturestoreJdbcConnector  # noqa: F401,E501
from swagger_client.models.featurestore_s3_connector import FeaturestoreS3Connector  # noqa: F401,E501
from swagger_client.models.project import Project  # noqa: F401,E501


class Featurestore(object):
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
        'project': 'Project',
        'created': 'datetime',
        'hive_db_id': 'int',
        'featurestore_jdbc_connector_connections': 'list[FeaturestoreJdbcConnector]',
        'featurestore_s3_connector_connections': 'list[FeaturestoreS3Connector]',
        'hopsfs_connections': 'list[FeaturestoreHopsfsConnector]'
    }

    attribute_map = {
        'id': 'id',
        'project': 'project',
        'created': 'created',
        'hive_db_id': 'hiveDbId',
        'featurestore_jdbc_connector_connections': 'featurestoreJdbcConnectorConnections',
        'featurestore_s3_connector_connections': 'featurestoreS3ConnectorConnections',
        'hopsfs_connections': 'hopsfsConnections'
    }

    def __init__(self, id=None, project=None, created=None, hive_db_id=None, featurestore_jdbc_connector_connections=None, featurestore_s3_connector_connections=None, hopsfs_connections=None):  # noqa: E501
        """Featurestore - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._project = None
        self._created = None
        self._hive_db_id = None
        self._featurestore_jdbc_connector_connections = None
        self._featurestore_s3_connector_connections = None
        self._hopsfs_connections = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if project is not None:
            self.project = project
        if created is not None:
            self.created = created
        self.hive_db_id = hive_db_id
        if featurestore_jdbc_connector_connections is not None:
            self.featurestore_jdbc_connector_connections = featurestore_jdbc_connector_connections
        if featurestore_s3_connector_connections is not None:
            self.featurestore_s3_connector_connections = featurestore_s3_connector_connections
        if hopsfs_connections is not None:
            self.hopsfs_connections = hopsfs_connections

    @property
    def id(self):
        """Gets the id of this Featurestore.  # noqa: E501


        :return: The id of this Featurestore.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Featurestore.


        :param id: The id of this Featurestore.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def project(self):
        """Gets the project of this Featurestore.  # noqa: E501


        :return: The project of this Featurestore.  # noqa: E501
        :rtype: Project
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Featurestore.


        :param project: The project of this Featurestore.  # noqa: E501
        :type: Project
        """

        self._project = project

    @property
    def created(self):
        """Gets the created of this Featurestore.  # noqa: E501


        :return: The created of this Featurestore.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Featurestore.


        :param created: The created of this Featurestore.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def hive_db_id(self):
        """Gets the hive_db_id of this Featurestore.  # noqa: E501


        :return: The hive_db_id of this Featurestore.  # noqa: E501
        :rtype: int
        """
        return self._hive_db_id

    @hive_db_id.setter
    def hive_db_id(self, hive_db_id):
        """Sets the hive_db_id of this Featurestore.


        :param hive_db_id: The hive_db_id of this Featurestore.  # noqa: E501
        :type: int
        """
        if hive_db_id is None:
            raise ValueError("Invalid value for `hive_db_id`, must not be `None`")  # noqa: E501

        self._hive_db_id = hive_db_id

    @property
    def featurestore_jdbc_connector_connections(self):
        """Gets the featurestore_jdbc_connector_connections of this Featurestore.  # noqa: E501


        :return: The featurestore_jdbc_connector_connections of this Featurestore.  # noqa: E501
        :rtype: list[FeaturestoreJdbcConnector]
        """
        return self._featurestore_jdbc_connector_connections

    @featurestore_jdbc_connector_connections.setter
    def featurestore_jdbc_connector_connections(self, featurestore_jdbc_connector_connections):
        """Sets the featurestore_jdbc_connector_connections of this Featurestore.


        :param featurestore_jdbc_connector_connections: The featurestore_jdbc_connector_connections of this Featurestore.  # noqa: E501
        :type: list[FeaturestoreJdbcConnector]
        """

        self._featurestore_jdbc_connector_connections = featurestore_jdbc_connector_connections

    @property
    def featurestore_s3_connector_connections(self):
        """Gets the featurestore_s3_connector_connections of this Featurestore.  # noqa: E501


        :return: The featurestore_s3_connector_connections of this Featurestore.  # noqa: E501
        :rtype: list[FeaturestoreS3Connector]
        """
        return self._featurestore_s3_connector_connections

    @featurestore_s3_connector_connections.setter
    def featurestore_s3_connector_connections(self, featurestore_s3_connector_connections):
        """Sets the featurestore_s3_connector_connections of this Featurestore.


        :param featurestore_s3_connector_connections: The featurestore_s3_connector_connections of this Featurestore.  # noqa: E501
        :type: list[FeaturestoreS3Connector]
        """

        self._featurestore_s3_connector_connections = featurestore_s3_connector_connections

    @property
    def hopsfs_connections(self):
        """Gets the hopsfs_connections of this Featurestore.  # noqa: E501


        :return: The hopsfs_connections of this Featurestore.  # noqa: E501
        :rtype: list[FeaturestoreHopsfsConnector]
        """
        return self._hopsfs_connections

    @hopsfs_connections.setter
    def hopsfs_connections(self, hopsfs_connections):
        """Sets the hopsfs_connections of this Featurestore.


        :param hopsfs_connections: The hopsfs_connections of this Featurestore.  # noqa: E501
        :type: list[FeaturestoreHopsfsConnector]
        """

        self._hopsfs_connections = hopsfs_connections

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
        if issubclass(Featurestore, dict):
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
        if not isinstance(other, Featurestore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other