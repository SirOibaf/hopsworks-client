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
from swagger_client.models.message import Message  # noqa: F401,E501
from swagger_client.models.users import Users  # noqa: F401,E501


class Message(object):
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
        'date_sent': 'datetime',
        'subject': 'str',
        'preview': 'str',
        'content': 'str',
        'unread': 'bool',
        'deleted': 'bool',
        'path': 'str',
        'users_collection': 'list[Users]',
        '_from': 'Users',
        'to': 'Users',
        'reply_to_msg': 'Message'
    }

    attribute_map = {
        'id': 'id',
        'date_sent': 'dateSent',
        'subject': 'subject',
        'preview': 'preview',
        'content': 'content',
        'unread': 'unread',
        'deleted': 'deleted',
        'path': 'path',
        'users_collection': 'usersCollection',
        '_from': 'from',
        'to': 'to',
        'reply_to_msg': 'replyToMsg'
    }

    def __init__(self, id=None, date_sent=None, subject=None, preview=None, content=None, unread=None, deleted=None, path=None, users_collection=None, _from=None, to=None, reply_to_msg=None):  # noqa: E501
        """Message - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._date_sent = None
        self._subject = None
        self._preview = None
        self._content = None
        self._unread = None
        self._deleted = None
        self._path = None
        self._users_collection = None
        self.__from = None
        self._to = None
        self._reply_to_msg = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.date_sent = date_sent
        if subject is not None:
            self.subject = subject
        if preview is not None:
            self.preview = preview
        self.content = content
        self.unread = unread
        self.deleted = deleted
        if path is not None:
            self.path = path
        if users_collection is not None:
            self.users_collection = users_collection
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if reply_to_msg is not None:
            self.reply_to_msg = reply_to_msg

    @property
    def id(self):
        """Gets the id of this Message.  # noqa: E501


        :return: The id of this Message.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Message.


        :param id: The id of this Message.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def date_sent(self):
        """Gets the date_sent of this Message.  # noqa: E501


        :return: The date_sent of this Message.  # noqa: E501
        :rtype: datetime
        """
        return self._date_sent

    @date_sent.setter
    def date_sent(self, date_sent):
        """Sets the date_sent of this Message.


        :param date_sent: The date_sent of this Message.  # noqa: E501
        :type: datetime
        """
        if date_sent is None:
            raise ValueError("Invalid value for `date_sent`, must not be `None`")  # noqa: E501

        self._date_sent = date_sent

    @property
    def subject(self):
        """Gets the subject of this Message.  # noqa: E501


        :return: The subject of this Message.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Message.


        :param subject: The subject of this Message.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def preview(self):
        """Gets the preview of this Message.  # noqa: E501


        :return: The preview of this Message.  # noqa: E501
        :rtype: str
        """
        return self._preview

    @preview.setter
    def preview(self, preview):
        """Sets the preview of this Message.


        :param preview: The preview of this Message.  # noqa: E501
        :type: str
        """

        self._preview = preview

    @property
    def content(self):
        """Gets the content of this Message.  # noqa: E501


        :return: The content of this Message.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Message.


        :param content: The content of this Message.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def unread(self):
        """Gets the unread of this Message.  # noqa: E501


        :return: The unread of this Message.  # noqa: E501
        :rtype: bool
        """
        return self._unread

    @unread.setter
    def unread(self, unread):
        """Sets the unread of this Message.


        :param unread: The unread of this Message.  # noqa: E501
        :type: bool
        """
        if unread is None:
            raise ValueError("Invalid value for `unread`, must not be `None`")  # noqa: E501

        self._unread = unread

    @property
    def deleted(self):
        """Gets the deleted of this Message.  # noqa: E501


        :return: The deleted of this Message.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Message.


        :param deleted: The deleted of this Message.  # noqa: E501
        :type: bool
        """
        if deleted is None:
            raise ValueError("Invalid value for `deleted`, must not be `None`")  # noqa: E501

        self._deleted = deleted

    @property
    def path(self):
        """Gets the path of this Message.  # noqa: E501


        :return: The path of this Message.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Message.


        :param path: The path of this Message.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def users_collection(self):
        """Gets the users_collection of this Message.  # noqa: E501


        :return: The users_collection of this Message.  # noqa: E501
        :rtype: list[Users]
        """
        return self._users_collection

    @users_collection.setter
    def users_collection(self, users_collection):
        """Sets the users_collection of this Message.


        :param users_collection: The users_collection of this Message.  # noqa: E501
        :type: list[Users]
        """

        self._users_collection = users_collection

    @property
    def _from(self):
        """Gets the _from of this Message.  # noqa: E501


        :return: The _from of this Message.  # noqa: E501
        :rtype: Users
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this Message.


        :param _from: The _from of this Message.  # noqa: E501
        :type: Users
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this Message.  # noqa: E501


        :return: The to of this Message.  # noqa: E501
        :rtype: Users
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Message.


        :param to: The to of this Message.  # noqa: E501
        :type: Users
        """

        self._to = to

    @property
    def reply_to_msg(self):
        """Gets the reply_to_msg of this Message.  # noqa: E501


        :return: The reply_to_msg of this Message.  # noqa: E501
        :rtype: Message
        """
        return self._reply_to_msg

    @reply_to_msg.setter
    def reply_to_msg(self, reply_to_msg):
        """Sets the reply_to_msg of this Message.


        :param reply_to_msg: The reply_to_msg of this Message.  # noqa: E501
        :type: Message
        """

        self._reply_to_msg = reply_to_msg

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
        if issubclass(Message, dict):
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
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
