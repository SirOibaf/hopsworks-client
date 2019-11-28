# UiServingConfigurationApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getConfiguration**](UiServingConfigurationApi.md#getConfiguration) | **GET** /servingconf | Get UI configuration for serving

<a name="getConfiguration"></a>
# **getConfiguration**
> RepresentConfigurationForServingUI getConfiguration()

Get UI configuration for serving

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UiServingConfigurationApi;


UiServingConfigurationApi apiInstance = new UiServingConfigurationApi();
try {
    RepresentConfigurationForServingUI result = apiInstance.getConfiguration();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UiServingConfigurationApi#getConfiguration");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RepresentConfigurationForServingUI**](RepresentConfigurationForServingUI.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

