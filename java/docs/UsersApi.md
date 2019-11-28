# UsersApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addSecret**](UsersApi.md#addSecret) | **POST** /users/secrets | Stores a secret for user
[**changeLoginCredentials**](UsersApi.md#changeLoginCredentials) | **POST** /users/credentials | Updates logedin User&#x27;s credentials.
[**changeSecurityQA**](UsersApi.md#changeSecurityQA) | **POST** /users/securityQA | Updates logedin User&#x27;s security quesion and answer.
[**changeTwoFactor**](UsersApi.md#changeTwoFactor) | **POST** /users/twoFactor | Updates logedin User&#x27;s two factor setting.
[**checkSession**](UsersApi.md#checkSession) | **GET** /users/apiKey/session | Check api key session.
[**create**](UsersApi.md#create) | **POST** /users/apiKey | Create an api key.
[**deleteAll**](UsersApi.md#deleteAll) | **DELETE** /users/apiKey | Delete all api keys.
[**deleteAllSecrets**](UsersApi.md#deleteAllSecrets) | **DELETE** /users/secrets | Deletes all secrets of a user
[**deleteByName**](UsersApi.md#deleteByName) | **DELETE** /users/apiKey/{name} | Delete api key by name.
[**deleteSecret**](UsersApi.md#deleteSecret) | **DELETE** /users/secrets/{secretName} | Deletes a secret by its name
[**findAll**](UsersApi.md#findAll) | **GET** /users | Get all users.
[**findAllById1**](UsersApi.md#findAllById1) | **GET** /users/activities/{activityId} | Finds an activity for a user by id.
[**findAllByUser1**](UsersApi.md#findAllByUser1) | **GET** /users/activities | Finds all activities for a user.
[**findById**](UsersApi.md#findById) | **GET** /users/{userId} | Find User by Id.
[**get4**](UsersApi.md#get4) | **GET** /users/apiKey | Get all api keys.
[**getAllSecrets**](UsersApi.md#getAllSecrets) | **GET** /users/secrets | Retrieves all secrets&#x27; names of a user
[**getByKey**](UsersApi.md#getByKey) | **GET** /users/apiKey/key | Find api key by name.
[**getByName3**](UsersApi.md#getByName3) | **GET** /users/apiKey/{name} | Find api key by name.
[**getQRCode**](UsersApi.md#getQRCode) | **POST** /users/getQRCode | Gets the logedin User&#x27;s QR code.
[**getRole**](UsersApi.md#getRole) | **POST** /users/getRole | Gets the logedin User&#x27;s role in project.
[**getScopes**](UsersApi.md#getScopes) | **GET** /users/apiKey/scopes | Get all api keys scopes.
[**getSecret**](UsersApi.md#getSecret) | **GET** /users/secrets/{secretName} | Gets the value of a private secret
[**getSharedSecret**](UsersApi.md#getSharedSecret) | **GET** /users/secrets/shared | Gets the value of a shared secret
[**getUserProfile**](UsersApi.md#getUserProfile) | **GET** /users/profile | Gets logged in User&#x27;s info.
[**update1**](UsersApi.md#update1) | **PUT** /users/apiKey | Update an api key.
[**updateProfile**](UsersApi.md#updateProfile) | **POST** /users/profile | Updates logged in User&#x27;s info.

<a name="addSecret"></a>
# **addSecret**
> addSecret(body)

Stores a secret for user

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
SecretDTO body = new SecretDTO(); // SecretDTO | 
try {
    apiInstance.addSecret(body);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#addSecret");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecretDTO**](SecretDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="changeLoginCredentials"></a>
# **changeLoginCredentials**
> RESTApiJsonResponse changeLoginCredentials(oldPassword, newPassword, confirmedPassword)

Updates logedin User&#x27;s credentials.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
String oldPassword = "oldPassword_example"; // String | 
String newPassword = "newPassword_example"; // String | 
String confirmedPassword = "confirmedPassword_example"; // String | 
try {
    RESTApiJsonResponse result = apiInstance.changeLoginCredentials(oldPassword, newPassword, confirmedPassword);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#changeLoginCredentials");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oldPassword** | [**String**](.md)|  | [optional]
 **newPassword** | [**String**](.md)|  | [optional]
 **confirmedPassword** | [**String**](.md)|  | [optional]

### Return type

[**RESTApiJsonResponse**](RESTApiJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

<a name="changeSecurityQA"></a>
# **changeSecurityQA**
> RESTApiJsonResponse changeSecurityQA(oldPassword, securityQuestion, securityAnswer)

Updates logedin User&#x27;s security quesion and answer.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
String oldPassword = "oldPassword_example"; // String | 
String securityQuestion = "securityQuestion_example"; // String | 
String securityAnswer = "securityAnswer_example"; // String | 
try {
    RESTApiJsonResponse result = apiInstance.changeSecurityQA(oldPassword, securityQuestion, securityAnswer);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#changeSecurityQA");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oldPassword** | [**String**](.md)|  | [optional]
 **securityQuestion** | [**String**](.md)|  | [optional]
 **securityAnswer** | [**String**](.md)|  | [optional]

### Return type

[**RESTApiJsonResponse**](RESTApiJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

<a name="changeTwoFactor"></a>
# **changeTwoFactor**
> RESTApiJsonResponse changeTwoFactor(password, twoFactor)

Updates logedin User&#x27;s two factor setting.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
String password = "password_example"; // String | 
Boolean twoFactor = true; // Boolean | 
try {
    RESTApiJsonResponse result = apiInstance.changeTwoFactor(password, twoFactor);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#changeTwoFactor");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | [**String**](.md)|  | [optional]
 **twoFactor** | [**Boolean**](.md)|  | [optional]

### Return type

[**RESTApiJsonResponse**](RESTApiJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

<a name="checkSession"></a>
# **checkSession**
> checkSession()

Check api key session.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
try {
    apiInstance.checkSession();
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#checkSession");
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
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
String name = "name_example"; // String | 
List<String> scope = Arrays.asList("scope_example"); // List<String> | 
try {
    ApiKeyDTO result = apiInstance.create(name, scope);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#create");
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
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
try {
    apiInstance.deleteAll();
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#deleteAll");
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

<a name="deleteAllSecrets"></a>
# **deleteAllSecrets**
> deleteAllSecrets()

Deletes all secrets of a user

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
try {
    apiInstance.deleteAllSecrets();
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#deleteAllSecrets");
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
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
String name = "name_example"; // String | 
try {
    apiInstance.deleteByName(name);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#deleteByName");
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

<a name="deleteSecret"></a>
# **deleteSecret**
> deleteSecret(secretName)

Deletes a secret by its name

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
String secretName = "secretName_example"; // String | 
try {
    apiInstance.deleteSecret(secretName);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#deleteSecret");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secretName** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="findAll"></a>
# **findAll**
> UserDTO findAll(offset, limit, sortBy, filterBy)

Get all users.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
Integer offset = 56; // Integer | 
Integer limit = 56; // Integer | 
String sortBy = "sortBy_example"; // String | ex. sort_by=first_name:asc,last_name:desc
List<String> filterBy = Arrays.asList("filterBy_example"); // List<String> | ex. filter_by=role:hops_admin,hops_user&filter_by=status:2
try {
    UserDTO result = apiInstance.findAll(offset, limit, sortBy, filterBy);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#findAll");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **Integer**|  | [optional]
 **limit** | **Integer**|  | [optional]
 **sortBy** | **String**| ex. sort_by&#x3D;first_name:asc,last_name:desc | [optional] [enum: first_name:asc, first_name:desc, last_name:asc, last_name:desc, date_created:asc, date_created:desc, email:asc, email:desc]
 **filterBy** | [**List&lt;String&gt;**](String.md)| ex. filter_by&#x3D;role:hops_admin,hops_user&amp;filter_by&#x3D;status:2 | [optional] [enum: role:hops_admin, role_neq:hops_admin, role:hops_user, role_neq:hops_user, role:agent, role_neq:agent, type:mobile_account, status:new_mobile_account, status:verified_account, status:activated_account, status:deactivated_account, status:blocked_account, status:lost_mobile, status:spam_account, status_gt:2, status_gt:2, status_lt:2, is_online:0, is_online:1, false_login:10, false_login_gt:20, false_login_lt:20, user_name:a, user_first_name:b, user_last_name:c, user_email:d, user_like:e]

### Return type

[**UserDTO**](UserDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="findAllById1"></a>
# **findAllById1**
> ActivitiesDTO findAllById1(activityId, expand)

Finds an activity for a user by id.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
Integer activityId = 56; // Integer | 
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=creator
try {
    ActivitiesDTO result = apiInstance.findAllById1(activityId, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#findAllById1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activityId** | **Integer**|  |
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;creator | [optional] [enum: expand=creator]

### Return type

[**ActivitiesDTO**](ActivitiesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="findAllByUser1"></a>
# **findAllByUser1**
> ActivitiesDTO findAllByUser1(offset, limit, sortBy, filterBy, expand)

Finds all activities for a user.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
Integer offset = 56; // Integer | 
Integer limit = 56; // Integer | 
String sortBy = "sortBy_example"; // String | ex. sort_by=ID:asc,date_created:desc
List<String> filterBy = Arrays.asList("filterBy_example"); // List<String> | ex. filter_by=flag:dataset
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=creator
try {
    ActivitiesDTO result = apiInstance.findAllByUser1(offset, limit, sortBy, filterBy, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#findAllByUser1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **Integer**|  | [optional]
 **limit** | **Integer**|  | [optional]
 **sortBy** | **String**| ex. sort_by&#x3D;ID:asc,date_created:desc | [optional] [enum: id:asc, id:desc, date_created:asc, date_created:desc, flag:asc, flag:desc]
 **filterBy** | [**List&lt;String&gt;**](String.md)| ex. filter_by&#x3D;flag:dataset | [optional] [enum: flag:project, flag:dataset, flag:member, flag:service, flag:job]
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;creator | [optional] [enum: expand=creator]

### Return type

[**ActivitiesDTO**](ActivitiesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="findById"></a>
# **findById**
> UserProfileDTO findById(userId)

Find User by Id.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
Integer userId = 56; // Integer | 
try {
    UserProfileDTO result = apiInstance.findById(userId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#findById");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **Integer**|  |

### Return type

[**UserProfileDTO**](UserProfileDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="get4"></a>
# **get4**
> ApiKeyDTO get4(offset, limit, sortBy, filterBy)

Get all api keys.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
Integer offset = 56; // Integer | 
Integer limit = 56; // Integer | 
String sortBy = "sortBy_example"; // String | ex. sort_by=Name:asc,created:desc,modified:desc
List<String> filterBy = Arrays.asList("filterBy_example"); // List<String> | ex. filter_by=name:key, created:2019-01-01T00:00:00.000, created_lt:2019-01-01T00:00:00.000, created_gt:2019-01-01T00:00:00.000, modified:2019-01-01T00:00:00.000, modified_lt:2019-01-01T00:00:00.000, modified_gt:2019-01-01T00:00:00.000
try {
    ApiKeyDTO result = apiInstance.get4(offset, limit, sortBy, filterBy);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#get4");
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

<a name="getAllSecrets"></a>
# **getAllSecrets**
> SecretDTO getAllSecrets()

Retrieves all secrets&#x27; names of a user

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
try {
    SecretDTO result = apiInstance.getAllSecrets();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#getAllSecrets");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SecretDTO**](SecretDTO.md)

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
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
String key = "key_example"; // String | 
try {
    ApiKeyDTO result = apiInstance.getByKey(key);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#getByKey");
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
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
String name = "name_example"; // String | 
try {
    ApiKeyDTO result = apiInstance.getByName3(name);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#getByName3");
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

<a name="getQRCode"></a>
# **getQRCode**
> RESTApiJsonResponse getQRCode(password)

Gets the logedin User&#x27;s QR code.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
String password = "password_example"; // String | 
try {
    RESTApiJsonResponse result = apiInstance.getQRCode(password);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#getQRCode");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | [**String**](.md)|  | [optional]

### Return type

[**RESTApiJsonResponse**](RESTApiJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

<a name="getRole"></a>
# **getRole**
> UserProjectDTO getRole(projectId)

Gets the logedin User&#x27;s role in project.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
Integer projectId = 56; // Integer | 
try {
    UserProjectDTO result = apiInstance.getRole(projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#getRole");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | [**Integer**](.md)|  | [optional]

### Return type

[**UserProjectDTO**](UserProjectDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

<a name="getScopes"></a>
# **getScopes**
> getScopes()

Get all api keys scopes.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
try {
    apiInstance.getScopes();
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#getScopes");
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

<a name="getSecret"></a>
# **getSecret**
> SecretDTO getSecret(secretName)

Gets the value of a private secret

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
String secretName = "secretName_example"; // String | 
try {
    SecretDTO result = apiInstance.getSecret(secretName);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#getSecret");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secretName** | **String**|  |

### Return type

[**SecretDTO**](SecretDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getSharedSecret"></a>
# **getSharedSecret**
> SecretDTO getSharedSecret(name, owner)

Gets the value of a shared secret

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
String name = "name_example"; // String | 
String owner = "owner_example"; // String | 
try {
    SecretDTO result = apiInstance.getSharedSecret(name, owner);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#getSharedSecret");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**|  | [optional]
 **owner** | **String**|  | [optional]

### Return type

[**SecretDTO**](SecretDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getUserProfile"></a>
# **getUserProfile**
> UserProfileDTO getUserProfile()

Gets logged in User&#x27;s info.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
try {
    UserProfileDTO result = apiInstance.getUserProfile();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#getUserProfile");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserProfileDTO**](UserProfileDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="update1"></a>
# **update1**
> ApiKeyDTO update1(name, action, scope)

Update an api key.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
String name = "name_example"; // String | 
String action = "action_example"; // String | 
List<String> scope = Arrays.asList("scope_example"); // List<String> | 
try {
    ApiKeyDTO result = apiInstance.update1(name, action, scope);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#update1");
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

<a name="updateProfile"></a>
# **updateProfile**
> UserProfileDTO updateProfile(firstname, lastname, phoneNumber, toursState)

Updates logged in User&#x27;s info.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UsersApi;


UsersApi apiInstance = new UsersApi();
String firstname = "firstname_example"; // String | 
String lastname = "lastname_example"; // String | 
String phoneNumber = "phoneNumber_example"; // String | 
Integer toursState = 56; // Integer | 
try {
    UserProfileDTO result = apiInstance.updateProfile(firstname, lastname, phoneNumber, toursState);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#updateProfile");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firstname** | [**String**](.md)|  | [optional]
 **lastname** | [**String**](.md)|  | [optional]
 **phoneNumber** | [**String**](.md)|  | [optional]
 **toursState** | [**Integer**](.md)|  | [optional]

### Return type

[**UserProfileDTO**](UserProfileDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

