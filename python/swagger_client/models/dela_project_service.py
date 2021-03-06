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
from swagger_client.models.response import Response  # noqa: F401,E501


class DelaProjectService(object):
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
        'project_id': 'int',
        'project_contents': 'Response'
    }

    attribute_map = {
        'project_id': 'projectId',
        'project_contents': 'projectContents'
    }

    def __init__(self, project_id=None, project_contents=None):  # noqa: E501
        """DelaProjectService - a model defined in Swagger"""  # noqa: E501
        self._project_id = None
        self._project_contents = None
        self.discriminator = None
        if project_id is not None:
            self.project_id = project_id
        if project_contents is not None:
            self.project_contents = project_contents

    @property
    def project_id(self):
        """Gets the project_id of this DelaProjectService.  # noqa: E501


        :return: The project_id of this DelaProjectService.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DelaProjectService.


        :param project_id: The project_id of this DelaProjectService.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def project_contents(self):
        """Gets the project_contents of this DelaProjectService.  # noqa: E501


        :return: The project_contents of this DelaProjectService.  # noqa: E501
        :rtype: Response
        """
        return self._project_contents

    @project_contents.setter
    def project_contents(self, project_contents):
        """Sets the project_contents of this DelaProjectService.


        :param project_contents: The project_contents of this DelaProjectService.  # noqa: E501
        :type: Response
        """

        self._project_contents = project_contents

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
        if issubclass(DelaProjectService, dict):
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
        if not isinstance(other, DelaProjectService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
