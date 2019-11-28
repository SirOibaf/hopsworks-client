# swagger_client.MaggyServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_driver**](MaggyServiceApi.md#get_driver) | **GET** /maggy/drivers/{appId} | Get a Maggy Driver Endpoint for this YARN appId
[**register**](MaggyServiceApi.md#register) | **POST** /maggy/drivers | Register a Maggy Driver Endpoint for this YARN appId (called by Spark Driver in maggy).

# **get_driver**
> MaggyDriver get_driver(app_id)

Get a Maggy Driver Endpoint for this YARN appId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaggyServiceApi()
app_id = 'app_id_example' # str | 

try:
    # Get a Maggy Driver Endpoint for this YARN appId
    api_response = api_instance.get_driver(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaggyServiceApi->get_driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

[**MaggyDriver**](MaggyDriver.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register**
> register(body=body)

Register a Maggy Driver Endpoint for this YARN appId (called by Spark Driver in maggy).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaggyServiceApi()
body = swagger_client.MaggyDriver() # MaggyDriver |  (optional)

try:
    # Register a Maggy Driver Endpoint for this YARN appId (called by Spark Driver in maggy).
    api_instance.register(body=body)
except ApiException as e:
    print("Exception when calling MaggyServiceApi->register: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MaggyDriver**](MaggyDriver.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

