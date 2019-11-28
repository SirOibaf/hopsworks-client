# swagger_client.TrainingDatasetServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_training_dataset**](TrainingDatasetServiceApi.md#create_training_dataset) | **POST** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets | Create training dataset for a featurestore
[**delete_training_dataset**](TrainingDatasetServiceApi.md#delete_training_dataset) | **DELETE** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid} | Delete a training datasets with a specific id from a featurestore
[**get_training_dataset_with_id**](TrainingDatasetServiceApi.md#get_training_dataset_with_id) | **GET** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid} | Get a training datasets with a specific id from a featurestore
[**get_training_datasets_for_featurestore**](TrainingDatasetServiceApi.md#get_training_datasets_for_featurestore) | **GET** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets | Get the list of training datasets for a featurestore
[**update_training_dataset**](TrainingDatasetServiceApi.md#update_training_dataset) | **PUT** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid} | Update a training datasets with a specific id from a featurestore

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
api_instance = swagger_client.TrainingDatasetServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.TrainingDatasetDTO() # TrainingDatasetDTO |  (optional)

try:
    # Create training dataset for a featurestore
    api_response = api_instance.create_training_dataset(featurestore_id, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrainingDatasetServiceApi->create_training_dataset: %s\n" % e)
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
api_instance = swagger_client.TrainingDatasetServiceApi()
trainingdatasetid = 56 # int | Id of the training dataset
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Delete a training datasets with a specific id from a featurestore
    api_response = api_instance.delete_training_dataset(trainingdatasetid, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrainingDatasetServiceApi->delete_training_dataset: %s\n" % e)
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
api_instance = swagger_client.TrainingDatasetServiceApi()
trainingdatasetid = 56 # int | Id of the training dataset
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get a training datasets with a specific id from a featurestore
    api_response = api_instance.get_training_dataset_with_id(trainingdatasetid, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrainingDatasetServiceApi->get_training_dataset_with_id: %s\n" % e)
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
api_instance = swagger_client.TrainingDatasetServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get the list of training datasets for a featurestore
    api_response = api_instance.get_training_datasets_for_featurestore(featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrainingDatasetServiceApi->get_training_datasets_for_featurestore: %s\n" % e)
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
api_instance = swagger_client.TrainingDatasetServiceApi()
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
    print("Exception when calling TrainingDatasetServiceApi->update_training_dataset: %s\n" % e)
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

