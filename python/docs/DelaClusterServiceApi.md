# swagger_client.DelaClusterServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_datasets**](DelaClusterServiceApi.md#get_public_datasets) | **GET** /delacluster | 

# **get_public_datasets**
> get_public_datasets()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DelaClusterServiceApi()

try:
    api_instance.get_public_datasets()
except ApiException as e:
    print("Exception when calling DelaClusterServiceApi->get_public_datasets: %s\n" % e)
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

