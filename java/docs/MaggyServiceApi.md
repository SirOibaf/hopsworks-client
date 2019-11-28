# MaggyServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDriver**](MaggyServiceApi.md#getDriver) | **GET** /maggy/drivers/{appId} | Get a Maggy Driver Endpoint for this YARN appId
[**register**](MaggyServiceApi.md#register) | **POST** /maggy/drivers | Register a Maggy Driver Endpoint for this YARN appId (called by Spark Driver in maggy).

<a name="getDriver"></a>
# **getDriver**
> MaggyDriver getDriver(appId)

Get a Maggy Driver Endpoint for this YARN appId

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MaggyServiceApi;


MaggyServiceApi apiInstance = new MaggyServiceApi();
String appId = "appId_example"; // String | 
try {
    MaggyDriver result = apiInstance.getDriver(appId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling MaggyServiceApi#getDriver");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**|  |

### Return type

[**MaggyDriver**](MaggyDriver.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="register"></a>
# **register**
> register(body)

Register a Maggy Driver Endpoint for this YARN appId (called by Spark Driver in maggy).

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MaggyServiceApi;


MaggyServiceApi apiInstance = new MaggyServiceApi();
MaggyDriver body = new MaggyDriver(); // MaggyDriver | 
try {
    apiInstance.register(body);
} catch (ApiException e) {
    System.err.println("Exception when calling MaggyServiceApi#register");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MaggyDriver**](MaggyDriver.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

