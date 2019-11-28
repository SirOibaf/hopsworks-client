# swagger_client.HopssiteServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_comment**](HopssiteServiceApi.md#add_comment) | **POST** /hopssite/datasets/{publicDSId}/comments | 
[**add_dataset_issue**](HopssiteServiceApi.md#add_dataset_issue) | **POST** /hopssite/datasets/{publicDSId}/issue | 
[**add_rating**](HopssiteServiceApi.md#add_rating) | **POST** /hopssite/datasets/{publicDSId}/rating | 
[**delete_comment**](HopssiteServiceApi.md#delete_comment) | **DELETE** /hopssite/datasets/{publicDSId}/comments/{commentId} | 
[**get_all_comments**](HopssiteServiceApi.md#get_all_comments) | **GET** /hopssite/datasets/{publicDSId}/comments | 
[**get_all_datasets**](HopssiteServiceApi.md#get_all_datasets) | **GET** /hopssite/datasets | 
[**get_cluster_id**](HopssiteServiceApi.md#get_cluster_id) | **GET** /hopssite/clusterId | 
[**get_dataset**](HopssiteServiceApi.md#get_dataset) | **GET** /hopssite/datasets/{publicDSId} | 
[**get_display_categories**](HopssiteServiceApi.md#get_display_categories) | **GET** /hopssite/categories | 
[**get_local_dataset**](HopssiteServiceApi.md#get_local_dataset) | **GET** /hopssite/datasets/{publicDSId}/local | 
[**get_rating**](HopssiteServiceApi.md#get_rating) | **GET** /hopssite/datasets/{publicDSId}/rating | 
[**get_service_info**](HopssiteServiceApi.md#get_service_info) | **GET** /hopssite/services/{service} | 
[**get_user_id**](HopssiteServiceApi.md#get_user_id) | **GET** /hopssite/userId | 
[**report_abuse**](HopssiteServiceApi.md#report_abuse) | **POST** /hopssite/datasets/{publicDSId}/comments/{commentId}/report | 
[**update_comment**](HopssiteServiceApi.md#update_comment) | **PUT** /hopssite/datasets/{publicDSId}/comments/{commentId} | 

# **add_comment**
> add_comment(public_ds_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HopssiteServiceApi()
public_ds_id = 'public_ds_id_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_instance.add_comment(public_ds_id, body=body)
except ApiException as e:
    print("Exception when calling HopssiteServiceApi->add_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_ds_id** | **str**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dataset_issue**
> add_dataset_issue(public_ds_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HopssiteServiceApi()
public_ds_id = 'public_ds_id_example' # str | 
body = swagger_client.DatasetIssueReqDTO() # DatasetIssueReqDTO |  (optional)

try:
    api_instance.add_dataset_issue(public_ds_id, body=body)
except ApiException as e:
    print("Exception when calling HopssiteServiceApi->add_dataset_issue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_ds_id** | **str**|  | 
 **body** | [**DatasetIssueReqDTO**](DatasetIssueReqDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_rating**
> add_rating(public_ds_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HopssiteServiceApi()
public_ds_id = 'public_ds_id_example' # str | 
body = swagger_client.RatingValueDTO() # RatingValueDTO |  (optional)

try:
    api_instance.add_rating(public_ds_id, body=body)
except ApiException as e:
    print("Exception when calling HopssiteServiceApi->add_rating: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_ds_id** | **str**|  | 
 **body** | [**RatingValueDTO**](RatingValueDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment**
> delete_comment(comment_id, public_ds_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HopssiteServiceApi()
comment_id = 56 # int | 
public_ds_id = 'public_ds_id_example' # str | 

try:
    api_instance.delete_comment(comment_id, public_ds_id)
except ApiException as e:
    print("Exception when calling HopssiteServiceApi->delete_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**|  | 
 **public_ds_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_comments**
> get_all_comments(public_ds_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HopssiteServiceApi()
public_ds_id = 'public_ds_id_example' # str | 

try:
    api_instance.get_all_comments(public_ds_id)
except ApiException as e:
    print("Exception when calling HopssiteServiceApi->get_all_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_ds_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_datasets**
> get_all_datasets(filter)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HopssiteServiceApi()
filter = 'filter_example' # str | 

try:
    api_instance.get_all_datasets(filter)
except ApiException as e:
    print("Exception when calling HopssiteServiceApi->get_all_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_id**
> get_cluster_id()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HopssiteServiceApi()

try:
    api_instance.get_cluster_id()
except ApiException as e:
    print("Exception when calling HopssiteServiceApi->get_cluster_id: %s\n" % e)
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

# **get_dataset**
> get_dataset(public_ds_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HopssiteServiceApi()
public_ds_id = 'public_ds_id_example' # str | 

try:
    api_instance.get_dataset(public_ds_id)
except ApiException as e:
    print("Exception when calling HopssiteServiceApi->get_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_ds_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_display_categories**
> get_display_categories()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HopssiteServiceApi()

try:
    api_instance.get_display_categories()
except ApiException as e:
    print("Exception when calling HopssiteServiceApi->get_display_categories: %s\n" % e)
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

# **get_local_dataset**
> get_local_dataset(public_ds_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HopssiteServiceApi()
public_ds_id = 'public_ds_id_example' # str | 

try:
    api_instance.get_local_dataset(public_ds_id)
except ApiException as e:
    print("Exception when calling HopssiteServiceApi->get_local_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_ds_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rating**
> get_rating(filter, public_ds_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HopssiteServiceApi()
filter = 'filter_example' # str | 
public_ds_id = 'public_ds_id_example' # str | 

try:
    api_instance.get_rating(filter, public_ds_id)
except ApiException as e:
    print("Exception when calling HopssiteServiceApi->get_rating: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**|  | 
 **public_ds_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_info**
> get_service_info(service)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HopssiteServiceApi()
service = 'service_example' # str | 

try:
    api_instance.get_service_info(service)
except ApiException as e:
    print("Exception when calling HopssiteServiceApi->get_service_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_id**
> get_user_id()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HopssiteServiceApi()

try:
    api_instance.get_user_id()
except ApiException as e:
    print("Exception when calling HopssiteServiceApi->get_user_id: %s\n" % e)
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

# **report_abuse**
> report_abuse(comment_id, public_ds_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HopssiteServiceApi()
comment_id = 56 # int | 
public_ds_id = 'public_ds_id_example' # str | 
body = swagger_client.CommentIssueReqDTO() # CommentIssueReqDTO |  (optional)

try:
    api_instance.report_abuse(comment_id, public_ds_id, body=body)
except ApiException as e:
    print("Exception when calling HopssiteServiceApi->report_abuse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**|  | 
 **public_ds_id** | **str**|  | 
 **body** | [**CommentIssueReqDTO**](CommentIssueReqDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment**
> update_comment(comment_id, public_ds_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HopssiteServiceApi()
comment_id = 56 # int | 
public_ds_id = 'public_ds_id_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_instance.update_comment(comment_id, public_ds_id, body=body)
except ApiException as e:
    print("Exception when calling HopssiteServiceApi->update_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**|  | 
 **public_ds_id** | **str**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

