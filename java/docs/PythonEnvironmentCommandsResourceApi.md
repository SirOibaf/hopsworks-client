# PythonEnvironmentCommandsResourceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](PythonEnvironmentCommandsResourceApi.md#delete) | **DELETE** /project/{projectId}/python/environments/{version}/commands | Delete commands for this environment
[**get**](PythonEnvironmentCommandsResourceApi.md#get) | **GET** /project/{projectId}/python/environments/{version}/commands | Get commands for this environment
[**getByName**](PythonEnvironmentCommandsResourceApi.md#getByName) | **GET** /project/{projectId}/python/environments/{version}/commands/{commandId} | Get commands by id

<a name="delete"></a>
# **delete**
> delete(version, projectId)

Delete commands for this environment

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentCommandsResourceApi;


PythonEnvironmentCommandsResourceApi apiInstance = new PythonEnvironmentCommandsResourceApi();
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.delete(version, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentCommandsResourceApi#delete");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="get"></a>
# **get**
> get(version, projectId, offset, limit, sortBy, filterBy)

Get commands for this environment

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentCommandsResourceApi;


PythonEnvironmentCommandsResourceApi apiInstance = new PythonEnvironmentCommandsResourceApi();
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
Integer offset = 56; // Integer | 
Integer limit = 56; // Integer | 
String sortBy = "sortBy_example"; // String | ex. sort_by=ID:asc,date_created:desc
List<String> filterBy = Arrays.asList("filterBy_example"); // List<String> | ex. filter_by=op:create
try {
    apiInstance.get(version, projectId, offset, limit, sortBy, filterBy);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentCommandsResourceApi#get");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **String**|  |
 **projectId** | **Integer**|  |
 **offset** | **Integer**|  | [optional]
 **limit** | **Integer**|  | [optional]
 **sortBy** | **String**| ex. sort_by&#x3D;ID:asc,date_created:desc | [optional] [enum: id:asc, id:desc, status:asc, status:desc, date_created:asc, date_created:desc, host:asc, host:desc]
 **filterBy** | [**List&lt;String&gt;**](String.md)| ex. filter_by&#x3D;op:create | [optional] [enum: op:CLONE, op:CREATE, op:BACKUP, op:REMOVE, op:LIST, op:INSTALL, op:UNINSTALL, op:UPGRADE, op:CLEAN, op:YML, status:NEW, status:SUCCESS, status:ONGOING, status:FAILED, machine_type:ALL, machine_type:CPU, machine_type:GPU, host_in:1, host_nin:4, host_lt:5, host_gt:3]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getByName"></a>
# **getByName**
> CommandDTO getByName(commandId, version, projectId)

Get commands by id

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentCommandsResourceApi;


PythonEnvironmentCommandsResourceApi apiInstance = new PythonEnvironmentCommandsResourceApi();
Integer commandId = 56; // Integer | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    CommandDTO result = apiInstance.getByName(commandId, version, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentCommandsResourceApi#getByName");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commandId** | **Integer**|  |
 **version** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

[**CommandDTO**](CommandDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

