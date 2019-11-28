# coding: utf-8

"""
    Hopsworks api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.1.0-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TrainingDatasetServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_training_dataset(self, featurestore_id, project_id, **kwargs):  # noqa: E501
        """Create training dataset for a featurestore  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_training_dataset(featurestore_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int featurestore_id: (required)
        :param int project_id: (required)
        :param TrainingDatasetDTO body:
        :return: TrainingDatasetDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_training_dataset_with_http_info(featurestore_id, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_training_dataset_with_http_info(featurestore_id, project_id, **kwargs)  # noqa: E501
            return data

    def create_training_dataset_with_http_info(self, featurestore_id, project_id, **kwargs):  # noqa: E501
        """Create training dataset for a featurestore  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_training_dataset_with_http_info(featurestore_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int featurestore_id: (required)
        :param int project_id: (required)
        :param TrainingDatasetDTO body:
        :return: TrainingDatasetDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['featurestore_id', 'project_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_training_dataset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'featurestore_id' is set
        if ('featurestore_id' not in params or
                params['featurestore_id'] is None):
            raise ValueError("Missing the required parameter `featurestore_id` when calling `create_training_dataset`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `create_training_dataset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'featurestore_id' in params:
            path_params['featurestoreId'] = params['featurestore_id']  # noqa: E501
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/project/{projectId}/featurestores/{featurestoreId}/trainingdatasets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TrainingDatasetDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_training_dataset(self, trainingdatasetid, featurestore_id, project_id, **kwargs):  # noqa: E501
        """Delete a training datasets with a specific id from a featurestore  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_training_dataset(trainingdatasetid, featurestore_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int trainingdatasetid: Id of the training dataset (required)
        :param int featurestore_id: (required)
        :param int project_id: (required)
        :return: TrainingDatasetDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_training_dataset_with_http_info(trainingdatasetid, featurestore_id, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_training_dataset_with_http_info(trainingdatasetid, featurestore_id, project_id, **kwargs)  # noqa: E501
            return data

    def delete_training_dataset_with_http_info(self, trainingdatasetid, featurestore_id, project_id, **kwargs):  # noqa: E501
        """Delete a training datasets with a specific id from a featurestore  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_training_dataset_with_http_info(trainingdatasetid, featurestore_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int trainingdatasetid: Id of the training dataset (required)
        :param int featurestore_id: (required)
        :param int project_id: (required)
        :return: TrainingDatasetDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['trainingdatasetid', 'featurestore_id', 'project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_training_dataset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'trainingdatasetid' is set
        if ('trainingdatasetid' not in params or
                params['trainingdatasetid'] is None):
            raise ValueError("Missing the required parameter `trainingdatasetid` when calling `delete_training_dataset`")  # noqa: E501
        # verify the required parameter 'featurestore_id' is set
        if ('featurestore_id' not in params or
                params['featurestore_id'] is None):
            raise ValueError("Missing the required parameter `featurestore_id` when calling `delete_training_dataset`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `delete_training_dataset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'trainingdatasetid' in params:
            path_params['trainingdatasetid'] = params['trainingdatasetid']  # noqa: E501
        if 'featurestore_id' in params:
            path_params['featurestoreId'] = params['featurestore_id']  # noqa: E501
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TrainingDatasetDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_training_dataset_with_id(self, trainingdatasetid, featurestore_id, project_id, **kwargs):  # noqa: E501
        """Get a training datasets with a specific id from a featurestore  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_training_dataset_with_id(trainingdatasetid, featurestore_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int trainingdatasetid: Id of the training dataset (required)
        :param int featurestore_id: (required)
        :param int project_id: (required)
        :return: TrainingDatasetDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_training_dataset_with_id_with_http_info(trainingdatasetid, featurestore_id, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_training_dataset_with_id_with_http_info(trainingdatasetid, featurestore_id, project_id, **kwargs)  # noqa: E501
            return data

    def get_training_dataset_with_id_with_http_info(self, trainingdatasetid, featurestore_id, project_id, **kwargs):  # noqa: E501
        """Get a training datasets with a specific id from a featurestore  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_training_dataset_with_id_with_http_info(trainingdatasetid, featurestore_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int trainingdatasetid: Id of the training dataset (required)
        :param int featurestore_id: (required)
        :param int project_id: (required)
        :return: TrainingDatasetDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['trainingdatasetid', 'featurestore_id', 'project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_training_dataset_with_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'trainingdatasetid' is set
        if ('trainingdatasetid' not in params or
                params['trainingdatasetid'] is None):
            raise ValueError("Missing the required parameter `trainingdatasetid` when calling `get_training_dataset_with_id`")  # noqa: E501
        # verify the required parameter 'featurestore_id' is set
        if ('featurestore_id' not in params or
                params['featurestore_id'] is None):
            raise ValueError("Missing the required parameter `featurestore_id` when calling `get_training_dataset_with_id`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `get_training_dataset_with_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'trainingdatasetid' in params:
            path_params['trainingdatasetid'] = params['trainingdatasetid']  # noqa: E501
        if 'featurestore_id' in params:
            path_params['featurestoreId'] = params['featurestore_id']  # noqa: E501
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TrainingDatasetDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_training_datasets_for_featurestore(self, featurestore_id, project_id, **kwargs):  # noqa: E501
        """Get the list of training datasets for a featurestore  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_training_datasets_for_featurestore(featurestore_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int featurestore_id: (required)
        :param int project_id: (required)
        :return: list[TrainingDatasetDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_training_datasets_for_featurestore_with_http_info(featurestore_id, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_training_datasets_for_featurestore_with_http_info(featurestore_id, project_id, **kwargs)  # noqa: E501
            return data

    def get_training_datasets_for_featurestore_with_http_info(self, featurestore_id, project_id, **kwargs):  # noqa: E501
        """Get the list of training datasets for a featurestore  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_training_datasets_for_featurestore_with_http_info(featurestore_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int featurestore_id: (required)
        :param int project_id: (required)
        :return: list[TrainingDatasetDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['featurestore_id', 'project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_training_datasets_for_featurestore" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'featurestore_id' is set
        if ('featurestore_id' not in params or
                params['featurestore_id'] is None):
            raise ValueError("Missing the required parameter `featurestore_id` when calling `get_training_datasets_for_featurestore`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `get_training_datasets_for_featurestore`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'featurestore_id' in params:
            path_params['featurestoreId'] = params['featurestore_id']  # noqa: E501
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/project/{projectId}/featurestores/{featurestoreId}/trainingdatasets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TrainingDatasetDTO]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_training_dataset(self, trainingdatasetid, featurestore_id, project_id, **kwargs):  # noqa: E501
        """Update a training datasets with a specific id from a featurestore  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_training_dataset(trainingdatasetid, featurestore_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int trainingdatasetid: Id of the training dataset (required)
        :param int featurestore_id: (required)
        :param int project_id: (required)
        :param TrainingDatasetDTO body:
        :param bool update_metadata: updateMetadata
        :param bool update_stats: updateStats
        :return: TrainingDatasetDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_training_dataset_with_http_info(trainingdatasetid, featurestore_id, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_training_dataset_with_http_info(trainingdatasetid, featurestore_id, project_id, **kwargs)  # noqa: E501
            return data

    def update_training_dataset_with_http_info(self, trainingdatasetid, featurestore_id, project_id, **kwargs):  # noqa: E501
        """Update a training datasets with a specific id from a featurestore  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_training_dataset_with_http_info(trainingdatasetid, featurestore_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int trainingdatasetid: Id of the training dataset (required)
        :param int featurestore_id: (required)
        :param int project_id: (required)
        :param TrainingDatasetDTO body:
        :param bool update_metadata: updateMetadata
        :param bool update_stats: updateStats
        :return: TrainingDatasetDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['trainingdatasetid', 'featurestore_id', 'project_id', 'body', 'update_metadata', 'update_stats']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_training_dataset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'trainingdatasetid' is set
        if ('trainingdatasetid' not in params or
                params['trainingdatasetid'] is None):
            raise ValueError("Missing the required parameter `trainingdatasetid` when calling `update_training_dataset`")  # noqa: E501
        # verify the required parameter 'featurestore_id' is set
        if ('featurestore_id' not in params or
                params['featurestore_id'] is None):
            raise ValueError("Missing the required parameter `featurestore_id` when calling `update_training_dataset`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `update_training_dataset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'trainingdatasetid' in params:
            path_params['trainingdatasetid'] = params['trainingdatasetid']  # noqa: E501
        if 'featurestore_id' in params:
            path_params['featurestoreId'] = params['featurestore_id']  # noqa: E501
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []
        if 'update_metadata' in params:
            query_params.append(('updateMetadata', params['update_metadata']))  # noqa: E501
        if 'update_stats' in params:
            query_params.append(('updateStats', params['update_stats']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TrainingDatasetDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)