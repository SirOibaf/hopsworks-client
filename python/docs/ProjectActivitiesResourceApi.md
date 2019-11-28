# swagger_client.ProjectActivitiesResourceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_all_by_id**](ProjectActivitiesResourceApi.md#find_all_by_id) | **GET** /project/{projectId}/activities/{activityId} | Finds an activity in project.
[**find_all_by_project**](ProjectActivitiesResourceApi.md#find_all_by_project) | **GET** /project/{projectId}/activities | Finds activities in project.

# **find_all_by_id**
> ActivitiesDTO find_all_by_id(activity_id, project_id, expand=expand)

Finds an activity in project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectActivitiesResourceApi()
activity_id = 56 # int | 
project_id = 56 # int | 
expand = ['expand_example'] # list[str] | ex. expand=creator (optional)

try:
    # Finds an activity in project.
    api_response = api_instance.find_all_by_id(activity_id, project_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectActivitiesResourceApi->find_all_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**|  | 
 **project_id** | **int**|  | 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;creator | [optional] 

### Return type

[**ActivitiesDTO**](ActivitiesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_by_project**
> ActivitiesDTO find_all_by_project(project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by, expand=expand)

Finds activities in project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectActivitiesResourceApi()
project_id = 56 # int | 
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
sort_by = 'sort_by_example' # str | ex. sort_by=ID:asc,date_created:desc (optional)
filter_by = ['filter_by_example'] # list[str] | ex. filter_by=flag:dataset (optional)
expand = ['expand_example'] # list[str] | ex. expand=creator (optional)

try:
    # Finds activities in project.
    api_response = api_instance.find_all_by_project(project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectActivitiesResourceApi->find_all_by_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort_by** | **str**| ex. sort_by&#x3D;ID:asc,date_created:desc | [optional] 
 **filter_by** | [**list[str]**](str.md)| ex. filter_by&#x3D;flag:dataset | [optional] 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;creator | [optional] 

### Return type

[**ActivitiesDTO**](ActivitiesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

