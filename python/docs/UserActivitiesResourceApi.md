# swagger_client.UserActivitiesResourceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_all_by_id1**](UserActivitiesResourceApi.md#find_all_by_id1) | **GET** /users/activities/{activityId} | Finds an activity for a user by id.
[**find_all_by_user1**](UserActivitiesResourceApi.md#find_all_by_user1) | **GET** /users/activities | Finds all activities for a user.

# **find_all_by_id1**
> ActivitiesDTO find_all_by_id1(activity_id, expand=expand)

Finds an activity for a user by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserActivitiesResourceApi()
activity_id = 56 # int | 
expand = ['expand_example'] # list[str] | ex. expand=creator (optional)

try:
    # Finds an activity for a user by id.
    api_response = api_instance.find_all_by_id1(activity_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivitiesResourceApi->find_all_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**|  | 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;creator | [optional] 

### Return type

[**ActivitiesDTO**](ActivitiesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_by_user1**
> ActivitiesDTO find_all_by_user1(offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by, expand=expand)

Finds all activities for a user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserActivitiesResourceApi()
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
sort_by = 'sort_by_example' # str | ex. sort_by=ID:asc,date_created:desc (optional)
filter_by = ['filter_by_example'] # list[str] | ex. filter_by=flag:dataset (optional)
expand = ['expand_example'] # list[str] | ex. expand=creator (optional)

try:
    # Finds all activities for a user.
    api_response = api_instance.find_all_by_user1(offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserActivitiesResourceApi->find_all_by_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

