# PythonEnvironmentsResourceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](PythonEnvironmentsResourceApi.md#delete) | **DELETE** /project/{projectId}/python/environments/{version}/commands | Delete commands for this environment
[**delete1**](PythonEnvironmentsResourceApi.md#delete1) | **DELETE** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Delete commands for this library
[**delete2**](PythonEnvironmentsResourceApi.md#delete2) | **DELETE** /project/{projectId}/python/environments/{version} | Remove the python environment with the specified version for this project
[**get**](PythonEnvironmentsResourceApi.md#get) | **GET** /project/{projectId}/python/environments/{version}/commands | Get commands for this environment
[**get1**](PythonEnvironmentsResourceApi.md#get1) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Get all commands for this library
[**get2**](PythonEnvironmentsResourceApi.md#get2) | **GET** /project/{projectId}/python/environments/{version}/libraries | Get the python libraries installed in this environment
[**get3**](PythonEnvironmentsResourceApi.md#get3) | **GET** /project/{projectId}/python/environments/{version} | Get the python environment for specific python version
[**getAll**](PythonEnvironmentsResourceApi.md#getAll) | **GET** /project/{projectId}/python/environments | Get all python environments for this project
[**getByName**](PythonEnvironmentsResourceApi.md#getByName) | **GET** /project/{projectId}/python/environments/{version}/commands/{commandId} | Get commands by id
[**getByName1**](PythonEnvironmentsResourceApi.md#getByName1) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library}/commands/{commandId} | Get command by id
[**getByName2**](PythonEnvironmentsResourceApi.md#getByName2) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library} | Get the a python library installed in this environment
[**install**](PythonEnvironmentsResourceApi.md#install) | **POST** /project/{projectId}/python/environments/{version}/libraries/{library} | Install a python library in the environment
[**post**](PythonEnvironmentsResourceApi.md#post) | **POST** /project/{projectId}/python/environments/{version} | Create an environment from version or export an environment as yaml file
[**postYml**](PythonEnvironmentsResourceApi.md#postYml) | **POST** /project/{projectId}/python/environments | Create an environment from yaml file
[**search**](PythonEnvironmentsResourceApi.md#search) | **GET** /project/{projectId}/python/environments/{version}/libraries/{search} | Search for libraries using conda or pip package managers
[**uninstall**](PythonEnvironmentsResourceApi.md#uninstall) | **DELETE** /project/{projectId}/python/environments/{version}/libraries/{library} | Uninstall a python library from the environment
[**update**](PythonEnvironmentsResourceApi.md#update) | **PUT** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Update commands for this library

<a name="delete"></a>
# **delete**
> delete(version, projectId)

Delete commands for this environment

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentsResourceApi;


PythonEnvironmentsResourceApi apiInstance = new PythonEnvironmentsResourceApi();
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.delete(version, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentsResourceApi#delete");
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

<a name="delete1"></a>
# **delete1**
> delete1(library, version, projectId)

Delete commands for this library

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentsResourceApi;


PythonEnvironmentsResourceApi apiInstance = new PythonEnvironmentsResourceApi();
String library = "library_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.delete1(library, version, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentsResourceApi#delete1");
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

<a name="delete2"></a>
# **delete2**
> EnvironmentDTO delete2(version, projectId)

Remove the python environment with the specified version for this project

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentsResourceApi;


PythonEnvironmentsResourceApi apiInstance = new PythonEnvironmentsResourceApi();
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    EnvironmentDTO result = apiInstance.delete2(version, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentsResourceApi#delete2");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="get"></a>
# **get**
> get(version, projectId, offset, limit, sortBy, filterBy)

Get commands for this environment

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentsResourceApi;


PythonEnvironmentsResourceApi apiInstance = new PythonEnvironmentsResourceApi();
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
Integer offset = 56; // Integer | 
Integer limit = 56; // Integer | 
String sortBy = "sortBy_example"; // String | ex. sort_by=ID:asc,date_created:desc
List<String> filterBy = Arrays.asList("filterBy_example"); // List<String> | ex. filter_by=op:create
try {
    apiInstance.get(version, projectId, offset, limit, sortBy, filterBy);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentsResourceApi#get");
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

<a name="get1"></a>
# **get1**
> CommandDTO get1(library, version, projectId, offset, limit, sortBy, filterBy)

Get all commands for this library

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentsResourceApi;


PythonEnvironmentsResourceApi apiInstance = new PythonEnvironmentsResourceApi();
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
    System.err.println("Exception when calling PythonEnvironmentsResourceApi#get1");
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
//import io.swagger.client.api.PythonEnvironmentsResourceApi;


PythonEnvironmentsResourceApi apiInstance = new PythonEnvironmentsResourceApi();
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
    System.err.println("Exception when calling PythonEnvironmentsResourceApi#get2");
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

<a name="get3"></a>
# **get3**
> EnvironmentDTO get3(version, projectId, expand)

Get the python environment for specific python version

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentsResourceApi;


PythonEnvironmentsResourceApi apiInstance = new PythonEnvironmentsResourceApi();
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=commands
try {
    EnvironmentDTO result = apiInstance.get3(version, projectId, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentsResourceApi#get3");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **String**|  |
 **projectId** | **Integer**|  |
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;commands | [optional] [enum: commands, libraries]

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getAll"></a>
# **getAll**
> EnvironmentDTO getAll(projectId, expand)

Get all python environments for this project

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentsResourceApi;


PythonEnvironmentsResourceApi apiInstance = new PythonEnvironmentsResourceApi();
Integer projectId = 56; // Integer | 
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=commands
try {
    EnvironmentDTO result = apiInstance.getAll(projectId, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentsResourceApi#getAll");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;commands | [optional] [enum: commands, libraries]

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getByName"></a>
# **getByName**
> CommandDTO getByName(commandId, version, projectId)

Get commands by id

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentsResourceApi;


PythonEnvironmentsResourceApi apiInstance = new PythonEnvironmentsResourceApi();
Integer commandId = 56; // Integer | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    CommandDTO result = apiInstance.getByName(commandId, version, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentsResourceApi#getByName");
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

<a name="getByName1"></a>
# **getByName1**
> CommandDTO getByName1(library, commandId, version, projectId)

Get command by id

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentsResourceApi;


PythonEnvironmentsResourceApi apiInstance = new PythonEnvironmentsResourceApi();
String library = "library_example"; // String | 
Integer commandId = 56; // Integer | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    CommandDTO result = apiInstance.getByName1(library, commandId, version, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentsResourceApi#getByName1");
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
//import io.swagger.client.api.PythonEnvironmentsResourceApi;


PythonEnvironmentsResourceApi apiInstance = new PythonEnvironmentsResourceApi();
String library = "library_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=commands
try {
    LibraryDTO result = apiInstance.getByName2(library, version, projectId, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentsResourceApi#getByName2");
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
//import io.swagger.client.api.PythonEnvironmentsResourceApi;


PythonEnvironmentsResourceApi apiInstance = new PythonEnvironmentsResourceApi();
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
    System.err.println("Exception when calling PythonEnvironmentsResourceApi#install");
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

<a name="post"></a>
# **post**
> EnvironmentDTO post(version, projectId, action)

Create an environment from version or export an environment as yaml file

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentsResourceApi;


PythonEnvironmentsResourceApi apiInstance = new PythonEnvironmentsResourceApi();
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
String action = "action_example"; // String | 
try {
    EnvironmentDTO result = apiInstance.post(version, projectId, action);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentsResourceApi#post");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **String**|  |
 **projectId** | **Integer**|  |
 **action** | **String**|  | [optional] [enum: CREATE, EXPORT]

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="postYml"></a>
# **postYml**
> EnvironmentDTO postYml(projectId, body)

Create an environment from yaml file

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentsResourceApi;


PythonEnvironmentsResourceApi apiInstance = new PythonEnvironmentsResourceApi();
Integer projectId = 56; // Integer | 
EnvironmentYmlDTO body = new EnvironmentYmlDTO(); // EnvironmentYmlDTO | 
try {
    EnvironmentDTO result = apiInstance.postYml(projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentsResourceApi#postYml");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**EnvironmentYmlDTO**](EnvironmentYmlDTO.md)|  | [optional]

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

<a name="search"></a>
# **search**
> LibrarySearchDTO search(search, version, projectId, query, channel)

Search for libraries using conda or pip package managers

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.PythonEnvironmentsResourceApi;


PythonEnvironmentsResourceApi apiInstance = new PythonEnvironmentsResourceApi();
String search = "search_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
String query = "query_example"; // String | 
String channel = "channel_example"; // String | 
try {
    LibrarySearchDTO result = apiInstance.search(search, version, projectId, query, channel);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentsResourceApi#search");
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
//import io.swagger.client.api.PythonEnvironmentsResourceApi;


PythonEnvironmentsResourceApi apiInstance = new PythonEnvironmentsResourceApi();
String library = "library_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.uninstall(library, version, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentsResourceApi#uninstall");
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
//import io.swagger.client.api.PythonEnvironmentsResourceApi;


PythonEnvironmentsResourceApi apiInstance = new PythonEnvironmentsResourceApi();
String library = "library_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.update(library, version, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling PythonEnvironmentsResourceApi#update");
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

