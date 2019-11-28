# StorageConnectorServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNewStorageConnectorWithType**](StorageConnectorServiceApi.md#createNewStorageConnectorWithType) | **POST** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType} | Create a new storage connector for the feature store
[**deleteStorageConnectorWithTypeAndId**](StorageConnectorServiceApi.md#deleteStorageConnectorWithTypeAndId) | **DELETE** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType}/{connectorId} | Delete storage connector with a specific id and type from a featurestore
[**getOnlineFeaturestoreStorageConnector**](StorageConnectorServiceApi.md#getOnlineFeaturestoreStorageConnector) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/onlinefeaturestore | Get online featurestore storage connector for this feature store
[**getStorageConnectorWithId**](StorageConnectorServiceApi.md#getStorageConnectorWithId) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType}/{connectorId} | Get a storage connector with a specific id and type from a featurestore
[**getStorageConnectors**](StorageConnectorServiceApi.md#getStorageConnectors) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors | Get all storage connectors of a feature store
[**getStorageConnectorsOfType**](StorageConnectorServiceApi.md#getStorageConnectorsOfType) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType} | Get all storage connectors of a specific type of a feature store
[**updateStorageConnectorWithId**](StorageConnectorServiceApi.md#updateStorageConnectorWithId) | **PUT** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType}/{connectorId} | Get a storage connector with a specific id and type from a featurestore

<a name="createNewStorageConnectorWithType"></a>
# **createNewStorageConnectorWithType**
> FeaturestoreStorageConnectorDTO createNewStorageConnectorWithType(connectorType, featurestoreId, projectId, body)

Create a new storage connector for the feature store

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.StorageConnectorServiceApi;


StorageConnectorServiceApi apiInstance = new StorageConnectorServiceApi();
String connectorType = "connectorType_example"; // String | storage connector type
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
FeaturestoreStorageConnectorDTO body = new FeaturestoreStorageConnectorDTO(); // FeaturestoreStorageConnectorDTO | 
try {
    FeaturestoreStorageConnectorDTO result = apiInstance.createNewStorageConnectorWithType(connectorType, featurestoreId, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling StorageConnectorServiceApi#createNewStorageConnectorWithType");
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

<a name="deleteStorageConnectorWithTypeAndId"></a>
# **deleteStorageConnectorWithTypeAndId**
> FeaturestoreStorageConnectorDTO deleteStorageConnectorWithTypeAndId(connectorType, connectorId, featurestoreId, projectId)

Delete storage connector with a specific id and type from a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.StorageConnectorServiceApi;


StorageConnectorServiceApi apiInstance = new StorageConnectorServiceApi();
String connectorType = "connectorType_example"; // String | storage connector type
Integer connectorId = 56; // Integer | Id of the storage connector
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    FeaturestoreStorageConnectorDTO result = apiInstance.deleteStorageConnectorWithTypeAndId(connectorType, connectorId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling StorageConnectorServiceApi#deleteStorageConnectorWithTypeAndId");
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

<a name="getOnlineFeaturestoreStorageConnector"></a>
# **getOnlineFeaturestoreStorageConnector**
> FeaturestoreStorageConnectorDTO getOnlineFeaturestoreStorageConnector(featurestoreId, projectId)

Get online featurestore storage connector for this feature store

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.StorageConnectorServiceApi;


StorageConnectorServiceApi apiInstance = new StorageConnectorServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    FeaturestoreStorageConnectorDTO result = apiInstance.getOnlineFeaturestoreStorageConnector(featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling StorageConnectorServiceApi#getOnlineFeaturestoreStorageConnector");
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
//import io.swagger.client.api.StorageConnectorServiceApi;


StorageConnectorServiceApi apiInstance = new StorageConnectorServiceApi();
String connectorType = "connectorType_example"; // String | storage connector type
Integer connectorId = 56; // Integer | Id of the storage connector
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    FeaturestoreStorageConnectorDTO result = apiInstance.getStorageConnectorWithId(connectorType, connectorId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling StorageConnectorServiceApi#getStorageConnectorWithId");
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
//import io.swagger.client.api.StorageConnectorServiceApi;


StorageConnectorServiceApi apiInstance = new StorageConnectorServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    List<FeaturestoreStorageConnectorDTO> result = apiInstance.getStorageConnectors(featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling StorageConnectorServiceApi#getStorageConnectors");
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
//import io.swagger.client.api.StorageConnectorServiceApi;


StorageConnectorServiceApi apiInstance = new StorageConnectorServiceApi();
String connectorType = "connectorType_example"; // String | storage connector type
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    List<FeaturestoreStorageConnectorDTO> result = apiInstance.getStorageConnectorsOfType(connectorType, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling StorageConnectorServiceApi#getStorageConnectorsOfType");
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

<a name="updateStorageConnectorWithId"></a>
# **updateStorageConnectorWithId**
> FeaturestoreStorageConnectorDTO updateStorageConnectorWithId(connectorType, connectorId, featurestoreId, projectId, body)

Get a storage connector with a specific id and type from a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.StorageConnectorServiceApi;


StorageConnectorServiceApi apiInstance = new StorageConnectorServiceApi();
String connectorType = "connectorType_example"; // String | storage connector type
Integer connectorId = 56; // Integer | Id of the storage connector
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
FeaturestoreStorageConnectorDTO body = new FeaturestoreStorageConnectorDTO(); // FeaturestoreStorageConnectorDTO | 
try {
    FeaturestoreStorageConnectorDTO result = apiInstance.updateStorageConnectorWithId(connectorType, connectorId, featurestoreId, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling StorageConnectorServiceApi#updateStorageConnectorWithId");
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

