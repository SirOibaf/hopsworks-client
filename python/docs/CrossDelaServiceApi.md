# swagger_client.CrossDelaServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**readme1**](CrossDelaServiceApi.md#readme1) | **GET** /remote/dela/datasets/{publicDSId}/readme | 

# **readme1**
> readme1(public_ds_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CrossDelaServiceApi()
public_ds_id = 'public_ds_id_example' # str | 

try:
    api_instance.readme1(public_ds_id)
except ApiException as e:
    print("Exception when calling CrossDelaServiceApi->readme1: %s\n" % e)
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

