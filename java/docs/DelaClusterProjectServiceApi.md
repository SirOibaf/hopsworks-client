# DelaClusterProjectServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**removePublic1**](DelaClusterProjectServiceApi.md#removePublic1) | **DELETE** /project/{projectId}/delacluster/{inodeId} | 
[**share**](DelaClusterProjectServiceApi.md#share) | **POST** /project/{projectId}/delacluster | 

<a name="removePublic1"></a>
# **removePublic1**
> removePublic1(inodeId, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DelaClusterProjectServiceApi;


DelaClusterProjectServiceApi apiInstance = new DelaClusterProjectServiceApi();
Long inodeId = 789L; // Long | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.removePublic1(inodeId, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling DelaClusterProjectServiceApi#removePublic1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inodeId** | **Long**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="share"></a>
# **share**
> share(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DelaClusterProjectServiceApi;


DelaClusterProjectServiceApi apiInstance = new DelaClusterProjectServiceApi();
Integer projectId = 56; // Integer | 
InodeIdDTO body = new InodeIdDTO(); // InodeIdDTO | 
try {
    apiInstance.share(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling DelaClusterProjectServiceApi#share");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**InodeIdDTO**](InodeIdDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

