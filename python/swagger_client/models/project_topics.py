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
from swagger_client.models.schema_topics import SchemaTopics  # noqa: F401,E501
from swagger_client.models.topic_acls import TopicAcls  # noqa: F401,E501


class ProjectTopics(object):
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
        'topic_name': 'str',
        'project': 'Project',
        'topic_acls_collection': 'list[TopicAcls]',
        'schema_topics': 'SchemaTopics'
    }

    attribute_map = {
        'id': 'id',
        'topic_name': 'topicName',
        'project': 'project',
        'topic_acls_collection': 'topicAclsCollection',
        'schema_topics': 'schemaTopics'
    }

    def __init__(self, id=None, topic_name=None, project=None, topic_acls_collection=None, schema_topics=None):  # noqa: E501
        """ProjectTopics - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._topic_name = None
        self._project = None
        self._topic_acls_collection = None
        self._schema_topics = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.topic_name = topic_name
        if project is not None:
            self.project = project
        if topic_acls_collection is not None:
            self.topic_acls_collection = topic_acls_collection
        if schema_topics is not None:
            self.schema_topics = schema_topics

    @property
    def id(self):
        """Gets the id of this ProjectTopics.  # noqa: E501


        :return: The id of this ProjectTopics.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectTopics.


        :param id: The id of this ProjectTopics.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def topic_name(self):
        """Gets the topic_name of this ProjectTopics.  # noqa: E501


        :return: The topic_name of this ProjectTopics.  # noqa: E501
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """Sets the topic_name of this ProjectTopics.


        :param topic_name: The topic_name of this ProjectTopics.  # noqa: E501
        :type: str
        """
        if topic_name is None:
            raise ValueError("Invalid value for `topic_name`, must not be `None`")  # noqa: E501

        self._topic_name = topic_name

    @property
    def project(self):
        """Gets the project of this ProjectTopics.  # noqa: E501


        :return: The project of this ProjectTopics.  # noqa: E501
        :rtype: Project
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ProjectTopics.


        :param project: The project of this ProjectTopics.  # noqa: E501
        :type: Project
        """

        self._project = project

    @property
    def topic_acls_collection(self):
        """Gets the topic_acls_collection of this ProjectTopics.  # noqa: E501


        :return: The topic_acls_collection of this ProjectTopics.  # noqa: E501
        :rtype: list[TopicAcls]
        """
        return self._topic_acls_collection

    @topic_acls_collection.setter
    def topic_acls_collection(self, topic_acls_collection):
        """Sets the topic_acls_collection of this ProjectTopics.


        :param topic_acls_collection: The topic_acls_collection of this ProjectTopics.  # noqa: E501
        :type: list[TopicAcls]
        """

        self._topic_acls_collection = topic_acls_collection

    @property
    def schema_topics(self):
        """Gets the schema_topics of this ProjectTopics.  # noqa: E501


        :return: The schema_topics of this ProjectTopics.  # noqa: E501
        :rtype: SchemaTopics
        """
        return self._schema_topics

    @schema_topics.setter
    def schema_topics(self, schema_topics):
        """Sets the schema_topics of this ProjectTopics.


        :param schema_topics: The schema_topics of this ProjectTopics.  # noqa: E501
        :type: SchemaTopics
        """

        self._schema_topics = schema_topics

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
        if issubclass(ProjectTopics, dict):
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
        if not isinstance(other, ProjectTopics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
