# FeaturegroupServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createFeaturegroup**](FeaturegroupServiceApi.md#createFeaturegroup) | **POST** /project/{projectId}/featurestores/{featurestoreId}/featuregroups | Create feature group in a featurestore
[**deleteFeatureGroupFromFeatureStore**](FeaturegroupServiceApi.md#deleteFeatureGroupFromFeatureStore) | **DELETE** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId} | Delete specific featuregroup from a specific featurestore
[**deleteFeaturegroupContents**](FeaturegroupServiceApi.md#deleteFeaturegroupContents) | **POST** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId}/clear | Delete featuregroup contents
[**getFeatureGroupFromFeatureStore**](FeaturegroupServiceApi.md#getFeatureGroupFromFeatureStore) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId} | Get specific featuregroup from a specific featurestore
[**getFeatureGroupPreview**](FeaturegroupServiceApi.md#getFeatureGroupPreview) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId}/preview | Preview feature data of a featuregroup
[**getFeatureGroupSchema**](FeaturegroupServiceApi.md#getFeatureGroupSchema) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId}/schema | Get the SQL schema of a featuregroup
[**getFeaturegroupsForFeaturestore**](FeaturegroupServiceApi.md#getFeaturegroupsForFeaturestore) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups | Get the list of feature groups for a featurestore
[**syncWithFeaturestore**](FeaturegroupServiceApi.md#syncWithFeaturestore) | **POST** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/sync | Synchornize Hive Table with the feature store
[**updateFeaturegroup**](FeaturegroupServiceApi.md#updateFeaturegroup) | **PUT** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId} | Update featuregroup contents

<a name="createFeaturegroup"></a>
# **createFeaturegroup**
> FeaturegroupDTO createFeaturegroup(featurestoreId, projectId, body)

Create feature group in a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturegroupServiceApi;


FeaturegroupServiceApi apiInstance = new FeaturegroupServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
FeaturegroupDTO body = new FeaturegroupDTO(); // FeaturegroupDTO | 
try {
    FeaturegroupDTO result = apiInstance.createFeaturegroup(featurestoreId, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturegroupServiceApi#createFeaturegroup");
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

<a name="deleteFeatureGroupFromFeatureStore"></a>
# **deleteFeatureGroupFromFeatureStore**
> FeaturegroupDTO deleteFeatureGroupFromFeatureStore(featuregroupId, featurestoreId, projectId)

Delete specific featuregroup from a specific featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturegroupServiceApi;


FeaturegroupServiceApi apiInstance = new FeaturegroupServiceApi();
Integer featuregroupId = 56; // Integer | Id of the featuregroup
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    FeaturegroupDTO result = apiInstance.deleteFeatureGroupFromFeatureStore(featuregroupId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturegroupServiceApi#deleteFeatureGroupFromFeatureStore");
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
//import io.swagger.client.api.FeaturegroupServiceApi;


FeaturegroupServiceApi apiInstance = new FeaturegroupServiceApi();
Integer featuregroupId = 56; // Integer | Id of the featuregroup
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    FeaturegroupDTO result = apiInstance.deleteFeaturegroupContents(featuregroupId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturegroupServiceApi#deleteFeaturegroupContents");
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

<a name="getFeatureGroupFromFeatureStore"></a>
# **getFeatureGroupFromFeatureStore**
> FeaturegroupDTO getFeatureGroupFromFeatureStore(featuregroupId, featurestoreId, projectId)

Get specific featuregroup from a specific featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturegroupServiceApi;


FeaturegroupServiceApi apiInstance = new FeaturegroupServiceApi();
Integer featuregroupId = 56; // Integer | Id of the featuregroup
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    FeaturegroupDTO result = apiInstance.getFeatureGroupFromFeatureStore(featuregroupId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturegroupServiceApi#getFeatureGroupFromFeatureStore");
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
//import io.swagger.client.api.FeaturegroupServiceApi;


FeaturegroupServiceApi apiInstance = new FeaturegroupServiceApi();
Integer featuregroupId = 56; // Integer | Id of the featuregroup
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    List<FeaturegroupPreview> result = apiInstance.getFeatureGroupPreview(featuregroupId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturegroupServiceApi#getFeatureGroupPreview");
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
//import io.swagger.client.api.FeaturegroupServiceApi;


FeaturegroupServiceApi apiInstance = new FeaturegroupServiceApi();
Integer featuregroupId = 56; // Integer | Id of the featuregroup
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    RowValueQueryResult result = apiInstance.getFeatureGroupSchema(featuregroupId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturegroupServiceApi#getFeatureGroupSchema");
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
//import io.swagger.client.api.FeaturegroupServiceApi;


FeaturegroupServiceApi apiInstance = new FeaturegroupServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    List<FeaturegroupDTO> result = apiInstance.getFeaturegroupsForFeaturestore(featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturegroupServiceApi#getFeaturegroupsForFeaturestore");
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

<a name="syncWithFeaturestore"></a>
# **syncWithFeaturestore**
> FeaturegroupDTO syncWithFeaturestore(featurestoreId, projectId, body)

Synchornize Hive Table with the feature store

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeaturegroupServiceApi;


FeaturegroupServiceApi apiInstance = new FeaturegroupServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
FeaturegroupDTO body = new FeaturegroupDTO(); // FeaturegroupDTO | 
try {
    FeaturegroupDTO result = apiInstance.syncWithFeaturestore(featurestoreId, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeaturegroupServiceApi#syncWithFeaturestore");
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
//import io.swagger.client.api.FeaturegroupServiceApi;


FeaturegroupServiceApi apiInstance = new FeaturegroupServiceApi();
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
    System.err.println("Exception when calling FeaturegroupServiceApi#updateFeaturegroup");
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

