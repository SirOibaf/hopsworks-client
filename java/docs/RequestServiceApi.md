# RequestServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**requestAccess**](RequestServiceApi.md#requestAccess) | **POST** /request/access | 
[**requestJoin**](RequestServiceApi.md#requestJoin) | **POST** /request/join | 

<a name="requestAccess"></a>
# **requestAccess**
> requestAccess(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.RequestServiceApi;


RequestServiceApi apiInstance = new RequestServiceApi();
RequestDTO body = new RequestDTO(); // RequestDTO | 
try {
    apiInstance.requestAccess(body);
} catch (ApiException e) {
    System.err.println("Exception when calling RequestServiceApi#requestAccess");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestDTO**](RequestDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

<a name="requestJoin"></a>
# **requestJoin**
> requestJoin(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.RequestServiceApi;


RequestServiceApi apiInstance = new RequestServiceApi();
RequestDTO body = new RequestDTO(); // RequestDTO | 
try {
    apiInstance.requestJoin(body);
} catch (ApiException e) {
    System.err.println("Exception when calling RequestServiceApi#requestJoin");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestDTO**](RequestDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

