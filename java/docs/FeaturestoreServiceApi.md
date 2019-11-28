# FeaturestoreServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addValidationRules**](FeaturestoreServiceApi.md#addValidationRules) | **POST** /project/{projectId}/featurestores/{featureStoreId}/datavalidation/{featuregroupId}/rules | Write Deequ validation rules to Filesystem so validation job can pick it up
[**createFeaturegroup**](FeaturestoreServiceApi.md#createFeaturegroup) | **POST** /project/{projectId}/featurestores/{featurestoreId}/featuregroups | Create feature group in a featurestore
[**createNewStorageConnectorWithType**](FeaturestoreServiceApi.md#createNewStorageConnectorWithType) | **POST** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType} | Create a new storage connector for the feature store
[**createOrUpdateImportJob**](FeaturestoreServiceApi.md#createOrUpdateImportJob) | **PUT** /project/{projectId}/featurestores/importjob | Configure job to import featuregroup
[**createOrUpdateTrainingDatasetJob**](FeaturestoreServiceApi.md#createOrUpdateTrainingDatasetJob) | **POST** /project/{projectId}/featurestores/trainingdatasetjob | Configure job to create training dataset
[**createTrainingDataset**](FeaturestoreServiceApi.md#createTrainingDataset) | **POST** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets | Create training dataset for a featurestore
[**deleteFeatureGroupFromFeatureStore**](FeaturestoreServiceApi.md#deleteFeatureGroupFromFeatureStore) | **DELETE** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId} | Delete specific featuregroup from a specific featurestore
[**deleteFeaturegroupContents**](FeaturestoreServiceApi.md#deleteFeaturegroupContents) | **POST** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId}/clear | Delete featuregroup contents
[**deleteStorageConnectorWithTypeAndId**](FeaturestoreServiceApi.md#deleteStorageConnectorWithTypeAndId) | **DELETE** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType}/{connectorId} | Delete storage connector with a specific id and type from a featurestore
[**deleteTrainingDataset**](FeaturestoreServiceApi.md#deleteTrainingDataset) | **DELETE** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid} | Delete a training datasets with a specific id from a featurestore
[**getFeatureGroupFromFeatureStore**](FeaturestoreServiceApi.md#getFeatureGroupFromFeatureStore) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId} | Get specific featuregroup from a specific featurestore
[**getFeatureGroupPreview**](FeaturestoreServiceApi.md#getFeatureGroupPreview) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId}/preview | Preview feature data of a featuregroup
[**getFeatureGroupSchema**](FeaturestoreServiceApi.md#getFeatureGroupSchema) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId}/schema | Get the SQL schema of a featuregroup
[**getFeaturegroupsForFeaturestore**](FeaturestoreServiceApi.md#getFeaturegroupsForFeaturestore) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups | Get the list of feature groups for a featurestore
[**getFeaturestore**](FeaturestoreServiceApi.md#getFeaturestore) | **GET** /project/{projectId}/featurestores/{featurestoreId} | Get featurestore with specific Id
[**getFeaturestoreByName**](FeaturestoreServiceApi.md#getFeaturestoreByName) | **GET** /project/{projectId}/featurestores/getByName/{featurestoreName} | Get featurestore with specific name
[**getFeaturestoreId**](FeaturestoreServiceApi.md#getFeaturestoreId) | **GET** /project/{projectId}/featurestores/{featurestoreName}/metadata | Get featurestore Metadata
[**getFeaturestoreSettings**](FeaturestoreServiceApi.md#getFeaturestoreSettings) | **GET** /project/{projectId}/featurestores/settings | Get featurestore settings
[**getFeaturestores**](FeaturestoreServiceApi.md#getFeaturestores) | **GET** /project/{projectId}/featurestores | Get the list of feature stores for the project
[**getOnlineFeaturestoreStorageConnector**](FeaturestoreServiceApi.md#getOnlineFeaturestoreStorageConnector) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/onlinefeaturestore | Get online featurestore storage connector for this feature store
[**getStorageConnectorWithId**](FeaturestoreServiceApi.md#getStorageConnectorWithId) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType}/{connectorId} | Get a storage connector with a specific id and type from a featurestore
[**getStorageConnectors**](FeaturestoreServiceApi.md#getStorageConnectors) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors | Get all storage connectors of a feature store
[**getStorageConnectorsOfType**](FeaturestoreServiceApi.md#getStorageConnectorsOfType) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType} | Get all storage connectors of a specific type of a feature store
[**getTrainingDatasetWithId**](FeaturestoreServiceApi.md#getTrainingDatasetWithId) | **GET** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid} | Get a training datasets with a specific id from a featurestore
[**getTrainingDatasetsForFeaturestore**](FeaturestoreServiceApi.md#getTrainingDatasetsForFeaturestore) | **GET** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets | Get the list of training datasets for a featurestore
[**getValidationResult**](FeaturestoreServiceApi.md#getValidationResult) | **GET** /project/{projectId}/featurestores/{featureStoreId}/datavalidation/{featuregroupId}/result | Fetch the result of a Deequ data validation job
[**getValidationRules**](FeaturestoreServiceApi.md#getValidationRules) | **GET** /project/{projectId}/featurestores/{featureStoreId}/datavalidation/{featuregroupId}/rules | Get previously stored Deequ validation rules
[**newFeaturestoreUtil**](FeaturestoreServiceApi.md#newFeaturestoreUtil) | **POST** /project/{projectId}/featurestores/util | Upload json input for featurestore-util jobs
[**syncWithFeaturestore**](FeaturestoreServiceApi.md#syncWithFeaturestore) | **POST** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/sync | Synchornize Hive Table with the feature store
[**updateFeaturegroup**](FeaturestoreServiceApi.md#updateFeaturegroup) | **PUT** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId} | Update featuregroup contents
[**updateStorageConnectorWithId**](FeaturestoreServiceApi.md#updateStorageConnectorWithId) | **PUT** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType}/{connectorId} | Get a storage connector with a specific id and type from a featurestore
[**updateTrainingDataset**](FeaturestoreServiceApi.md#updateTrainingDataset) | **PUT** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid} | Update a training datasets with a specific id from a featurestore

<a name="addValidationRules"></a>
# **addValidationRules**
> DataValidationSettingsDTO addValidationRules(featuregroupId, featureStoreId, projectId, body)

Write Deequ validation rules to Filesystem so validation job can pick it up

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer featuregroupId = 56; // Integer | 
Integer featureStoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
ConstraintGroupDTO body = new ConstraintGroupDTO(); // ConstraintGroupDTO | 
try {
    DataValidationSettingsDTO result = apiInstance.addValidationRules(featuregroupId, featureStoreId, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#addValidationRules");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**|  |
 **featureStoreId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **body** | [**ConstraintGroupDTO**](ConstraintGroupDTO.md)|  | [optional]

### Return type

[**DataValidationSettingsDTO**](DataValidationSettingsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

<a name="createFeaturegroup"></a>
# **createFeaturegroup**
> FeaturegroupDTO createFeaturegroup(featurestoreId, projectId, body)

Create feature group in a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
FeaturegroupDTO body = new FeaturegroupDTO(); // FeaturegroupDTO | 
try {
    FeaturegroupDTO result = apiInstance.createFeaturegroup(featurestoreId, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#createFeaturegroup");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **body** | [**FeaturegroupDTO**](FeaturegroupDTO.md)|  | [optional]

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createNewStorageConnectorWithType"></a>
# **createNewStorageConnectorWithType**
> FeaturestoreStorageConnectorDTO createNewStorageConnectorWithType(connectorType, featurestoreId, projectId, body)

Create a new storage connector for the feature store

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
String connectorType = "connectorType_example"; // String | storage connector type
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
FeaturestoreStorageConnectorDTO body = new FeaturestoreStorageConnectorDTO(); // FeaturestoreStorageConnectorDTO | 
try {
    FeaturestoreStorageConnectorDTO result = apiInstance.createNewStorageConnectorWithType(connectorType, featurestoreId, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#createNewStorageConnectorWithType");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectorType** | **String**| storage connector type | [enum: HopsFS, JDBC, S3]
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **body** | [**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)|  | [optional]

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createOrUpdateImportJob"></a>
# **createOrUpdateImportJob**
> JobDTO createOrUpdateImportJob(body, projectId)

Configure job to import featuregroup

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
FeaturegroupImportJobDTO body = new FeaturegroupImportJobDTO(); // FeaturegroupImportJobDTO | Job configuration
Integer projectId = 56; // Integer | 
try {
    JobDTO result = apiInstance.createOrUpdateImportJob(body, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#createOrUpdateImportJob");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeaturegroupImportJobDTO**](FeaturegroupImportJobDTO.md)| Job configuration |
 **projectId** | **Integer**|  |

### Return type

[**JobDTO**](JobDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createOrUpdateTrainingDatasetJob"></a>
# **createOrUpdateTrainingDatasetJob**
> JobDTO createOrUpdateTrainingDatasetJob(body, projectId)

Configure job to create training dataset

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
TrainingDatasetJobDTO body = new TrainingDatasetJobDTO(); // TrainingDatasetJobDTO | Job configuration
Integer projectId = 56; // Integer | 
try {
    JobDTO result = apiInstance.createOrUpdateTrainingDatasetJob(body, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#createOrUpdateTrainingDatasetJob");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrainingDatasetJobDTO**](TrainingDatasetJobDTO.md)| Job configuration |
 **projectId** | **Integer**|  |

### Return type

[**JobDTO**](JobDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createTrainingDataset"></a>
# **createTrainingDataset**
> TrainingDatasetDTO createTrainingDataset(featurestoreId, projectId, body)

Create training dataset for a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
TrainingDatasetDTO body = new TrainingDatasetDTO(); // TrainingDatasetDTO | 
try {
    TrainingDatasetDTO result = apiInstance.createTrainingDataset(featurestoreId, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#createTrainingDataset");
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

<a name="deleteFeatureGroupFromFeatureStore"></a>
# **deleteFeatureGroupFromFeatureStore**
> FeaturegroupDTO deleteFeatureGroupFromFeatureStore(featuregroupId, featurestoreId, projectId)

Delete specific featuregroup from a specific featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer featuregroupId = 56; // Integer | Id of the featuregroup
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    FeaturegroupDTO result = apiInstance.deleteFeatureGroupFromFeatureStore(featuregroupId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#deleteFeatureGroupFromFeatureStore");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**| Id of the featuregroup |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteFeaturegroupContents"></a>
# **deleteFeaturegroupContents**
> FeaturegroupDTO deleteFeaturegroupContents(featuregroupId, featurestoreId, projectId)

Delete featuregroup contents

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer featuregroupId = 56; // Integer | Id of the featuregroup
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    FeaturegroupDTO result = apiInstance.deleteFeaturegroupContents(featuregroupId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#deleteFeaturegroupContents");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**| Id of the featuregroup |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteStorageConnectorWithTypeAndId"></a>
# **deleteStorageConnectorWithTypeAndId**
> FeaturestoreStorageConnectorDTO deleteStorageConnectorWithTypeAndId(connectorType, connectorId, featurestoreId, projectId)

Delete storage connector with a specific id and type from a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
String connectorType = "connectorType_example"; // String | storage connector type
Integer connectorId = 56; // Integer | Id of the storage connector
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    FeaturestoreStorageConnectorDTO result = apiInstance.deleteStorageConnectorWithTypeAndId(connectorType, connectorId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#deleteStorageConnectorWithTypeAndId");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectorType** | **String**| storage connector type | [enum: HopsFS, JDBC, S3]
 **connectorId** | **Integer**| Id of the storage connector |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteTrainingDataset"></a>
# **deleteTrainingDataset**
> TrainingDatasetDTO deleteTrainingDataset(trainingdatasetid, featurestoreId, projectId)

Delete a training datasets with a specific id from a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer trainingdatasetid = 56; // Integer | Id of the training dataset
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    TrainingDatasetDTO result = apiInstance.deleteTrainingDataset(trainingdatasetid, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#deleteTrainingDataset");
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

<a name="getFeatureGroupFromFeatureStore"></a>
# **getFeatureGroupFromFeatureStore**
> FeaturegroupDTO getFeatureGroupFromFeatureStore(featuregroupId, featurestoreId, projectId)

Get specific featuregroup from a specific featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer featuregroupId = 56; // Integer | Id of the featuregroup
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    FeaturegroupDTO result = apiInstance.getFeatureGroupFromFeatureStore(featuregroupId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#getFeatureGroupFromFeatureStore");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**| Id of the featuregroup |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getFeatureGroupPreview"></a>
# **getFeatureGroupPreview**
> List&lt;FeaturegroupPreview&gt; getFeatureGroupPreview(featuregroupId, featurestoreId, projectId)

Preview feature data of a featuregroup

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer featuregroupId = 56; // Integer | Id of the featuregroup
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    List<FeaturegroupPreview> result = apiInstance.getFeatureGroupPreview(featuregroupId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#getFeatureGroupPreview");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**| Id of the featuregroup |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**List&lt;FeaturegroupPreview&gt;**](FeaturegroupPreview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getFeatureGroupSchema"></a>
# **getFeatureGroupSchema**
> RowValueQueryResult getFeatureGroupSchema(featuregroupId, featurestoreId, projectId)

Get the SQL schema of a featuregroup

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer featuregroupId = 56; // Integer | Id of the featuregroup
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    RowValueQueryResult result = apiInstance.getFeatureGroupSchema(featuregroupId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#getFeatureGroupSchema");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**| Id of the featuregroup |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**RowValueQueryResult**](RowValueQueryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getFeaturegroupsForFeaturestore"></a>
# **getFeaturegroupsForFeaturestore**
> List&lt;FeaturegroupDTO&gt; getFeaturegroupsForFeaturestore(featurestoreId, projectId)

Get the list of feature groups for a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    List<FeaturegroupDTO> result = apiInstance.getFeaturegroupsForFeaturestore(featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#getFeaturegroupsForFeaturestore");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**List&lt;FeaturegroupDTO&gt;**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getFeaturestore"></a>
# **getFeaturestore**
> FeaturestoreDTO getFeaturestore(featurestoreId, projectId)

Get featurestore with specific Id

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer featurestoreId = 56; // Integer | Id of the featurestore
Integer projectId = 56; // Integer | 
try {
    FeaturestoreDTO result = apiInstance.getFeaturestore(featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#getFeaturestore");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreId** | **Integer**| Id of the featurestore |
 **projectId** | **Integer**|  |

### Return type

[**FeaturestoreDTO**](FeaturestoreDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getFeaturestoreByName"></a>
# **getFeaturestoreByName**
> FeaturestoreDTO getFeaturestoreByName(featurestoreName, projectId)

Get featurestore with specific name

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
String featurestoreName = "featurestoreName_example"; // String | Id of the featurestore
Integer projectId = 56; // Integer | 
try {
    FeaturestoreDTO result = apiInstance.getFeaturestoreByName(featurestoreName, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#getFeaturestoreByName");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreName** | **String**| Id of the featurestore |
 **projectId** | **Integer**|  |

### Return type

[**FeaturestoreDTO**](FeaturestoreDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getFeaturestoreId"></a>
# **getFeaturestoreId**
> FeaturestoreClientSettingsDTO getFeaturestoreId(featurestoreName, projectId)

Get featurestore Metadata

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
String featurestoreName = "featurestoreName_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    FeaturestoreClientSettingsDTO result = apiInstance.getFeaturestoreId(featurestoreName, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#getFeaturestoreId");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreName** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

[**FeaturestoreClientSettingsDTO**](FeaturestoreClientSettingsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getFeaturestoreSettings"></a>
# **getFeaturestoreSettings**
> FeaturestoreClientSettingsDTO getFeaturestoreSettings(projectId)

Get featurestore settings

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer projectId = 56; // Integer | 
try {
    FeaturestoreClientSettingsDTO result = apiInstance.getFeaturestoreSettings(projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#getFeaturestoreSettings");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

[**FeaturestoreClientSettingsDTO**](FeaturestoreClientSettingsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getFeaturestores"></a>
# **getFeaturestores**
> List&lt;FeaturestoreDTO&gt; getFeaturestores(projectId)

Get the list of feature stores for the project

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer projectId = 56; // Integer | 
try {
    List<FeaturestoreDTO> result = apiInstance.getFeaturestores(projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#getFeaturestores");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

[**List&lt;FeaturestoreDTO&gt;**](FeaturestoreDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getOnlineFeaturestoreStorageConnector"></a>
# **getOnlineFeaturestoreStorageConnector**
> FeaturestoreStorageConnectorDTO getOnlineFeaturestoreStorageConnector(featurestoreId, projectId)

Get online featurestore storage connector for this feature store

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    FeaturestoreStorageConnectorDTO result = apiInstance.getOnlineFeaturestoreStorageConnector(featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#getOnlineFeaturestoreStorageConnector");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getStorageConnectorWithId"></a>
# **getStorageConnectorWithId**
> FeaturestoreStorageConnectorDTO getStorageConnectorWithId(connectorType, connectorId, featurestoreId, projectId)

Get a storage connector with a specific id and type from a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
String connectorType = "connectorType_example"; // String | storage connector type
Integer connectorId = 56; // Integer | Id of the storage connector
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    FeaturestoreStorageConnectorDTO result = apiInstance.getStorageConnectorWithId(connectorType, connectorId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#getStorageConnectorWithId");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectorType** | **String**| storage connector type | [enum: HopsFS, JDBC, S3]
 **connectorId** | **Integer**| Id of the storage connector |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getStorageConnectors"></a>
# **getStorageConnectors**
> List&lt;FeaturestoreStorageConnectorDTO&gt; getStorageConnectors(featurestoreId, projectId)

Get all storage connectors of a feature store

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    List<FeaturestoreStorageConnectorDTO> result = apiInstance.getStorageConnectors(featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#getStorageConnectors");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**List&lt;FeaturestoreStorageConnectorDTO&gt;**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getStorageConnectorsOfType"></a>
# **getStorageConnectorsOfType**
> List&lt;FeaturestoreStorageConnectorDTO&gt; getStorageConnectorsOfType(connectorType, featurestoreId, projectId)

Get all storage connectors of a specific type of a feature store

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
String connectorType = "connectorType_example"; // String | storage connector type
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    List<FeaturestoreStorageConnectorDTO> result = apiInstance.getStorageConnectorsOfType(connectorType, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#getStorageConnectorsOfType");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectorType** | **String**| storage connector type | [enum: HopsFS, JDBC, S3]
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**List&lt;FeaturestoreStorageConnectorDTO&gt;**](FeaturestoreStorageConnectorDTO.md)

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
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer trainingdatasetid = 56; // Integer | Id of the training dataset
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    TrainingDatasetDTO result = apiInstance.getTrainingDatasetWithId(trainingdatasetid, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#getTrainingDatasetWithId");
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
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    List<TrainingDatasetDTO> result = apiInstance.getTrainingDatasetsForFeaturestore(featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#getTrainingDatasetsForFeaturestore");
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

<a name="getValidationResult"></a>
# **getValidationResult**
> ValidationResult getValidationResult(featuregroupId, featureStoreId, projectId)

Fetch the result of a Deequ data validation job

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer featuregroupId = 56; // Integer | 
Integer featureStoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    ValidationResult result = apiInstance.getValidationResult(featuregroupId, featureStoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#getValidationResult");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**|  |
 **featureStoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getValidationRules"></a>
# **getValidationRules**
> ConstraintGroupDTO getValidationRules(featuregroupId, featureStoreId, projectId)

Get previously stored Deequ validation rules

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer featuregroupId = 56; // Integer | 
Integer featureStoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    ConstraintGroupDTO result = apiInstance.getValidationRules(featuregroupId, featureStoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#getValidationRules");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**|  |
 **featureStoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**ConstraintGroupDTO**](ConstraintGroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="newFeaturestoreUtil"></a>
# **newFeaturestoreUtil**
> newFeaturestoreUtil(projectId, body)

Upload json input for featurestore-util jobs

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer projectId = 56; // Integer | 
FeaturestoreUtilJobDTO body = new FeaturestoreUtilJobDTO(); // FeaturestoreUtilJobDTO | 
try {
    apiInstance.newFeaturestoreUtil(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#newFeaturestoreUtil");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**FeaturestoreUtilJobDTO**](FeaturestoreUtilJobDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="syncWithFeaturestore"></a>
# **syncWithFeaturestore**
> FeaturegroupDTO syncWithFeaturestore(featurestoreId, projectId, body)

Synchornize Hive Table with the feature store

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
FeaturegroupDTO body = new FeaturegroupDTO(); // FeaturegroupDTO | 
try {
    FeaturegroupDTO result = apiInstance.syncWithFeaturestore(featurestoreId, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#syncWithFeaturestore");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **body** | [**FeaturegroupDTO**](FeaturegroupDTO.md)|  | [optional]

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

<a name="updateFeaturegroup"></a>
# **updateFeaturegroup**
> FeaturegroupDTO updateFeaturegroup(featuregroupId, featurestoreId, projectId, body, updateMetadata, updateStats, enableOnline, disableOnline, updateStatsSettings)

Update featuregroup contents

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
Integer featuregroupId = 56; // Integer | Id of the featuregroup
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
FeaturegroupDTO body = new FeaturegroupDTO(); // FeaturegroupDTO | 
Boolean updateMetadata = true; // Boolean | updateMetadata
Boolean updateStats = true; // Boolean | updateStats
Boolean enableOnline = true; // Boolean | enableOnline
Boolean disableOnline = true; // Boolean | disableOnline
Boolean updateStatsSettings = true; // Boolean | updateStatsSettings
try {
    FeaturegroupDTO result = apiInstance.updateFeaturegroup(featuregroupId, featurestoreId, projectId, body, updateMetadata, updateStats, enableOnline, disableOnline, updateStatsSettings);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#updateFeaturegroup");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**| Id of the featuregroup |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **body** | [**FeaturegroupDTO**](FeaturegroupDTO.md)|  | [optional]
 **updateMetadata** | **Boolean**| updateMetadata | [optional]
 **updateStats** | **Boolean**| updateStats | [optional]
 **enableOnline** | **Boolean**| enableOnline | [optional]
 **disableOnline** | **Boolean**| disableOnline | [optional]
 **updateStatsSettings** | **Boolean**| updateStatsSettings | [optional]

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateStorageConnectorWithId"></a>
# **updateStorageConnectorWithId**
> FeaturestoreStorageConnectorDTO updateStorageConnectorWithId(connectorType, connectorId, featurestoreId, projectId, body)

Get a storage connector with a specific id and type from a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
String connectorType = "connectorType_example"; // String | storage connector type
Integer connectorId = 56; // Integer | Id of the storage connector
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
FeaturestoreStorageConnectorDTO body = new FeaturestoreStorageConnectorDTO(); // FeaturestoreStorageConnectorDTO | 
try {
    FeaturestoreStorageConnectorDTO result = apiInstance.updateStorageConnectorWithId(connectorType, connectorId, featurestoreId, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturestoreServiceApi#updateStorageConnectorWithId");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectorType** | **String**| storage connector type | [enum: HopsFS, JDBC, S3]
 **connectorId** | **Integer**| Id of the storage connector |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **body** | [**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)|  | [optional]

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateTrainingDataset"></a>
# **updateTrainingDataset**
> TrainingDatasetDTO updateTrainingDataset(trainingdatasetid, featurestoreId, projectId, body, updateMetadata, updateStats)

Update a training datasets with a specific id from a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturestoreServiceApi;


FeaturestoreServiceApi apiInstance = new FeaturestoreServiceApi();
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
    System.err.println("Exception when calling FeaturestoreServiceApi#updateTrainingDataset");
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

