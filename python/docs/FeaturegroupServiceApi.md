# swagger_client.FeaturegroupServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_featuregroup**](FeaturegroupServiceApi.md#create_featuregroup) | **POST** /project/{projectId}/featurestores/{featurestoreId}/featuregroups | Create feature group in a featurestore
[**delete_feature_group_from_feature_store**](FeaturegroupServiceApi.md#delete_feature_group_from_feature_store) | **DELETE** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId} | Delete specific featuregroup from a specific featurestore
[**delete_featuregroup_contents**](FeaturegroupServiceApi.md#delete_featuregroup_contents) | **POST** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId}/clear | Delete featuregroup contents
[**get_feature_group_from_feature_store**](FeaturegroupServiceApi.md#get_feature_group_from_feature_store) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId} | Get specific featuregroup from a specific featurestore
[**get_feature_group_preview**](FeaturegroupServiceApi.md#get_feature_group_preview) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId}/preview | Preview feature data of a featuregroup
[**get_feature_group_schema**](FeaturegroupServiceApi.md#get_feature_group_schema) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId}/schema | Get the SQL schema of a featuregroup
[**get_featuregroups_for_featurestore**](FeaturegroupServiceApi.md#get_featuregroups_for_featurestore) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups | Get the list of feature groups for a featurestore
[**sync_with_featurestore**](FeaturegroupServiceApi.md#sync_with_featurestore) | **POST** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/sync | Synchornize Hive Table with the feature store
[**update_featuregroup**](FeaturegroupServiceApi.md#update_featuregroup) | **PUT** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId} | Update featuregroup contents

# **create_featuregroup**
> FeaturegroupDTO create_featuregroup(featurestore_id, project_id, body=body)

Create feature group in a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturegroupServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.FeaturegroupDTO() # FeaturegroupDTO |  (optional)

try:
    # Create feature group in a featurestore
    api_response = api_instance.create_featuregroup(featurestore_id, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturegroupServiceApi->create_featuregroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**FeaturegroupDTO**](FeaturegroupDTO.md)|  | [optional] 

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feature_group_from_feature_store**
> FeaturegroupDTO delete_feature_group_from_feature_store(featuregroup_id, featurestore_id, project_id)

Delete specific featuregroup from a specific featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturegroupServiceApi()
featuregroup_id = 56 # int | Id of the featuregroup
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Delete specific featuregroup from a specific featurestore
    api_response = api_instance.delete_feature_group_from_feature_store(featuregroup_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturegroupServiceApi->delete_feature_group_from_feature_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**| Id of the featuregroup | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_featuregroup_contents**
> FeaturegroupDTO delete_featuregroup_contents(featuregroup_id, featurestore_id, project_id)

Delete featuregroup contents

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturegroupServiceApi()
featuregroup_id = 56 # int | Id of the featuregroup
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Delete featuregroup contents
    api_response = api_instance.delete_featuregroup_contents(featuregroup_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturegroupServiceApi->delete_featuregroup_contents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**| Id of the featuregroup | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_group_from_feature_store**
> FeaturegroupDTO get_feature_group_from_feature_store(featuregroup_id, featurestore_id, project_id)

Get specific featuregroup from a specific featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturegroupServiceApi()
featuregroup_id = 56 # int | Id of the featuregroup
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get specific featuregroup from a specific featurestore
    api_response = api_instance.get_feature_group_from_feature_store(featuregroup_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturegroupServiceApi->get_feature_group_from_feature_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**| Id of the featuregroup | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_group_preview**
> list[FeaturegroupPreview] get_feature_group_preview(featuregroup_id, featurestore_id, project_id)

Preview feature data of a featuregroup

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturegroupServiceApi()
featuregroup_id = 56 # int | Id of the featuregroup
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Preview feature data of a featuregroup
    api_response = api_instance.get_feature_group_preview(featuregroup_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturegroupServiceApi->get_feature_group_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**| Id of the featuregroup | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**list[FeaturegroupPreview]**](FeaturegroupPreview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_group_schema**
> RowValueQueryResult get_feature_group_schema(featuregroup_id, featurestore_id, project_id)

Get the SQL schema of a featuregroup

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturegroupServiceApi()
featuregroup_id = 56 # int | Id of the featuregroup
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get the SQL schema of a featuregroup
    api_response = api_instance.get_feature_group_schema(featuregroup_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturegroupServiceApi->get_feature_group_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**| Id of the featuregroup | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**RowValueQueryResult**](RowValueQueryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_featuregroups_for_featurestore**
> list[FeaturegroupDTO] get_featuregroups_for_featurestore(featurestore_id, project_id)

Get the list of feature groups for a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturegroupServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get the list of feature groups for a featurestore
    api_response = api_instance.get_featuregroups_for_featurestore(featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturegroupServiceApi->get_featuregroups_for_featurestore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**list[FeaturegroupDTO]**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_with_featurestore**
> FeaturegroupDTO sync_with_featurestore(featurestore_id, project_id, body=body)

Synchornize Hive Table with the feature store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturegroupServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.FeaturegroupDTO() # FeaturegroupDTO |  (optional)

try:
    # Synchornize Hive Table with the feature store
    api_response = api_instance.sync_with_featurestore(featurestore_id, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturegroupServiceApi->sync_with_featurestore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**FeaturegroupDTO**](FeaturegroupDTO.md)|  | [optional] 

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_featuregroup**
> FeaturegroupDTO update_featuregroup(featuregroup_id, featurestore_id, project_id, body=body, update_metadata=update_metadata, update_stats=update_stats, enable_online=enable_online, disable_online=disable_online, update_stats_settings=update_stats_settings)

Update featuregroup contents

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturegroupServiceApi()
featuregroup_id = 56 # int | Id of the featuregroup
featurestore_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.FeaturegroupDTO() # FeaturegroupDTO |  (optional)
update_metadata = true # bool | updateMetadata (optional)
update_stats = true # bool | updateStats (optional)
enable_online = true # bool | enableOnline (optional)
disable_online = true # bool | disableOnline (optional)
update_stats_settings = true # bool | updateStatsSettings (optional)

try:
    # Update featuregroup contents
    api_response = api_instance.update_featuregroup(featuregroup_id, featurestore_id, project_id, body=body, update_metadata=update_metadata, update_stats=update_stats, enable_online=enable_online, disable_online=disable_online, update_stats_settings=update_stats_settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturegroupServiceApi->update_featuregroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**| Id of the featuregroup | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**FeaturegroupDTO**](FeaturegroupDTO.md)|  | [optional] 
 **update_metadata** | **bool**| updateMetadata | [optional] 
 **update_stats** | **bool**| updateStats | [optional] 
 **enable_online** | **bool**| enableOnline | [optional] 
 **disable_online** | **bool**| disableOnline | [optional] 
 **update_stats_settings** | **bool**| updateStatsSettings | [optional] 

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

