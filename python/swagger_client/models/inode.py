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
from swagger_client.models.hdfs_groups import HdfsGroups  # noqa: F401,E501
from swagger_client.models.hdfs_users import HdfsUsers  # noqa: F401,E501
from swagger_client.models.inode_pk import InodePK  # noqa: F401,E501
from swagger_client.models.template import Template  # noqa: F401,E501


class Inode(object):
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
        'inode_pk': 'InodePK',
        'id': 'int',
        'modification_time': 'int',
        'access_time': 'int',
        'hdfs_user': 'HdfsUsers',
        'hdfs_group': 'HdfsGroups',
        'permission': 'int',
        'client_name': 'str',
        'client_machine': 'str',
        'generation_stamp': 'int',
        'header': 'int',
        'symlink': 'str',
        'quota_enabled': 'bool',
        'under_construction': 'bool',
        'subtree_locked': 'bool',
        'meta_enabled': 'bool',
        'dir': 'bool',
        'subtree_lock_owner': 'int',
        'size': 'int',
        'templates': 'list[Template]',
        'template': 'int'
    }

    attribute_map = {
        'inode_pk': 'inodePK',
        'id': 'id',
        'modification_time': 'modificationTime',
        'access_time': 'accessTime',
        'hdfs_user': 'hdfsUser',
        'hdfs_group': 'hdfsGroup',
        'permission': 'permission',
        'client_name': 'clientName',
        'client_machine': 'clientMachine',
        'generation_stamp': 'generationStamp',
        'header': 'header',
        'symlink': 'symlink',
        'quota_enabled': 'quotaEnabled',
        'under_construction': 'underConstruction',
        'subtree_locked': 'subtreeLocked',
        'meta_enabled': 'metaEnabled',
        'dir': 'dir',
        'subtree_lock_owner': 'subtreeLockOwner',
        'size': 'size',
        'templates': 'templates',
        'template': 'template'
    }

    def __init__(self, inode_pk=None, id=None, modification_time=None, access_time=None, hdfs_user=None, hdfs_group=None, permission=None, client_name=None, client_machine=None, generation_stamp=None, header=None, symlink=None, quota_enabled=None, under_construction=None, subtree_locked=None, meta_enabled=None, dir=None, subtree_lock_owner=None, size=None, templates=None, template=None):  # noqa: E501
        """Inode - a model defined in Swagger"""  # noqa: E501
        self._inode_pk = None
        self._id = None
        self._modification_time = None
        self._access_time = None
        self._hdfs_user = None
        self._hdfs_group = None
        self._permission = None
        self._client_name = None
        self._client_machine = None
        self._generation_stamp = None
        self._header = None
        self._symlink = None
        self._quota_enabled = None
        self._under_construction = None
        self._subtree_locked = None
        self._meta_enabled = None
        self._dir = None
        self._subtree_lock_owner = None
        self._size = None
        self._templates = None
        self._template = None
        self.discriminator = None
        if inode_pk is not None:
            self.inode_pk = inode_pk
        self.id = id
        if modification_time is not None:
            self.modification_time = modification_time
        if access_time is not None:
            self.access_time = access_time
        if hdfs_user is not None:
            self.hdfs_user = hdfs_user
        if hdfs_group is not None:
            self.hdfs_group = hdfs_group
        if permission is not None:
            self.permission = permission
        if client_name is not None:
            self.client_name = client_name
        if client_machine is not None:
            self.client_machine = client_machine
        if generation_stamp is not None:
            self.generation_stamp = generation_stamp
        if header is not None:
            self.header = header
        if symlink is not None:
            self.symlink = symlink
        self.quota_enabled = quota_enabled
        self.under_construction = under_construction
        if subtree_locked is not None:
            self.subtree_locked = subtree_locked
        self.meta_enabled = meta_enabled
        self.dir = dir
        if subtree_lock_owner is not None:
            self.subtree_lock_owner = subtree_lock_owner
        self.size = size
        if templates is not None:
            self.templates = templates
        if template is not None:
            self.template = template

    @property
    def inode_pk(self):
        """Gets the inode_pk of this Inode.  # noqa: E501


        :return: The inode_pk of this Inode.  # noqa: E501
        :rtype: InodePK
        """
        return self._inode_pk

    @inode_pk.setter
    def inode_pk(self, inode_pk):
        """Sets the inode_pk of this Inode.


        :param inode_pk: The inode_pk of this Inode.  # noqa: E501
        :type: InodePK
        """

        self._inode_pk = inode_pk

    @property
    def id(self):
        """Gets the id of this Inode.  # noqa: E501


        :return: The id of this Inode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Inode.


        :param id: The id of this Inode.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def modification_time(self):
        """Gets the modification_time of this Inode.  # noqa: E501


        :return: The modification_time of this Inode.  # noqa: E501
        :rtype: int
        """
        return self._modification_time

    @modification_time.setter
    def modification_time(self, modification_time):
        """Sets the modification_time of this Inode.


        :param modification_time: The modification_time of this Inode.  # noqa: E501
        :type: int
        """

        self._modification_time = modification_time

    @property
    def access_time(self):
        """Gets the access_time of this Inode.  # noqa: E501


        :return: The access_time of this Inode.  # noqa: E501
        :rtype: int
        """
        return self._access_time

    @access_time.setter
    def access_time(self, access_time):
        """Sets the access_time of this Inode.


        :param access_time: The access_time of this Inode.  # noqa: E501
        :type: int
        """

        self._access_time = access_time

    @property
    def hdfs_user(self):
        """Gets the hdfs_user of this Inode.  # noqa: E501


        :return: The hdfs_user of this Inode.  # noqa: E501
        :rtype: HdfsUsers
        """
        return self._hdfs_user

    @hdfs_user.setter
    def hdfs_user(self, hdfs_user):
        """Sets the hdfs_user of this Inode.


        :param hdfs_user: The hdfs_user of this Inode.  # noqa: E501
        :type: HdfsUsers
        """

        self._hdfs_user = hdfs_user

    @property
    def hdfs_group(self):
        """Gets the hdfs_group of this Inode.  # noqa: E501


        :return: The hdfs_group of this Inode.  # noqa: E501
        :rtype: HdfsGroups
        """
        return self._hdfs_group

    @hdfs_group.setter
    def hdfs_group(self, hdfs_group):
        """Sets the hdfs_group of this Inode.


        :param hdfs_group: The hdfs_group of this Inode.  # noqa: E501
        :type: HdfsGroups
        """

        self._hdfs_group = hdfs_group

    @property
    def permission(self):
        """Gets the permission of this Inode.  # noqa: E501


        :return: The permission of this Inode.  # noqa: E501
        :rtype: int
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this Inode.


        :param permission: The permission of this Inode.  # noqa: E501
        :type: int
        """

        self._permission = permission

    @property
    def client_name(self):
        """Gets the client_name of this Inode.  # noqa: E501


        :return: The client_name of this Inode.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this Inode.


        :param client_name: The client_name of this Inode.  # noqa: E501
        :type: str
        """

        self._client_name = client_name

    @property
    def client_machine(self):
        """Gets the client_machine of this Inode.  # noqa: E501


        :return: The client_machine of this Inode.  # noqa: E501
        :rtype: str
        """
        return self._client_machine

    @client_machine.setter
    def client_machine(self, client_machine):
        """Sets the client_machine of this Inode.


        :param client_machine: The client_machine of this Inode.  # noqa: E501
        :type: str
        """

        self._client_machine = client_machine

    @property
    def generation_stamp(self):
        """Gets the generation_stamp of this Inode.  # noqa: E501


        :return: The generation_stamp of this Inode.  # noqa: E501
        :rtype: int
        """
        return self._generation_stamp

    @generation_stamp.setter
    def generation_stamp(self, generation_stamp):
        """Sets the generation_stamp of this Inode.


        :param generation_stamp: The generation_stamp of this Inode.  # noqa: E501
        :type: int
        """

        self._generation_stamp = generation_stamp

    @property
    def header(self):
        """Gets the header of this Inode.  # noqa: E501


        :return: The header of this Inode.  # noqa: E501
        :rtype: int
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this Inode.


        :param header: The header of this Inode.  # noqa: E501
        :type: int
        """

        self._header = header

    @property
    def symlink(self):
        """Gets the symlink of this Inode.  # noqa: E501


        :return: The symlink of this Inode.  # noqa: E501
        :rtype: str
        """
        return self._symlink

    @symlink.setter
    def symlink(self, symlink):
        """Sets the symlink of this Inode.


        :param symlink: The symlink of this Inode.  # noqa: E501
        :type: str
        """

        self._symlink = symlink

    @property
    def quota_enabled(self):
        """Gets the quota_enabled of this Inode.  # noqa: E501


        :return: The quota_enabled of this Inode.  # noqa: E501
        :rtype: bool
        """
        return self._quota_enabled

    @quota_enabled.setter
    def quota_enabled(self, quota_enabled):
        """Sets the quota_enabled of this Inode.


        :param quota_enabled: The quota_enabled of this Inode.  # noqa: E501
        :type: bool
        """
        if quota_enabled is None:
            raise ValueError("Invalid value for `quota_enabled`, must not be `None`")  # noqa: E501

        self._quota_enabled = quota_enabled

    @property
    def under_construction(self):
        """Gets the under_construction of this Inode.  # noqa: E501


        :return: The under_construction of this Inode.  # noqa: E501
        :rtype: bool
        """
        return self._under_construction

    @under_construction.setter
    def under_construction(self, under_construction):
        """Sets the under_construction of this Inode.


        :param under_construction: The under_construction of this Inode.  # noqa: E501
        :type: bool
        """
        if under_construction is None:
            raise ValueError("Invalid value for `under_construction`, must not be `None`")  # noqa: E501

        self._under_construction = under_construction

    @property
    def subtree_locked(self):
        """Gets the subtree_locked of this Inode.  # noqa: E501


        :return: The subtree_locked of this Inode.  # noqa: E501
        :rtype: bool
        """
        return self._subtree_locked

    @subtree_locked.setter
    def subtree_locked(self, subtree_locked):
        """Sets the subtree_locked of this Inode.


        :param subtree_locked: The subtree_locked of this Inode.  # noqa: E501
        :type: bool
        """

        self._subtree_locked = subtree_locked

    @property
    def meta_enabled(self):
        """Gets the meta_enabled of this Inode.  # noqa: E501


        :return: The meta_enabled of this Inode.  # noqa: E501
        :rtype: bool
        """
        return self._meta_enabled

    @meta_enabled.setter
    def meta_enabled(self, meta_enabled):
        """Sets the meta_enabled of this Inode.


        :param meta_enabled: The meta_enabled of this Inode.  # noqa: E501
        :type: bool
        """
        if meta_enabled is None:
            raise ValueError("Invalid value for `meta_enabled`, must not be `None`")  # noqa: E501

        self._meta_enabled = meta_enabled

    @property
    def dir(self):
        """Gets the dir of this Inode.  # noqa: E501


        :return: The dir of this Inode.  # noqa: E501
        :rtype: bool
        """
        return self._dir

    @dir.setter
    def dir(self, dir):
        """Sets the dir of this Inode.


        :param dir: The dir of this Inode.  # noqa: E501
        :type: bool
        """
        if dir is None:
            raise ValueError("Invalid value for `dir`, must not be `None`")  # noqa: E501

        self._dir = dir

    @property
    def subtree_lock_owner(self):
        """Gets the subtree_lock_owner of this Inode.  # noqa: E501


        :return: The subtree_lock_owner of this Inode.  # noqa: E501
        :rtype: int
        """
        return self._subtree_lock_owner

    @subtree_lock_owner.setter
    def subtree_lock_owner(self, subtree_lock_owner):
        """Sets the subtree_lock_owner of this Inode.


        :param subtree_lock_owner: The subtree_lock_owner of this Inode.  # noqa: E501
        :type: int
        """

        self._subtree_lock_owner = subtree_lock_owner

    @property
    def size(self):
        """Gets the size of this Inode.  # noqa: E501


        :return: The size of this Inode.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Inode.


        :param size: The size of this Inode.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def templates(self):
        """Gets the templates of this Inode.  # noqa: E501


        :return: The templates of this Inode.  # noqa: E501
        :rtype: list[Template]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this Inode.


        :param templates: The templates of this Inode.  # noqa: E501
        :type: list[Template]
        """

        self._templates = templates

    @property
    def template(self):
        """Gets the template of this Inode.  # noqa: E501


        :return: The template of this Inode.  # noqa: E501
        :rtype: int
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this Inode.


        :param template: The template of this Inode.  # noqa: E501
        :type: int
        """

        self._template = template

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
        if issubclass(Inode, dict):
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
        if not isinstance(other, Inode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other