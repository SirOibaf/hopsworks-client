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


class InodeView(object):
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
        'name': 'str',
        'dir': 'bool',
        'parent': 'bool',
        'path': 'str',
        'size': 'int',
        'shared': 'bool',
        'owning_project_name': 'str',
        'modification': 'datetime',
        'access_time': 'datetime',
        'id': 'int',
        'parent_id': 'int',
        'template': 'int',
        'description': 'str',
        'status': 'bool',
        'under_construction': 'bool',
        'owner': 'str',
        'permission': 'str',
        'email': 'str',
        'public_ds': 'int',
        'shared_with': 'int',
        'searchable': 'bool',
        'zip_state': 'str',
        'public_id': 'str',
        'type': 'str',
        'public_dataset': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'dir': 'dir',
        'parent': 'parent',
        'path': 'path',
        'size': 'size',
        'shared': 'shared',
        'owning_project_name': 'owningProjectName',
        'modification': 'modification',
        'access_time': 'accessTime',
        'id': 'id',
        'parent_id': 'parentId',
        'template': 'template',
        'description': 'description',
        'status': 'status',
        'under_construction': 'underConstruction',
        'owner': 'owner',
        'permission': 'permission',
        'email': 'email',
        'public_ds': 'publicDs',
        'shared_with': 'sharedWith',
        'searchable': 'searchable',
        'zip_state': 'zipState',
        'public_id': 'publicId',
        'type': 'type',
        'public_dataset': 'publicDataset'
    }

    def __init__(self, name=None, dir=None, parent=None, path=None, size=None, shared=None, owning_project_name=None, modification=None, access_time=None, id=None, parent_id=None, template=None, description=None, status=None, under_construction=None, owner=None, permission=None, email=None, public_ds=None, shared_with=None, searchable=None, zip_state=None, public_id=None, type=None, public_dataset=None):  # noqa: E501
        """InodeView - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._dir = None
        self._parent = None
        self._path = None
        self._size = None
        self._shared = None
        self._owning_project_name = None
        self._modification = None
        self._access_time = None
        self._id = None
        self._parent_id = None
        self._template = None
        self._description = None
        self._status = None
        self._under_construction = None
        self._owner = None
        self._permission = None
        self._email = None
        self._public_ds = None
        self._shared_with = None
        self._searchable = None
        self._zip_state = None
        self._public_id = None
        self._type = None
        self._public_dataset = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if dir is not None:
            self.dir = dir
        if parent is not None:
            self.parent = parent
        if path is not None:
            self.path = path
        if size is not None:
            self.size = size
        if shared is not None:
            self.shared = shared
        if owning_project_name is not None:
            self.owning_project_name = owning_project_name
        if modification is not None:
            self.modification = modification
        if access_time is not None:
            self.access_time = access_time
        if id is not None:
            self.id = id
        if parent_id is not None:
            self.parent_id = parent_id
        if template is not None:
            self.template = template
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if under_construction is not None:
            self.under_construction = under_construction
        if owner is not None:
            self.owner = owner
        if permission is not None:
            self.permission = permission
        if email is not None:
            self.email = email
        if public_ds is not None:
            self.public_ds = public_ds
        if shared_with is not None:
            self.shared_with = shared_with
        if searchable is not None:
            self.searchable = searchable
        if zip_state is not None:
            self.zip_state = zip_state
        if public_id is not None:
            self.public_id = public_id
        if type is not None:
            self.type = type
        if public_dataset is not None:
            self.public_dataset = public_dataset

    @property
    def name(self):
        """Gets the name of this InodeView.  # noqa: E501


        :return: The name of this InodeView.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InodeView.


        :param name: The name of this InodeView.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def dir(self):
        """Gets the dir of this InodeView.  # noqa: E501


        :return: The dir of this InodeView.  # noqa: E501
        :rtype: bool
        """
        return self._dir

    @dir.setter
    def dir(self, dir):
        """Sets the dir of this InodeView.


        :param dir: The dir of this InodeView.  # noqa: E501
        :type: bool
        """

        self._dir = dir

    @property
    def parent(self):
        """Gets the parent of this InodeView.  # noqa: E501


        :return: The parent of this InodeView.  # noqa: E501
        :rtype: bool
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this InodeView.


        :param parent: The parent of this InodeView.  # noqa: E501
        :type: bool
        """

        self._parent = parent

    @property
    def path(self):
        """Gets the path of this InodeView.  # noqa: E501


        :return: The path of this InodeView.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this InodeView.


        :param path: The path of this InodeView.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def size(self):
        """Gets the size of this InodeView.  # noqa: E501


        :return: The size of this InodeView.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this InodeView.


        :param size: The size of this InodeView.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def shared(self):
        """Gets the shared of this InodeView.  # noqa: E501


        :return: The shared of this InodeView.  # noqa: E501
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this InodeView.


        :param shared: The shared of this InodeView.  # noqa: E501
        :type: bool
        """

        self._shared = shared

    @property
    def owning_project_name(self):
        """Gets the owning_project_name of this InodeView.  # noqa: E501


        :return: The owning_project_name of this InodeView.  # noqa: E501
        :rtype: str
        """
        return self._owning_project_name

    @owning_project_name.setter
    def owning_project_name(self, owning_project_name):
        """Sets the owning_project_name of this InodeView.


        :param owning_project_name: The owning_project_name of this InodeView.  # noqa: E501
        :type: str
        """

        self._owning_project_name = owning_project_name

    @property
    def modification(self):
        """Gets the modification of this InodeView.  # noqa: E501


        :return: The modification of this InodeView.  # noqa: E501
        :rtype: datetime
        """
        return self._modification

    @modification.setter
    def modification(self, modification):
        """Sets the modification of this InodeView.


        :param modification: The modification of this InodeView.  # noqa: E501
        :type: datetime
        """

        self._modification = modification

    @property
    def access_time(self):
        """Gets the access_time of this InodeView.  # noqa: E501


        :return: The access_time of this InodeView.  # noqa: E501
        :rtype: datetime
        """
        return self._access_time

    @access_time.setter
    def access_time(self, access_time):
        """Sets the access_time of this InodeView.


        :param access_time: The access_time of this InodeView.  # noqa: E501
        :type: datetime
        """

        self._access_time = access_time

    @property
    def id(self):
        """Gets the id of this InodeView.  # noqa: E501


        :return: The id of this InodeView.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InodeView.


        :param id: The id of this InodeView.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this InodeView.  # noqa: E501


        :return: The parent_id of this InodeView.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this InodeView.


        :param parent_id: The parent_id of this InodeView.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def template(self):
        """Gets the template of this InodeView.  # noqa: E501


        :return: The template of this InodeView.  # noqa: E501
        :rtype: int
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this InodeView.


        :param template: The template of this InodeView.  # noqa: E501
        :type: int
        """

        self._template = template

    @property
    def description(self):
        """Gets the description of this InodeView.  # noqa: E501


        :return: The description of this InodeView.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InodeView.


        :param description: The description of this InodeView.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this InodeView.  # noqa: E501


        :return: The status of this InodeView.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InodeView.


        :param status: The status of this InodeView.  # noqa: E501
        :type: bool
        """

        self._status = status

    @property
    def under_construction(self):
        """Gets the under_construction of this InodeView.  # noqa: E501


        :return: The under_construction of this InodeView.  # noqa: E501
        :rtype: bool
        """
        return self._under_construction

    @under_construction.setter
    def under_construction(self, under_construction):
        """Sets the under_construction of this InodeView.


        :param under_construction: The under_construction of this InodeView.  # noqa: E501
        :type: bool
        """

        self._under_construction = under_construction

    @property
    def owner(self):
        """Gets the owner of this InodeView.  # noqa: E501


        :return: The owner of this InodeView.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this InodeView.


        :param owner: The owner of this InodeView.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def permission(self):
        """Gets the permission of this InodeView.  # noqa: E501


        :return: The permission of this InodeView.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this InodeView.


        :param permission: The permission of this InodeView.  # noqa: E501
        :type: str
        """

        self._permission = permission

    @property
    def email(self):
        """Gets the email of this InodeView.  # noqa: E501


        :return: The email of this InodeView.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InodeView.


        :param email: The email of this InodeView.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def public_ds(self):
        """Gets the public_ds of this InodeView.  # noqa: E501


        :return: The public_ds of this InodeView.  # noqa: E501
        :rtype: int
        """
        return self._public_ds

    @public_ds.setter
    def public_ds(self, public_ds):
        """Sets the public_ds of this InodeView.


        :param public_ds: The public_ds of this InodeView.  # noqa: E501
        :type: int
        """

        self._public_ds = public_ds

    @property
    def shared_with(self):
        """Gets the shared_with of this InodeView.  # noqa: E501


        :return: The shared_with of this InodeView.  # noqa: E501
        :rtype: int
        """
        return self._shared_with

    @shared_with.setter
    def shared_with(self, shared_with):
        """Sets the shared_with of this InodeView.


        :param shared_with: The shared_with of this InodeView.  # noqa: E501
        :type: int
        """

        self._shared_with = shared_with

    @property
    def searchable(self):
        """Gets the searchable of this InodeView.  # noqa: E501


        :return: The searchable of this InodeView.  # noqa: E501
        :rtype: bool
        """
        return self._searchable

    @searchable.setter
    def searchable(self, searchable):
        """Sets the searchable of this InodeView.


        :param searchable: The searchable of this InodeView.  # noqa: E501
        :type: bool
        """

        self._searchable = searchable

    @property
    def zip_state(self):
        """Gets the zip_state of this InodeView.  # noqa: E501


        :return: The zip_state of this InodeView.  # noqa: E501
        :rtype: str
        """
        return self._zip_state

    @zip_state.setter
    def zip_state(self, zip_state):
        """Sets the zip_state of this InodeView.


        :param zip_state: The zip_state of this InodeView.  # noqa: E501
        :type: str
        """

        self._zip_state = zip_state

    @property
    def public_id(self):
        """Gets the public_id of this InodeView.  # noqa: E501


        :return: The public_id of this InodeView.  # noqa: E501
        :rtype: str
        """
        return self._public_id

    @public_id.setter
    def public_id(self, public_id):
        """Sets the public_id of this InodeView.


        :param public_id: The public_id of this InodeView.  # noqa: E501
        :type: str
        """

        self._public_id = public_id

    @property
    def type(self):
        """Gets the type of this InodeView.  # noqa: E501


        :return: The type of this InodeView.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InodeView.


        :param type: The type of this InodeView.  # noqa: E501
        :type: str
        """
        allowed_values = ["DATASET", "HIVEDB", "FEATURESTORE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def public_dataset(self):
        """Gets the public_dataset of this InodeView.  # noqa: E501


        :return: The public_dataset of this InodeView.  # noqa: E501
        :rtype: bool
        """
        return self._public_dataset

    @public_dataset.setter
    def public_dataset(self, public_dataset):
        """Sets the public_dataset of this InodeView.


        :param public_dataset: The public_dataset of this InodeView.  # noqa: E501
        :type: bool
        """

        self._public_dataset = public_dataset

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
        if issubclass(InodeView, dict):
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
        if not isinstance(other, InodeView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other