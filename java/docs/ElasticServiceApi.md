# ElasticServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datasetSearch**](ElasticServiceApi.md#datasetSearch) | **GET** /elastic/datasetsearch/{projectId}/{datasetName}/{searchTerm} | 
[**globalSearch**](ElasticServiceApi.md#globalSearch) | **GET** /elastic/globalsearch/{searchTerm} | 
[**projectSearch**](ElasticServiceApi.md#projectSearch) | **GET** /elastic/projectsearch/{projectId}/{searchTerm} | 

<a name="datasetSearch"></a>
# **datasetSearch**
> datasetSearch(projectId, datasetName, searchTerm)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ElasticServiceApi;


ElasticServiceApi apiInstance = new ElasticServiceApi();
Integer projectId = 56; // Integer | 
String datasetName = "datasetName_example"; // String | 
String searchTerm = "searchTerm_example"; // String | 
try {
    apiInstance.datasetSearch(projectId, datasetName, searchTerm);
} catch (ApiException e) {
    System.err.println("Exception when calling ElasticServiceApi#datasetSearch");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **datasetName** | **String**|  |
 **searchTerm** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="globalSearch"></a>
# **globalSearch**
> globalSearch(searchTerm)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ElasticServiceApi;


ElasticServiceApi apiInstance = new ElasticServiceApi();
String searchTerm = "searchTerm_example"; // String | 
try {
    apiInstance.globalSearch(searchTerm);
} catch (ApiException e) {
    System.err.println("Exception when calling ElasticServiceApi#globalSearch");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchTerm** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="projectSearch"></a>
# **projectSearch**
> projectSearch(projectId, searchTerm)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ElasticServiceApi;


ElasticServiceApi apiInstance = new ElasticServiceApi();
Integer projectId = 56; // Integer | 
String searchTerm = "searchTerm_example"; // String | 
try {
    apiInstance.projectSearch(projectId, searchTerm);
} catch (ApiException e) {
    System.err.println("Exception when calling ElasticServiceApi#projectSearch");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **searchTerm** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

