# DelaServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**details**](DelaServiceApi.md#details) | **GET** /dela/transfers/{publicDSId} | 
[**getClientType**](DelaServiceApi.md#getClientType) | **GET** /dela/client | 
[**getContentsForUser**](DelaServiceApi.md#getContentsForUser) | **GET** /dela/transfers | 
[**getPublicDatasets1**](DelaServiceApi.md#getPublicDatasets1) | **GET** /dela | 
[**publicSearch**](DelaServiceApi.md#publicSearch) | **GET** /dela/search | 
[**readme**](DelaServiceApi.md#readme) | **POST** /dela/datasets/{publicDSId}/readme | Gets readme file from a provided list of peers

<a name="details"></a>
# **details**
> details(publicDSId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DelaServiceApi;


DelaServiceApi apiInstance = new DelaServiceApi();
String publicDSId = "publicDSId_example"; // String | 
try {
    apiInstance.details(publicDSId);
} catch (ApiException e) {
    System.err.println("Exception when calling DelaServiceApi#details");
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

<a name="getClientType"></a>
# **getClientType**
> getClientType()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DelaServiceApi;


DelaServiceApi apiInstance = new DelaServiceApi();
try {
    apiInstance.getClientType();
} catch (ApiException e) {
    System.err.println("Exception when calling DelaServiceApi#getClientType");
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

<a name="getContentsForUser"></a>
# **getContentsForUser**
> getContentsForUser(filter)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DelaServiceApi;


DelaServiceApi apiInstance = new DelaServiceApi();
String filter = "filter_example"; // String | 
try {
    apiInstance.getContentsForUser(filter);
} catch (ApiException e) {
    System.err.println("Exception when calling DelaServiceApi#getContentsForUser");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **String**|  | [optional] [enum: USER]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getPublicDatasets1"></a>
# **getPublicDatasets1**
> getPublicDatasets1()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DelaServiceApi;


DelaServiceApi apiInstance = new DelaServiceApi();
try {
    apiInstance.getPublicDatasets1();
} catch (ApiException e) {
    System.err.println("Exception when calling DelaServiceApi#getPublicDatasets1");
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

<a name="publicSearch"></a>
# **publicSearch**
> publicSearch(query)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DelaServiceApi;


DelaServiceApi apiInstance = new DelaServiceApi();
String query = "query_example"; // String | 
try {
    apiInstance.publicSearch(query);
} catch (ApiException e) {
    System.err.println("Exception when calling DelaServiceApi#publicSearch");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="readme"></a>
# **readme**
> readme(publicDSId, body)

Gets readme file from a provided list of peers

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DelaServiceApi;


DelaServiceApi apiInstance = new DelaServiceApi();
String publicDSId = "publicDSId_example"; // String | 
BootstrapDTO body = new BootstrapDTO(); // BootstrapDTO | 
try {
    apiInstance.readme(publicDSId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling DelaServiceApi#readme");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicDSId** | **String**|  |
 **body** | [**BootstrapDTO**](BootstrapDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

