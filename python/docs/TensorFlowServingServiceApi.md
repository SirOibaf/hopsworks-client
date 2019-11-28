# swagger_client.TensorFlowServingServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update**](TensorFlowServingServiceApi.md#create_or_update) | **PUT** /project/{projectId}/serving | Create or update a serving instance
[**delete_serving**](TensorFlowServingServiceApi.md#delete_serving) | **DELETE** /project/{projectId}/serving/{servingId} | Delete a serving instance
[**get_serving**](TensorFlowServingServiceApi.md#get_serving) | **GET** /project/{projectId}/serving/{servingId} | Get info about a serving instance for the project
[**get_servings**](TensorFlowServingServiceApi.md#get_servings) | **GET** /project/{projectId}/serving | Get the list of serving instances for the project
[**start_or_stop**](TensorFlowServingServiceApi.md#start_or_stop) | **POST** /project/{projectId}/serving/{servingId} | Start or stop a Serving instance

# **create_or_update**
> create_or_update(body, project_id)

Create or update a serving instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TensorFlowServingServiceApi()
body = swagger_client.RepresentsAServingModel() # RepresentsAServingModel | serving specification
project_id = 56 # int | 

try:
    # Create or update a serving instance
    api_instance.create_or_update(body, project_id)
except ApiException as e:
    print("Exception when calling TensorFlowServingServiceApi->create_or_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RepresentsAServingModel**](RepresentsAServingModel.md)| serving specification | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_serving**
> delete_serving(serving_id, project_id)

Delete a serving instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TensorFlowServingServiceApi()
serving_id = 56 # int | Id of the serving instance
project_id = 56 # int | 

try:
    # Delete a serving instance
    api_instance.delete_serving(serving_id, project_id)
except ApiException as e:
    print("Exception when calling TensorFlowServingServiceApi->delete_serving: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serving_id** | **int**| Id of the serving instance | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_serving**
> RepresentsAServingModel get_serving(serving_id, project_id)

Get info about a serving instance for the project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TensorFlowServingServiceApi()
serving_id = 56 # int | Id of the Serving instance
project_id = 56 # int | 

try:
    # Get info about a serving instance for the project
    api_response = api_instance.get_serving(serving_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TensorFlowServingServiceApi->get_serving: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serving_id** | **int**| Id of the Serving instance | 
 **project_id** | **int**|  | 

### Return type

[**RepresentsAServingModel**](RepresentsAServingModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_servings**
> list[RepresentsAServingModel] get_servings(project_id)

Get the list of serving instances for the project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TensorFlowServingServiceApi()
project_id = 56 # int | 

try:
    # Get the list of serving instances for the project
    api_response = api_instance.get_servings(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TensorFlowServingServiceApi->get_servings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**list[RepresentsAServingModel]**](RepresentsAServingModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_or_stop**
> start_or_stop(serving_id, action, project_id)

Start or stop a Serving instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TensorFlowServingServiceApi()
serving_id = 56 # int | ID of the Serving instance to start/stop
action = 'action_example' # str | Action
project_id = 56 # int | 

try:
    # Start or stop a Serving instance
    api_instance.start_or_stop(serving_id, action, project_id)
except ApiException as e:
    print("Exception when calling TensorFlowServingServiceApi->start_or_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serving_id** | **int**| ID of the Serving instance to start/stop | 
 **action** | **str**| Action | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

