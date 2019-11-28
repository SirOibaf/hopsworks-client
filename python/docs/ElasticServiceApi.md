# swagger_client.ElasticServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataset_search**](ElasticServiceApi.md#dataset_search) | **GET** /elastic/datasetsearch/{projectId}/{datasetName}/{searchTerm} | 
[**global_search**](ElasticServiceApi.md#global_search) | **GET** /elastic/globalsearch/{searchTerm} | 
[**project_search**](ElasticServiceApi.md#project_search) | **GET** /elastic/projectsearch/{projectId}/{searchTerm} | 

# **dataset_search**
> dataset_search(project_id, dataset_name, search_term)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElasticServiceApi()
project_id = 56 # int | 
dataset_name = 'dataset_name_example' # str | 
search_term = 'search_term_example' # str | 

try:
    api_instance.dataset_search(project_id, dataset_name, search_term)
except ApiException as e:
    print("Exception when calling ElasticServiceApi->dataset_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **dataset_name** | **str**|  | 
 **search_term** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **global_search**
> global_search(search_term)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElasticServiceApi()
search_term = 'search_term_example' # str | 

try:
    api_instance.global_search(search_term)
except ApiException as e:
    print("Exception when calling ElasticServiceApi->global_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_search**
> project_search(project_id, search_term)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ElasticServiceApi()
project_id = 56 # int | 
search_term = 'search_term_example' # str | 

try:
    api_instance.project_search(project_id, search_term)
except ApiException as e:
    print("Exception when calling ElasticServiceApi->project_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **search_term** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

