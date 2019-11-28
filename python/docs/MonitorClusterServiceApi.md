# swagger_client.MonitorClusterServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_roles**](MonitorClusterServiceApi.md#get_all_roles) | **GET** /kmon/services | 
[**get_host_roles**](MonitorClusterServiceApi.md#get_host_roles) | **GET** /kmon/hosts/{hostId}/services | 
[**get_hosts**](MonitorClusterServiceApi.md#get_hosts) | **GET** /kmon/hosts/{hostId} | 
[**get_hosts1**](MonitorClusterServiceApi.md#get_hosts1) | **GET** /kmon/hosts | 
[**get_roles**](MonitorClusterServiceApi.md#get_roles) | **GET** /kmon/groups/{groupName}/services/{serviceName} | 
[**get_service_roles**](MonitorClusterServiceApi.md#get_service_roles) | **GET** /kmon/groups/{groupName} | 
[**service_on_host_op**](MonitorClusterServiceApi.md#service_on_host_op) | **POST** /kmon/groups/{groupName}/services/{serviceName}/hosts/{hostId} | 
[**service_op**](MonitorClusterServiceApi.md#service_op) | **POST** /kmon/groups/{groupName} | 
[**service_op1**](MonitorClusterServiceApi.md#service_op1) | **POST** /kmon/groups/{groupName}/services/{serviceName} | 

# **get_all_roles**
> get_all_roles()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonitorClusterServiceApi()

try:
    api_instance.get_all_roles()
except ApiException as e:
    print("Exception when calling MonitorClusterServiceApi->get_all_roles: %s\n" % e)
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

# **get_host_roles**
> get_host_roles(host_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonitorClusterServiceApi()
host_id = 'host_id_example' # str | 

try:
    api_instance.get_host_roles(host_id)
except ApiException as e:
    print("Exception when calling MonitorClusterServiceApi->get_host_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hosts**
> get_hosts(host_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonitorClusterServiceApi()
host_id = 'host_id_example' # str | 

try:
    api_instance.get_hosts(host_id)
except ApiException as e:
    print("Exception when calling MonitorClusterServiceApi->get_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hosts1**
> get_hosts1()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonitorClusterServiceApi()

try:
    api_instance.get_hosts1()
except ApiException as e:
    print("Exception when calling MonitorClusterServiceApi->get_hosts1: %s\n" % e)
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

# **get_roles**
> get_roles(group_name, service_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonitorClusterServiceApi()
group_name = 'group_name_example' # str | 
service_name = 'service_name_example' # str | 

try:
    api_instance.get_roles(group_name, service_name)
except ApiException as e:
    print("Exception when calling MonitorClusterServiceApi->get_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**|  | 
 **service_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_roles**
> get_service_roles(group_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonitorClusterServiceApi()
group_name = 'group_name_example' # str | 

try:
    api_instance.get_service_roles(group_name)
except ApiException as e:
    print("Exception when calling MonitorClusterServiceApi->get_service_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_on_host_op**
> service_on_host_op(group_name, service_name, host_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonitorClusterServiceApi()
group_name = 'group_name_example' # str | 
service_name = 'service_name_example' # str | 
host_id = 'host_id_example' # str | 
body = swagger_client.ServicesActionDTO() # ServicesActionDTO |  (optional)

try:
    api_instance.service_on_host_op(group_name, service_name, host_id, body=body)
except ApiException as e:
    print("Exception when calling MonitorClusterServiceApi->service_on_host_op: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**|  | 
 **service_name** | **str**|  | 
 **host_id** | **str**|  | 
 **body** | [**ServicesActionDTO**](ServicesActionDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_op**
> service_op(group_name, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonitorClusterServiceApi()
group_name = 'group_name_example' # str | 
body = swagger_client.ServicesActionDTO() # ServicesActionDTO |  (optional)

try:
    api_instance.service_op(group_name, body=body)
except ApiException as e:
    print("Exception when calling MonitorClusterServiceApi->service_op: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**|  | 
 **body** | [**ServicesActionDTO**](ServicesActionDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_op1**
> service_op1(group_name, service_name, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonitorClusterServiceApi()
group_name = 'group_name_example' # str | 
service_name = 'service_name_example' # str | 
body = swagger_client.ServicesActionDTO() # ServicesActionDTO |  (optional)

try:
    api_instance.service_op1(group_name, service_name, body=body)
except ApiException as e:
    print("Exception when calling MonitorClusterServiceApi->service_op1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**|  | 
 **service_name** | **str**|  | 
 **body** | [**ServicesActionDTO**](ServicesActionDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

