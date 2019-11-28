# PythonEnvironmentLibraryCommandsResourceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete1**](PythonEnvironmentLibraryCommandsResourceApi.md#delete1) | **DELETE** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Delete commands for this library
[**get1**](PythonEnvironmentLibraryCommandsResourceApi.md#get1) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Get all commands for this library
[**getByName1**](PythonEnvironmentLibraryCommandsResourceApi.md#getByName1) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library}/commands/{commandId} | Get command by id
[**update**](PythonEnvironmentLibraryCommandsResourceApi.md#update) | **PUT** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Update commands for this library

<a name="delete1"></a>
# **delete1**
> delete1(library, version, projectId)

Delete commands for this library

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentLibraryCommandsResourceApi;


PythonEnvironmentLibraryCommandsResourceApi apiInstance = new PythonEnvironmentLibraryCommandsResourceApi();
String library = "library_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.delete1(library, version, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentLibraryCommandsResourceApi#delete1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **String**|  |
 **version** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="get1"></a>
# **get1**
> CommandDTO get1(library, version, projectId, offset, limit, sortBy, filterBy)

Get all commands for this library

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentLibraryCommandsResourceApi;


PythonEnvironmentLibraryCommandsResourceApi apiInstance = new PythonEnvironmentLibraryCommandsResourceApi();
String library = "library_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
Integer offset = 56; // Integer | 
Integer limit = 56; // Integer | 
String sortBy = "sortBy_example"; // String | ex. sort_by=ID:asc,date_created:desc
List<String> filterBy = Arrays.asList("filterBy_example"); // List<String> | ex. filter_by=op:create
try {
    CommandDTO result = apiInstance.get1(library, version, projectId, offset, limit, sortBy, filterBy);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentLibraryCommandsResourceApi#get1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **String**|  |
 **version** | **String**|  |
 **projectId** | **Integer**|  |
 **offset** | **Integer**|  | [optional]
 **limit** | **Integer**|  | [optional]
 **sortBy** | **String**| ex. sort_by&#x3D;ID:asc,date_created:desc | [optional] [enum: id:asc, id:desc, status:asc, status:desc, date_created:asc, date_created:desc, host:asc, host:desc]
 **filterBy** | [**List&lt;String&gt;**](String.md)| ex. filter_by&#x3D;op:create | [optional] [enum: op:CLONE, op:CREATE, op:BACKUP, op:REMOVE, op:LIST, op:INSTALL, op:UNINSTALL, op:UPGRADE, op:CLEAN, op:YML, status:NEW, status:SUCCESS, status:ONGOING, status:FAILED, machine_type:ALL, machine_type:CPU, machine_type:GPU, host_in:1, host_nin:4, host_lt:5, host_gt:3]

### Return type

[**CommandDTO**](CommandDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getByName1"></a>
# **getByName1**
> CommandDTO getByName1(library, commandId, version, projectId)

Get command by id

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentLibraryCommandsResourceApi;


PythonEnvironmentLibraryCommandsResourceApi apiInstance = new PythonEnvironmentLibraryCommandsResourceApi();
String library = "library_example"; // String | 
Integer commandId = 56; // Integer | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    CommandDTO result = apiInstance.getByName1(library, commandId, version, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentLibraryCommandsResourceApi#getByName1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **String**|  |
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

<a name="update"></a>
# **update**
> update(library, version, projectId)

Update commands for this library

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentLibraryCommandsResourceApi;


PythonEnvironmentLibraryCommandsResourceApi apiInstance = new PythonEnvironmentLibraryCommandsResourceApi();
String library = "library_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.update(library, version, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentLibraryCommandsResourceApi#update");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **String**|  |
 **version** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

