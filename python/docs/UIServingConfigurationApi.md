# swagger_client.UIServingConfigurationApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configuration**](UIServingConfigurationApi.md#get_configuration) | **GET** /servingconf | Get UI configuration for serving

# **get_configuration**
> RepresentConfigurationForServingUI get_configuration()

Get UI configuration for serving

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UIServingConfigurationApi()

try:
    # Get UI configuration for serving
    api_response = api_instance.get_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UIServingConfigurationApi->get_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RepresentConfigurationForServingUI**](RepresentConfigurationForServingUI.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

