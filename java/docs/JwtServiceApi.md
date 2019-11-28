# JwtServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createToken**](JwtServiceApi.md#createToken) | **POST** /jwt | Create application token
[**invalidateServiceToken**](JwtServiceApi.md#invalidateServiceToken) | **DELETE** /jwt/service/{token} | Invalidate a service JWT and also delete the signing key encoded in the token
[**invalidateToken**](JwtServiceApi.md#invalidateToken) | **DELETE** /jwt/{token} | Invalidate application token
[**removeSigingKey**](JwtServiceApi.md#removeSigingKey) | **DELETE** /jwt/key/{keyName} | Delete a JWT signing key
[**renewServiceToken**](JwtServiceApi.md#renewServiceToken) | **PUT** /jwt/service | Renew a service JWT without invalidating the previous token
[**renewToken**](JwtServiceApi.md#renewToken) | **PUT** /jwt | Renew application token

<a name="createToken"></a>
# **createToken**
> JWTResponseDTO createToken(body)

Create application token

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.JwtServiceApi;


JwtServiceApi apiInstance = new JwtServiceApi();
SpecificationForGeneratingNewJWT body = new SpecificationForGeneratingNewJWT(); // SpecificationForGeneratingNewJWT | 
try {
    JWTResponseDTO result = apiInstance.createToken(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling JwtServiceApi#createToken");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpecificationForGeneratingNewJWT**](SpecificationForGeneratingNewJWT.md)|  | [optional]

### Return type

[**JWTResponseDTO**](JWTResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="invalidateServiceToken"></a>
# **invalidateServiceToken**
> invalidateServiceToken(token)

Invalidate a service JWT and also delete the signing key encoded in the token

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.JwtServiceApi;


JwtServiceApi apiInstance = new JwtServiceApi();
String token = "token_example"; // String | Service token to invalidate
try {
    apiInstance.invalidateServiceToken(token);
} catch (ApiException e) {
    System.err.println("Exception when calling JwtServiceApi#invalidateServiceToken");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **String**| Service token to invalidate |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="invalidateToken"></a>
# **invalidateToken**
> invalidateToken(token)

Invalidate application token

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.JwtServiceApi;


JwtServiceApi apiInstance = new JwtServiceApi();
String token = "token_example"; // String | Token to invalidate
try {
    apiInstance.invalidateToken(token);
} catch (ApiException e) {
    System.err.println("Exception when calling JwtServiceApi#invalidateToken");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **String**| Token to invalidate |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="removeSigingKey"></a>
# **removeSigingKey**
> removeSigingKey(keyName)

Delete a JWT signing key

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.JwtServiceApi;


JwtServiceApi apiInstance = new JwtServiceApi();
String keyName = "keyName_example"; // String | Name of the signing key to remove
try {
    apiInstance.removeSigingKey(keyName);
} catch (ApiException e) {
    System.err.println("Exception when calling JwtServiceApi#removeSigingKey");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyName** | **String**| Name of the signing key to remove |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="renewServiceToken"></a>
# **renewServiceToken**
> ServiceJWTDTO renewServiceToken(body)

Renew a service JWT without invalidating the previous token

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.JwtServiceApi;


JwtServiceApi apiInstance = new JwtServiceApi();
SpecificationToRenewAnExistingJWT body = new SpecificationToRenewAnExistingJWT(); // SpecificationToRenewAnExistingJWT | 
try {
    ServiceJWTDTO result = apiInstance.renewServiceToken(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling JwtServiceApi#renewServiceToken");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpecificationToRenewAnExistingJWT**](SpecificationToRenewAnExistingJWT.md)|  | [optional]

### Return type

[**ServiceJWTDTO**](ServiceJWTDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="renewToken"></a>
# **renewToken**
> JWTResponseDTO renewToken(body)

Renew application token

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.JwtServiceApi;


JwtServiceApi apiInstance = new JwtServiceApi();
SpecificationToRenewAnExistingJWT body = new SpecificationToRenewAnExistingJWT(); // SpecificationToRenewAnExistingJWT | 
try {
    JWTResponseDTO result = apiInstance.renewToken(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling JwtServiceApi#renewToken");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpecificationToRenewAnExistingJWT**](SpecificationToRenewAnExistingJWT.md)|  | [optional]

### Return type

[**JWTResponseDTO**](JWTResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

