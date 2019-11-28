# swagger_client.ApiKeyResourceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_session**](ApiKeyResourceApi.md#check_session) | **GET** /users/apiKey/session | Check api key session.
[**create**](ApiKeyResourceApi.md#create) | **POST** /users/apiKey | Create an api key.
[**delete_all**](ApiKeyResourceApi.md#delete_all) | **DELETE** /users/apiKey | Delete all api keys.
[**delete_by_name**](ApiKeyResourceApi.md#delete_by_name) | **DELETE** /users/apiKey/{name} | Delete api key by name.
[**get4**](ApiKeyResourceApi.md#get4) | **GET** /users/apiKey | Get all api keys.
[**get_by_key**](ApiKeyResourceApi.md#get_by_key) | **GET** /users/apiKey/key | Find api key by name.
[**get_by_name3**](ApiKeyResourceApi.md#get_by_name3) | **GET** /users/apiKey/{name} | Find api key by name.
[**get_scopes**](ApiKeyResourceApi.md#get_scopes) | **GET** /users/apiKey/scopes | Get all api keys scopes.
[**update1**](ApiKeyResourceApi.md#update1) | **PUT** /users/apiKey | Update an api key.

# **check_session**
> check_session()

Check api key session.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeyResourceApi()

try:
    # Check api key session.
    api_instance.check_session()
except ApiException as e:
    print("Exception when calling ApiKeyResourceApi->check_session: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> ApiKeyDTO create(name=name, scope=scope)

Create an api key.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeyResourceApi()
name = 'name_example' # str |  (optional)
scope = ['scope_example'] # list[str] |  (optional)

try:
    # Create an api key.
    api_response = api_instance.create(name=name, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeyResourceApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **scope** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**ApiKeyDTO**](ApiKeyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all**
> delete_all()

Delete all api keys.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeyResourceApi()

try:
    # Delete all api keys.
    api_instance.delete_all()
except ApiException as e:
    print("Exception when calling ApiKeyResourceApi->delete_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_by_name**
> delete_by_name(name)

Delete api key by name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeyResourceApi()
name = 'name_example' # str | 

try:
    # Delete api key by name.
    api_instance.delete_by_name(name)
except ApiException as e:
    print("Exception when calling ApiKeyResourceApi->delete_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get4**
> ApiKeyDTO get4(offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by)

Get all api keys.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeyResourceApi()
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
sort_by = 'sort_by_example' # str | ex. sort_by=Name:asc,created:desc,modified:desc (optional)
filter_by = ['filter_by_example'] # list[str] | ex. filter_by=name:key, created:2019-01-01T00:00:00.000, created_lt:2019-01-01T00:00:00.000, created_gt:2019-01-01T00:00:00.000, modified:2019-01-01T00:00:00.000, modified_lt:2019-01-01T00:00:00.000, modified_gt:2019-01-01T00:00:00.000 (optional)

try:
    # Get all api keys.
    api_response = api_instance.get4(offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeyResourceApi->get4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort_by** | **str**| ex. sort_by&#x3D;Name:asc,created:desc,modified:desc | [optional] 
 **filter_by** | [**list[str]**](str.md)| ex. filter_by&#x3D;name:key, created:2019-01-01T00:00:00.000, created_lt:2019-01-01T00:00:00.000, created_gt:2019-01-01T00:00:00.000, modified:2019-01-01T00:00:00.000, modified_lt:2019-01-01T00:00:00.000, modified_gt:2019-01-01T00:00:00.000 | [optional] 

### Return type

[**ApiKeyDTO**](ApiKeyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_key**
> ApiKeyDTO get_by_key(key=key)

Find api key by name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeyResourceApi()
key = 'key_example' # str |  (optional)

try:
    # Find api key by name.
    api_response = api_instance.get_by_key(key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeyResourceApi->get_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | [optional] 

### Return type

[**ApiKeyDTO**](ApiKeyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_name3**
> ApiKeyDTO get_by_name3(name)

Find api key by name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeyResourceApi()
name = 'name_example' # str | 

try:
    # Find api key by name.
    api_response = api_instance.get_by_name3(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeyResourceApi->get_by_name3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ApiKeyDTO**](ApiKeyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scopes**
> get_scopes()

Get all api keys scopes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeyResourceApi()

try:
    # Get all api keys scopes.
    api_instance.get_scopes()
except ApiException as e:
    print("Exception when calling ApiKeyResourceApi->get_scopes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update1**
> ApiKeyDTO update1(name=name, action=action, scope=scope)

Update an api key.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeyResourceApi()
name = 'name_example' # str |  (optional)
action = 'action_example' # str |  (optional)
scope = ['scope_example'] # list[str] |  (optional)

try:
    # Update an api key.
    api_response = api_instance.update1(name=name, action=action, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeyResourceApi->update1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **action** | **str**|  | [optional] 
 **scope** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**ApiKeyDTO**](ApiKeyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

