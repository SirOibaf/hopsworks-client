# MessageServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**countUnreadMessagesByUser**](MessageServiceApi.md#countUnreadMessagesByUser) | **GET** /message/countUnread | 
[**deleteMessage**](MessageServiceApi.md#deleteMessage) | **DELETE** /message/{msgId} | 
[**emptyTrash**](MessageServiceApi.md#emptyTrash) | **DELETE** /message/empty | 
[**getAllDeletedMessagesByUser**](MessageServiceApi.md#getAllDeletedMessagesByUser) | **GET** /message/deleted | 
[**getAllMessagesByUser**](MessageServiceApi.md#getAllMessagesByUser) | **GET** /message | 
[**markAsRead**](MessageServiceApi.md#markAsRead) | **PUT** /message/markAsRead/{msgId} | 
[**moveToTrash**](MessageServiceApi.md#moveToTrash) | **PUT** /message/moveToTrash/{msgId} | 
[**reply**](MessageServiceApi.md#reply) | **POST** /message/reply/{msgId} | 
[**restoreFromTrash**](MessageServiceApi.md#restoreFromTrash) | **PUT** /message/restoreFromTrash/{msgId} | 

<a name="countUnreadMessagesByUser"></a>
# **countUnreadMessagesByUser**
> countUnreadMessagesByUser()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MessageServiceApi;


MessageServiceApi apiInstance = new MessageServiceApi();
try {
    apiInstance.countUnreadMessagesByUser();
} catch (ApiException e) {
    System.err.println("Exception when calling MessageServiceApi#countUnreadMessagesByUser");
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

<a name="deleteMessage"></a>
# **deleteMessage**
> deleteMessage(msgId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MessageServiceApi;


MessageServiceApi apiInstance = new MessageServiceApi();
Integer msgId = 56; // Integer | 
try {
    apiInstance.deleteMessage(msgId);
} catch (ApiException e) {
    System.err.println("Exception when calling MessageServiceApi#deleteMessage");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msgId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="emptyTrash"></a>
# **emptyTrash**
> emptyTrash()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MessageServiceApi;


MessageServiceApi apiInstance = new MessageServiceApi();
try {
    apiInstance.emptyTrash();
} catch (ApiException e) {
    System.err.println("Exception when calling MessageServiceApi#emptyTrash");
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

<a name="getAllDeletedMessagesByUser"></a>
# **getAllDeletedMessagesByUser**
> getAllDeletedMessagesByUser()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MessageServiceApi;


MessageServiceApi apiInstance = new MessageServiceApi();
try {
    apiInstance.getAllDeletedMessagesByUser();
} catch (ApiException e) {
    System.err.println("Exception when calling MessageServiceApi#getAllDeletedMessagesByUser");
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

<a name="getAllMessagesByUser"></a>
# **getAllMessagesByUser**
> getAllMessagesByUser()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MessageServiceApi;


MessageServiceApi apiInstance = new MessageServiceApi();
try {
    apiInstance.getAllMessagesByUser();
} catch (ApiException e) {
    System.err.println("Exception when calling MessageServiceApi#getAllMessagesByUser");
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

<a name="markAsRead"></a>
# **markAsRead**
> markAsRead(msgId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MessageServiceApi;


MessageServiceApi apiInstance = new MessageServiceApi();
Integer msgId = 56; // Integer | 
try {
    apiInstance.markAsRead(msgId);
} catch (ApiException e) {
    System.err.println("Exception when calling MessageServiceApi#markAsRead");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msgId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="moveToTrash"></a>
# **moveToTrash**
> moveToTrash(msgId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MessageServiceApi;


MessageServiceApi apiInstance = new MessageServiceApi();
Integer msgId = 56; // Integer | 
try {
    apiInstance.moveToTrash(msgId);
} catch (ApiException e) {
    System.err.println("Exception when calling MessageServiceApi#moveToTrash");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msgId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="reply"></a>
# **reply**
> reply(msgId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MessageServiceApi;


MessageServiceApi apiInstance = new MessageServiceApi();
Integer msgId = 56; // Integer | 
String body = "body_example"; // String | 
try {
    apiInstance.reply(msgId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling MessageServiceApi#reply");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msgId** | **Integer**|  |
 **body** | [**String**](String.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

<a name="restoreFromTrash"></a>
# **restoreFromTrash**
> restoreFromTrash(msgId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MessageServiceApi;


MessageServiceApi apiInstance = new MessageServiceApi();
Integer msgId = 56; // Integer | 
try {
    apiInstance.restoreFromTrash(msgId);
} catch (ApiException e) {
    System.err.println("Exception when calling MessageServiceApi#restoreFromTrash");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msgId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

