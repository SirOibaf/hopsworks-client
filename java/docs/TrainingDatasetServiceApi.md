# TrainingDatasetServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTrainingDataset**](TrainingDatasetServiceApi.md#createTrainingDataset) | **POST** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets | Create training dataset for a featurestore
[**deleteTrainingDataset**](TrainingDatasetServiceApi.md#deleteTrainingDataset) | **DELETE** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid} | Delete a training datasets with a specific id from a featurestore
[**getTrainingDatasetWithId**](TrainingDatasetServiceApi.md#getTrainingDatasetWithId) | **GET** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid} | Get a training datasets with a specific id from a featurestore
[**getTrainingDatasetsForFeaturestore**](TrainingDatasetServiceApi.md#getTrainingDatasetsForFeaturestore) | **GET** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets | Get the list of training datasets for a featurestore
[**updateTrainingDataset**](TrainingDatasetServiceApi.md#updateTrainingDataset) | **PUT** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid} | Update a training datasets with a specific id from a featurestore

<a name="createTrainingDataset"></a>
# **createTrainingDataset**
> TrainingDatasetDTO createTrainingDataset(featurestoreId, projectId, body)

Create training dataset for a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.TrainingDatasetServiceApi;


TrainingDatasetServiceApi apiInstance = new TrainingDatasetServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
TrainingDatasetDTO body = new TrainingDatasetDTO(); // TrainingDatasetDTO | 
try {
    TrainingDatasetDTO result = apiInstance.createTrainingDataset(featurestoreId, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TrainingDatasetServiceApi#createTrainingDataset");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **body** | [**TrainingDatasetDTO**](TrainingDatasetDTO.md)|  | [optional]

### Return type

[**TrainingDatasetDTO**](TrainingDatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deleteTrainingDataset"></a>
# **deleteTrainingDataset**
> TrainingDatasetDTO deleteTrainingDataset(trainingdatasetid, featurestoreId, projectId)

Delete a training datasets with a specific id from a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.TrainingDatasetServiceApi;


TrainingDatasetServiceApi apiInstance = new TrainingDatasetServiceApi();
Integer trainingdatasetid = 56; // Integer | Id of the training dataset
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    TrainingDatasetDTO result = apiInstance.deleteTrainingDataset(trainingdatasetid, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TrainingDatasetServiceApi#deleteTrainingDataset");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trainingdatasetid** | **Integer**| Id of the training dataset |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**TrainingDatasetDTO**](TrainingDatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getTrainingDatasetWithId"></a>
# **getTrainingDatasetWithId**
> TrainingDatasetDTO getTrainingDatasetWithId(trainingdatasetid, featurestoreId, projectId)

Get a training datasets with a specific id from a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.TrainingDatasetServiceApi;


TrainingDatasetServiceApi apiInstance = new TrainingDatasetServiceApi();
Integer trainingdatasetid = 56; // Integer | Id of the training dataset
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    TrainingDatasetDTO result = apiInstance.getTrainingDatasetWithId(trainingdatasetid, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TrainingDatasetServiceApi#getTrainingDatasetWithId");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trainingdatasetid** | **Integer**| Id of the training dataset |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**TrainingDatasetDTO**](TrainingDatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getTrainingDatasetsForFeaturestore"></a>
# **getTrainingDatasetsForFeaturestore**
> List&lt;TrainingDatasetDTO&gt; getTrainingDatasetsForFeaturestore(featurestoreId, projectId)

Get the list of training datasets for a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.TrainingDatasetServiceApi;


TrainingDatasetServiceApi apiInstance = new TrainingDatasetServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    List<TrainingDatasetDTO> result = apiInstance.getTrainingDatasetsForFeaturestore(featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TrainingDatasetServiceApi#getTrainingDatasetsForFeaturestore");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**List&lt;TrainingDatasetDTO&gt;**](TrainingDatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="updateTrainingDataset"></a>
# **updateTrainingDataset**
> TrainingDatasetDTO updateTrainingDataset(trainingdatasetid, featurestoreId, projectId, body, updateMetadata, updateStats)

Update a training datasets with a specific id from a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.TrainingDatasetServiceApi;


TrainingDatasetServiceApi apiInstance = new TrainingDatasetServiceApi();
Integer trainingdatasetid = 56; // Integer | Id of the training dataset
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
TrainingDatasetDTO body = new TrainingDatasetDTO(); // TrainingDatasetDTO | 
Boolean updateMetadata = true; // Boolean | updateMetadata
Boolean updateStats = true; // Boolean | updateStats
try {
    TrainingDatasetDTO result = apiInstance.updateTrainingDataset(trainingdatasetid, featurestoreId, projectId, body, updateMetadata, updateStats);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TrainingDatasetServiceApi#updateTrainingDataset");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trainingdatasetid** | **Integer**| Id of the training dataset |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **body** | [**TrainingDatasetDTO**](TrainingDatasetDTO.md)|  | [optional]
 **updateMetadata** | **Boolean**| updateMetadata | [optional]
 **updateStats** | **Boolean**| updateStats | [optional]

### Return type

[**TrainingDatasetDTO**](TrainingDatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

