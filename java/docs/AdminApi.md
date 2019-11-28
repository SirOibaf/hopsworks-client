# AdminApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acceptUser**](AdminApi.md#acceptUser) | **POST** /admin/users/{email}/accepted | 
[**addNewClusterNode**](AdminApi.md#addNewClusterNode) | **POST** /admin/hosts | 
[**changeClusterStatus**](AdminApi.md#changeClusterStatus) | **POST** /admin/llap | 
[**changeMasterEncryptionPassword**](AdminApi.md#changeMasterEncryptionPassword) | **PUT** /admin/encryptionPass | 
[**clusterStatus**](AdminApi.md#clusterStatus) | **GET** /admin/llap | 
[**createProjectAsUser**](AdminApi.md#createProjectAsUser) | **POST** /admin/projects/createas | 
[**deleteNode**](AdminApi.md#deleteNode) | **DELETE** /admin/hosts/{hostid} | 
[**deleteProject**](AdminApi.md#deleteProject) | **DELETE** /admin/projects/{id} | 
[**forceDeleteProject**](AdminApi.md#forceDeleteProject) | **DELETE** /admin/projects/{name}/force | 
[**getAllClusterNodes**](AdminApi.md#getAllClusterNodes) | **GET** /admin/hosts | 
[**getAllGroups**](AdminApi.md#getAllGroups) | **GET** /admin/usergroups | 
[**getAllUsers**](AdminApi.md#getAllUsers) | **GET** /admin/users | 
[**getKafkaSettings**](AdminApi.md#getKafkaSettings) | **GET** /admin/kafka/settings | Get kafka system settings
[**getMaterializerState**](AdminApi.md#getMaterializerState) | **GET** /admin/materializer | 
[**getProjectAdminInfo**](AdminApi.md#getProjectAdminInfo) | **GET** /admin/projects/{id} | 
[**getProjectsAdminInfo**](AdminApi.md#getProjectsAdminInfo) | **GET** /admin/projects | 
[**getUpdatePasswordStatus**](AdminApi.md#getUpdatePasswordStatus) | **GET** /admin/encryptionPass/{opId} | 
[**getUser**](AdminApi.md#getUser) | **GET** /admin/users/{email} | 
[**pendingUser**](AdminApi.md#pendingUser) | **POST** /admin/users/{email}/pending | 
[**refreshVariables**](AdminApi.md#refreshVariables) | **POST** /admin/variables/refresh | 
[**rejectUser**](AdminApi.md#rejectUser) | **POST** /admin/users/{email}/rejected | 
[**removeLocalMaterializedCrypto**](AdminApi.md#removeLocalMaterializedCrypto) | **DELETE** /admin/materializer/local/{name}/{directory} | 
[**removeRemoteMaterializedCrypto**](AdminApi.md#removeRemoteMaterializedCrypto) | **DELETE** /admin/materializer/remote/{name}/{directory} | 
[**renewServiceJWT**](AdminApi.md#renewServiceJWT) | **PUT** /admin/servicetoken | 
[**restartAgent**](AdminApi.md#restartAgent) | **PUT** /admin/kagent/{hostname} | 
[**serviceKeyRotate**](AdminApi.md#serviceKeyRotate) | **POST** /admin/rotate | 
[**setProjectAdminInfo**](AdminApi.md#setProjectAdminInfo) | **PUT** /admin/projects | 
[**startAgent**](AdminApi.md#startAgent) | **POST** /admin/kagent/{hostname} | 
[**stopAgent**](AdminApi.md#stopAgent) | **DELETE** /admin/kagent/{hostname} | 
[**updateClusterNode**](AdminApi.md#updateClusterNode) | **PUT** /admin/hosts | 
[**updateUser**](AdminApi.md#updateUser) | **POST** /admin/users/{email} | 
[**updateVariables**](AdminApi.md#updateVariables) | **POST** /admin/variables | 

<a name="acceptUser"></a>
# **acceptUser**
> acceptUser(email, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
String email = "email_example"; // String | 
Users body = new Users(); // Users | 
try {
    apiInstance.acceptUser(email, body);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#acceptUser");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **String**|  |
 **body** | [**Users**](Users.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

<a name="addNewClusterNode"></a>
# **addNewClusterNode**
> addNewClusterNode(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
Hosts body = new Hosts(); // Hosts | 
try {
    apiInstance.addNewClusterNode(body);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#addNewClusterNode");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Hosts**](Hosts.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="changeClusterStatus"></a>
# **changeClusterStatus**
> changeClusterStatus(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
LlapClusterStatus body = new LlapClusterStatus(); // LlapClusterStatus | 
try {
    apiInstance.changeClusterStatus(body);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#changeClusterStatus");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LlapClusterStatus**](LlapClusterStatus.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="changeMasterEncryptionPassword"></a>
# **changeMasterEncryptionPassword**
> changeMasterEncryptionPassword(oldPassword, newPassword)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
String oldPassword = "oldPassword_example"; // String | 
String newPassword = "newPassword_example"; // String | 
try {
    apiInstance.changeMasterEncryptionPassword(oldPassword, newPassword);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#changeMasterEncryptionPassword");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oldPassword** | [**String**](.md)|  | [optional]
 **newPassword** | [**String**](.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

<a name="clusterStatus"></a>
# **clusterStatus**
> clusterStatus()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
try {
    apiInstance.clusterStatus();
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#clusterStatus");
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

<a name="createProjectAsUser"></a>
# **createProjectAsUser**
> createProjectAsUser(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
ProjectDTO body = new ProjectDTO(); // ProjectDTO | 
try {
    apiInstance.createProjectAsUser(body);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#createProjectAsUser");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectDTO**](ProjectDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="deleteNode"></a>
# **deleteNode**
> deleteNode(hostid)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
String hostid = "hostid_example"; // String | 
try {
    apiInstance.deleteNode(hostid);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#deleteNode");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostid** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="deleteProject"></a>
# **deleteProject**
> deleteProject(id)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
Integer id = 56; // Integer | 
try {
    apiInstance.deleteProject(id);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#deleteProject");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="forceDeleteProject"></a>
# **forceDeleteProject**
> forceDeleteProject(name)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
String name = "name_example"; // String | 
try {
    apiInstance.forceDeleteProject(name);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#forceDeleteProject");
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

<a name="getAllClusterNodes"></a>
# **getAllClusterNodes**
> getAllClusterNodes()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
try {
    apiInstance.getAllClusterNodes();
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#getAllClusterNodes");
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

<a name="getAllGroups"></a>
# **getAllGroups**
> getAllGroups()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
try {
    apiInstance.getAllGroups();
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#getAllGroups");
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

<a name="getAllUsers"></a>
# **getAllUsers**
> getAllUsers(status)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
String status = "status_example"; // String | 
try {
    apiInstance.getAllUsers(status);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#getAllUsers");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **String**|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getKafkaSettings"></a>
# **getKafkaSettings**
> getKafkaSettings()

Get kafka system settings

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
try {
    apiInstance.getKafkaSettings();
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#getKafkaSettings");
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

<a name="getMaterializerState"></a>
# **getMaterializerState**
> getMaterializerState()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
try {
    apiInstance.getMaterializerState();
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#getMaterializerState");
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

<a name="getProjectAdminInfo"></a>
# **getProjectAdminInfo**
> getProjectAdminInfo(id)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
Integer id = 56; // Integer | 
try {
    apiInstance.getProjectAdminInfo(id);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#getProjectAdminInfo");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getProjectsAdminInfo"></a>
# **getProjectsAdminInfo**
> getProjectsAdminInfo()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
try {
    apiInstance.getProjectsAdminInfo();
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#getProjectsAdminInfo");
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

<a name="getUpdatePasswordStatus"></a>
# **getUpdatePasswordStatus**
> getUpdatePasswordStatus(opId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
Integer opId = 56; // Integer | 
try {
    apiInstance.getUpdatePasswordStatus(opId);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#getUpdatePasswordStatus");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getUser"></a>
# **getUser**
> getUser(email)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
String email = "email_example"; // String | 
try {
    apiInstance.getUser(email);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#getUser");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="pendingUser"></a>
# **pendingUser**
> pendingUser(email)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
String email = "email_example"; // String | 
try {
    apiInstance.pendingUser(email);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#pendingUser");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="refreshVariables"></a>
# **refreshVariables**
> refreshVariables()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
try {
    apiInstance.refreshVariables();
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#refreshVariables");
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

<a name="rejectUser"></a>
# **rejectUser**
> rejectUser(email)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
String email = "email_example"; // String | 
try {
    apiInstance.rejectUser(email);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#rejectUser");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="removeLocalMaterializedCrypto"></a>
# **removeLocalMaterializedCrypto**
> removeLocalMaterializedCrypto(name, directory)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
String name = "name_example"; // String | 
String directory = "directory_example"; // String | 
try {
    apiInstance.removeLocalMaterializedCrypto(name, directory);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#removeLocalMaterializedCrypto");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**|  |
 **directory** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="removeRemoteMaterializedCrypto"></a>
# **removeRemoteMaterializedCrypto**
> removeRemoteMaterializedCrypto(name, directory)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
String name = "name_example"; // String | 
String directory = "directory_example"; // String | 
try {
    apiInstance.removeRemoteMaterializedCrypto(name, directory);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#removeRemoteMaterializedCrypto");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**|  |
 **directory** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="renewServiceJWT"></a>
# **renewServiceJWT**
> renewServiceJWT()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
try {
    apiInstance.renewServiceJWT();
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#renewServiceJWT");
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

<a name="restartAgent"></a>
# **restartAgent**
> restartAgent(hostname)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
String hostname = "hostname_example"; // String | 
try {
    apiInstance.restartAgent(hostname);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#restartAgent");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="serviceKeyRotate"></a>
# **serviceKeyRotate**
> serviceKeyRotate()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
try {
    apiInstance.serviceKeyRotate();
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#serviceKeyRotate");
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

<a name="setProjectAdminInfo"></a>
# **setProjectAdminInfo**
> setProjectAdminInfo(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
ProjectAdminInfoDTO body = new ProjectAdminInfoDTO(); // ProjectAdminInfoDTO | 
try {
    apiInstance.setProjectAdminInfo(body);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#setProjectAdminInfo");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectAdminInfoDTO**](ProjectAdminInfoDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="startAgent"></a>
# **startAgent**
> startAgent(hostname)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
String hostname = "hostname_example"; // String | 
try {
    apiInstance.startAgent(hostname);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#startAgent");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="stopAgent"></a>
# **stopAgent**
> stopAgent(hostname)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
String hostname = "hostname_example"; // String | 
try {
    apiInstance.stopAgent(hostname);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#stopAgent");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="updateClusterNode"></a>
# **updateClusterNode**
> updateClusterNode(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
Hosts body = new Hosts(); // Hosts | 
try {
    apiInstance.updateClusterNode(body);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#updateClusterNode");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Hosts**](Hosts.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="updateUser"></a>
# **updateUser**
> updateUser(email, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
String email = "email_example"; // String | 
Users body = new Users(); // Users | 
try {
    apiInstance.updateUser(email, body);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#updateUser");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **String**|  |
 **body** | [**Users**](Users.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

<a name="updateVariables"></a>
# **updateVariables**
> updateVariables(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AdminApi;


AdminApi apiInstance = new AdminApi();
VariablesRequest body = new VariablesRequest(); // VariablesRequest | 
try {
    apiInstance.updateVariables(body);
} catch (ApiException e) {
    System.err.println("Exception when calling AdminApi#updateVariables");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VariablesRequest**](VariablesRequest.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

