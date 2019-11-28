# swagger_client.PythonEnvironmentsResourceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](PythonEnvironmentsResourceApi.md#delete) | **DELETE** /project/{projectId}/python/environments/{version}/commands | Delete commands for this environment
[**delete1**](PythonEnvironmentsResourceApi.md#delete1) | **DELETE** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Delete commands for this library
[**delete2**](PythonEnvironmentsResourceApi.md#delete2) | **DELETE** /project/{projectId}/python/environments/{version} | Remove the python environment with the specified version for this project
[**get**](PythonEnvironmentsResourceApi.md#get) | **GET** /project/{projectId}/python/environments/{version}/commands | Get commands for this environment
[**get1**](PythonEnvironmentsResourceApi.md#get1) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Get all commands for this library
[**get2**](PythonEnvironmentsResourceApi.md#get2) | **GET** /project/{projectId}/python/environments/{version}/libraries | Get the python libraries installed in this environment
[**get3**](PythonEnvironmentsResourceApi.md#get3) | **GET** /project/{projectId}/python/environments/{version} | Get the python environment for specific python version
[**get_all**](PythonEnvironmentsResourceApi.md#get_all) | **GET** /project/{projectId}/python/environments | Get all python environments for this project
[**get_by_name**](PythonEnvironmentsResourceApi.md#get_by_name) | **GET** /project/{projectId}/python/environments/{version}/commands/{commandId} | Get commands by id
[**get_by_name1**](PythonEnvironmentsResourceApi.md#get_by_name1) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library}/commands/{commandId} | Get command by id
[**get_by_name2**](PythonEnvironmentsResourceApi.md#get_by_name2) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library} | Get the a python library installed in this environment
[**install**](PythonEnvironmentsResourceApi.md#install) | **POST** /project/{projectId}/python/environments/{version}/libraries/{library} | Install a python library in the environment
[**post**](PythonEnvironmentsResourceApi.md#post) | **POST** /project/{projectId}/python/environments/{version} | Create an environment from version or export an environment as yaml file
[**post_yml**](PythonEnvironmentsResourceApi.md#post_yml) | **POST** /project/{projectId}/python/environments | Create an environment from yaml file
[**search**](PythonEnvironmentsResourceApi.md#search) | **GET** /project/{projectId}/python/environments/{version}/libraries/{search} | Search for libraries using conda or pip package managers
[**uninstall**](PythonEnvironmentsResourceApi.md#uninstall) | **DELETE** /project/{projectId}/python/environments/{version}/libraries/{library} | Uninstall a python library from the environment
[**update**](PythonEnvironmentsResourceApi.md#update) | **PUT** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Update commands for this library

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
api_instance = swagger_client.PythonEnvironmentsResourceApi()
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Delete commands for this environment
    api_instance.delete(version, project_id)
except ApiException as e:
    print("Exception when calling PythonEnvironmentsResourceApi->delete: %s\n" % e)
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
api_instance = swagger_client.PythonEnvironmentsResourceApi()
library = 'library_example' # str | 
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Delete commands for this library
    api_instance.delete1(library, version, project_id)
except ApiException as e:
    print("Exception when calling PythonEnvironmentsResourceApi->delete1: %s\n" % e)
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

# **delete2**
> EnvironmentDTO delete2(version, project_id)

Remove the python environment with the specified version for this project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PythonEnvironmentsResourceApi()
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Remove the python environment with the specified version for this project
    api_response = api_instance.delete2(version, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonEnvironmentsResourceApi->delete2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
api_instance = swagger_client.PythonEnvironmentsResourceApi()
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
    print("Exception when calling PythonEnvironmentsResourceApi->get: %s\n" % e)
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
api_instance = swagger_client.PythonEnvironmentsResourceApi()
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
    print("Exception when calling PythonEnvironmentsResourceApi->get1: %s\n" % e)
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
api_instance = swagger_client.PythonEnvironmentsResourceApi()
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
    print("Exception when calling PythonEnvironmentsResourceApi->get2: %s\n" % e)
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

# **get3**
> EnvironmentDTO get3(version, project_id, expand=expand)

Get the python environment for specific python version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PythonEnvironmentsResourceApi()
version = 'version_example' # str | 
project_id = 56 # int | 
expand = ['expand_example'] # list[str] | ex. expand=commands (optional)

try:
    # Get the python environment for specific python version
    api_response = api_instance.get3(version, project_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonEnvironmentsResourceApi->get3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **project_id** | **int**|  | 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;commands | [optional] 

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> EnvironmentDTO get_all(project_id, expand=expand)

Get all python environments for this project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PythonEnvironmentsResourceApi()
project_id = 56 # int | 
expand = ['expand_example'] # list[str] | ex. expand=commands (optional)

try:
    # Get all python environments for this project
    api_response = api_instance.get_all(project_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonEnvironmentsResourceApi->get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;commands | [optional] 

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
api_instance = swagger_client.PythonEnvironmentsResourceApi()
command_id = 56 # int | 
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Get commands by id
    api_response = api_instance.get_by_name(command_id, version, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonEnvironmentsResourceApi->get_by_name: %s\n" % e)
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
api_instance = swagger_client.PythonEnvironmentsResourceApi()
library = 'library_example' # str | 
command_id = 56 # int | 
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Get command by id
    api_response = api_instance.get_by_name1(library, command_id, version, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonEnvironmentsResourceApi->get_by_name1: %s\n" % e)
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
api_instance = swagger_client.PythonEnvironmentsResourceApi()
library = 'library_example' # str | 
version = 'version_example' # str | 
project_id = 56 # int | 
expand = ['expand_example'] # list[str] | ex. expand=commands (optional)

try:
    # Get the a python library installed in this environment
    api_response = api_instance.get_by_name2(library, version, project_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonEnvironmentsResourceApi->get_by_name2: %s\n" % e)
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
api_instance = swagger_client.PythonEnvironmentsResourceApi()
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
    print("Exception when calling PythonEnvironmentsResourceApi->install: %s\n" % e)
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

# **post**
> EnvironmentDTO post(version, project_id, action=action)

Create an environment from version or export an environment as yaml file

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PythonEnvironmentsResourceApi()
version = 'version_example' # str | 
project_id = 56 # int | 
action = 'action_example' # str |  (optional)

try:
    # Create an environment from version or export an environment as yaml file
    api_response = api_instance.post(version, project_id, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonEnvironmentsResourceApi->post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **project_id** | **int**|  | 
 **action** | **str**|  | [optional] 

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_yml**
> EnvironmentDTO post_yml(project_id, body=body)

Create an environment from yaml file

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PythonEnvironmentsResourceApi()
project_id = 56 # int | 
body = swagger_client.EnvironmentYmlDTO() # EnvironmentYmlDTO |  (optional)

try:
    # Create an environment from yaml file
    api_response = api_instance.post_yml(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonEnvironmentsResourceApi->post_yml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**EnvironmentYmlDTO**](EnvironmentYmlDTO.md)|  | [optional] 

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

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
api_instance = swagger_client.PythonEnvironmentsResourceApi()
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
    print("Exception when calling PythonEnvironmentsResourceApi->search: %s\n" % e)
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
api_instance = swagger_client.PythonEnvironmentsResourceApi()
library = 'library_example' # str | 
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Uninstall a python library from the environment
    api_instance.uninstall(library, version, project_id)
except ApiException as e:
    print("Exception when calling PythonEnvironmentsResourceApi->uninstall: %s\n" % e)
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
api_instance = swagger_client.PythonEnvironmentsResourceApi()
library = 'library_example' # str | 
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Update commands for this library
    api_instance.update(library, version, project_id)
except ApiException as e:
    print("Exception when calling PythonEnvironmentsResourceApi->update: %s\n" % e)
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

