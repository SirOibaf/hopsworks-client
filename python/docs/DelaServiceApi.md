# swagger_client.DelaServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**details**](DelaServiceApi.md#details) | **GET** /dela/transfers/{publicDSId} | 
[**get_client_type**](DelaServiceApi.md#get_client_type) | **GET** /dela/client | 
[**get_contents_for_user**](DelaServiceApi.md#get_contents_for_user) | **GET** /dela/transfers | 
[**get_public_datasets1**](DelaServiceApi.md#get_public_datasets1) | **GET** /dela | 
[**public_search**](DelaServiceApi.md#public_search) | **GET** /dela/search | 
[**readme**](DelaServiceApi.md#readme) | **POST** /dela/datasets/{publicDSId}/readme | Gets readme file from a provided list of peers

# **details**
> details(public_ds_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DelaServiceApi()
public_ds_id = 'public_ds_id_example' # str | 

try:
    api_instance.details(public_ds_id)
except ApiException as e:
    print("Exception when calling DelaServiceApi->details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_ds_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_type**
> get_client_type()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DelaServiceApi()

try:
    api_instance.get_client_type()
except ApiException as e:
    print("Exception when calling DelaServiceApi->get_client_type: %s\n" % e)
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

# **get_contents_for_user**
> get_contents_for_user(filter=filter)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DelaServiceApi()
filter = 'filter_example' # str |  (optional)

try:
    api_instance.get_contents_for_user(filter=filter)
except ApiException as e:
    print("Exception when calling DelaServiceApi->get_contents_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_datasets1**
> get_public_datasets1()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DelaServiceApi()

try:
    api_instance.get_public_datasets1()
except ApiException as e:
    print("Exception when calling DelaServiceApi->get_public_datasets1: %s\n" % e)
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

# **public_search**
> public_search(query)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DelaServiceApi()
query = 'query_example' # str | 

try:
    api_instance.public_search(query)
except ApiException as e:
    print("Exception when calling DelaServiceApi->public_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **readme**
> readme(public_ds_id, body=body)

Gets readme file from a provided list of peers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DelaServiceApi()
public_ds_id = 'public_ds_id_example' # str | 
body = swagger_client.BootstrapDTO() # BootstrapDTO |  (optional)

try:
    # Gets readme file from a provided list of peers
    api_instance.readme(public_ds_id, body=body)
except ApiException as e:
    print("Exception when calling DelaServiceApi->readme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_ds_id** | **str**|  | 
 **body** | [**BootstrapDTO**](BootstrapDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

