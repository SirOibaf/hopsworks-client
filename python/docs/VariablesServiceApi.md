# swagger_client.VariablesServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_auth_status**](VariablesServiceApi.md#get_auth_status) | **GET** /variables/authStatus | 
[**get_conda_default_repo**](VariablesServiceApi.md#get_conda_default_repo) | **GET** /variables/conda | 
[**get_ldap_auth_status**](VariablesServiceApi.md#get_ldap_auth_status) | **GET** /variables/ldap | 
[**get_security_questions**](VariablesServiceApi.md#get_security_questions) | **GET** /variables/securityQuestions | 
[**get_twofactor**](VariablesServiceApi.md#get_twofactor) | **GET** /variables/twofactor | 
[**get_var**](VariablesServiceApi.md#get_var) | **GET** /variables/{id} | 
[**get_versions**](VariablesServiceApi.md#get_versions) | **GET** /variables/versions | 

# **get_auth_status**
> get_auth_status()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariablesServiceApi()

try:
    api_instance.get_auth_status()
except ApiException as e:
    print("Exception when calling VariablesServiceApi->get_auth_status: %s\n" % e)
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

# **get_conda_default_repo**
> get_conda_default_repo()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariablesServiceApi()

try:
    api_instance.get_conda_default_repo()
except ApiException as e:
    print("Exception when calling VariablesServiceApi->get_conda_default_repo: %s\n" % e)
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

# **get_ldap_auth_status**
> get_ldap_auth_status()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariablesServiceApi()

try:
    api_instance.get_ldap_auth_status()
except ApiException as e:
    print("Exception when calling VariablesServiceApi->get_ldap_auth_status: %s\n" % e)
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

# **get_security_questions**
> get_security_questions()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariablesServiceApi()

try:
    api_instance.get_security_questions()
except ApiException as e:
    print("Exception when calling VariablesServiceApi->get_security_questions: %s\n" % e)
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

# **get_twofactor**
> get_twofactor()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariablesServiceApi()

try:
    api_instance.get_twofactor()
except ApiException as e:
    print("Exception when calling VariablesServiceApi->get_twofactor: %s\n" % e)
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

# **get_var**
> get_var(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariablesServiceApi()
id = 'id_example' # str | 

try:
    api_instance.get_var(id)
except ApiException as e:
    print("Exception when calling VariablesServiceApi->get_var: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versions**
> get_versions()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VariablesServiceApi()

try:
    api_instance.get_versions()
except ApiException as e:
    print("Exception when calling VariablesServiceApi->get_versions: %s\n" % e)
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

