# swagger_client.EndpointServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_endpoint**](EndpointServiceApi.md#find_endpoint) | **GET** /endpoint | 

# **find_endpoint**
> find_endpoint()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EndpointServiceApi()

try:
    api_instance.find_endpoint()
except ApiException as e:
    print("Exception when calling EndpointServiceApi->find_endpoint: %s\n" % e)
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

