# AuthApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jwtSession**](AuthApi.md#jwtSession) | **GET** /auth/jwt/session | 
[**login**](AuthApi.md#login) | **GET** /auth/isAdmin | 
[**login1**](AuthApi.md#login1) | **POST** /auth/login | 
[**logout**](AuthApi.md#logout) | **GET** /auth/logout | 
[**passwordRecovery**](AuthApi.md#passwordRecovery) | **POST** /auth/reset/password | 
[**qrCodeRecovery**](AuthApi.md#qrCodeRecovery) | **POST** /auth/reset/qrCode | 
[**recoverPassword**](AuthApi.md#recoverPassword) | **POST** /auth/recover/password | 
[**recoverQRCode**](AuthApi.md#recoverQRCode) | **POST** /auth/recover/qrCode | 
[**register1**](AuthApi.md#register1) | **POST** /auth/register | 
[**serviceLogin**](AuthApi.md#serviceLogin) | **POST** /auth/service | 
[**serviceLogout**](AuthApi.md#serviceLogout) | **DELETE** /auth/service | 
[**session**](AuthApi.md#session) | **GET** /auth/session | 
[**validatePasswordRecovery**](AuthApi.md#validatePasswordRecovery) | **POST** /auth/reset/validate | 
[**validateUserMail**](AuthApi.md#validateUserMail) | **POST** /auth/validate/email | 

<a name="jwtSession"></a>
# **jwtSession**
> jwtSession()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AuthApi;


AuthApi apiInstance = new AuthApi();
try {
    apiInstance.jwtSession();
} catch (ApiException e) {
    System.err.println("Exception when calling AuthApi#jwtSession");
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

<a name="login"></a>
# **login**
> login()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AuthApi;


AuthApi apiInstance = new AuthApi();
try {
    apiInstance.login();
} catch (ApiException e) {
    System.err.println("Exception when calling AuthApi#login");
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

<a name="login1"></a>
# **login1**
> login1(email, password, otp)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AuthApi;


AuthApi apiInstance = new AuthApi();
String email = "email_example"; // String | 
String password = "password_example"; // String | 
String otp = "otp_example"; // String | 
try {
    apiInstance.login1(email, password, otp);
} catch (ApiException e) {
    System.err.println("Exception when calling AuthApi#login1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**String**](.md)|  | [optional]
 **password** | [**String**](.md)|  | [optional]
 **otp** | [**String**](.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

<a name="logout"></a>
# **logout**
> logout()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AuthApi;


AuthApi apiInstance = new AuthApi();
try {
    apiInstance.logout();
} catch (ApiException e) {
    System.err.println("Exception when calling AuthApi#logout");
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

<a name="passwordRecovery"></a>
# **passwordRecovery**
> passwordRecovery(key, newPassword, confirmPassword)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AuthApi;


AuthApi apiInstance = new AuthApi();
String key = "key_example"; // String | 
String newPassword = "newPassword_example"; // String | 
String confirmPassword = "confirmPassword_example"; // String | 
try {
    apiInstance.passwordRecovery(key, newPassword, confirmPassword);
} catch (ApiException e) {
    System.err.println("Exception when calling AuthApi#passwordRecovery");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | [**String**](.md)|  | [optional]
 **newPassword** | [**String**](.md)|  | [optional]
 **confirmPassword** | [**String**](.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

<a name="qrCodeRecovery"></a>
# **qrCodeRecovery**
> qrCodeRecovery(key)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AuthApi;


AuthApi apiInstance = new AuthApi();
String key = "key_example"; // String | 
try {
    apiInstance.qrCodeRecovery(key);
} catch (ApiException e) {
    System.err.println("Exception when calling AuthApi#qrCodeRecovery");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | [**String**](.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

<a name="recoverPassword"></a>
# **recoverPassword**
> recoverPassword(email, securityQuestion, securityAnswer)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AuthApi;


AuthApi apiInstance = new AuthApi();
String email = "email_example"; // String | 
String securityQuestion = "securityQuestion_example"; // String | 
String securityAnswer = "securityAnswer_example"; // String | 
try {
    apiInstance.recoverPassword(email, securityQuestion, securityAnswer);
} catch (ApiException e) {
    System.err.println("Exception when calling AuthApi#recoverPassword");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**String**](.md)|  | [optional]
 **securityQuestion** | [**String**](.md)|  | [optional]
 **securityAnswer** | [**String**](.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

<a name="recoverQRCode"></a>
# **recoverQRCode**
> recoverQRCode(email, password)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AuthApi;


AuthApi apiInstance = new AuthApi();
String email = "email_example"; // String | 
String password = "password_example"; // String | 
try {
    apiInstance.recoverQRCode(email, password);
} catch (ApiException e) {
    System.err.println("Exception when calling AuthApi#recoverQRCode");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**String**](.md)|  | [optional]
 **password** | [**String**](.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

<a name="register1"></a>
# **register1**
> register1(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AuthApi;


AuthApi apiInstance = new AuthApi();
UserDTO body = new UserDTO(); // UserDTO | 
try {
    apiInstance.register1(body);
} catch (ApiException e) {
    System.err.println("Exception when calling AuthApi#register1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserDTO**](UserDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="serviceLogin"></a>
# **serviceLogin**
> serviceLogin(email, password)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AuthApi;


AuthApi apiInstance = new AuthApi();
String email = "email_example"; // String | 
String password = "password_example"; // String | 
try {
    apiInstance.serviceLogin(email, password);
} catch (ApiException e) {
    System.err.println("Exception when calling AuthApi#serviceLogin");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**String**](.md)|  | [optional]
 **password** | [**String**](.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

<a name="serviceLogout"></a>
# **serviceLogout**
> serviceLogout()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AuthApi;


AuthApi apiInstance = new AuthApi();
try {
    apiInstance.serviceLogout();
} catch (ApiException e) {
    System.err.println("Exception when calling AuthApi#serviceLogout");
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

<a name="session"></a>
# **session**
> session()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AuthApi;


AuthApi apiInstance = new AuthApi();
try {
    apiInstance.session();
} catch (ApiException e) {
    System.err.println("Exception when calling AuthApi#session");
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

<a name="validatePasswordRecovery"></a>
# **validatePasswordRecovery**
> validatePasswordRecovery(key)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AuthApi;


AuthApi apiInstance = new AuthApi();
String key = "key_example"; // String | 
try {
    apiInstance.validatePasswordRecovery(key);
} catch (ApiException e) {
    System.err.println("Exception when calling AuthApi#validatePasswordRecovery");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | [**String**](.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

<a name="validateUserMail"></a>
# **validateUserMail**
> validateUserMail(key)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AuthApi;


AuthApi apiInstance = new AuthApi();
String key = "key_example"; // String | 
try {
    apiInstance.validateUserMail(key);
} catch (ApiException e) {
    System.err.println("Exception when calling AuthApi#validateUserMail");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | [**String**](.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

