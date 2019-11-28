# swagger_client.AirflowRelatedEndpointsApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compose_dag**](AirflowRelatedEndpointsApi.md#compose_dag) | **POST** /project/{projectId}/airflow/dag | Generate an Airflow Python DAG file from a DAG definition
[**secret_dir**](AirflowRelatedEndpointsApi.md#secret_dir) | **GET** /project/{projectId}/airflow/secretDir | Create project secret directory in Airflow home
[**store_airflow_jwt**](AirflowRelatedEndpointsApi.md#store_airflow_jwt) | **POST** /project/{projectId}/airflow/jwt | Generate a JWT for Airflow usage and store it in project&#x27;s secret directory in Airflow

# **compose_dag**
> compose_dag(project_id, body=body)

Generate an Airflow Python DAG file from a DAG definition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AirflowRelatedEndpointsApi()
project_id = 56 # int | 
body = swagger_client.AirflowDagDTO() # AirflowDagDTO |  (optional)

try:
    # Generate an Airflow Python DAG file from a DAG definition
    api_instance.compose_dag(project_id, body=body)
except ApiException as e:
    print("Exception when calling AirflowRelatedEndpointsApi->compose_dag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**AirflowDagDTO**](AirflowDagDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_dir**
> secret_dir(project_id)

Create project secret directory in Airflow home

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AirflowRelatedEndpointsApi()
project_id = 56 # int | 

try:
    # Create project secret directory in Airflow home
    api_instance.secret_dir(project_id)
except ApiException as e:
    print("Exception when calling AirflowRelatedEndpointsApi->secret_dir: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_airflow_jwt**
> store_airflow_jwt(project_id)

Generate a JWT for Airflow usage and store it in project's secret directory in Airflow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AirflowRelatedEndpointsApi()
project_id = 56 # int | 

try:
    # Generate a JWT for Airflow usage and store it in project's secret directory in Airflow
    api_instance.store_airflow_jwt(project_id)
except ApiException as e:
    print("Exception when calling AirflowRelatedEndpointsApi->store_airflow_jwt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

