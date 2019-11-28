# ModelInferenceServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**infer**](ModelInferenceServiceApi.md#infer) | **POST** /project/{projectId}/inference/models/{modelName}{version}{verb} | Make inference

<a name="infer"></a>
# **infer**
> infer(modelName, version, verb, projectId, body)

Make inference

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ModelInferenceServiceApi;


ModelInferenceServiceApi apiInstance = new ModelInferenceServiceApi();
String modelName = "modelName_example"; // String | Name of the model to query
String version = "version_example"; // String | Version of the model to query
String verb = "verb_example"; // String | Type of query
Integer projectId = 56; // Integer | 
String body = "body_example"; // String | 
try {
    apiInstance.infer(modelName, version, verb, projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ModelInferenceServiceApi#infer");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modelName** | **String**| Name of the model to query |
 **version** | **String**| Version of the model to query |
 **verb** | **String**| Type of query |
 **projectId** | **Integer**|  |
 **body** | [**String**](String.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

