# MonitorClusterServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllRoles**](MonitorClusterServiceApi.md#getAllRoles) | **GET** /kmon/services | 
[**getHostRoles**](MonitorClusterServiceApi.md#getHostRoles) | **GET** /kmon/hosts/{hostId}/services | 
[**getHosts**](MonitorClusterServiceApi.md#getHosts) | **GET** /kmon/hosts/{hostId} | 
[**getHosts1**](MonitorClusterServiceApi.md#getHosts1) | **GET** /kmon/hosts | 
[**getRoles**](MonitorClusterServiceApi.md#getRoles) | **GET** /kmon/groups/{groupName}/services/{serviceName} | 
[**getServiceRoles**](MonitorClusterServiceApi.md#getServiceRoles) | **GET** /kmon/groups/{groupName} | 
[**serviceOnHostOp**](MonitorClusterServiceApi.md#serviceOnHostOp) | **POST** /kmon/groups/{groupName}/services/{serviceName}/hosts/{hostId} | 
[**serviceOp**](MonitorClusterServiceApi.md#serviceOp) | **POST** /kmon/groups/{groupName} | 
[**serviceOp1**](MonitorClusterServiceApi.md#serviceOp1) | **POST** /kmon/groups/{groupName}/services/{serviceName} | 

<a name="getAllRoles"></a>
# **getAllRoles**
> getAllRoles()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MonitorClusterServiceApi;


MonitorClusterServiceApi apiInstance = new MonitorClusterServiceApi();
try {
    apiInstance.getAllRoles();
} catch (ApiException e) {
    System.err.println("Exception when calling MonitorClusterServiceApi#getAllRoles");
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

<a name="getHostRoles"></a>
# **getHostRoles**
> getHostRoles(hostId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MonitorClusterServiceApi;


MonitorClusterServiceApi apiInstance = new MonitorClusterServiceApi();
String hostId = "hostId_example"; // String | 
try {
    apiInstance.getHostRoles(hostId);
} catch (ApiException e) {
    System.err.println("Exception when calling MonitorClusterServiceApi#getHostRoles");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostId** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getHosts"></a>
# **getHosts**
> getHosts(hostId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MonitorClusterServiceApi;


MonitorClusterServiceApi apiInstance = new MonitorClusterServiceApi();
String hostId = "hostId_example"; // String | 
try {
    apiInstance.getHosts(hostId);
} catch (ApiException e) {
    System.err.println("Exception when calling MonitorClusterServiceApi#getHosts");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostId** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getHosts1"></a>
# **getHosts1**
> getHosts1()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MonitorClusterServiceApi;


MonitorClusterServiceApi apiInstance = new MonitorClusterServiceApi();
try {
    apiInstance.getHosts1();
} catch (ApiException e) {
    System.err.println("Exception when calling MonitorClusterServiceApi#getHosts1");
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

<a name="getRoles"></a>
# **getRoles**
> getRoles(groupName, serviceName)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MonitorClusterServiceApi;


MonitorClusterServiceApi apiInstance = new MonitorClusterServiceApi();
String groupName = "groupName_example"; // String | 
String serviceName = "serviceName_example"; // String | 
try {
    apiInstance.getRoles(groupName, serviceName);
} catch (ApiException e) {
    System.err.println("Exception when calling MonitorClusterServiceApi#getRoles");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupName** | **String**|  |
 **serviceName** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getServiceRoles"></a>
# **getServiceRoles**
> getServiceRoles(groupName)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MonitorClusterServiceApi;


MonitorClusterServiceApi apiInstance = new MonitorClusterServiceApi();
String groupName = "groupName_example"; // String | 
try {
    apiInstance.getServiceRoles(groupName);
} catch (ApiException e) {
    System.err.println("Exception when calling MonitorClusterServiceApi#getServiceRoles");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupName** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="serviceOnHostOp"></a>
# **serviceOnHostOp**
> serviceOnHostOp(groupName, serviceName, hostId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MonitorClusterServiceApi;


MonitorClusterServiceApi apiInstance = new MonitorClusterServiceApi();
String groupName = "groupName_example"; // String | 
String serviceName = "serviceName_example"; // String | 
String hostId = "hostId_example"; // String | 
ServicesActionDTO body = new ServicesActionDTO(); // ServicesActionDTO | 
try {
    apiInstance.serviceOnHostOp(groupName, serviceName, hostId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling MonitorClusterServiceApi#serviceOnHostOp");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupName** | **String**|  |
 **serviceName** | **String**|  |
 **hostId** | **String**|  |
 **body** | [**ServicesActionDTO**](ServicesActionDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="serviceOp"></a>
# **serviceOp**
> serviceOp(groupName, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MonitorClusterServiceApi;


MonitorClusterServiceApi apiInstance = new MonitorClusterServiceApi();
String groupName = "groupName_example"; // String | 
ServicesActionDTO body = new ServicesActionDTO(); // ServicesActionDTO | 
try {
    apiInstance.serviceOp(groupName, body);
} catch (ApiException e) {
    System.err.println("Exception when calling MonitorClusterServiceApi#serviceOp");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupName** | **String**|  |
 **body** | [**ServicesActionDTO**](ServicesActionDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="serviceOp1"></a>
# **serviceOp1**
> serviceOp1(groupName, serviceName, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MonitorClusterServiceApi;


MonitorClusterServiceApi apiInstance = new MonitorClusterServiceApi();
String groupName = "groupName_example"; // String | 
String serviceName = "serviceName_example"; // String | 
ServicesActionDTO body = new ServicesActionDTO(); // ServicesActionDTO | 
try {
    apiInstance.serviceOp1(groupName, serviceName, body);
} catch (ApiException e) {
    System.err.println("Exception when calling MonitorClusterServiceApi#serviceOp1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupName** | **String**|  |
 **serviceName** | **String**|  |
 **body** | [**ServicesActionDTO**](ServicesActionDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

