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


class ProjectActivitiesResourceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def find_all_by_id(self, activity_id, project_id, **kwargs):  # noqa: E501
        """Finds an activity in project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_all_by_id(activity_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int activity_id: (required)
        :param int project_id: (required)
        :param list[str] expand: ex. expand=creator
        :return: ActivitiesDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.find_all_by_id_with_http_info(activity_id, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.find_all_by_id_with_http_info(activity_id, project_id, **kwargs)  # noqa: E501
            return data

    def find_all_by_id_with_http_info(self, activity_id, project_id, **kwargs):  # noqa: E501
        """Finds an activity in project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_all_by_id_with_http_info(activity_id, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int activity_id: (required)
        :param int project_id: (required)
        :param list[str] expand: ex. expand=creator
        :return: ActivitiesDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['activity_id', 'project_id', 'expand']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_all_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'activity_id' is set
        if ('activity_id' not in params or
                params['activity_id'] is None):
            raise ValueError("Missing the required parameter `activity_id` when calling `find_all_by_id`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `find_all_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'activity_id' in params:
            path_params['activityId'] = params['activity_id']  # noqa: E501
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []
        if 'expand' in params:
            query_params.append(('expand', params['expand']))  # noqa: E501
            collection_formats['expand'] = 'multi'  # noqa: E501

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
            '/project/{projectId}/activities/{activityId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActivitiesDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_all_by_project(self, project_id, **kwargs):  # noqa: E501
        """Finds activities in project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_all_by_project(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: (required)
        :param int offset:
        :param int limit:
        :param str sort_by: ex. sort_by=ID:asc,date_created:desc
        :param list[str] filter_by: ex. filter_by=flag:dataset
        :param list[str] expand: ex. expand=creator
        :return: ActivitiesDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.find_all_by_project_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.find_all_by_project_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def find_all_by_project_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """Finds activities in project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_all_by_project_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: (required)
        :param int offset:
        :param int limit:
        :param str sort_by: ex. sort_by=ID:asc,date_created:desc
        :param list[str] filter_by: ex. filter_by=flag:dataset
        :param list[str] expand: ex. expand=creator
        :return: ActivitiesDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'offset', 'limit', 'sort_by', 'filter_by', 'expand']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_all_by_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `find_all_by_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
        if 'filter_by' in params:
            query_params.append(('filter_by', params['filter_by']))  # noqa: E501
            collection_formats['filter_by'] = 'multi'  # noqa: E501
        if 'expand' in params:
            query_params.append(('expand', params['expand']))  # noqa: E501
            collection_formats['expand'] = 'multi'  # noqa: E501

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
            '/project/{projectId}/activities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActivitiesDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
