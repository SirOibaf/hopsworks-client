# MetadataServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addMetadataWithSchema**](MetadataServiceApi.md#addMetadataWithSchema) | **POST** /metadata/addWithSchema | 
[**attachSchemalessMetadata**](MetadataServiceApi.md#attachSchemalessMetadata) | **PUT** /metadata/schemaless/{xattrName}/{path} | Create or Update a schemaless metadata for a path.
[**detachSchemalessMetadata**](MetadataServiceApi.md#detachSchemalessMetadata) | **DELETE** /metadata/schemaless/{xattrName}/{path} | Delete the schemaless metadata attached to a path.
[**detachTemplateFromInode**](MetadataServiceApi.md#detachTemplateFromInode) | **GET** /metadata/detachtemplate/{inodeid}/{templateid} | 
[**fetchAvailableTemplatesForInode**](MetadataServiceApi.md#fetchAvailableTemplatesForInode) | **GET** /metadata/fetchavailabletemplatesforinode/{inodeid} | 
[**fetchMetadata**](MetadataServiceApi.md#fetchMetadata) | **GET** /metadata/fetchmetadata/{inodepid}/{inodename}/{tableid} | 
[**fetchMetadataCompact**](MetadataServiceApi.md#fetchMetadataCompact) | **GET** /metadata/{inodepid} | 
[**fetchTemplate**](MetadataServiceApi.md#fetchTemplate) | **GET** /metadata/fetchtemplate/{templateid}/{sender} | 
[**fetchTemplatesforInode**](MetadataServiceApi.md#fetchTemplatesforInode) | **GET** /metadata/fetchtemplatesforinode/{inodeid} | 
[**getSchemalessMetadata**](MetadataServiceApi.md#getSchemalessMetadata) | **GET** /metadata/schemaless/{xattrName}/{path} | Get the schemaless metadata attached to a path.
[**removeMetadataWithSchema**](MetadataServiceApi.md#removeMetadataWithSchema) | **POST** /metadata/removeWithSchema | 
[**testMethod**](MetadataServiceApi.md#testMethod) | **GET** /metadata/upload | 
[**updateMetadataWithSchema**](MetadataServiceApi.md#updateMetadataWithSchema) | **POST** /metadata/updateWithSchema | 
[**uploadMethod**](MetadataServiceApi.md#uploadMethod) | **POST** /metadata/upload | 

<a name="addMetadataWithSchema"></a>
# **addMetadataWithSchema**
> addMetadataWithSchema(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MetadataServiceApi;


MetadataServiceApi apiInstance = new MetadataServiceApi();
String body = "body_example"; // String | 
try {
    apiInstance.addMetadataWithSchema(body);
} catch (ApiException e) {
    System.err.println("Exception when calling MetadataServiceApi#addMetadataWithSchema");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**String**](String.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="attachSchemalessMetadata"></a>
# **attachSchemalessMetadata**
> attachSchemalessMetadata(xattrName, path, body)

Create or Update a schemaless metadata for a path.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MetadataServiceApi;


MetadataServiceApi apiInstance = new MetadataServiceApi();
String xattrName = "xattrName_example"; // String | 
String path = "path_example"; // String | 
String body = "body_example"; // String | 
try {
    apiInstance.attachSchemalessMetadata(xattrName, path, body);
} catch (ApiException e) {
    System.err.println("Exception when calling MetadataServiceApi#attachSchemalessMetadata");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xattrName** | **String**|  |
 **path** | **String**|  |
 **body** | [**String**](String.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="detachSchemalessMetadata"></a>
# **detachSchemalessMetadata**
> detachSchemalessMetadata(xattrName, path)

Delete the schemaless metadata attached to a path.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MetadataServiceApi;


MetadataServiceApi apiInstance = new MetadataServiceApi();
String xattrName = "xattrName_example"; // String | 
String path = "path_example"; // String | 
try {
    apiInstance.detachSchemalessMetadata(xattrName, path);
} catch (ApiException e) {
    System.err.println("Exception when calling MetadataServiceApi#detachSchemalessMetadata");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xattrName** | **String**|  |
 **path** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="detachTemplateFromInode"></a>
# **detachTemplateFromInode**
> detachTemplateFromInode(inodeid, templateid)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MetadataServiceApi;


MetadataServiceApi apiInstance = new MetadataServiceApi();
Long inodeid = 789L; // Long | 
Integer templateid = 56; // Integer | 
try {
    apiInstance.detachTemplateFromInode(inodeid, templateid);
} catch (ApiException e) {
    System.err.println("Exception when calling MetadataServiceApi#detachTemplateFromInode");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inodeid** | **Long**|  |
 **templateid** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="fetchAvailableTemplatesForInode"></a>
# **fetchAvailableTemplatesForInode**
> fetchAvailableTemplatesForInode(inodeid)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MetadataServiceApi;


MetadataServiceApi apiInstance = new MetadataServiceApi();
Long inodeid = 789L; // Long | 
try {
    apiInstance.fetchAvailableTemplatesForInode(inodeid);
} catch (ApiException e) {
    System.err.println("Exception when calling MetadataServiceApi#fetchAvailableTemplatesForInode");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inodeid** | **Long**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="fetchMetadata"></a>
# **fetchMetadata**
> fetchMetadata(inodepid, inodename, tableid)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MetadataServiceApi;


MetadataServiceApi apiInstance = new MetadataServiceApi();
Long inodepid = 789L; // Long | 
String inodename = "inodename_example"; // String | 
Integer tableid = 56; // Integer | 
try {
    apiInstance.fetchMetadata(inodepid, inodename, tableid);
} catch (ApiException e) {
    System.err.println("Exception when calling MetadataServiceApi#fetchMetadata");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inodepid** | **Long**|  |
 **inodename** | **String**|  |
 **tableid** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="fetchMetadataCompact"></a>
# **fetchMetadataCompact**
> fetchMetadataCompact(inodepid)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MetadataServiceApi;


MetadataServiceApi apiInstance = new MetadataServiceApi();
Long inodepid = 789L; // Long | 
try {
    apiInstance.fetchMetadataCompact(inodepid);
} catch (ApiException e) {
    System.err.println("Exception when calling MetadataServiceApi#fetchMetadataCompact");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inodepid** | **Long**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="fetchTemplate"></a>
# **fetchTemplate**
> fetchTemplate(templateid, sender)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MetadataServiceApi;


MetadataServiceApi apiInstance = new MetadataServiceApi();
Integer templateid = 56; // Integer | 
String sender = "sender_example"; // String | 
try {
    apiInstance.fetchTemplate(templateid, sender);
} catch (ApiException e) {
    System.err.println("Exception when calling MetadataServiceApi#fetchTemplate");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateid** | **Integer**|  |
 **sender** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="fetchTemplatesforInode"></a>
# **fetchTemplatesforInode**
> fetchTemplatesforInode(inodeid)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MetadataServiceApi;


MetadataServiceApi apiInstance = new MetadataServiceApi();
Long inodeid = 789L; // Long | 
try {
    apiInstance.fetchTemplatesforInode(inodeid);
} catch (ApiException e) {
    System.err.println("Exception when calling MetadataServiceApi#fetchTemplatesforInode");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inodeid** | **Long**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getSchemalessMetadata"></a>
# **getSchemalessMetadata**
> getSchemalessMetadata(xattrName, path)

Get the schemaless metadata attached to a path.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MetadataServiceApi;


MetadataServiceApi apiInstance = new MetadataServiceApi();
String xattrName = "xattrName_example"; // String | 
String path = "path_example"; // String | 
try {
    apiInstance.getSchemalessMetadata(xattrName, path);
} catch (ApiException e) {
    System.err.println("Exception when calling MetadataServiceApi#getSchemalessMetadata");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xattrName** | **String**|  |
 **path** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="removeMetadataWithSchema"></a>
# **removeMetadataWithSchema**
> removeMetadataWithSchema(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MetadataServiceApi;


MetadataServiceApi apiInstance = new MetadataServiceApi();
String body = "body_example"; // String | 
try {
    apiInstance.removeMetadataWithSchema(body);
} catch (ApiException e) {
    System.err.println("Exception when calling MetadataServiceApi#removeMetadataWithSchema");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**String**](String.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="testMethod"></a>
# **testMethod**
> testMethod()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MetadataServiceApi;


MetadataServiceApi apiInstance = new MetadataServiceApi();
try {
    apiInstance.testMethod();
} catch (ApiException e) {
    System.err.println("Exception when calling MetadataServiceApi#testMethod");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="updateMetadataWithSchema"></a>
# **updateMetadataWithSchema**
> updateMetadataWithSchema(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MetadataServiceApi;


MetadataServiceApi apiInstance = new MetadataServiceApi();
String body = "body_example"; // String | 
try {
    apiInstance.updateMetadataWithSchema(body);
} catch (ApiException e) {
    System.err.println("Exception when calling MetadataServiceApi#updateMetadataWithSchema");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**String**](String.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="uploadMethod"></a>
# **uploadMethod**
> uploadMethod(file, flowChunkNumber, flowChunkSize, flowCurrentChunkSize, flowFilename, flowIdentifier, flowRelativePath, flowTotalChunks, flowTotalSize)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MetadataServiceApi;


MetadataServiceApi apiInstance = new MetadataServiceApi();
File file = new File("file_example"); // File | 
String flowChunkNumber = "flowChunkNumber_example"; // String | 
String flowChunkSize = "flowChunkSize_example"; // String | 
String flowCurrentChunkSize = "flowCurrentChunkSize_example"; // String | 
String flowFilename = "flowFilename_example"; // String | 
String flowIdentifier = "flowIdentifier_example"; // String | 
String flowRelativePath = "flowRelativePath_example"; // String | 
String flowTotalChunks = "flowTotalChunks_example"; // String | 
String flowTotalSize = "flowTotalSize_example"; // String | 
try {
    apiInstance.uploadMethod(file, flowChunkNumber, flowChunkSize, flowCurrentChunkSize, flowFilename, flowIdentifier, flowRelativePath, flowTotalChunks, flowTotalSize);
} catch (ApiException e) {
    System.err.println("Exception when calling MetadataServiceApi#uploadMethod");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **File**|  | [optional]
 **flowChunkNumber** | [**String**](.md)|  | [optional]
 **flowChunkSize** | [**String**](.md)|  | [optional]
 **flowCurrentChunkSize** | [**String**](.md)|  | [optional]
 **flowFilename** | [**String**](.md)|  | [optional]
 **flowIdentifier** | [**String**](.md)|  | [optional]
 **flowRelativePath** | [**String**](.md)|  | [optional]
 **flowTotalChunks** | [**String**](.md)|  | [optional]
 **flowTotalSize** | [**String**](.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

