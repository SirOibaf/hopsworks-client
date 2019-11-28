# swagger_client.PythonEnvironmentLibraryCommandsResourceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete1**](PythonEnvironmentLibraryCommandsResourceApi.md#delete1) | **DELETE** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Delete commands for this library
[**get1**](PythonEnvironmentLibraryCommandsResourceApi.md#get1) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Get all commands for this library
[**get_by_name1**](PythonEnvironmentLibraryCommandsResourceApi.md#get_by_name1) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library}/commands/{commandId} | Get command by id
[**update**](PythonEnvironmentLibraryCommandsResourceApi.md#update) | **PUT** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Update commands for this library

# **delete1**
> delete1(library, version, project_id)

Delete commands for this library

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PythonEnvironmentLibraryCommandsResourceApi()
library = 'library_example' # str | 
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Delete commands for this library
    api_instance.delete1(library, version, project_id)
except ApiException as e:
    print("Exception when calling PythonEnvironmentLibraryCommandsResourceApi->delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **str**|  | 
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

# **get1**
> CommandDTO get1(library, version, project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by)

Get all commands for this library

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PythonEnvironmentLibraryCommandsResourceApi()
library = 'library_example' # str | 
version = 'version_example' # str | 
project_id = 56 # int | 
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
sort_by = 'sort_by_example' # str | ex. sort_by=ID:asc,date_created:desc (optional)
filter_by = ['filter_by_example'] # list[str] | ex. filter_by=op:create (optional)

try:
    # Get all commands for this library
    api_response = api_instance.get1(library, version, project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonEnvironmentLibraryCommandsResourceApi->get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **str**|  | 
 **version** | **str**|  | 
 **project_id** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort_by** | **str**| ex. sort_by&#x3D;ID:asc,date_created:desc | [optional] 
 **filter_by** | [**list[str]**](str.md)| ex. filter_by&#x3D;op:create | [optional] 

### Return type

[**CommandDTO**](CommandDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_name1**
> CommandDTO get_by_name1(library, command_id, version, project_id)

Get command by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PythonEnvironmentLibraryCommandsResourceApi()
library = 'library_example' # str | 
command_id = 56 # int | 
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Get command by id
    api_response = api_instance.get_by_name1(library, command_id, version, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonEnvironmentLibraryCommandsResourceApi->get_by_name1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **str**|  | 
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

# **update**
> update(library, version, project_id)

Update commands for this library

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PythonEnvironmentLibraryCommandsResourceApi()
library = 'library_example' # str | 
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Update commands for this library
    api_instance.update(library, version, project_id)
except ApiException as e:
    print("Exception when calling PythonEnvironmentLibraryCommandsResourceApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **str**|  | 
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

