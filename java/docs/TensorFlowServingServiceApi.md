# TensorFlowServingServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrUpdate**](TensorFlowServingServiceApi.md#createOrUpdate) | **PUT** /project/{projectId}/serving | Create or update a serving instance
[**deleteServing**](TensorFlowServingServiceApi.md#deleteServing) | **DELETE** /project/{projectId}/serving/{servingId} | Delete a serving instance
[**getServing**](TensorFlowServingServiceApi.md#getServing) | **GET** /project/{projectId}/serving/{servingId} | Get info about a serving instance for the project
[**getServings**](TensorFlowServingServiceApi.md#getServings) | **GET** /project/{projectId}/serving | Get the list of serving instances for the project
[**startOrStop**](TensorFlowServingServiceApi.md#startOrStop) | **POST** /project/{projectId}/serving/{servingId} | Start or stop a Serving instance

<a name="createOrUpdate"></a>
# **createOrUpdate**
> createOrUpdate(body, projectId)

Create or update a serving instance

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.TensorFlowServingServiceApi;


TensorFlowServingServiceApi apiInstance = new TensorFlowServingServiceApi();
RepresentsAServingModel body = new RepresentsAServingModel(); // RepresentsAServingModel | serving specification
Integer projectId = 56; // Integer | 
try {
    apiInstance.createOrUpdate(body, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling TensorFlowServingServiceApi#createOrUpdate");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RepresentsAServingModel**](RepresentsAServingModel.md)| serving specification |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="deleteServing"></a>
# **deleteServing**
> deleteServing(servingId, projectId)

Delete a serving instance

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.TensorFlowServingServiceApi;


TensorFlowServingServiceApi apiInstance = new TensorFlowServingServiceApi();
Integer servingId = 56; // Integer | Id of the serving instance
Integer projectId = 56; // Integer | 
try {
    apiInstance.deleteServing(servingId, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling TensorFlowServingServiceApi#deleteServing");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **servingId** | **Integer**| Id of the serving instance |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getServing"></a>
# **getServing**
> RepresentsAServingModel getServing(servingId, projectId)

Get info about a serving instance for the project

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.TensorFlowServingServiceApi;


TensorFlowServingServiceApi apiInstance = new TensorFlowServingServiceApi();
Integer servingId = 56; // Integer | Id of the Serving instance
Integer projectId = 56; // Integer | 
try {
    RepresentsAServingModel result = apiInstance.getServing(servingId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TensorFlowServingServiceApi#getServing");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **servingId** | **Integer**| Id of the Serving instance |
 **projectId** | **Integer**|  |

### Return type

[**RepresentsAServingModel**](RepresentsAServingModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getServings"></a>
# **getServings**
> List&lt;RepresentsAServingModel&gt; getServings(projectId)

Get the list of serving instances for the project

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.TensorFlowServingServiceApi;


TensorFlowServingServiceApi apiInstance = new TensorFlowServingServiceApi();
Integer projectId = 56; // Integer | 
try {
    List<RepresentsAServingModel> result = apiInstance.getServings(projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TensorFlowServingServiceApi#getServings");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

[**List&lt;RepresentsAServingModel&gt;**](RepresentsAServingModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="startOrStop"></a>
# **startOrStop**
> startOrStop(servingId, action, projectId)

Start or stop a Serving instance

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.TensorFlowServingServiceApi;


TensorFlowServingServiceApi apiInstance = new TensorFlowServingServiceApi();
Integer servingId = 56; // Integer | ID of the Serving instance to start/stop
String action = "action_example"; // String | Action
Integer projectId = 56; // Integer | 
try {
    apiInstance.startOrStop(servingId, action, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling TensorFlowServingServiceApi#startOrStop");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **servingId** | **Integer**| ID of the Serving instance to start/stop |
 **action** | **String**| Action | [enum: START, STOP]
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

