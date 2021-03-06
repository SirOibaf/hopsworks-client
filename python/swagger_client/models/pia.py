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


class Pia(object):
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
        'personal_data': 'str',
        'how_data_collected': 'str',
        'specified_explicit_legitimate': 'int',
        'consent_process': 'str',
        'consent_basis': 'str',
        'data_minimized': 'int',
        'data_uptodate': 'int',
        'users_informed_how': 'str',
        'user_controls_data_collection_retention': 'str',
        'data_encrypted': 'int',
        'data_anonymized': 'int',
        'data_pseudonymized': 'int',
        'data_backedup': 'int',
        'data_security_measures': 'str',
        'data_portability_measure': 'str',
        'subject_access_rights': 'str',
        'risks': 'str',
        'project_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'personal_data': 'personalData',
        'how_data_collected': 'howDataCollected',
        'specified_explicit_legitimate': 'specifiedExplicitLegitimate',
        'consent_process': 'consentProcess',
        'consent_basis': 'consentBasis',
        'data_minimized': 'dataMinimized',
        'data_uptodate': 'dataUptodate',
        'users_informed_how': 'usersInformedHow',
        'user_controls_data_collection_retention': 'userControlsDataCollectionRetention',
        'data_encrypted': 'dataEncrypted',
        'data_anonymized': 'dataAnonymized',
        'data_pseudonymized': 'dataPseudonymized',
        'data_backedup': 'dataBackedup',
        'data_security_measures': 'dataSecurityMeasures',
        'data_portability_measure': 'dataPortabilityMeasure',
        'subject_access_rights': 'subjectAccessRights',
        'risks': 'risks',
        'project_id': 'projectId'
    }

    def __init__(self, id=None, personal_data=None, how_data_collected=None, specified_explicit_legitimate=None, consent_process=None, consent_basis=None, data_minimized=None, data_uptodate=None, users_informed_how=None, user_controls_data_collection_retention=None, data_encrypted=None, data_anonymized=None, data_pseudonymized=None, data_backedup=None, data_security_measures=None, data_portability_measure=None, subject_access_rights=None, risks=None, project_id=None):  # noqa: E501
        """Pia - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._personal_data = None
        self._how_data_collected = None
        self._specified_explicit_legitimate = None
        self._consent_process = None
        self._consent_basis = None
        self._data_minimized = None
        self._data_uptodate = None
        self._users_informed_how = None
        self._user_controls_data_collection_retention = None
        self._data_encrypted = None
        self._data_anonymized = None
        self._data_pseudonymized = None
        self._data_backedup = None
        self._data_security_measures = None
        self._data_portability_measure = None
        self._subject_access_rights = None
        self._risks = None
        self._project_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.personal_data = personal_data
        self.how_data_collected = how_data_collected
        self.specified_explicit_legitimate = specified_explicit_legitimate
        if consent_process is not None:
            self.consent_process = consent_process
        if consent_basis is not None:
            self.consent_basis = consent_basis
        self.data_minimized = data_minimized
        self.data_uptodate = data_uptodate
        self.users_informed_how = users_informed_how
        self.user_controls_data_collection_retention = user_controls_data_collection_retention
        self.data_encrypted = data_encrypted
        self.data_anonymized = data_anonymized
        self.data_pseudonymized = data_pseudonymized
        self.data_backedup = data_backedup
        self.data_security_measures = data_security_measures
        self.data_portability_measure = data_portability_measure
        self.subject_access_rights = subject_access_rights
        self.risks = risks
        if project_id is not None:
            self.project_id = project_id

    @property
    def id(self):
        """Gets the id of this Pia.  # noqa: E501


        :return: The id of this Pia.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Pia.


        :param id: The id of this Pia.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def personal_data(self):
        """Gets the personal_data of this Pia.  # noqa: E501


        :return: The personal_data of this Pia.  # noqa: E501
        :rtype: str
        """
        return self._personal_data

    @personal_data.setter
    def personal_data(self, personal_data):
        """Sets the personal_data of this Pia.


        :param personal_data: The personal_data of this Pia.  # noqa: E501
        :type: str
        """
        if personal_data is None:
            raise ValueError("Invalid value for `personal_data`, must not be `None`")  # noqa: E501

        self._personal_data = personal_data

    @property
    def how_data_collected(self):
        """Gets the how_data_collected of this Pia.  # noqa: E501


        :return: The how_data_collected of this Pia.  # noqa: E501
        :rtype: str
        """
        return self._how_data_collected

    @how_data_collected.setter
    def how_data_collected(self, how_data_collected):
        """Sets the how_data_collected of this Pia.


        :param how_data_collected: The how_data_collected of this Pia.  # noqa: E501
        :type: str
        """
        if how_data_collected is None:
            raise ValueError("Invalid value for `how_data_collected`, must not be `None`")  # noqa: E501

        self._how_data_collected = how_data_collected

    @property
    def specified_explicit_legitimate(self):
        """Gets the specified_explicit_legitimate of this Pia.  # noqa: E501


        :return: The specified_explicit_legitimate of this Pia.  # noqa: E501
        :rtype: int
        """
        return self._specified_explicit_legitimate

    @specified_explicit_legitimate.setter
    def specified_explicit_legitimate(self, specified_explicit_legitimate):
        """Sets the specified_explicit_legitimate of this Pia.


        :param specified_explicit_legitimate: The specified_explicit_legitimate of this Pia.  # noqa: E501
        :type: int
        """
        if specified_explicit_legitimate is None:
            raise ValueError("Invalid value for `specified_explicit_legitimate`, must not be `None`")  # noqa: E501

        self._specified_explicit_legitimate = specified_explicit_legitimate

    @property
    def consent_process(self):
        """Gets the consent_process of this Pia.  # noqa: E501


        :return: The consent_process of this Pia.  # noqa: E501
        :rtype: str
        """
        return self._consent_process

    @consent_process.setter
    def consent_process(self, consent_process):
        """Sets the consent_process of this Pia.


        :param consent_process: The consent_process of this Pia.  # noqa: E501
        :type: str
        """

        self._consent_process = consent_process

    @property
    def consent_basis(self):
        """Gets the consent_basis of this Pia.  # noqa: E501


        :return: The consent_basis of this Pia.  # noqa: E501
        :rtype: str
        """
        return self._consent_basis

    @consent_basis.setter
    def consent_basis(self, consent_basis):
        """Sets the consent_basis of this Pia.


        :param consent_basis: The consent_basis of this Pia.  # noqa: E501
        :type: str
        """

        self._consent_basis = consent_basis

    @property
    def data_minimized(self):
        """Gets the data_minimized of this Pia.  # noqa: E501


        :return: The data_minimized of this Pia.  # noqa: E501
        :rtype: int
        """
        return self._data_minimized

    @data_minimized.setter
    def data_minimized(self, data_minimized):
        """Sets the data_minimized of this Pia.


        :param data_minimized: The data_minimized of this Pia.  # noqa: E501
        :type: int
        """
        if data_minimized is None:
            raise ValueError("Invalid value for `data_minimized`, must not be `None`")  # noqa: E501

        self._data_minimized = data_minimized

    @property
    def data_uptodate(self):
        """Gets the data_uptodate of this Pia.  # noqa: E501


        :return: The data_uptodate of this Pia.  # noqa: E501
        :rtype: int
        """
        return self._data_uptodate

    @data_uptodate.setter
    def data_uptodate(self, data_uptodate):
        """Sets the data_uptodate of this Pia.


        :param data_uptodate: The data_uptodate of this Pia.  # noqa: E501
        :type: int
        """
        if data_uptodate is None:
            raise ValueError("Invalid value for `data_uptodate`, must not be `None`")  # noqa: E501

        self._data_uptodate = data_uptodate

    @property
    def users_informed_how(self):
        """Gets the users_informed_how of this Pia.  # noqa: E501


        :return: The users_informed_how of this Pia.  # noqa: E501
        :rtype: str
        """
        return self._users_informed_how

    @users_informed_how.setter
    def users_informed_how(self, users_informed_how):
        """Sets the users_informed_how of this Pia.


        :param users_informed_how: The users_informed_how of this Pia.  # noqa: E501
        :type: str
        """
        if users_informed_how is None:
            raise ValueError("Invalid value for `users_informed_how`, must not be `None`")  # noqa: E501

        self._users_informed_how = users_informed_how

    @property
    def user_controls_data_collection_retention(self):
        """Gets the user_controls_data_collection_retention of this Pia.  # noqa: E501


        :return: The user_controls_data_collection_retention of this Pia.  # noqa: E501
        :rtype: str
        """
        return self._user_controls_data_collection_retention

    @user_controls_data_collection_retention.setter
    def user_controls_data_collection_retention(self, user_controls_data_collection_retention):
        """Sets the user_controls_data_collection_retention of this Pia.


        :param user_controls_data_collection_retention: The user_controls_data_collection_retention of this Pia.  # noqa: E501
        :type: str
        """
        if user_controls_data_collection_retention is None:
            raise ValueError("Invalid value for `user_controls_data_collection_retention`, must not be `None`")  # noqa: E501

        self._user_controls_data_collection_retention = user_controls_data_collection_retention

    @property
    def data_encrypted(self):
        """Gets the data_encrypted of this Pia.  # noqa: E501


        :return: The data_encrypted of this Pia.  # noqa: E501
        :rtype: int
        """
        return self._data_encrypted

    @data_encrypted.setter
    def data_encrypted(self, data_encrypted):
        """Sets the data_encrypted of this Pia.


        :param data_encrypted: The data_encrypted of this Pia.  # noqa: E501
        :type: int
        """
        if data_encrypted is None:
            raise ValueError("Invalid value for `data_encrypted`, must not be `None`")  # noqa: E501

        self._data_encrypted = data_encrypted

    @property
    def data_anonymized(self):
        """Gets the data_anonymized of this Pia.  # noqa: E501


        :return: The data_anonymized of this Pia.  # noqa: E501
        :rtype: int
        """
        return self._data_anonymized

    @data_anonymized.setter
    def data_anonymized(self, data_anonymized):
        """Sets the data_anonymized of this Pia.


        :param data_anonymized: The data_anonymized of this Pia.  # noqa: E501
        :type: int
        """
        if data_anonymized is None:
            raise ValueError("Invalid value for `data_anonymized`, must not be `None`")  # noqa: E501

        self._data_anonymized = data_anonymized

    @property
    def data_pseudonymized(self):
        """Gets the data_pseudonymized of this Pia.  # noqa: E501


        :return: The data_pseudonymized of this Pia.  # noqa: E501
        :rtype: int
        """
        return self._data_pseudonymized

    @data_pseudonymized.setter
    def data_pseudonymized(self, data_pseudonymized):
        """Sets the data_pseudonymized of this Pia.


        :param data_pseudonymized: The data_pseudonymized of this Pia.  # noqa: E501
        :type: int
        """
        if data_pseudonymized is None:
            raise ValueError("Invalid value for `data_pseudonymized`, must not be `None`")  # noqa: E501

        self._data_pseudonymized = data_pseudonymized

    @property
    def data_backedup(self):
        """Gets the data_backedup of this Pia.  # noqa: E501


        :return: The data_backedup of this Pia.  # noqa: E501
        :rtype: int
        """
        return self._data_backedup

    @data_backedup.setter
    def data_backedup(self, data_backedup):
        """Sets the data_backedup of this Pia.


        :param data_backedup: The data_backedup of this Pia.  # noqa: E501
        :type: int
        """
        if data_backedup is None:
            raise ValueError("Invalid value for `data_backedup`, must not be `None`")  # noqa: E501

        self._data_backedup = data_backedup

    @property
    def data_security_measures(self):
        """Gets the data_security_measures of this Pia.  # noqa: E501


        :return: The data_security_measures of this Pia.  # noqa: E501
        :rtype: str
        """
        return self._data_security_measures

    @data_security_measures.setter
    def data_security_measures(self, data_security_measures):
        """Sets the data_security_measures of this Pia.


        :param data_security_measures: The data_security_measures of this Pia.  # noqa: E501
        :type: str
        """
        if data_security_measures is None:
            raise ValueError("Invalid value for `data_security_measures`, must not be `None`")  # noqa: E501

        self._data_security_measures = data_security_measures

    @property
    def data_portability_measure(self):
        """Gets the data_portability_measure of this Pia.  # noqa: E501


        :return: The data_portability_measure of this Pia.  # noqa: E501
        :rtype: str
        """
        return self._data_portability_measure

    @data_portability_measure.setter
    def data_portability_measure(self, data_portability_measure):
        """Sets the data_portability_measure of this Pia.


        :param data_portability_measure: The data_portability_measure of this Pia.  # noqa: E501
        :type: str
        """
        if data_portability_measure is None:
            raise ValueError("Invalid value for `data_portability_measure`, must not be `None`")  # noqa: E501

        self._data_portability_measure = data_portability_measure

    @property
    def subject_access_rights(self):
        """Gets the subject_access_rights of this Pia.  # noqa: E501


        :return: The subject_access_rights of this Pia.  # noqa: E501
        :rtype: str
        """
        return self._subject_access_rights

    @subject_access_rights.setter
    def subject_access_rights(self, subject_access_rights):
        """Sets the subject_access_rights of this Pia.


        :param subject_access_rights: The subject_access_rights of this Pia.  # noqa: E501
        :type: str
        """
        if subject_access_rights is None:
            raise ValueError("Invalid value for `subject_access_rights`, must not be `None`")  # noqa: E501

        self._subject_access_rights = subject_access_rights

    @property
    def risks(self):
        """Gets the risks of this Pia.  # noqa: E501


        :return: The risks of this Pia.  # noqa: E501
        :rtype: str
        """
        return self._risks

    @risks.setter
    def risks(self, risks):
        """Sets the risks of this Pia.


        :param risks: The risks of this Pia.  # noqa: E501
        :type: str
        """
        if risks is None:
            raise ValueError("Invalid value for `risks`, must not be `None`")  # noqa: E501

        self._risks = risks

    @property
    def project_id(self):
        """Gets the project_id of this Pia.  # noqa: E501


        :return: The project_id of this Pia.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Pia.


        :param project_id: The project_id of this Pia.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

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
        if issubclass(Pia, dict):
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
        if not isinstance(other, Pia):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
