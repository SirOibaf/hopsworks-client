# ApiKeyResourceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkSession**](ApiKeyResourceApi.md#checkSession) | **GET** /users/apiKey/session | Check api key session.
[**create**](ApiKeyResourceApi.md#create) | **POST** /users/apiKey | Create an api key.
[**deleteAll**](ApiKeyResourceApi.md#deleteAll) | **DELETE** /users/apiKey | Delete all api keys.
[**deleteByName**](ApiKeyResourceApi.md#deleteByName) | **DELETE** /users/apiKey/{name} | Delete api key by name.
[**get4**](ApiKeyResourceApi.md#get4) | **GET** /users/apiKey | Get all api keys.
[**getByKey**](ApiKeyResourceApi.md#getByKey) | **GET** /users/apiKey/key | Find api key by name.
[**getByName3**](ApiKeyResourceApi.md#getByName3) | **GET** /users/apiKey/{name} | Find api key by name.
[**getScopes**](ApiKeyResourceApi.md#getScopes) | **GET** /users/apiKey/scopes | Get all api keys scopes.
[**update1**](ApiKeyResourceApi.md#update1) | **PUT** /users/apiKey | Update an api key.

<a name="checkSession"></a>
# **checkSession**
> checkSession()

Check api key session.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ApiKeyResourceApi;


ApiKeyResourceApi apiInstance = new ApiKeyResourceApi();
try {
    apiInstance.checkSession();
} catch (ApiException e) {
    System.err.println("Exception when calling ApiKeyResourceApi#checkSession");
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

<a name="create"></a>
# **create**
> ApiKeyDTO create(name, scope)

Create an api key.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ApiKeyResourceApi;


ApiKeyResourceApi apiInstance = new ApiKeyResourceApi();
String name = "name_example"; // String | 
List<String> scope = Arrays.asList("scope_example"); // List<String> | 
try {
    ApiKeyDTO result = apiInstance.create(name, scope);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ApiKeyResourceApi#create");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**|  | [optional]
 **scope** | [**List&lt;String&gt;**](String.md)|  | [optional] [enum: JOB, DATASET_VIEW, DATASET_CREATE, DATASET_DELETE, INFERENCE, FEATURESTORE, PROJECT]

### Return type

[**ApiKeyDTO**](ApiKeyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteAll"></a>
# **deleteAll**
> deleteAll()

Delete all api keys.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ApiKeyResourceApi;


ApiKeyResourceApi apiInstance = new ApiKeyResourceApi();
try {
    apiInstance.deleteAll();
} catch (ApiException e) {
    System.err.println("Exception when calling ApiKeyResourceApi#deleteAll");
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

<a name="deleteByName"></a>
# **deleteByName**
> deleteByName(name)

Delete api key by name.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ApiKeyResourceApi;


ApiKeyResourceApi apiInstance = new ApiKeyResourceApi();
String name = "name_example"; // String | 
try {
    apiInstance.deleteByName(name);
} catch (ApiException e) {
    System.err.println("Exception when calling ApiKeyResourceApi#deleteByName");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="get4"></a>
# **get4**
> ApiKeyDTO get4(offset, limit, sortBy, filterBy)

Get all api keys.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ApiKeyResourceApi;


ApiKeyResourceApi apiInstance = new ApiKeyResourceApi();
Integer offset = 56; // Integer | 
Integer limit = 56; // Integer | 
String sortBy = "sortBy_example"; // String | ex. sort_by=Name:asc,created:desc,modified:desc
List<String> filterBy = Arrays.asList("filterBy_example"); // List<String> | ex. filter_by=name:key, created:2019-01-01T00:00:00.000, created_lt:2019-01-01T00:00:00.000, created_gt:2019-01-01T00:00:00.000, modified:2019-01-01T00:00:00.000, modified_lt:2019-01-01T00:00:00.000, modified_gt:2019-01-01T00:00:00.000
try {
    ApiKeyDTO result = apiInstance.get4(offset, limit, sortBy, filterBy);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ApiKeyResourceApi#get4");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **Integer**|  | [optional]
 **limit** | **Integer**|  | [optional]
 **sortBy** | **String**| ex. sort_by&#x3D;Name:asc,created:desc,modified:desc | [optional] [enum: name:asc, name:desc, created:asc, created:desc, modified:asc, modified:desc]
 **filterBy** | [**List&lt;String&gt;**](String.md)| ex. filter_by&#x3D;name:key, created:2019-01-01T00:00:00.000, created_lt:2019-01-01T00:00:00.000, created_gt:2019-01-01T00:00:00.000, modified:2019-01-01T00:00:00.000, modified_lt:2019-01-01T00:00:00.000, modified_gt:2019-01-01T00:00:00.000 | [optional]

### Return type

[**ApiKeyDTO**](ApiKeyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getByKey"></a>
# **getByKey**
> ApiKeyDTO getByKey(key)

Find api key by name.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ApiKeyResourceApi;


ApiKeyResourceApi apiInstance = new ApiKeyResourceApi();
String key = "key_example"; // String | 
try {
    ApiKeyDTO result = apiInstance.getByKey(key);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ApiKeyResourceApi#getByKey");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**|  | [optional]

### Return type

[**ApiKeyDTO**](ApiKeyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getByName3"></a>
# **getByName3**
> ApiKeyDTO getByName3(name)

Find api key by name.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ApiKeyResourceApi;


ApiKeyResourceApi apiInstance = new ApiKeyResourceApi();
String name = "name_example"; // String | 
try {
    ApiKeyDTO result = apiInstance.getByName3(name);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ApiKeyResourceApi#getByName3");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**|  |

### Return type

[**ApiKeyDTO**](ApiKeyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getScopes"></a>
# **getScopes**
> getScopes()

Get all api keys scopes.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ApiKeyResourceApi;


ApiKeyResourceApi apiInstance = new ApiKeyResourceApi();
try {
    apiInstance.getScopes();
} catch (ApiException e) {
    System.err.println("Exception when calling ApiKeyResourceApi#getScopes");
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

<a name="update1"></a>
# **update1**
> ApiKeyDTO update1(name, action, scope)

Update an api key.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ApiKeyResourceApi;


ApiKeyResourceApi apiInstance = new ApiKeyResourceApi();
String name = "name_example"; // String | 
String action = "action_example"; // String | 
List<String> scope = Arrays.asList("scope_example"); // List<String> | 
try {
    ApiKeyDTO result = apiInstance.update1(name, action, scope);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ApiKeyResourceApi#update1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**|  | [optional]
 **action** | **String**|  | [optional] [enum: ADD, DELETE, UPDATE]
 **scope** | [**List&lt;String&gt;**](String.md)|  | [optional] [enum: JOB, DATASET_VIEW, DATASET_CREATE, DATASET_DELETE, INFERENCE, FEATURESTORE, PROJECT]

### Return type

[**ApiKeyDTO**](ApiKeyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

