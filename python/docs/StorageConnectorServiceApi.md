# swagger_client.StorageConnectorServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_storage_connector_with_type**](StorageConnectorServiceApi.md#create_new_storage_connector_with_type) | **POST** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType} | Create a new storage connector for the feature store
[**delete_storage_connector_with_type_and_id**](StorageConnectorServiceApi.md#delete_storage_connector_with_type_and_id) | **DELETE** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType}/{connectorId} | Delete storage connector with a specific id and type from a featurestore
[**get_online_featurestore_storage_connector**](StorageConnectorServiceApi.md#get_online_featurestore_storage_connector) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/onlinefeaturestore | Get online featurestore storage connector for this feature store
[**get_storage_connector_with_id**](StorageConnectorServiceApi.md#get_storage_connector_with_id) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType}/{connectorId} | Get a storage connector with a specific id and type from a featurestore
[**get_storage_connectors**](StorageConnectorServiceApi.md#get_storage_connectors) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors | Get all storage connectors of a feature store
[**get_storage_connectors_of_type**](StorageConnectorServiceApi.md#get_storage_connectors_of_type) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType} | Get all storage connectors of a specific type of a feature store
[**update_storage_connector_with_id**](StorageConnectorServiceApi.md#update_storage_connector_with_id) | **PUT** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType}/{connectorId} | Get a storage connector with a specific id and type from a featurestore

# **create_new_storage_connector_with_type**
> FeaturestoreStorageConnectorDTO create_new_storage_connector_with_type(connector_type, featurestore_id, project_id, body=body)

Create a new storage connector for the feature store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageConnectorServiceApi()
connector_type = 'connector_type_example' # str | storage connector type
featurestore_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.FeaturestoreStorageConnectorDTO() # FeaturestoreStorageConnectorDTO |  (optional)

try:
    # Create a new storage connector for the feature store
    api_response = api_instance.create_new_storage_connector_with_type(connector_type, featurestore_id, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageConnectorServiceApi->create_new_storage_connector_with_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_type** | **str**| storage connector type | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)|  | [optional] 

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storage_connector_with_type_and_id**
> FeaturestoreStorageConnectorDTO delete_storage_connector_with_type_and_id(connector_type, connector_id, featurestore_id, project_id)

Delete storage connector with a specific id and type from a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageConnectorServiceApi()
connector_type = 'connector_type_example' # str | storage connector type
connector_id = 56 # int | Id of the storage connector
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Delete storage connector with a specific id and type from a featurestore
    api_response = api_instance.delete_storage_connector_with_type_and_id(connector_type, connector_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageConnectorServiceApi->delete_storage_connector_with_type_and_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_type** | **str**| storage connector type | 
 **connector_id** | **int**| Id of the storage connector | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_online_featurestore_storage_connector**
> FeaturestoreStorageConnectorDTO get_online_featurestore_storage_connector(featurestore_id, project_id)

Get online featurestore storage connector for this feature store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageConnectorServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get online featurestore storage connector for this feature store
    api_response = api_instance.get_online_featurestore_storage_connector(featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageConnectorServiceApi->get_online_featurestore_storage_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_connector_with_id**
> FeaturestoreStorageConnectorDTO get_storage_connector_with_id(connector_type, connector_id, featurestore_id, project_id)

Get a storage connector with a specific id and type from a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageConnectorServiceApi()
connector_type = 'connector_type_example' # str | storage connector type
connector_id = 56 # int | Id of the storage connector
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get a storage connector with a specific id and type from a featurestore
    api_response = api_instance.get_storage_connector_with_id(connector_type, connector_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageConnectorServiceApi->get_storage_connector_with_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_type** | **str**| storage connector type | 
 **connector_id** | **int**| Id of the storage connector | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_connectors**
> list[FeaturestoreStorageConnectorDTO] get_storage_connectors(featurestore_id, project_id)

Get all storage connectors of a feature store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageConnectorServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get all storage connectors of a feature store
    api_response = api_instance.get_storage_connectors(featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageConnectorServiceApi->get_storage_connectors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**list[FeaturestoreStorageConnectorDTO]**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_connectors_of_type**
> list[FeaturestoreStorageConnectorDTO] get_storage_connectors_of_type(connector_type, featurestore_id, project_id)

Get all storage connectors of a specific type of a feature store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageConnectorServiceApi()
connector_type = 'connector_type_example' # str | storage connector type
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get all storage connectors of a specific type of a feature store
    api_response = api_instance.get_storage_connectors_of_type(connector_type, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageConnectorServiceApi->get_storage_connectors_of_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_type** | **str**| storage connector type | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**list[FeaturestoreStorageConnectorDTO]**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storage_connector_with_id**
> FeaturestoreStorageConnectorDTO update_storage_connector_with_id(connector_type, connector_id, featurestore_id, project_id, body=body)

Get a storage connector with a specific id and type from a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageConnectorServiceApi()
connector_type = 'connector_type_example' # str | storage connector type
connector_id = 56 # int | Id of the storage connector
featurestore_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.FeaturestoreStorageConnectorDTO() # FeaturestoreStorageConnectorDTO |  (optional)

try:
    # Get a storage connector with a specific id and type from a featurestore
    api_response = api_instance.update_storage_connector_with_id(connector_type, connector_id, featurestore_id, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageConnectorServiceApi->update_storage_connector_with_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_type** | **str**| storage connector type | 
 **connector_id** | **int**| Id of the storage connector | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)|  | [optional] 

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

