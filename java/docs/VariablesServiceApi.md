# VariablesServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAuthStatus**](VariablesServiceApi.md#getAuthStatus) | **GET** /variables/authStatus | 
[**getCondaDefaultRepo**](VariablesServiceApi.md#getCondaDefaultRepo) | **GET** /variables/conda | 
[**getLDAPAuthStatus**](VariablesServiceApi.md#getLDAPAuthStatus) | **GET** /variables/ldap | 
[**getSecurityQuestions**](VariablesServiceApi.md#getSecurityQuestions) | **GET** /variables/securityQuestions | 
[**getTwofactor**](VariablesServiceApi.md#getTwofactor) | **GET** /variables/twofactor | 
[**getVar**](VariablesServiceApi.md#getVar) | **GET** /variables/{id} | 
[**getVersions**](VariablesServiceApi.md#getVersions) | **GET** /variables/versions | 

<a name="getAuthStatus"></a>
# **getAuthStatus**
> getAuthStatus()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.VariablesServiceApi;


VariablesServiceApi apiInstance = new VariablesServiceApi();
try {
    apiInstance.getAuthStatus();
} catch (ApiException e) {
    System.err.println("Exception when calling VariablesServiceApi#getAuthStatus");
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

<a name="getCondaDefaultRepo"></a>
# **getCondaDefaultRepo**
> getCondaDefaultRepo()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.VariablesServiceApi;


VariablesServiceApi apiInstance = new VariablesServiceApi();
try {
    apiInstance.getCondaDefaultRepo();
} catch (ApiException e) {
    System.err.println("Exception when calling VariablesServiceApi#getCondaDefaultRepo");
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

<a name="getLDAPAuthStatus"></a>
# **getLDAPAuthStatus**
> getLDAPAuthStatus()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.VariablesServiceApi;


VariablesServiceApi apiInstance = new VariablesServiceApi();
try {
    apiInstance.getLDAPAuthStatus();
} catch (ApiException e) {
    System.err.println("Exception when calling VariablesServiceApi#getLDAPAuthStatus");
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

<a name="getSecurityQuestions"></a>
# **getSecurityQuestions**
> getSecurityQuestions()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.VariablesServiceApi;


VariablesServiceApi apiInstance = new VariablesServiceApi();
try {
    apiInstance.getSecurityQuestions();
} catch (ApiException e) {
    System.err.println("Exception when calling VariablesServiceApi#getSecurityQuestions");
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

<a name="getTwofactor"></a>
# **getTwofactor**
> getTwofactor()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.VariablesServiceApi;


VariablesServiceApi apiInstance = new VariablesServiceApi();
try {
    apiInstance.getTwofactor();
} catch (ApiException e) {
    System.err.println("Exception when calling VariablesServiceApi#getTwofactor");
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

<a name="getVar"></a>
# **getVar**
> getVar(id)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.VariablesServiceApi;


VariablesServiceApi apiInstance = new VariablesServiceApi();
String id = "id_example"; // String | 
try {
    apiInstance.getVar(id);
} catch (ApiException e) {
    System.err.println("Exception when calling VariablesServiceApi#getVar");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getVersions"></a>
# **getVersions**
> getVersions()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.VariablesServiceApi;


VariablesServiceApi apiInstance = new VariablesServiceApi();
try {
    apiInstance.getVersions();
} catch (ApiException e) {
    System.err.println("Exception when calling VariablesServiceApi#getVersions");
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

