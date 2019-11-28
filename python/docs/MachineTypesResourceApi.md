# swagger_client.MachineTypesResourceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_machine_type**](MachineTypesResourceApi.md#get_machine_type) | **GET** /machines/{type} | Get number of machines for a machine type
[**get_machine_types**](MachineTypesResourceApi.md#get_machine_types) | **GET** /machines | Get all types of machines for conda

# **get_machine_type**
> MachineTypeDTO get_machine_type(type)

Get number of machines for a machine type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MachineTypesResourceApi()
type = 'type_example' # str | 

try:
    # Get number of machines for a machine type
    api_response = api_instance.get_machine_type(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineTypesResourceApi->get_machine_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 

### Return type

[**MachineTypeDTO**](MachineTypeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_machine_types**
> MachineTypeDTO get_machine_types()

Get all types of machines for conda

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MachineTypesResourceApi()

try:
    # Get all types of machines for conda
    api_response = api_instance.get_machine_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineTypesResourceApi->get_machine_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MachineTypeDTO**](MachineTypeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

