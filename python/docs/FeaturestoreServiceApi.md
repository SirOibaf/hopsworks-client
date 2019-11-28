# swagger_client.FeaturestoreServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_validation_rules**](FeaturestoreServiceApi.md#add_validation_rules) | **POST** /project/{projectId}/featurestores/{featureStoreId}/datavalidation/{featuregroupId}/rules | Write Deequ validation rules to Filesystem so validation job can pick it up
[**create_featuregroup**](FeaturestoreServiceApi.md#create_featuregroup) | **POST** /project/{projectId}/featurestores/{featurestoreId}/featuregroups | Create feature group in a featurestore
[**create_new_storage_connector_with_type**](FeaturestoreServiceApi.md#create_new_storage_connector_with_type) | **POST** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType} | Create a new storage connector for the feature store
[**create_or_update_import_job**](FeaturestoreServiceApi.md#create_or_update_import_job) | **PUT** /project/{projectId}/featurestores/importjob | Configure job to import featuregroup
[**create_or_update_training_dataset_job**](FeaturestoreServiceApi.md#create_or_update_training_dataset_job) | **POST** /project/{projectId}/featurestores/trainingdatasetjob | Configure job to create training dataset
[**create_training_dataset**](FeaturestoreServiceApi.md#create_training_dataset) | **POST** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets | Create training dataset for a featurestore
[**delete_feature_group_from_feature_store**](FeaturestoreServiceApi.md#delete_feature_group_from_feature_store) | **DELETE** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId} | Delete specific featuregroup from a specific featurestore
[**delete_featuregroup_contents**](FeaturestoreServiceApi.md#delete_featuregroup_contents) | **POST** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId}/clear | Delete featuregroup contents
[**delete_storage_connector_with_type_and_id**](FeaturestoreServiceApi.md#delete_storage_connector_with_type_and_id) | **DELETE** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType}/{connectorId} | Delete storage connector with a specific id and type from a featurestore
[**delete_training_dataset**](FeaturestoreServiceApi.md#delete_training_dataset) | **DELETE** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid} | Delete a training datasets with a specific id from a featurestore
[**get_feature_group_from_feature_store**](FeaturestoreServiceApi.md#get_feature_group_from_feature_store) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId} | Get specific featuregroup from a specific featurestore
[**get_feature_group_preview**](FeaturestoreServiceApi.md#get_feature_group_preview) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId}/preview | Preview feature data of a featuregroup
[**get_feature_group_schema**](FeaturestoreServiceApi.md#get_feature_group_schema) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId}/schema | Get the SQL schema of a featuregroup
[**get_featuregroups_for_featurestore**](FeaturestoreServiceApi.md#get_featuregroups_for_featurestore) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups | Get the list of feature groups for a featurestore
[**get_featurestore**](FeaturestoreServiceApi.md#get_featurestore) | **GET** /project/{projectId}/featurestores/{featurestoreId} | Get featurestore with specific Id
[**get_featurestore_by_name**](FeaturestoreServiceApi.md#get_featurestore_by_name) | **GET** /project/{projectId}/featurestores/getByName/{featurestoreName} | Get featurestore with specific name
[**get_featurestore_id**](FeaturestoreServiceApi.md#get_featurestore_id) | **GET** /project/{projectId}/featurestores/{featurestoreName}/metadata | Get featurestore Metadata
[**get_featurestore_settings**](FeaturestoreServiceApi.md#get_featurestore_settings) | **GET** /project/{projectId}/featurestores/settings | Get featurestore settings
[**get_featurestores**](FeaturestoreServiceApi.md#get_featurestores) | **GET** /project/{projectId}/featurestores | Get the list of feature stores for the project
[**get_online_featurestore_storage_connector**](FeaturestoreServiceApi.md#get_online_featurestore_storage_connector) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/onlinefeaturestore | Get online featurestore storage connector for this feature store
[**get_storage_connector_with_id**](FeaturestoreServiceApi.md#get_storage_connector_with_id) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType}/{connectorId} | Get a storage connector with a specific id and type from a featurestore
[**get_storage_connectors**](FeaturestoreServiceApi.md#get_storage_connectors) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors | Get all storage connectors of a feature store
[**get_storage_connectors_of_type**](FeaturestoreServiceApi.md#get_storage_connectors_of_type) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType} | Get all storage connectors of a specific type of a feature store
[**get_training_dataset_with_id**](FeaturestoreServiceApi.md#get_training_dataset_with_id) | **GET** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid} | Get a training datasets with a specific id from a featurestore
[**get_training_datasets_for_featurestore**](FeaturestoreServiceApi.md#get_training_datasets_for_featurestore) | **GET** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets | Get the list of training datasets for a featurestore
[**get_validation_result**](FeaturestoreServiceApi.md#get_validation_result) | **GET** /project/{projectId}/featurestores/{featureStoreId}/datavalidation/{featuregroupId}/result | Fetch the result of a Deequ data validation job
[**get_validation_rules**](FeaturestoreServiceApi.md#get_validation_rules) | **GET** /project/{projectId}/featurestores/{featureStoreId}/datavalidation/{featuregroupId}/rules | Get previously stored Deequ validation rules
[**new_featurestore_util**](FeaturestoreServiceApi.md#new_featurestore_util) | **POST** /project/{projectId}/featurestores/util | Upload json input for featurestore-util jobs
[**sync_with_featurestore**](FeaturestoreServiceApi.md#sync_with_featurestore) | **POST** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/sync | Synchornize Hive Table with the feature store
[**update_featuregroup**](FeaturestoreServiceApi.md#update_featuregroup) | **PUT** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId} | Update featuregroup contents
[**update_storage_connector_with_id**](FeaturestoreServiceApi.md#update_storage_connector_with_id) | **PUT** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType}/{connectorId} | Get a storage connector with a specific id and type from a featurestore
[**update_training_dataset**](FeaturestoreServiceApi.md#update_training_dataset) | **PUT** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid} | Update a training datasets with a specific id from a featurestore

# **add_validation_rules**
> DataValidationSettingsDTO add_validation_rules(featuregroup_id, feature_store_id, project_id, body=body)

Write Deequ validation rules to Filesystem so validation job can pick it up

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturestoreServiceApi()
featuregroup_id = 56 # int | 
feature_store_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.ConstraintGroupDTO() # ConstraintGroupDTO |  (optional)

try:
    # Write Deequ validation rules to Filesystem so validation job can pick it up
    api_response = api_instance.add_validation_rules(featuregroup_id, feature_store_id, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->add_validation_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**|  | 
 **feature_store_id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**ConstraintGroupDTO**](ConstraintGroupDTO.md)|  | [optional] 

### Return type

[**DataValidationSettingsDTO**](DataValidationSettingsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = swagger_client.FeaturestoreServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.FeaturegroupDTO() # FeaturegroupDTO |  (optional)

try:
    # Create feature group in a featurestore
    api_response = api_instance.create_featuregroup(featurestore_id, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->create_featuregroup: %s\n" % e)
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
api_instance = swagger_client.FeaturestoreServiceApi()
connector_type = 'connector_type_example' # str | storage connector type
featurestore_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.FeaturestoreStorageConnectorDTO() # FeaturestoreStorageConnectorDTO |  (optional)

try:
    # Create a new storage connector for the feature store
    api_response = api_instance.create_new_storage_connector_with_type(connector_type, featurestore_id, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->create_new_storage_connector_with_type: %s\n" % e)
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

# **create_or_update_import_job**
> JobDTO create_or_update_import_job(body, project_id)

Configure job to import featuregroup

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturestoreServiceApi()
body = swagger_client.FeaturegroupImportJobDTO() # FeaturegroupImportJobDTO | Job configuration
project_id = 56 # int | 

try:
    # Configure job to import featuregroup
    api_response = api_instance.create_or_update_import_job(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->create_or_update_import_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeaturegroupImportJobDTO**](FeaturegroupImportJobDTO.md)| Job configuration | 
 **project_id** | **int**|  | 

### Return type

[**JobDTO**](JobDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_training_dataset_job**
> JobDTO create_or_update_training_dataset_job(body, project_id)

Configure job to create training dataset

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturestoreServiceApi()
body = swagger_client.TrainingDatasetJobDTO() # TrainingDatasetJobDTO | Job configuration
project_id = 56 # int | 

try:
    # Configure job to create training dataset
    api_response = api_instance.create_or_update_training_dataset_job(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->create_or_update_training_dataset_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrainingDatasetJobDTO**](TrainingDatasetJobDTO.md)| Job configuration | 
 **project_id** | **int**|  | 

### Return type

[**JobDTO**](JobDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_training_dataset**
> TrainingDatasetDTO create_training_dataset(featurestore_id, project_id, body=body)

Create training dataset for a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturestoreServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.TrainingDatasetDTO() # TrainingDatasetDTO |  (optional)

try:
    # Create training dataset for a featurestore
    api_response = api_instance.create_training_dataset(featurestore_id, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->create_training_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**TrainingDatasetDTO**](TrainingDatasetDTO.md)|  | [optional] 

### Return type

[**TrainingDatasetDTO**](TrainingDatasetDTO.md)

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
api_instance = swagger_client.FeaturestoreServiceApi()
featuregroup_id = 56 # int | Id of the featuregroup
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Delete specific featuregroup from a specific featurestore
    api_response = api_instance.delete_feature_group_from_feature_store(featuregroup_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->delete_feature_group_from_feature_store: %s\n" % e)
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
api_instance = swagger_client.FeaturestoreServiceApi()
featuregroup_id = 56 # int | Id of the featuregroup
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Delete featuregroup contents
    api_response = api_instance.delete_featuregroup_contents(featuregroup_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->delete_featuregroup_contents: %s\n" % e)
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
api_instance = swagger_client.FeaturestoreServiceApi()
connector_type = 'connector_type_example' # str | storage connector type
connector_id = 56 # int | Id of the storage connector
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Delete storage connector with a specific id and type from a featurestore
    api_response = api_instance.delete_storage_connector_with_type_and_id(connector_type, connector_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->delete_storage_connector_with_type_and_id: %s\n" % e)
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

# **delete_training_dataset**
> TrainingDatasetDTO delete_training_dataset(trainingdatasetid, featurestore_id, project_id)

Delete a training datasets with a specific id from a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturestoreServiceApi()
trainingdatasetid = 56 # int | Id of the training dataset
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Delete a training datasets with a specific id from a featurestore
    api_response = api_instance.delete_training_dataset(trainingdatasetid, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->delete_training_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trainingdatasetid** | **int**| Id of the training dataset | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**TrainingDatasetDTO**](TrainingDatasetDTO.md)

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
api_instance = swagger_client.FeaturestoreServiceApi()
featuregroup_id = 56 # int | Id of the featuregroup
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get specific featuregroup from a specific featurestore
    api_response = api_instance.get_feature_group_from_feature_store(featuregroup_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->get_feature_group_from_feature_store: %s\n" % e)
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
api_instance = swagger_client.FeaturestoreServiceApi()
featuregroup_id = 56 # int | Id of the featuregroup
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Preview feature data of a featuregroup
    api_response = api_instance.get_feature_group_preview(featuregroup_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->get_feature_group_preview: %s\n" % e)
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
api_instance = swagger_client.FeaturestoreServiceApi()
featuregroup_id = 56 # int | Id of the featuregroup
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get the SQL schema of a featuregroup
    api_response = api_instance.get_feature_group_schema(featuregroup_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->get_feature_group_schema: %s\n" % e)
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
api_instance = swagger_client.FeaturestoreServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get the list of feature groups for a featurestore
    api_response = api_instance.get_featuregroups_for_featurestore(featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->get_featuregroups_for_featurestore: %s\n" % e)
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

# **get_featurestore**
> FeaturestoreDTO get_featurestore(featurestore_id, project_id)

Get featurestore with specific Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturestoreServiceApi()
featurestore_id = 56 # int | Id of the featurestore
project_id = 56 # int | 

try:
    # Get featurestore with specific Id
    api_response = api_instance.get_featurestore(featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->get_featurestore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_id** | **int**| Id of the featurestore | 
 **project_id** | **int**|  | 

### Return type

[**FeaturestoreDTO**](FeaturestoreDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_featurestore_by_name**
> FeaturestoreDTO get_featurestore_by_name(featurestore_name, project_id)

Get featurestore with specific name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturestoreServiceApi()
featurestore_name = 'featurestore_name_example' # str | Id of the featurestore
project_id = 56 # int | 

try:
    # Get featurestore with specific name
    api_response = api_instance.get_featurestore_by_name(featurestore_name, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->get_featurestore_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_name** | **str**| Id of the featurestore | 
 **project_id** | **int**|  | 

### Return type

[**FeaturestoreDTO**](FeaturestoreDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_featurestore_id**
> FeaturestoreClientSettingsDTO get_featurestore_id(featurestore_name, project_id)

Get featurestore Metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturestoreServiceApi()
featurestore_name = 'featurestore_name_example' # str | 
project_id = 56 # int | 

try:
    # Get featurestore Metadata
    api_response = api_instance.get_featurestore_id(featurestore_name, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->get_featurestore_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_name** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

[**FeaturestoreClientSettingsDTO**](FeaturestoreClientSettingsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_featurestore_settings**
> FeaturestoreClientSettingsDTO get_featurestore_settings(project_id)

Get featurestore settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturestoreServiceApi()
project_id = 56 # int | 

try:
    # Get featurestore settings
    api_response = api_instance.get_featurestore_settings(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->get_featurestore_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**FeaturestoreClientSettingsDTO**](FeaturestoreClientSettingsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_featurestores**
> list[FeaturestoreDTO] get_featurestores(project_id)

Get the list of feature stores for the project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturestoreServiceApi()
project_id = 56 # int | 

try:
    # Get the list of feature stores for the project
    api_response = api_instance.get_featurestores(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->get_featurestores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**list[FeaturestoreDTO]**](FeaturestoreDTO.md)

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
api_instance = swagger_client.FeaturestoreServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get online featurestore storage connector for this feature store
    api_response = api_instance.get_online_featurestore_storage_connector(featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->get_online_featurestore_storage_connector: %s\n" % e)
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
api_instance = swagger_client.FeaturestoreServiceApi()
connector_type = 'connector_type_example' # str | storage connector type
connector_id = 56 # int | Id of the storage connector
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get a storage connector with a specific id and type from a featurestore
    api_response = api_instance.get_storage_connector_with_id(connector_type, connector_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->get_storage_connector_with_id: %s\n" % e)
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
api_instance = swagger_client.FeaturestoreServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get all storage connectors of a feature store
    api_response = api_instance.get_storage_connectors(featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->get_storage_connectors: %s\n" % e)
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
api_instance = swagger_client.FeaturestoreServiceApi()
connector_type = 'connector_type_example' # str | storage connector type
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get all storage connectors of a specific type of a feature store
    api_response = api_instance.get_storage_connectors_of_type(connector_type, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->get_storage_connectors_of_type: %s\n" % e)
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

# **get_training_dataset_with_id**
> TrainingDatasetDTO get_training_dataset_with_id(trainingdatasetid, featurestore_id, project_id)

Get a training datasets with a specific id from a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturestoreServiceApi()
trainingdatasetid = 56 # int | Id of the training dataset
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get a training datasets with a specific id from a featurestore
    api_response = api_instance.get_training_dataset_with_id(trainingdatasetid, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->get_training_dataset_with_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trainingdatasetid** | **int**| Id of the training dataset | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**TrainingDatasetDTO**](TrainingDatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_training_datasets_for_featurestore**
> list[TrainingDatasetDTO] get_training_datasets_for_featurestore(featurestore_id, project_id)

Get the list of training datasets for a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturestoreServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get the list of training datasets for a featurestore
    api_response = api_instance.get_training_datasets_for_featurestore(featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->get_training_datasets_for_featurestore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**list[TrainingDatasetDTO]**](TrainingDatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validation_result**
> ValidationResult get_validation_result(featuregroup_id, feature_store_id, project_id)

Fetch the result of a Deequ data validation job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturestoreServiceApi()
featuregroup_id = 56 # int | 
feature_store_id = 56 # int | 
project_id = 56 # int | 

try:
    # Fetch the result of a Deequ data validation job
    api_response = api_instance.get_validation_result(featuregroup_id, feature_store_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->get_validation_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**|  | 
 **feature_store_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validation_rules**
> ConstraintGroupDTO get_validation_rules(featuregroup_id, feature_store_id, project_id)

Get previously stored Deequ validation rules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturestoreServiceApi()
featuregroup_id = 56 # int | 
feature_store_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get previously stored Deequ validation rules
    api_response = api_instance.get_validation_rules(featuregroup_id, feature_store_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->get_validation_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**|  | 
 **feature_store_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**ConstraintGroupDTO**](ConstraintGroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_featurestore_util**
> new_featurestore_util(project_id, body=body)

Upload json input for featurestore-util jobs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturestoreServiceApi()
project_id = 56 # int | 
body = swagger_client.FeaturestoreUtilJobDTO() # FeaturestoreUtilJobDTO |  (optional)

try:
    # Upload json input for featurestore-util jobs
    api_instance.new_featurestore_util(project_id, body=body)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->new_featurestore_util: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**FeaturestoreUtilJobDTO**](FeaturestoreUtilJobDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

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
api_instance = swagger_client.FeaturestoreServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.FeaturegroupDTO() # FeaturegroupDTO |  (optional)

try:
    # Synchornize Hive Table with the feature store
    api_response = api_instance.sync_with_featurestore(featurestore_id, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->sync_with_featurestore: %s\n" % e)
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
api_instance = swagger_client.FeaturestoreServiceApi()
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
    print("Exception when calling FeaturestoreServiceApi->update_featuregroup: %s\n" % e)
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
api_instance = swagger_client.FeaturestoreServiceApi()
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
    print("Exception when calling FeaturestoreServiceApi->update_storage_connector_with_id: %s\n" % e)
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

# **update_training_dataset**
> TrainingDatasetDTO update_training_dataset(trainingdatasetid, featurestore_id, project_id, body=body, update_metadata=update_metadata, update_stats=update_stats)

Update a training datasets with a specific id from a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturestoreServiceApi()
trainingdatasetid = 56 # int | Id of the training dataset
featurestore_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.TrainingDatasetDTO() # TrainingDatasetDTO |  (optional)
update_metadata = true # bool | updateMetadata (optional)
update_stats = true # bool | updateStats (optional)

try:
    # Update a training datasets with a specific id from a featurestore
    api_response = api_instance.update_training_dataset(trainingdatasetid, featurestore_id, project_id, body=body, update_metadata=update_metadata, update_stats=update_stats)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturestoreServiceApi->update_training_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trainingdatasetid** | **int**| Id of the training dataset | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**TrainingDatasetDTO**](TrainingDatasetDTO.md)|  | [optional] 
 **update_metadata** | **bool**| updateMetadata | [optional] 
 **update_stats** | **bool**| updateStats | [optional] 

### Return type

[**TrainingDatasetDTO**](TrainingDatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

