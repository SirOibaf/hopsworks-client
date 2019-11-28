# swagger_client.UsersApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_secret**](UsersApi.md#add_secret) | **POST** /users/secrets | Stores a secret for user
[**change_login_credentials**](UsersApi.md#change_login_credentials) | **POST** /users/credentials | Updates logedin User&#x27;s credentials.
[**change_security_qa**](UsersApi.md#change_security_qa) | **POST** /users/securityQA | Updates logedin User&#x27;s security quesion and answer.
[**change_two_factor**](UsersApi.md#change_two_factor) | **POST** /users/twoFactor | Updates logedin User&#x27;s two factor setting.
[**check_session**](UsersApi.md#check_session) | **GET** /users/apiKey/session | Check api key session.
[**create**](UsersApi.md#create) | **POST** /users/apiKey | Create an api key.
[**delete_all**](UsersApi.md#delete_all) | **DELETE** /users/apiKey | Delete all api keys.
[**delete_all_secrets**](UsersApi.md#delete_all_secrets) | **DELETE** /users/secrets | Deletes all secrets of a user
[**delete_by_name**](UsersApi.md#delete_by_name) | **DELETE** /users/apiKey/{name} | Delete api key by name.
[**delete_secret**](UsersApi.md#delete_secret) | **DELETE** /users/secrets/{secretName} | Deletes a secret by its name
[**find_all**](UsersApi.md#find_all) | **GET** /users | Get all users.
[**find_all_by_id1**](UsersApi.md#find_all_by_id1) | **GET** /users/activities/{activityId} | Finds an activity for a user by id.
[**find_all_by_user1**](UsersApi.md#find_all_by_user1) | **GET** /users/activities | Finds all activities for a user.
[**find_by_id**](UsersApi.md#find_by_id) | **GET** /users/{userId} | Find User by Id.
[**get4**](UsersApi.md#get4) | **GET** /users/apiKey | Get all api keys.
[**get_all_secrets**](UsersApi.md#get_all_secrets) | **GET** /users/secrets | Retrieves all secrets&#x27; names of a user
[**get_by_key**](UsersApi.md#get_by_key) | **GET** /users/apiKey/key | Find api key by name.
[**get_by_name3**](UsersApi.md#get_by_name3) | **GET** /users/apiKey/{name} | Find api key by name.
[**get_qr_code**](UsersApi.md#get_qr_code) | **POST** /users/getQRCode | Gets the logedin User&#x27;s QR code.
[**get_role**](UsersApi.md#get_role) | **POST** /users/getRole | Gets the logedin User&#x27;s role in project.
[**get_scopes**](UsersApi.md#get_scopes) | **GET** /users/apiKey/scopes | Get all api keys scopes.
[**get_secret**](UsersApi.md#get_secret) | **GET** /users/secrets/{secretName} | Gets the value of a private secret
[**get_shared_secret**](UsersApi.md#get_shared_secret) | **GET** /users/secrets/shared | Gets the value of a shared secret
[**get_user_profile**](UsersApi.md#get_user_profile) | **GET** /users/profile | Gets logged in User&#x27;s info.
[**update1**](UsersApi.md#update1) | **PUT** /users/apiKey | Update an api key.
[**update_profile**](UsersApi.md#update_profile) | **POST** /users/profile | Updates logged in User&#x27;s info.

# **add_secret**
> add_secret(body=body)

Stores a secret for user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.SecretDTO() # SecretDTO |  (optional)

try:
    # Stores a secret for user
    api_instance.add_secret(body=body)
except ApiException as e:
    print("Exception when calling UsersApi->add_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecretDTO**](SecretDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_login_credentials**
> RESTApiJsonResponse change_login_credentials(old_password=old_password, new_password=new_password, confirmed_password=confirmed_password)

Updates logedin User's credentials.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
old_password = 'old_password_example' # str |  (optional)
new_password = 'new_password_example' # str |  (optional)
confirmed_password = 'confirmed_password_example' # str |  (optional)

try:
    # Updates logedin User's credentials.
    api_response = api_instance.change_login_credentials(old_password=old_password, new_password=new_password, confirmed_password=confirmed_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->change_login_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **old_password** | [**str**](.md)|  | [optional] 
 **new_password** | [**str**](.md)|  | [optional] 
 **confirmed_password** | [**str**](.md)|  | [optional] 

### Return type

[**RESTApiJsonResponse**](RESTApiJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_security_qa**
> RESTApiJsonResponse change_security_qa(old_password=old_password, security_question=security_question, security_answer=security_answer)

Updates logedin User's security quesion and answer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
old_password = 'old_password_example' # str |  (optional)
security_question = 'security_question_example' # str |  (optional)
security_answer = 'security_answer_example' # str |  (optional)

try:
    # Updates logedin User's security quesion and answer.
    api_response = api_instance.change_security_qa(old_password=old_password, security_question=security_question, security_answer=security_answer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->change_security_qa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **old_password** | [**str**](.md)|  | [optional] 
 **security_question** | [**str**](.md)|  | [optional] 
 **security_answer** | [**str**](.md)|  | [optional] 

### Return type

[**RESTApiJsonResponse**](RESTApiJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_two_factor**
> RESTApiJsonResponse change_two_factor(password=password, two_factor=two_factor)

Updates logedin User's two factor setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
password = 'password_example' # str |  (optional)
two_factor = True # bool |  (optional)

try:
    # Updates logedin User's two factor setting.
    api_response = api_instance.change_two_factor(password=password, two_factor=two_factor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->change_two_factor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | [**str**](.md)|  | [optional] 
 **two_factor** | [**bool**](.md)|  | [optional] 

### Return type

[**RESTApiJsonResponse**](RESTApiJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_session**
> check_session()

Check api key session.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()

try:
    # Check api key session.
    api_instance.check_session()
except ApiException as e:
    print("Exception when calling UsersApi->check_session: %s\n" % e)
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

# **create**
> ApiKeyDTO create(name=name, scope=scope)

Create an api key.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
name = 'name_example' # str |  (optional)
scope = ['scope_example'] # list[str] |  (optional)

try:
    # Create an api key.
    api_response = api_instance.create(name=name, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **scope** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**ApiKeyDTO**](ApiKeyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all**
> delete_all()

Delete all api keys.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()

try:
    # Delete all api keys.
    api_instance.delete_all()
except ApiException as e:
    print("Exception when calling UsersApi->delete_all: %s\n" % e)
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

# **delete_all_secrets**
> delete_all_secrets()

Deletes all secrets of a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()

try:
    # Deletes all secrets of a user
    api_instance.delete_all_secrets()
except ApiException as e:
    print("Exception when calling UsersApi->delete_all_secrets: %s\n" % e)
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

# **delete_by_name**
> delete_by_name(name)

Delete api key by name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
name = 'name_example' # str | 

try:
    # Delete api key by name.
    api_instance.delete_by_name(name)
except ApiException as e:
    print("Exception when calling UsersApi->delete_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_secret**
> delete_secret(secret_name)

Deletes a secret by its name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
secret_name = 'secret_name_example' # str | 

try:
    # Deletes a secret by its name
    api_instance.delete_secret(secret_name)
except ApiException as e:
    print("Exception when calling UsersApi->delete_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all**
> UserDTO find_all(offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by)

Get all users.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
sort_by = 'sort_by_example' # str | ex. sort_by=first_name:asc,last_name:desc (optional)
filter_by = ['filter_by_example'] # list[str] | ex. filter_by=role:hops_admin,hops_user&filter_by=status:2 (optional)

try:
    # Get all users.
    api_response = api_instance.find_all(offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort_by** | **str**| ex. sort_by&#x3D;first_name:asc,last_name:desc | [optional] 
 **filter_by** | [**list[str]**](str.md)| ex. filter_by&#x3D;role:hops_admin,hops_user&amp;filter_by&#x3D;status:2 | [optional] 

### Return type

[**UserDTO**](UserDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_by_id1**
> ActivitiesDTO find_all_by_id1(activity_id, expand=expand)

Finds an activity for a user by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
activity_id = 56 # int | 
expand = ['expand_example'] # list[str] | ex. expand=creator (optional)

try:
    # Finds an activity for a user by id.
    api_response = api_instance.find_all_by_id1(activity_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->find_all_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**|  | 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;creator | [optional] 

### Return type

[**ActivitiesDTO**](ActivitiesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_by_user1**
> ActivitiesDTO find_all_by_user1(offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by, expand=expand)

Finds all activities for a user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
sort_by = 'sort_by_example' # str | ex. sort_by=ID:asc,date_created:desc (optional)
filter_by = ['filter_by_example'] # list[str] | ex. filter_by=flag:dataset (optional)
expand = ['expand_example'] # list[str] | ex. expand=creator (optional)

try:
    # Finds all activities for a user.
    api_response = api_instance.find_all_by_user1(offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->find_all_by_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort_by** | **str**| ex. sort_by&#x3D;ID:asc,date_created:desc | [optional] 
 **filter_by** | [**list[str]**](str.md)| ex. filter_by&#x3D;flag:dataset | [optional] 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;creator | [optional] 

### Return type

[**ActivitiesDTO**](ActivitiesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_id**
> UserProfileDTO find_by_id(user_id)

Find User by Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 56 # int | 

try:
    # Find User by Id.
    api_response = api_instance.find_by_id(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->find_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**UserProfileDTO**](UserProfileDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get4**
> ApiKeyDTO get4(offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by)

Get all api keys.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
sort_by = 'sort_by_example' # str | ex. sort_by=Name:asc,created:desc,modified:desc (optional)
filter_by = ['filter_by_example'] # list[str] | ex. filter_by=name:key, created:2019-01-01T00:00:00.000, created_lt:2019-01-01T00:00:00.000, created_gt:2019-01-01T00:00:00.000, modified:2019-01-01T00:00:00.000, modified_lt:2019-01-01T00:00:00.000, modified_gt:2019-01-01T00:00:00.000 (optional)

try:
    # Get all api keys.
    api_response = api_instance.get4(offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort_by** | **str**| ex. sort_by&#x3D;Name:asc,created:desc,modified:desc | [optional] 
 **filter_by** | [**list[str]**](str.md)| ex. filter_by&#x3D;name:key, created:2019-01-01T00:00:00.000, created_lt:2019-01-01T00:00:00.000, created_gt:2019-01-01T00:00:00.000, modified:2019-01-01T00:00:00.000, modified_lt:2019-01-01T00:00:00.000, modified_gt:2019-01-01T00:00:00.000 | [optional] 

### Return type

[**ApiKeyDTO**](ApiKeyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_secrets**
> SecretDTO get_all_secrets()

Retrieves all secrets' names of a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()

try:
    # Retrieves all secrets' names of a user
    api_response = api_instance.get_all_secrets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_all_secrets: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_key**
> ApiKeyDTO get_by_key(key=key)

Find api key by name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
key = 'key_example' # str |  (optional)

try:
    # Find api key by name.
    api_response = api_instance.get_by_key(key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | [optional] 

### Return type

[**ApiKeyDTO**](ApiKeyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_name3**
> ApiKeyDTO get_by_name3(name)

Find api key by name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
name = 'name_example' # str | 

try:
    # Find api key by name.
    api_response = api_instance.get_by_name3(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_by_name3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ApiKeyDTO**](ApiKeyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_qr_code**
> RESTApiJsonResponse get_qr_code(password=password)

Gets the logedin User's QR code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
password = 'password_example' # str |  (optional)

try:
    # Gets the logedin User's QR code.
    api_response = api_instance.get_qr_code(password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_qr_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | [**str**](.md)|  | [optional] 

### Return type

[**RESTApiJsonResponse**](RESTApiJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> UserProjectDTO get_role(project_id=project_id)

Gets the logedin User's role in project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
project_id = 56 # int |  (optional)

try:
    # Gets the logedin User's role in project.
    api_response = api_instance.get_role(project_id=project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**int**](.md)|  | [optional] 

### Return type

[**UserProjectDTO**](UserProjectDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scopes**
> get_scopes()

Get all api keys scopes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()

try:
    # Get all api keys scopes.
    api_instance.get_scopes()
except ApiException as e:
    print("Exception when calling UsersApi->get_scopes: %s\n" % e)
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

# **get_secret**
> SecretDTO get_secret(secret_name)

Gets the value of a private secret

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
secret_name = 'secret_name_example' # str | 

try:
    # Gets the value of a private secret
    api_response = api_instance.get_secret(secret_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_name** | **str**|  | 

### Return type

[**SecretDTO**](SecretDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_secret**
> SecretDTO get_shared_secret(name=name, owner=owner)

Gets the value of a shared secret

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
name = 'name_example' # str |  (optional)
owner = 'owner_example' # str |  (optional)

try:
    # Gets the value of a shared secret
    api_response = api_instance.get_shared_secret(name=name, owner=owner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_shared_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **owner** | **str**|  | [optional] 

### Return type

[**SecretDTO**](SecretDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_profile**
> UserProfileDTO get_user_profile()

Gets logged in User's info.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()

try:
    # Gets logged in User's info.
    api_response = api_instance.get_user_profile()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_profile: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update1**
> ApiKeyDTO update1(name=name, action=action, scope=scope)

Update an api key.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
name = 'name_example' # str |  (optional)
action = 'action_example' # str |  (optional)
scope = ['scope_example'] # list[str] |  (optional)

try:
    # Update an api key.
    api_response = api_instance.update1(name=name, action=action, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **action** | **str**|  | [optional] 
 **scope** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**ApiKeyDTO**](ApiKeyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**
> UserProfileDTO update_profile(firstname=firstname, lastname=lastname, phone_number=phone_number, tours_state=tours_state)

Updates logged in User's info.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
firstname = 'firstname_example' # str |  (optional)
lastname = 'lastname_example' # str |  (optional)
phone_number = 'phone_number_example' # str |  (optional)
tours_state = 56 # int |  (optional)

try:
    # Updates logged in User's info.
    api_response = api_instance.update_profile(firstname=firstname, lastname=lastname, phone_number=phone_number, tours_state=tours_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firstname** | [**str**](.md)|  | [optional] 
 **lastname** | [**str**](.md)|  | [optional] 
 **phone_number** | [**str**](.md)|  | [optional] 
 **tours_state** | [**int**](.md)|  | [optional] 

### Return type

[**UserProfileDTO**](UserProfileDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

