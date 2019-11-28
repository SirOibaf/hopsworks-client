# swagger_client.JWTServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](JWTServiceApi.md#create_token) | **POST** /jwt | Create application token
[**invalidate_service_token**](JWTServiceApi.md#invalidate_service_token) | **DELETE** /jwt/service/{token} | Invalidate a service JWT and also delete the signing key encoded in the token
[**invalidate_token**](JWTServiceApi.md#invalidate_token) | **DELETE** /jwt/{token} | Invalidate application token
[**remove_siging_key**](JWTServiceApi.md#remove_siging_key) | **DELETE** /jwt/key/{keyName} | Delete a JWT signing key
[**renew_service_token**](JWTServiceApi.md#renew_service_token) | **PUT** /jwt/service | Renew a service JWT without invalidating the previous token
[**renew_token**](JWTServiceApi.md#renew_token) | **PUT** /jwt | Renew application token

# **create_token**
> JWTResponseDTO create_token(body=body)

Create application token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JWTServiceApi()
body = swagger_client.SpecificationForGeneratingNewJWT() # SpecificationForGeneratingNewJWT |  (optional)

try:
    # Create application token
    api_response = api_instance.create_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JWTServiceApi->create_token: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_service_token**
> invalidate_service_token(token)

Invalidate a service JWT and also delete the signing key encoded in the token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JWTServiceApi()
token = 'token_example' # str | Service token to invalidate

try:
    # Invalidate a service JWT and also delete the signing key encoded in the token
    api_instance.invalidate_service_token(token)
except ApiException as e:
    print("Exception when calling JWTServiceApi->invalidate_service_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Service token to invalidate | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_token**
> invalidate_token(token)

Invalidate application token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JWTServiceApi()
token = 'token_example' # str | Token to invalidate

try:
    # Invalidate application token
    api_instance.invalidate_token(token)
except ApiException as e:
    print("Exception when calling JWTServiceApi->invalidate_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Token to invalidate | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_siging_key**
> remove_siging_key(key_name)

Delete a JWT signing key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JWTServiceApi()
key_name = 'key_name_example' # str | Name of the signing key to remove

try:
    # Delete a JWT signing key
    api_instance.remove_siging_key(key_name)
except ApiException as e:
    print("Exception when calling JWTServiceApi->remove_siging_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_name** | **str**| Name of the signing key to remove | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_service_token**
> ServiceJWTDTO renew_service_token(body=body)

Renew a service JWT without invalidating the previous token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JWTServiceApi()
body = swagger_client.SpecificationToRenewAnExistingJWT() # SpecificationToRenewAnExistingJWT |  (optional)

try:
    # Renew a service JWT without invalidating the previous token
    api_response = api_instance.renew_service_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JWTServiceApi->renew_service_token: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_token**
> JWTResponseDTO renew_token(body=body)

Renew application token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JWTServiceApi()
body = swagger_client.SpecificationToRenewAnExistingJWT() # SpecificationToRenewAnExistingJWT |  (optional)

try:
    # Renew application token
    api_response = api_instance.renew_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JWTServiceApi->renew_token: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

