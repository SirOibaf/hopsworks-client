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
from swagger_client.models.entity_tag import EntityTag  # noqa: F401,E501
from swagger_client.models.link import Link  # noqa: F401,E501
from swagger_client.models.locale import Locale  # noqa: F401,E501
from swagger_client.models.media_type import MediaType  # noqa: F401,E501
from swagger_client.models.new_cookie import NewCookie  # noqa: F401,E501
from swagger_client.models.status_type import StatusType  # noqa: F401,E501


class Response(object):
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
        'status_info': 'StatusType',
        'media_type': 'MediaType',
        'allowed_methods': 'list[str]',
        'entity_tag': 'EntityTag',
        'links': 'list[Link]',
        'string_headers': 'dict(str, list[str])',
        'cookies': 'dict(str, NewCookie)',
        'metadata': 'dict(str, list[object])',
        'entity': 'object',
        '_date': 'datetime',
        'headers': 'dict(str, list[object])',
        'last_modified': 'datetime',
        'status': 'int',
        'length': 'int',
        'language': 'Locale',
        'location': 'str'
    }

    attribute_map = {
        'status_info': 'statusInfo',
        'media_type': 'mediaType',
        'allowed_methods': 'allowedMethods',
        'entity_tag': 'entityTag',
        'links': 'links',
        'string_headers': 'stringHeaders',
        'cookies': 'cookies',
        'metadata': 'metadata',
        'entity': 'entity',
        '_date': 'date',
        'headers': 'headers',
        'last_modified': 'lastModified',
        'status': 'status',
        'length': 'length',
        'language': 'language',
        'location': 'location'
    }

    def __init__(self, status_info=None, media_type=None, allowed_methods=None, entity_tag=None, links=None, string_headers=None, cookies=None, metadata=None, entity=None, _date=None, headers=None, last_modified=None, status=None, length=None, language=None, location=None):  # noqa: E501
        """Response - a model defined in Swagger"""  # noqa: E501
        self._status_info = None
        self._media_type = None
        self._allowed_methods = None
        self._entity_tag = None
        self._links = None
        self._string_headers = None
        self._cookies = None
        self._metadata = None
        self._entity = None
        self.__date = None
        self._headers = None
        self._last_modified = None
        self._status = None
        self._length = None
        self._language = None
        self._location = None
        self.discriminator = None
        if status_info is not None:
            self.status_info = status_info
        if media_type is not None:
            self.media_type = media_type
        if allowed_methods is not None:
            self.allowed_methods = allowed_methods
        if entity_tag is not None:
            self.entity_tag = entity_tag
        if links is not None:
            self.links = links
        if string_headers is not None:
            self.string_headers = string_headers
        if cookies is not None:
            self.cookies = cookies
        if metadata is not None:
            self.metadata = metadata
        if entity is not None:
            self.entity = entity
        if _date is not None:
            self._date = _date
        if headers is not None:
            self.headers = headers
        if last_modified is not None:
            self.last_modified = last_modified
        if status is not None:
            self.status = status
        if length is not None:
            self.length = length
        if language is not None:
            self.language = language
        if location is not None:
            self.location = location

    @property
    def status_info(self):
        """Gets the status_info of this Response.  # noqa: E501


        :return: The status_info of this Response.  # noqa: E501
        :rtype: StatusType
        """
        return self._status_info

    @status_info.setter
    def status_info(self, status_info):
        """Sets the status_info of this Response.


        :param status_info: The status_info of this Response.  # noqa: E501
        :type: StatusType
        """

        self._status_info = status_info

    @property
    def media_type(self):
        """Gets the media_type of this Response.  # noqa: E501


        :return: The media_type of this Response.  # noqa: E501
        :rtype: MediaType
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this Response.


        :param media_type: The media_type of this Response.  # noqa: E501
        :type: MediaType
        """

        self._media_type = media_type

    @property
    def allowed_methods(self):
        """Gets the allowed_methods of this Response.  # noqa: E501


        :return: The allowed_methods of this Response.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_methods

    @allowed_methods.setter
    def allowed_methods(self, allowed_methods):
        """Sets the allowed_methods of this Response.


        :param allowed_methods: The allowed_methods of this Response.  # noqa: E501
        :type: list[str]
        """

        self._allowed_methods = allowed_methods

    @property
    def entity_tag(self):
        """Gets the entity_tag of this Response.  # noqa: E501


        :return: The entity_tag of this Response.  # noqa: E501
        :rtype: EntityTag
        """
        return self._entity_tag

    @entity_tag.setter
    def entity_tag(self, entity_tag):
        """Sets the entity_tag of this Response.


        :param entity_tag: The entity_tag of this Response.  # noqa: E501
        :type: EntityTag
        """

        self._entity_tag = entity_tag

    @property
    def links(self):
        """Gets the links of this Response.  # noqa: E501


        :return: The links of this Response.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Response.


        :param links: The links of this Response.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def string_headers(self):
        """Gets the string_headers of this Response.  # noqa: E501


        :return: The string_headers of this Response.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._string_headers

    @string_headers.setter
    def string_headers(self, string_headers):
        """Sets the string_headers of this Response.


        :param string_headers: The string_headers of this Response.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._string_headers = string_headers

    @property
    def cookies(self):
        """Gets the cookies of this Response.  # noqa: E501


        :return: The cookies of this Response.  # noqa: E501
        :rtype: dict(str, NewCookie)
        """
        return self._cookies

    @cookies.setter
    def cookies(self, cookies):
        """Sets the cookies of this Response.


        :param cookies: The cookies of this Response.  # noqa: E501
        :type: dict(str, NewCookie)
        """

        self._cookies = cookies

    @property
    def metadata(self):
        """Gets the metadata of this Response.  # noqa: E501


        :return: The metadata of this Response.  # noqa: E501
        :rtype: dict(str, list[object])
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Response.


        :param metadata: The metadata of this Response.  # noqa: E501
        :type: dict(str, list[object])
        """

        self._metadata = metadata

    @property
    def entity(self):
        """Gets the entity of this Response.  # noqa: E501


        :return: The entity of this Response.  # noqa: E501
        :rtype: object
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this Response.


        :param entity: The entity of this Response.  # noqa: E501
        :type: object
        """

        self._entity = entity

    @property
    def _date(self):
        """Gets the _date of this Response.  # noqa: E501


        :return: The _date of this Response.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this Response.


        :param _date: The _date of this Response.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def headers(self):
        """Gets the headers of this Response.  # noqa: E501


        :return: The headers of this Response.  # noqa: E501
        :rtype: dict(str, list[object])
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this Response.


        :param headers: The headers of this Response.  # noqa: E501
        :type: dict(str, list[object])
        """

        self._headers = headers

    @property
    def last_modified(self):
        """Gets the last_modified of this Response.  # noqa: E501


        :return: The last_modified of this Response.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this Response.


        :param last_modified: The last_modified of this Response.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def status(self):
        """Gets the status of this Response.  # noqa: E501


        :return: The status of this Response.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Response.


        :param status: The status of this Response.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def length(self):
        """Gets the length of this Response.  # noqa: E501


        :return: The length of this Response.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Response.


        :param length: The length of this Response.  # noqa: E501
        :type: int
        """

        self._length = length

    @property
    def language(self):
        """Gets the language of this Response.  # noqa: E501


        :return: The language of this Response.  # noqa: E501
        :rtype: Locale
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Response.


        :param language: The language of this Response.  # noqa: E501
        :type: Locale
        """

        self._language = language

    @property
    def location(self):
        """Gets the location of this Response.  # noqa: E501


        :return: The location of this Response.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Response.


        :param location: The location of this Response.  # noqa: E501
        :type: str
        """

        self._location = location

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
        if issubclass(Response, dict):
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
        if not isinstance(other, Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other