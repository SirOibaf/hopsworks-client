# swagger_client.ModelInferenceServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**infer**](ModelInferenceServiceApi.md#infer) | **POST** /project/{projectId}/inference/models/{modelName}{version}{verb} | Make inference

# **infer**
> infer(model_name, version, verb, project_id, body=body)

Make inference

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ModelInferenceServiceApi()
model_name = 'model_name_example' # str | Name of the model to query
version = 'version_example' # str | Version of the model to query
verb = 'verb_example' # str | Type of query
project_id = 56 # int | 
body = 'body_example' # str |  (optional)

try:
    # Make inference
    api_instance.infer(model_name, version, verb, project_id, body=body)
except ApiException as e:
    print("Exception when calling ModelInferenceServiceApi->infer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**| Name of the model to query | 
 **version** | **str**| Version of the model to query | 
 **verb** | **str**| Type of query | 
 **project_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

