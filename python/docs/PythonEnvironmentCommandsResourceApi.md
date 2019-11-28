# swagger_client.PythonEnvironmentCommandsResourceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](PythonEnvironmentCommandsResourceApi.md#delete) | **DELETE** /project/{projectId}/python/environments/{version}/commands | Delete commands for this environment
[**get**](PythonEnvironmentCommandsResourceApi.md#get) | **GET** /project/{projectId}/python/environments/{version}/commands | Get commands for this environment
[**get_by_name**](PythonEnvironmentCommandsResourceApi.md#get_by_name) | **GET** /project/{projectId}/python/environments/{version}/commands/{commandId} | Get commands by id

# **delete**
> delete(version, project_id)

Delete commands for this environment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PythonEnvironmentCommandsResourceApi()
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Delete commands for this environment
    api_instance.delete(version, project_id)
except ApiException as e:
    print("Exception when calling PythonEnvironmentCommandsResourceApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> get(version, project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by)

Get commands for this environment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PythonEnvironmentCommandsResourceApi()
version = 'version_example' # str | 
project_id = 56 # int | 
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
sort_by = 'sort_by_example' # str | ex. sort_by=ID:asc,date_created:desc (optional)
filter_by = ['filter_by_example'] # list[str] | ex. filter_by=op:create (optional)

try:
    # Get commands for this environment
    api_instance.get(version, project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by)
except ApiException as e:
    print("Exception when calling PythonEnvironmentCommandsResourceApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **project_id** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort_by** | **str**| ex. sort_by&#x3D;ID:asc,date_created:desc | [optional] 
 **filter_by** | [**list[str]**](str.md)| ex. filter_by&#x3D;op:create | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_name**
> CommandDTO get_by_name(command_id, version, project_id)

Get commands by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PythonEnvironmentCommandsResourceApi()
command_id = 56 # int | 
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Get commands by id
    api_response = api_instance.get_by_name(command_id, version, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonEnvironmentCommandsResourceApi->get_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **int**|  | 
 **version** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

[**CommandDTO**](CommandDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

