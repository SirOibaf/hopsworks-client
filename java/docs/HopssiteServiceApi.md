# HopssiteServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addComment**](HopssiteServiceApi.md#addComment) | **POST** /hopssite/datasets/{publicDSId}/comments | 
[**addDatasetIssue**](HopssiteServiceApi.md#addDatasetIssue) | **POST** /hopssite/datasets/{publicDSId}/issue | 
[**addRating**](HopssiteServiceApi.md#addRating) | **POST** /hopssite/datasets/{publicDSId}/rating | 
[**deleteComment**](HopssiteServiceApi.md#deleteComment) | **DELETE** /hopssite/datasets/{publicDSId}/comments/{commentId} | 
[**getAllComments**](HopssiteServiceApi.md#getAllComments) | **GET** /hopssite/datasets/{publicDSId}/comments | 
[**getAllDatasets**](HopssiteServiceApi.md#getAllDatasets) | **GET** /hopssite/datasets | 
[**getClusterId**](HopssiteServiceApi.md#getClusterId) | **GET** /hopssite/clusterId | 
[**getDataset**](HopssiteServiceApi.md#getDataset) | **GET** /hopssite/datasets/{publicDSId} | 
[**getDisplayCategories**](HopssiteServiceApi.md#getDisplayCategories) | **GET** /hopssite/categories | 
[**getLocalDataset**](HopssiteServiceApi.md#getLocalDataset) | **GET** /hopssite/datasets/{publicDSId}/local | 
[**getRating**](HopssiteServiceApi.md#getRating) | **GET** /hopssite/datasets/{publicDSId}/rating | 
[**getServiceInfo**](HopssiteServiceApi.md#getServiceInfo) | **GET** /hopssite/services/{service} | 
[**getUserId**](HopssiteServiceApi.md#getUserId) | **GET** /hopssite/userId | 
[**reportAbuse**](HopssiteServiceApi.md#reportAbuse) | **POST** /hopssite/datasets/{publicDSId}/comments/{commentId}/report | 
[**updateComment**](HopssiteServiceApi.md#updateComment) | **PUT** /hopssite/datasets/{publicDSId}/comments/{commentId} | 

<a name="addComment"></a>
# **addComment**
> addComment(publicDSId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.HopssiteServiceApi;


HopssiteServiceApi apiInstance = new HopssiteServiceApi();
String publicDSId = "publicDSId_example"; // String | 
String body = "body_example"; // String | 
try {
    apiInstance.addComment(publicDSId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling HopssiteServiceApi#addComment");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicDSId** | **String**|  |
 **body** | [**String**](String.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="addDatasetIssue"></a>
# **addDatasetIssue**
> addDatasetIssue(publicDSId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.HopssiteServiceApi;


HopssiteServiceApi apiInstance = new HopssiteServiceApi();
String publicDSId = "publicDSId_example"; // String | 
DatasetIssueReqDTO body = new DatasetIssueReqDTO(); // DatasetIssueReqDTO | 
try {
    apiInstance.addDatasetIssue(publicDSId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling HopssiteServiceApi#addDatasetIssue");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicDSId** | **String**|  |
 **body** | [**DatasetIssueReqDTO**](DatasetIssueReqDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="addRating"></a>
# **addRating**
> addRating(publicDSId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.HopssiteServiceApi;


HopssiteServiceApi apiInstance = new HopssiteServiceApi();
String publicDSId = "publicDSId_example"; // String | 
RatingValueDTO body = new RatingValueDTO(); // RatingValueDTO | 
try {
    apiInstance.addRating(publicDSId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling HopssiteServiceApi#addRating");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicDSId** | **String**|  |
 **body** | [**RatingValueDTO**](RatingValueDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="deleteComment"></a>
# **deleteComment**
> deleteComment(commentId, publicDSId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.HopssiteServiceApi;


HopssiteServiceApi apiInstance = new HopssiteServiceApi();
Integer commentId = 56; // Integer | 
String publicDSId = "publicDSId_example"; // String | 
try {
    apiInstance.deleteComment(commentId, publicDSId);
} catch (ApiException e) {
    System.err.println("Exception when calling HopssiteServiceApi#deleteComment");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commentId** | **Integer**|  |
 **publicDSId** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getAllComments"></a>
# **getAllComments**
> getAllComments(publicDSId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.HopssiteServiceApi;


HopssiteServiceApi apiInstance = new HopssiteServiceApi();
String publicDSId = "publicDSId_example"; // String | 
try {
    apiInstance.getAllComments(publicDSId);
} catch (ApiException e) {
    System.err.println("Exception when calling HopssiteServiceApi#getAllComments");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicDSId** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getAllDatasets"></a>
# **getAllDatasets**
> getAllDatasets(filter)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.HopssiteServiceApi;


HopssiteServiceApi apiInstance = new HopssiteServiceApi();
String filter = "filter_example"; // String | 
try {
    apiInstance.getAllDatasets(filter);
} catch (ApiException e) {
    System.err.println("Exception when calling HopssiteServiceApi#getAllDatasets");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **String**|  | [enum: ALL, TOP_RATED, NEW]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getClusterId"></a>
# **getClusterId**
> getClusterId()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.HopssiteServiceApi;


HopssiteServiceApi apiInstance = new HopssiteServiceApi();
try {
    apiInstance.getClusterId();
} catch (ApiException e) {
    System.err.println("Exception when calling HopssiteServiceApi#getClusterId");
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

<a name="getDataset"></a>
# **getDataset**
> getDataset(publicDSId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.HopssiteServiceApi;


HopssiteServiceApi apiInstance = new HopssiteServiceApi();
String publicDSId = "publicDSId_example"; // String | 
try {
    apiInstance.getDataset(publicDSId);
} catch (ApiException e) {
    System.err.println("Exception when calling HopssiteServiceApi#getDataset");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicDSId** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getDisplayCategories"></a>
# **getDisplayCategories**
> getDisplayCategories()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.HopssiteServiceApi;


HopssiteServiceApi apiInstance = new HopssiteServiceApi();
try {
    apiInstance.getDisplayCategories();
} catch (ApiException e) {
    System.err.println("Exception when calling HopssiteServiceApi#getDisplayCategories");
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

<a name="getLocalDataset"></a>
# **getLocalDataset**
> getLocalDataset(publicDSId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.HopssiteServiceApi;


HopssiteServiceApi apiInstance = new HopssiteServiceApi();
String publicDSId = "publicDSId_example"; // String | 
try {
    apiInstance.getLocalDataset(publicDSId);
} catch (ApiException e) {
    System.err.println("Exception when calling HopssiteServiceApi#getLocalDataset");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicDSId** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getRating"></a>
# **getRating**
> getRating(filter, publicDSId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.HopssiteServiceApi;


HopssiteServiceApi apiInstance = new HopssiteServiceApi();
String filter = "filter_example"; // String | 
String publicDSId = "publicDSId_example"; // String | 
try {
    apiInstance.getRating(filter, publicDSId);
} catch (ApiException e) {
    System.err.println("Exception when calling HopssiteServiceApi#getRating");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **String**|  | [enum: USER, DATASET]
 **publicDSId** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getServiceInfo"></a>
# **getServiceInfo**
> getServiceInfo(service)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.HopssiteServiceApi;


HopssiteServiceApi apiInstance = new HopssiteServiceApi();
String service = "service_example"; // String | 
try {
    apiInstance.getServiceInfo(service);
} catch (ApiException e) {
    System.err.println("Exception when calling HopssiteServiceApi#getServiceInfo");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getUserId"></a>
# **getUserId**
> getUserId()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.HopssiteServiceApi;


HopssiteServiceApi apiInstance = new HopssiteServiceApi();
try {
    apiInstance.getUserId();
} catch (ApiException e) {
    System.err.println("Exception when calling HopssiteServiceApi#getUserId");
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

<a name="reportAbuse"></a>
# **reportAbuse**
> reportAbuse(commentId, publicDSId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.HopssiteServiceApi;


HopssiteServiceApi apiInstance = new HopssiteServiceApi();
Integer commentId = 56; // Integer | 
String publicDSId = "publicDSId_example"; // String | 
CommentIssueReqDTO body = new CommentIssueReqDTO(); // CommentIssueReqDTO | 
try {
    apiInstance.reportAbuse(commentId, publicDSId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling HopssiteServiceApi#reportAbuse");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commentId** | **Integer**|  |
 **publicDSId** | **String**|  |
 **body** | [**CommentIssueReqDTO**](CommentIssueReqDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="updateComment"></a>
# **updateComment**
> updateComment(commentId, publicDSId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.HopssiteServiceApi;


HopssiteServiceApi apiInstance = new HopssiteServiceApi();
Integer commentId = 56; // Integer | 
String publicDSId = "publicDSId_example"; // String | 
String body = "body_example"; // String | 
try {
    apiInstance.updateComment(commentId, publicDSId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling HopssiteServiceApi#updateComment");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commentId** | **Integer**|  |
 **publicDSId** | **String**|  |
 **body** | [**String**](String.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

