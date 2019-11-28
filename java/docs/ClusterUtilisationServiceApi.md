# ClusterUtilisationServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getGpus**](ClusterUtilisationServiceApi.md#getGpus) | **GET** /clusterUtilisation/metrics | 

<a name="getGpus"></a>
# **getGpus**
> getGpus()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ClusterUtilisationServiceApi;


ClusterUtilisationServiceApi apiInstance = new ClusterUtilisationServiceApi();
try {
    apiInstance.getGpus();
} catch (ApiException e) {
    System.err.println("Exception when calling ClusterUtilisationServiceApi#getGpus");
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

