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
from swagger_client.models.quotas_dto import QuotasDTO  # noqa: F401,E501


class ProjectAdminInfoDTO(object):
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
        'project_name': 'str',
        'project_owner': 'str',
        'archived': 'bool',
        'payment_type': 'str',
        'last_quota_update': 'datetime',
        'project_quotas': 'QuotasDTO'
    }

    attribute_map = {
        'project_name': 'projectName',
        'project_owner': 'projectOwner',
        'archived': 'archived',
        'payment_type': 'paymentType',
        'last_quota_update': 'lastQuotaUpdate',
        'project_quotas': 'projectQuotas'
    }

    def __init__(self, project_name=None, project_owner=None, archived=None, payment_type=None, last_quota_update=None, project_quotas=None):  # noqa: E501
        """ProjectAdminInfoDTO - a model defined in Swagger"""  # noqa: E501
        self._project_name = None
        self._project_owner = None
        self._archived = None
        self._payment_type = None
        self._last_quota_update = None
        self._project_quotas = None
        self.discriminator = None
        if project_name is not None:
            self.project_name = project_name
        if project_owner is not None:
            self.project_owner = project_owner
        if archived is not None:
            self.archived = archived
        if payment_type is not None:
            self.payment_type = payment_type
        if last_quota_update is not None:
            self.last_quota_update = last_quota_update
        if project_quotas is not None:
            self.project_quotas = project_quotas

    @property
    def project_name(self):
        """Gets the project_name of this ProjectAdminInfoDTO.  # noqa: E501


        :return: The project_name of this ProjectAdminInfoDTO.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ProjectAdminInfoDTO.


        :param project_name: The project_name of this ProjectAdminInfoDTO.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def project_owner(self):
        """Gets the project_owner of this ProjectAdminInfoDTO.  # noqa: E501


        :return: The project_owner of this ProjectAdminInfoDTO.  # noqa: E501
        :rtype: str
        """
        return self._project_owner

    @project_owner.setter
    def project_owner(self, project_owner):
        """Sets the project_owner of this ProjectAdminInfoDTO.


        :param project_owner: The project_owner of this ProjectAdminInfoDTO.  # noqa: E501
        :type: str
        """

        self._project_owner = project_owner

    @property
    def archived(self):
        """Gets the archived of this ProjectAdminInfoDTO.  # noqa: E501


        :return: The archived of this ProjectAdminInfoDTO.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this ProjectAdminInfoDTO.


        :param archived: The archived of this ProjectAdminInfoDTO.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def payment_type(self):
        """Gets the payment_type of this ProjectAdminInfoDTO.  # noqa: E501


        :return: The payment_type of this ProjectAdminInfoDTO.  # noqa: E501
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this ProjectAdminInfoDTO.


        :param payment_type: The payment_type of this ProjectAdminInfoDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["PREPAID", "NOLIMIT"]  # noqa: E501
        if payment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_type, allowed_values)
            )

        self._payment_type = payment_type

    @property
    def last_quota_update(self):
        """Gets the last_quota_update of this ProjectAdminInfoDTO.  # noqa: E501


        :return: The last_quota_update of this ProjectAdminInfoDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_quota_update

    @last_quota_update.setter
    def last_quota_update(self, last_quota_update):
        """Sets the last_quota_update of this ProjectAdminInfoDTO.


        :param last_quota_update: The last_quota_update of this ProjectAdminInfoDTO.  # noqa: E501
        :type: datetime
        """

        self._last_quota_update = last_quota_update

    @property
    def project_quotas(self):
        """Gets the project_quotas of this ProjectAdminInfoDTO.  # noqa: E501


        :return: The project_quotas of this ProjectAdminInfoDTO.  # noqa: E501
        :rtype: QuotasDTO
        """
        return self._project_quotas

    @project_quotas.setter
    def project_quotas(self, project_quotas):
        """Sets the project_quotas of this ProjectAdminInfoDTO.


        :param project_quotas: The project_quotas of this ProjectAdminInfoDTO.  # noqa: E501
        :type: QuotasDTO
        """

        self._project_quotas = project_quotas

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
        if issubclass(ProjectAdminInfoDTO, dict):
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
        if not isinstance(other, ProjectAdminInfoDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other