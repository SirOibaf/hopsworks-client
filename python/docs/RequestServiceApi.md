# swagger_client.RequestServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_access**](RequestServiceApi.md#request_access) | **POST** /request/access | 
[**request_join**](RequestServiceApi.md#request_join) | **POST** /request/join | 

# **request_access**
> request_access(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RequestServiceApi()
body = swagger_client.RequestDTO() # RequestDTO |  (optional)

try:
    api_instance.request_access(body=body)
except ApiException as e:
    print("Exception when calling RequestServiceApi->request_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestDTO**](RequestDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_join**
> request_join(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RequestServiceApi()
body = swagger_client.RequestDTO() # RequestDTO |  (optional)

try:
    api_instance.request_join(body=body)
except ApiException as e:
    print("Exception when calling RequestServiceApi->request_join: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestDTO**](RequestDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

