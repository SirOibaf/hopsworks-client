# swagger_client.PythonEnvironmentLibraryResourceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete1**](PythonEnvironmentLibraryResourceApi.md#delete1) | **DELETE** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Delete commands for this library
[**get1**](PythonEnvironmentLibraryResourceApi.md#get1) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Get all commands for this library
[**get2**](PythonEnvironmentLibraryResourceApi.md#get2) | **GET** /project/{projectId}/python/environments/{version}/libraries | Get the python libraries installed in this environment
[**get_by_name1**](PythonEnvironmentLibraryResourceApi.md#get_by_name1) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library}/commands/{commandId} | Get command by id
[**get_by_name2**](PythonEnvironmentLibraryResourceApi.md#get_by_name2) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library} | Get the a python library installed in this environment
[**install**](PythonEnvironmentLibraryResourceApi.md#install) | **POST** /project/{projectId}/python/environments/{version}/libraries/{library} | Install a python library in the environment
[**search**](PythonEnvironmentLibraryResourceApi.md#search) | **GET** /project/{projectId}/python/environments/{version}/libraries/{search} | Search for libraries using conda or pip package managers
[**uninstall**](PythonEnvironmentLibraryResourceApi.md#uninstall) | **DELETE** /project/{projectId}/python/environments/{version}/libraries/{library} | Uninstall a python library from the environment
[**update**](PythonEnvironmentLibraryResourceApi.md#update) | **PUT** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Update commands for this library

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
api_instance = swagger_client.PythonEnvironmentLibraryResourceApi()
library = 'library_example' # str | 
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Delete commands for this library
    api_instance.delete1(library, version, project_id)
except ApiException as e:
    print("Exception when calling PythonEnvironmentLibraryResourceApi->delete1: %s\n" % e)
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
api_instance = swagger_client.PythonEnvironmentLibraryResourceApi()
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
    print("Exception when calling PythonEnvironmentLibraryResourceApi->get1: %s\n" % e)
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

# **get2**
> LibraryDTO get2(version, project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by, expand=expand)

Get the python libraries installed in this environment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PythonEnvironmentLibraryResourceApi()
version = 'version_example' # str | 
project_id = 56 # int | 
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
sort_by = 'sort_by_example' # str | ex. sort_by=ID:asc,dependency:desc (optional)
filter_by = ['filter_by_example'] # list[str] | ex. filter_by=preinstalled:1 (optional)
expand = ['expand_example'] # list[str] | ex. expand=commands (optional)

try:
    # Get the python libraries installed in this environment
    api_response = api_instance.get2(version, project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonEnvironmentLibraryResourceApi->get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **project_id** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort_by** | **str**| ex. sort_by&#x3D;ID:asc,dependency:desc | [optional] 
 **filter_by** | [**list[str]**](str.md)| ex. filter_by&#x3D;preinstalled:1 | [optional] 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;commands | [optional] 

### Return type

[**LibraryDTO**](LibraryDTO.md)

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
api_instance = swagger_client.PythonEnvironmentLibraryResourceApi()
library = 'library_example' # str | 
command_id = 56 # int | 
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Get command by id
    api_response = api_instance.get_by_name1(library, command_id, version, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonEnvironmentLibraryResourceApi->get_by_name1: %s\n" % e)
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

# **get_by_name2**
> LibraryDTO get_by_name2(library, version, project_id, expand=expand)

Get the a python library installed in this environment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PythonEnvironmentLibraryResourceApi()
library = 'library_example' # str | 
version = 'version_example' # str | 
project_id = 56 # int | 
expand = ['expand_example'] # list[str] | ex. expand=commands (optional)

try:
    # Get the a python library installed in this environment
    api_response = api_instance.get_by_name2(library, version, project_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonEnvironmentLibraryResourceApi->get_by_name2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **str**|  | 
 **version** | **str**|  | 
 **project_id** | **int**|  | 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;commands | [optional] 

### Return type

[**LibraryDTO**](LibraryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install**
> install(library, version2, project_id, package_manager=package_manager, version=version, channel=channel, machine=machine)

Install a python library in the environment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PythonEnvironmentLibraryResourceApi()
library = 'library_example' # str | 
version2 = 'version_example' # str | 
project_id = 56 # int | 
package_manager = 'package_manager_example' # str |  (optional)
version = 'version_example' # str |  (optional)
channel = 'channel_example' # str |  (optional)
machine = 'machine_example' # str |  (optional)

try:
    # Install a python library in the environment
    api_instance.install(library, version2, project_id, package_manager=package_manager, version=version, channel=channel, machine=machine)
except ApiException as e:
    print("Exception when calling PythonEnvironmentLibraryResourceApi->install: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **str**|  | 
 **version2** | **str**|  | 
 **project_id** | **int**|  | 
 **package_manager** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **channel** | **str**|  | [optional] 
 **machine** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> LibrarySearchDTO search(search, version, project_id, query=query, channel=channel)

Search for libraries using conda or pip package managers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PythonEnvironmentLibraryResourceApi()
search = 'search_example' # str | 
version = 'version_example' # str | 
project_id = 56 # int | 
query = 'query_example' # str |  (optional)
channel = 'channel_example' # str |  (optional)

try:
    # Search for libraries using conda or pip package managers
    api_response = api_instance.search(search, version, project_id, query=query, channel=channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonEnvironmentLibraryResourceApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | 
 **version** | **str**|  | 
 **project_id** | **int**|  | 
 **query** | **str**|  | [optional] 
 **channel** | **str**|  | [optional] 

### Return type

[**LibrarySearchDTO**](LibrarySearchDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uninstall**
> uninstall(library, version, project_id)

Uninstall a python library from the environment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PythonEnvironmentLibraryResourceApi()
library = 'library_example' # str | 
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Uninstall a python library from the environment
    api_instance.uninstall(library, version, project_id)
except ApiException as e:
    print("Exception when calling PythonEnvironmentLibraryResourceApi->uninstall: %s\n" % e)
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
api_instance = swagger_client.PythonEnvironmentLibraryResourceApi()
library = 'library_example' # str | 
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Update commands for this library
    api_instance.update(library, version, project_id)
except ApiException as e:
    print("Exception when calling PythonEnvironmentLibraryResourceApi->update: %s\n" % e)
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

