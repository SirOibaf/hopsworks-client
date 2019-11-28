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
from swagger_client.models.dataset_request import DatasetRequest  # noqa: F401,E501
from swagger_client.models.featurestore import Featurestore  # noqa: F401,E501
from swagger_client.models.inode import Inode  # noqa: F401,E501
from swagger_client.models.project import Project  # noqa: F401,E501


class Dataset(object):
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
        'inode': 'Inode',
        'name': 'str',
        'description': 'str',
        'project': 'Project',
        'editable': 'str',
        'searchable': 'bool',
        'status': 'bool',
        'public_ds': 'int',
        'public_ds_id': 'str',
        'shared': 'bool',
        'type': 'str',
        'featurestore': 'Featurestore',
        'dataset_request_collection': 'list[DatasetRequest]',
        'inode_id': 'int',
        'public_ds_state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'inode': 'inode',
        'name': 'name',
        'description': 'description',
        'project': 'project',
        'editable': 'editable',
        'searchable': 'searchable',
        'status': 'status',
        'public_ds': 'publicDs',
        'public_ds_id': 'publicDsId',
        'shared': 'shared',
        'type': 'type',
        'featurestore': 'featurestore',
        'dataset_request_collection': 'datasetRequestCollection',
        'inode_id': 'inodeId',
        'public_ds_state': 'publicDsState'
    }

    def __init__(self, id=None, inode=None, name=None, description=None, project=None, editable=None, searchable=None, status=None, public_ds=None, public_ds_id=None, shared=None, type=None, featurestore=None, dataset_request_collection=None, inode_id=None, public_ds_state=None):  # noqa: E501
        """Dataset - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._inode = None
        self._name = None
        self._description = None
        self._project = None
        self._editable = None
        self._searchable = None
        self._status = None
        self._public_ds = None
        self._public_ds_id = None
        self._shared = None
        self._type = None
        self._featurestore = None
        self._dataset_request_collection = None
        self._inode_id = None
        self._public_ds_state = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if inode is not None:
            self.inode = inode
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if project is not None:
            self.project = project
        self.editable = editable
        self.searchable = searchable
        self.status = status
        self.public_ds = public_ds
        if public_ds_id is not None:
            self.public_ds_id = public_ds_id
        self.shared = shared
        self.type = type
        if featurestore is not None:
            self.featurestore = featurestore
        if dataset_request_collection is not None:
            self.dataset_request_collection = dataset_request_collection
        if inode_id is not None:
            self.inode_id = inode_id
        if public_ds_state is not None:
            self.public_ds_state = public_ds_state

    @property
    def id(self):
        """Gets the id of this Dataset.  # noqa: E501


        :return: The id of this Dataset.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Dataset.


        :param id: The id of this Dataset.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def inode(self):
        """Gets the inode of this Dataset.  # noqa: E501


        :return: The inode of this Dataset.  # noqa: E501
        :rtype: Inode
        """
        return self._inode

    @inode.setter
    def inode(self, inode):
        """Sets the inode of this Dataset.


        :param inode: The inode of this Dataset.  # noqa: E501
        :type: Inode
        """

        self._inode = inode

    @property
    def name(self):
        """Gets the name of this Dataset.  # noqa: E501


        :return: The name of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Dataset.


        :param name: The name of this Dataset.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Dataset.  # noqa: E501


        :return: The description of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Dataset.


        :param description: The description of this Dataset.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def project(self):
        """Gets the project of this Dataset.  # noqa: E501


        :return: The project of this Dataset.  # noqa: E501
        :rtype: Project
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Dataset.


        :param project: The project of this Dataset.  # noqa: E501
        :type: Project
        """

        self._project = project

    @property
    def editable(self):
        """Gets the editable of this Dataset.  # noqa: E501


        :return: The editable of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this Dataset.


        :param editable: The editable of this Dataset.  # noqa: E501
        :type: str
        """
        if editable is None:
            raise ValueError("Invalid value for `editable`, must not be `None`")  # noqa: E501
        allowed_values = ["GROUP_WRITABLE_SB", "GROUP_WRITABLE", "OWNER_ONLY"]  # noqa: E501
        if editable not in allowed_values:
            raise ValueError(
                "Invalid value for `editable` ({0}), must be one of {1}"  # noqa: E501
                .format(editable, allowed_values)
            )

        self._editable = editable

    @property
    def searchable(self):
        """Gets the searchable of this Dataset.  # noqa: E501


        :return: The searchable of this Dataset.  # noqa: E501
        :rtype: bool
        """
        return self._searchable

    @searchable.setter
    def searchable(self, searchable):
        """Sets the searchable of this Dataset.


        :param searchable: The searchable of this Dataset.  # noqa: E501
        :type: bool
        """
        if searchable is None:
            raise ValueError("Invalid value for `searchable`, must not be `None`")  # noqa: E501

        self._searchable = searchable

    @property
    def status(self):
        """Gets the status of this Dataset.  # noqa: E501


        :return: The status of this Dataset.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Dataset.


        :param status: The status of this Dataset.  # noqa: E501
        :type: bool
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def public_ds(self):
        """Gets the public_ds of this Dataset.  # noqa: E501


        :return: The public_ds of this Dataset.  # noqa: E501
        :rtype: int
        """
        return self._public_ds

    @public_ds.setter
    def public_ds(self, public_ds):
        """Sets the public_ds of this Dataset.


        :param public_ds: The public_ds of this Dataset.  # noqa: E501
        :type: int
        """
        if public_ds is None:
            raise ValueError("Invalid value for `public_ds`, must not be `None`")  # noqa: E501

        self._public_ds = public_ds

    @property
    def public_ds_id(self):
        """Gets the public_ds_id of this Dataset.  # noqa: E501


        :return: The public_ds_id of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._public_ds_id

    @public_ds_id.setter
    def public_ds_id(self, public_ds_id):
        """Sets the public_ds_id of this Dataset.


        :param public_ds_id: The public_ds_id of this Dataset.  # noqa: E501
        :type: str
        """

        self._public_ds_id = public_ds_id

    @property
    def shared(self):
        """Gets the shared of this Dataset.  # noqa: E501


        :return: The shared of this Dataset.  # noqa: E501
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this Dataset.


        :param shared: The shared of this Dataset.  # noqa: E501
        :type: bool
        """
        if shared is None:
            raise ValueError("Invalid value for `shared`, must not be `None`")  # noqa: E501

        self._shared = shared

    @property
    def type(self):
        """Gets the type of this Dataset.  # noqa: E501


        :return: The type of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Dataset.


        :param type: The type of this Dataset.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["DATASET", "HIVEDB", "FEATURESTORE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def featurestore(self):
        """Gets the featurestore of this Dataset.  # noqa: E501


        :return: The featurestore of this Dataset.  # noqa: E501
        :rtype: Featurestore
        """
        return self._featurestore

    @featurestore.setter
    def featurestore(self, featurestore):
        """Sets the featurestore of this Dataset.


        :param featurestore: The featurestore of this Dataset.  # noqa: E501
        :type: Featurestore
        """

        self._featurestore = featurestore

    @property
    def dataset_request_collection(self):
        """Gets the dataset_request_collection of this Dataset.  # noqa: E501


        :return: The dataset_request_collection of this Dataset.  # noqa: E501
        :rtype: list[DatasetRequest]
        """
        return self._dataset_request_collection

    @dataset_request_collection.setter
    def dataset_request_collection(self, dataset_request_collection):
        """Sets the dataset_request_collection of this Dataset.


        :param dataset_request_collection: The dataset_request_collection of this Dataset.  # noqa: E501
        :type: list[DatasetRequest]
        """

        self._dataset_request_collection = dataset_request_collection

    @property
    def inode_id(self):
        """Gets the inode_id of this Dataset.  # noqa: E501


        :return: The inode_id of this Dataset.  # noqa: E501
        :rtype: int
        """
        return self._inode_id

    @inode_id.setter
    def inode_id(self, inode_id):
        """Sets the inode_id of this Dataset.


        :param inode_id: The inode_id of this Dataset.  # noqa: E501
        :type: int
        """

        self._inode_id = inode_id

    @property
    def public_ds_state(self):
        """Gets the public_ds_state of this Dataset.  # noqa: E501


        :return: The public_ds_state of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._public_ds_state

    @public_ds_state.setter
    def public_ds_state(self, public_ds_state):
        """Sets the public_ds_state of this Dataset.


        :param public_ds_state: The public_ds_state of this Dataset.  # noqa: E501
        :type: str
        """
        allowed_values = ["PRIVATE", "CLUSTER", "HOPS"]  # noqa: E501
        if public_ds_state not in allowed_values:
            raise ValueError(
                "Invalid value for `public_ds_state` ({0}), must be one of {1}"  # noqa: E501
                .format(public_ds_state, allowed_values)
            )

        self._public_ds_state = public_ds_state

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
        if issubclass(Dataset, dict):
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
        if not isinstance(other, Dataset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other