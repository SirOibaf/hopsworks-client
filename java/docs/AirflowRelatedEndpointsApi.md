# AirflowRelatedEndpointsApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**composeDAG**](AirflowRelatedEndpointsApi.md#composeDAG) | **POST** /project/{projectId}/airflow/dag | Generate an Airflow Python DAG file from a DAG definition
[**secretDir**](AirflowRelatedEndpointsApi.md#secretDir) | **GET** /project/{projectId}/airflow/secretDir | Create project secret directory in Airflow home
[**storeAirflowJWT**](AirflowRelatedEndpointsApi.md#storeAirflowJWT) | **POST** /project/{projectId}/airflow/jwt | Generate a JWT for Airflow usage and store it in project&#x27;s secret directory in Airflow

<a name="composeDAG"></a>
# **composeDAG**
> composeDAG(projectId, body)

Generate an Airflow Python DAG file from a DAG definition

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AirflowRelatedEndpointsApi;


AirflowRelatedEndpointsApi apiInstance = new AirflowRelatedEndpointsApi();
Integer projectId = 56; // Integer | 
AirflowDagDTO body = new AirflowDagDTO(); // AirflowDagDTO | 
try {
    apiInstance.composeDAG(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling AirflowRelatedEndpointsApi#composeDAG");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**AirflowDagDTO**](AirflowDagDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

<a name="secretDir"></a>
# **secretDir**
> secretDir(projectId)

Create project secret directory in Airflow home

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AirflowRelatedEndpointsApi;


AirflowRelatedEndpointsApi apiInstance = new AirflowRelatedEndpointsApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.secretDir(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling AirflowRelatedEndpointsApi#secretDir");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="storeAirflowJWT"></a>
# **storeAirflowJWT**
> storeAirflowJWT(projectId)

Generate a JWT for Airflow usage and store it in project&#x27;s secret directory in Airflow

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AirflowRelatedEndpointsApi;


AirflowRelatedEndpointsApi apiInstance = new AirflowRelatedEndpointsApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.storeAirflowJWT(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling AirflowRelatedEndpointsApi#storeAirflowJWT");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

