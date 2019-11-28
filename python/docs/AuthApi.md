# swagger_client.AuthApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jwt_session**](AuthApi.md#jwt_session) | **GET** /auth/jwt/session | 
[**login**](AuthApi.md#login) | **GET** /auth/isAdmin | 
[**login1**](AuthApi.md#login1) | **POST** /auth/login | 
[**logout**](AuthApi.md#logout) | **GET** /auth/logout | 
[**password_recovery**](AuthApi.md#password_recovery) | **POST** /auth/reset/password | 
[**qr_code_recovery**](AuthApi.md#qr_code_recovery) | **POST** /auth/reset/qrCode | 
[**recover_password**](AuthApi.md#recover_password) | **POST** /auth/recover/password | 
[**recover_qr_code**](AuthApi.md#recover_qr_code) | **POST** /auth/recover/qrCode | 
[**register1**](AuthApi.md#register1) | **POST** /auth/register | 
[**service_login**](AuthApi.md#service_login) | **POST** /auth/service | 
[**service_logout**](AuthApi.md#service_logout) | **DELETE** /auth/service | 
[**session**](AuthApi.md#session) | **GET** /auth/session | 
[**validate_password_recovery**](AuthApi.md#validate_password_recovery) | **POST** /auth/reset/validate | 
[**validate_user_mail**](AuthApi.md#validate_user_mail) | **POST** /auth/validate/email | 

# **jwt_session**
> jwt_session()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()

try:
    api_instance.jwt_session()
except ApiException as e:
    print("Exception when calling AuthApi->jwt_session: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> login()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()

try:
    api_instance.login()
except ApiException as e:
    print("Exception when calling AuthApi->login: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login1**
> login1(email=email, password=password, otp=otp)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
email = 'email_example' # str |  (optional)
password = 'password_example' # str |  (optional)
otp = 'otp_example' # str |  (optional)

try:
    api_instance.login1(email=email, password=password, otp=otp)
except ApiException as e:
    print("Exception when calling AuthApi->login1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**str**](.md)|  | [optional] 
 **password** | [**str**](.md)|  | [optional] 
 **otp** | [**str**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()

try:
    api_instance.logout()
except ApiException as e:
    print("Exception when calling AuthApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_recovery**
> password_recovery(key=key, new_password=new_password, confirm_password=confirm_password)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
key = 'key_example' # str |  (optional)
new_password = 'new_password_example' # str |  (optional)
confirm_password = 'confirm_password_example' # str |  (optional)

try:
    api_instance.password_recovery(key=key, new_password=new_password, confirm_password=confirm_password)
except ApiException as e:
    print("Exception when calling AuthApi->password_recovery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | [**str**](.md)|  | [optional] 
 **new_password** | [**str**](.md)|  | [optional] 
 **confirm_password** | [**str**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qr_code_recovery**
> qr_code_recovery(key=key)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
key = 'key_example' # str |  (optional)

try:
    api_instance.qr_code_recovery(key=key)
except ApiException as e:
    print("Exception when calling AuthApi->qr_code_recovery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | [**str**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recover_password**
> recover_password(email=email, security_question=security_question, security_answer=security_answer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
email = 'email_example' # str |  (optional)
security_question = 'security_question_example' # str |  (optional)
security_answer = 'security_answer_example' # str |  (optional)

try:
    api_instance.recover_password(email=email, security_question=security_question, security_answer=security_answer)
except ApiException as e:
    print("Exception when calling AuthApi->recover_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**str**](.md)|  | [optional] 
 **security_question** | [**str**](.md)|  | [optional] 
 **security_answer** | [**str**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recover_qr_code**
> recover_qr_code(email=email, password=password)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
email = 'email_example' # str |  (optional)
password = 'password_example' # str |  (optional)

try:
    api_instance.recover_qr_code(email=email, password=password)
except ApiException as e:
    print("Exception when calling AuthApi->recover_qr_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**str**](.md)|  | [optional] 
 **password** | [**str**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register1**
> register1(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
body = swagger_client.UserDTO() # UserDTO |  (optional)

try:
    api_instance.register1(body=body)
except ApiException as e:
    print("Exception when calling AuthApi->register1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserDTO**](UserDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_login**
> service_login(email=email, password=password)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
email = 'email_example' # str |  (optional)
password = 'password_example' # str |  (optional)

try:
    api_instance.service_login(email=email, password=password)
except ApiException as e:
    print("Exception when calling AuthApi->service_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**str**](.md)|  | [optional] 
 **password** | [**str**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_logout**
> service_logout()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()

try:
    api_instance.service_logout()
except ApiException as e:
    print("Exception when calling AuthApi->service_logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session**
> session()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()

try:
    api_instance.session()
except ApiException as e:
    print("Exception when calling AuthApi->session: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_password_recovery**
> validate_password_recovery(key=key)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
key = 'key_example' # str |  (optional)

try:
    api_instance.validate_password_recovery(key=key)
except ApiException as e:
    print("Exception when calling AuthApi->validate_password_recovery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | [**str**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_user_mail**
> validate_user_mail(key=key)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
key = 'key_example' # str |  (optional)

try:
    api_instance.validate_user_mail(key=key)
except ApiException as e:
    print("Exception when calling AuthApi->validate_user_mail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | [**str**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

