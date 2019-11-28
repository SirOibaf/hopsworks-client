# swagger_client.ClusterUtilisationServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_gpus**](ClusterUtilisationServiceApi.md#get_gpus) | **GET** /clusterUtilisation/metrics | 

# **get_gpus**
> get_gpus()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterUtilisationServiceApi()

try:
    api_instance.get_gpus()
except ApiException as e:
    print("Exception when calling ClusterUtilisationServiceApi->get_gpus: %s\n" % e)
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

