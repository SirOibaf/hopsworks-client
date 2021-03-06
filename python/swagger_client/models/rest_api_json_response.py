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


class RESTApiJsonResponse(object):
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
        'error_msg': 'str',
        'success_message': 'str',
        'error_code': 'int',
        'usr_msg': 'str',
        'dev_msg': 'str',
        'trace': 'str',
        'field_errors': 'list[str]',
        'data': 'object',
        'session_id': 'str',
        'qrcode': 'str'
    }

    attribute_map = {
        'error_msg': 'errorMsg',
        'success_message': 'successMessage',
        'error_code': 'errorCode',
        'usr_msg': 'usrMsg',
        'dev_msg': 'devMsg',
        'trace': 'trace',
        'field_errors': 'fieldErrors',
        'data': 'data',
        'session_id': 'sessionID',
        'qrcode': 'qrcode'
    }

    def __init__(self, error_msg=None, success_message=None, error_code=None, usr_msg=None, dev_msg=None, trace=None, field_errors=None, data=None, session_id=None, qrcode=None):  # noqa: E501
        """RESTApiJsonResponse - a model defined in Swagger"""  # noqa: E501
        self._error_msg = None
        self._success_message = None
        self._error_code = None
        self._usr_msg = None
        self._dev_msg = None
        self._trace = None
        self._field_errors = None
        self._data = None
        self._session_id = None
        self._qrcode = None
        self.discriminator = None
        if error_msg is not None:
            self.error_msg = error_msg
        if success_message is not None:
            self.success_message = success_message
        if error_code is not None:
            self.error_code = error_code
        if usr_msg is not None:
            self.usr_msg = usr_msg
        if dev_msg is not None:
            self.dev_msg = dev_msg
        if trace is not None:
            self.trace = trace
        if field_errors is not None:
            self.field_errors = field_errors
        if data is not None:
            self.data = data
        if session_id is not None:
            self.session_id = session_id
        if qrcode is not None:
            self.qrcode = qrcode

    @property
    def error_msg(self):
        """Gets the error_msg of this RESTApiJsonResponse.  # noqa: E501


        :return: The error_msg of this RESTApiJsonResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this RESTApiJsonResponse.


        :param error_msg: The error_msg of this RESTApiJsonResponse.  # noqa: E501
        :type: str
        """

        self._error_msg = error_msg

    @property
    def success_message(self):
        """Gets the success_message of this RESTApiJsonResponse.  # noqa: E501


        :return: The success_message of this RESTApiJsonResponse.  # noqa: E501
        :rtype: str
        """
        return self._success_message

    @success_message.setter
    def success_message(self, success_message):
        """Sets the success_message of this RESTApiJsonResponse.


        :param success_message: The success_message of this RESTApiJsonResponse.  # noqa: E501
        :type: str
        """

        self._success_message = success_message

    @property
    def error_code(self):
        """Gets the error_code of this RESTApiJsonResponse.  # noqa: E501


        :return: The error_code of this RESTApiJsonResponse.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this RESTApiJsonResponse.


        :param error_code: The error_code of this RESTApiJsonResponse.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def usr_msg(self):
        """Gets the usr_msg of this RESTApiJsonResponse.  # noqa: E501


        :return: The usr_msg of this RESTApiJsonResponse.  # noqa: E501
        :rtype: str
        """
        return self._usr_msg

    @usr_msg.setter
    def usr_msg(self, usr_msg):
        """Sets the usr_msg of this RESTApiJsonResponse.


        :param usr_msg: The usr_msg of this RESTApiJsonResponse.  # noqa: E501
        :type: str
        """

        self._usr_msg = usr_msg

    @property
    def dev_msg(self):
        """Gets the dev_msg of this RESTApiJsonResponse.  # noqa: E501


        :return: The dev_msg of this RESTApiJsonResponse.  # noqa: E501
        :rtype: str
        """
        return self._dev_msg

    @dev_msg.setter
    def dev_msg(self, dev_msg):
        """Sets the dev_msg of this RESTApiJsonResponse.


        :param dev_msg: The dev_msg of this RESTApiJsonResponse.  # noqa: E501
        :type: str
        """

        self._dev_msg = dev_msg

    @property
    def trace(self):
        """Gets the trace of this RESTApiJsonResponse.  # noqa: E501


        :return: The trace of this RESTApiJsonResponse.  # noqa: E501
        :rtype: str
        """
        return self._trace

    @trace.setter
    def trace(self, trace):
        """Sets the trace of this RESTApiJsonResponse.


        :param trace: The trace of this RESTApiJsonResponse.  # noqa: E501
        :type: str
        """

        self._trace = trace

    @property
    def field_errors(self):
        """Gets the field_errors of this RESTApiJsonResponse.  # noqa: E501


        :return: The field_errors of this RESTApiJsonResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._field_errors

    @field_errors.setter
    def field_errors(self, field_errors):
        """Sets the field_errors of this RESTApiJsonResponse.


        :param field_errors: The field_errors of this RESTApiJsonResponse.  # noqa: E501
        :type: list[str]
        """

        self._field_errors = field_errors

    @property
    def data(self):
        """Gets the data of this RESTApiJsonResponse.  # noqa: E501


        :return: The data of this RESTApiJsonResponse.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this RESTApiJsonResponse.


        :param data: The data of this RESTApiJsonResponse.  # noqa: E501
        :type: object
        """

        self._data = data

    @property
    def session_id(self):
        """Gets the session_id of this RESTApiJsonResponse.  # noqa: E501


        :return: The session_id of this RESTApiJsonResponse.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this RESTApiJsonResponse.


        :param session_id: The session_id of this RESTApiJsonResponse.  # noqa: E501
        :type: str
        """

        self._session_id = session_id

    @property
    def qrcode(self):
        """Gets the qrcode of this RESTApiJsonResponse.  # noqa: E501


        :return: The qrcode of this RESTApiJsonResponse.  # noqa: E501
        :rtype: str
        """
        return self._qrcode

    @qrcode.setter
    def qrcode(self, qrcode):
        """Sets the qrcode of this RESTApiJsonResponse.


        :param qrcode: The qrcode of this RESTApiJsonResponse.  # noqa: E501
        :type: str
        """

        self._qrcode = qrcode

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
        if issubclass(RESTApiJsonResponse, dict):
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
        if not isinstance(other, RESTApiJsonResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
