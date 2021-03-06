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
from swagger_client.models.project_team_pk import ProjectTeamPK  # noqa: F401,E501
from swagger_client.models.users import Users  # noqa: F401,E501


class ProjectTeam(object):
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
        'project': 'Project',
        'user': 'Users',
        'project_team_pk': 'ProjectTeamPK',
        'team_role': 'str',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'project': 'project',
        'user': 'user',
        'project_team_pk': 'projectTeamPK',
        'team_role': 'teamRole',
        'timestamp': 'timestamp'
    }

    def __init__(self, project=None, user=None, project_team_pk=None, team_role=None, timestamp=None):  # noqa: E501
        """ProjectTeam - a model defined in Swagger"""  # noqa: E501
        self._project = None
        self._user = None
        self._project_team_pk = None
        self._team_role = None
        self._timestamp = None
        self.discriminator = None
        if project is not None:
            self.project = project
        if user is not None:
            self.user = user
        if project_team_pk is not None:
            self.project_team_pk = project_team_pk
        if team_role is not None:
            self.team_role = team_role
        self.timestamp = timestamp

    @property
    def project(self):
        """Gets the project of this ProjectTeam.  # noqa: E501


        :return: The project of this ProjectTeam.  # noqa: E501
        :rtype: Project
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ProjectTeam.


        :param project: The project of this ProjectTeam.  # noqa: E501
        :type: Project
        """

        self._project = project

    @property
    def user(self):
        """Gets the user of this ProjectTeam.  # noqa: E501


        :return: The user of this ProjectTeam.  # noqa: E501
        :rtype: Users
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ProjectTeam.


        :param user: The user of this ProjectTeam.  # noqa: E501
        :type: Users
        """

        self._user = user

    @property
    def project_team_pk(self):
        """Gets the project_team_pk of this ProjectTeam.  # noqa: E501


        :return: The project_team_pk of this ProjectTeam.  # noqa: E501
        :rtype: ProjectTeamPK
        """
        return self._project_team_pk

    @project_team_pk.setter
    def project_team_pk(self, project_team_pk):
        """Sets the project_team_pk of this ProjectTeam.


        :param project_team_pk: The project_team_pk of this ProjectTeam.  # noqa: E501
        :type: ProjectTeamPK
        """

        self._project_team_pk = project_team_pk

    @property
    def team_role(self):
        """Gets the team_role of this ProjectTeam.  # noqa: E501


        :return: The team_role of this ProjectTeam.  # noqa: E501
        :rtype: str
        """
        return self._team_role

    @team_role.setter
    def team_role(self, team_role):
        """Sets the team_role of this ProjectTeam.


        :param team_role: The team_role of this ProjectTeam.  # noqa: E501
        :type: str
        """

        self._team_role = team_role

    @property
    def timestamp(self):
        """Gets the timestamp of this ProjectTeam.  # noqa: E501


        :return: The timestamp of this ProjectTeam.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ProjectTeam.


        :param timestamp: The timestamp of this ProjectTeam.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

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
        if issubclass(ProjectTeam, dict):
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
        if not isinstance(other, ProjectTeam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
