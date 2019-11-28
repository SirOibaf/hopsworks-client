# PythonEnvironmentLibraryResourceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete1**](PythonEnvironmentLibraryResourceApi.md#delete1) | **DELETE** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Delete commands for this library
[**get1**](PythonEnvironmentLibraryResourceApi.md#get1) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Get all commands for this library
[**get2**](PythonEnvironmentLibraryResourceApi.md#get2) | **GET** /project/{projectId}/python/environments/{version}/libraries | Get the python libraries installed in this environment
[**getByName1**](PythonEnvironmentLibraryResourceApi.md#getByName1) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library}/commands/{commandId} | Get command by id
[**getByName2**](PythonEnvironmentLibraryResourceApi.md#getByName2) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library} | Get the a python library installed in this environment
[**install**](PythonEnvironmentLibraryResourceApi.md#install) | **POST** /project/{projectId}/python/environments/{version}/libraries/{library} | Install a python library in the environment
[**search**](PythonEnvironmentLibraryResourceApi.md#search) | **GET** /project/{projectId}/python/environments/{version}/libraries/{search} | Search for libraries using conda or pip package managers
[**uninstall**](PythonEnvironmentLibraryResourceApi.md#uninstall) | **DELETE** /project/{projectId}/python/environments/{version}/libraries/{library} | Uninstall a python library from the environment
[**update**](PythonEnvironmentLibraryResourceApi.md#update) | **PUT** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Update commands for this library

<a name="delete1"></a>
# **delete1**
> delete1(library, version, projectId)

Delete commands for this library

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentLibraryResourceApi;


PythonEnvironmentLibraryResourceApi apiInstance = new PythonEnvironmentLibraryResourceApi();
String library = "library_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.delete1(library, version, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentLibraryResourceApi#delete1");
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
//import io.swagger.client.api.PythonEnvironmentLibraryResourceApi;


PythonEnvironmentLibraryResourceApi apiInstance = new PythonEnvironmentLibraryResourceApi();
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
    System.err.println("Exception when calling PythonEnvironmentLibraryResourceApi#get1");
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

<a name="get2"></a>
# **get2**
> LibraryDTO get2(version, projectId, offset, limit, sortBy, filterBy, expand)

Get the python libraries installed in this environment

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentLibraryResourceApi;


PythonEnvironmentLibraryResourceApi apiInstance = new PythonEnvironmentLibraryResourceApi();
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
Integer offset = 56; // Integer | 
Integer limit = 56; // Integer | 
String sortBy = "sortBy_example"; // String | ex. sort_by=ID:asc,dependency:desc
List<String> filterBy = Arrays.asList("filterBy_example"); // List<String> | ex. filter_by=preinstalled:1
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=commands
try {
    LibraryDTO result = apiInstance.get2(version, projectId, offset, limit, sortBy, filterBy, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentLibraryResourceApi#get2");
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
 **sortBy** | **String**| ex. sort_by&#x3D;ID:asc,dependency:desc | [optional] [enum: id:asc, id:desc, dependency:asc, dependency:desc, status:asc, status:desc]
 **filterBy** | [**List&lt;String&gt;**](String.md)| ex. filter_by&#x3D;preinstalled:1 | [optional] [enum: preinstalled:1, preinstalled:0, status:new, status:success, status:ongoing, status:failed]
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;commands | [optional] [enum: commands]

### Return type

[**LibraryDTO**](LibraryDTO.md)

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
//import io.swagger.client.api.PythonEnvironmentLibraryResourceApi;


PythonEnvironmentLibraryResourceApi apiInstance = new PythonEnvironmentLibraryResourceApi();
String library = "library_example"; // String | 
Integer commandId = 56; // Integer | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    CommandDTO result = apiInstance.getByName1(library, commandId, version, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentLibraryResourceApi#getByName1");
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

<a name="getByName2"></a>
# **getByName2**
> LibraryDTO getByName2(library, version, projectId, expand)

Get the a python library installed in this environment

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentLibraryResourceApi;


PythonEnvironmentLibraryResourceApi apiInstance = new PythonEnvironmentLibraryResourceApi();
String library = "library_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=commands
try {
    LibraryDTO result = apiInstance.getByName2(library, version, projectId, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentLibraryResourceApi#getByName2");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **String**|  |
 **version** | **String**|  |
 **projectId** | **Integer**|  |
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;commands | [optional] [enum: commands]

### Return type

[**LibraryDTO**](LibraryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="install"></a>
# **install**
> install(library, version2, projectId, packageManager, version, channel, machine)

Install a python library in the environment

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentLibraryResourceApi;


PythonEnvironmentLibraryResourceApi apiInstance = new PythonEnvironmentLibraryResourceApi();
String library = "library_example"; // String | 
String version2 = "version_example"; // String | 
Integer projectId = 56; // Integer | 
String packageManager = "packageManager_example"; // String | 
String version = "version_example"; // String | 
String channel = "channel_example"; // String | 
String machine = "machine_example"; // String | 
try {
    apiInstance.install(library, version2, projectId, packageManager, version, channel, machine);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentLibraryResourceApi#install");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **String**|  |
 **version2** | **String**|  |
 **projectId** | **Integer**|  |
 **packageManager** | **String**|  | [optional] [enum: CONDA, PIP]
 **version** | **String**|  | [optional]
 **channel** | **String**|  | [optional]
 **machine** | **String**|  | [optional] [enum: ALL, CPU, GPU]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="search"></a>
# **search**
> LibrarySearchDTO search(search, version, projectId, query, channel)

Search for libraries using conda or pip package managers

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentLibraryResourceApi;


PythonEnvironmentLibraryResourceApi apiInstance = new PythonEnvironmentLibraryResourceApi();
String search = "search_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
String query = "query_example"; // String | 
String channel = "channel_example"; // String | 
try {
    LibrarySearchDTO result = apiInstance.search(search, version, projectId, query, channel);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentLibraryResourceApi#search");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **String**|  |
 **version** | **String**|  |
 **projectId** | **Integer**|  |
 **query** | **String**|  | [optional]
 **channel** | **String**|  | [optional]

### Return type

[**LibrarySearchDTO**](LibrarySearchDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="uninstall"></a>
# **uninstall**
> uninstall(library, version, projectId)

Uninstall a python library from the environment

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentLibraryResourceApi;


PythonEnvironmentLibraryResourceApi apiInstance = new PythonEnvironmentLibraryResourceApi();
String library = "library_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.uninstall(library, version, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentLibraryResourceApi#uninstall");
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

<a name="update"></a>
# **update**
> update(library, version, projectId)

Update commands for this library

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentLibraryResourceApi;


PythonEnvironmentLibraryResourceApi apiInstance = new PythonEnvironmentLibraryResourceApi();
String library = "library_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.update(library, version, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentLibraryResourceApi#update");
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

