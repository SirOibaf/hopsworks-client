# CrossDelaServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**readme1**](CrossDelaServiceApi.md#readme1) | **GET** /remote/dela/datasets/{publicDSId}/readme | 

<a name="readme1"></a>
# **readme1**
> readme1(publicDSId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.CrossDelaServiceApi;


CrossDelaServiceApi apiInstance = new CrossDelaServiceApi();
String publicDSId = "publicDSId_example"; // String | 
try {
    apiInstance.readme1(publicDSId);
} catch (ApiException e) {
    System.err.println("Exception when calling CrossDelaServiceApi#readme1");
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

