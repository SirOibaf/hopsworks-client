# EndpointServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findEndpoint**](EndpointServiceApi.md#findEndpoint) | **GET** /endpoint | 

<a name="findEndpoint"></a>
# **findEndpoint**
> findEndpoint()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.EndpointServiceApi;


EndpointServiceApi apiInstance = new EndpointServiceApi();
try {
    apiInstance.findEndpoint();
} catch (ApiException e) {
    System.err.println("Exception when calling EndpointServiceApi#findEndpoint");
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

