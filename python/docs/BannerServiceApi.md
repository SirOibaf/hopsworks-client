# swagger_client.BannerServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_pwd_changed**](BannerServiceApi.md#admin_pwd_changed) | **GET** /banner/admin_pwd_changed | 
[**find_banner**](BannerServiceApi.md#find_banner) | **GET** /banner | 
[**find_user_banner**](BannerServiceApi.md#find_user_banner) | **GET** /banner/user | 
[**first_login**](BannerServiceApi.md#first_login) | **GET** /banner/firstlogin | 
[**is_first_time_login**](BannerServiceApi.md#is_first_time_login) | **GET** /banner/firsttime | 

# **admin_pwd_changed**
> admin_pwd_changed()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BannerServiceApi()

try:
    api_instance.admin_pwd_changed()
except ApiException as e:
    print("Exception when calling BannerServiceApi->admin_pwd_changed: %s\n" % e)
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

# **find_banner**
> find_banner()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BannerServiceApi()

try:
    api_instance.find_banner()
except ApiException as e:
    print("Exception when calling BannerServiceApi->find_banner: %s\n" % e)
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

# **find_user_banner**
> find_user_banner()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BannerServiceApi()

try:
    api_instance.find_user_banner()
except ApiException as e:
    print("Exception when calling BannerServiceApi->find_user_banner: %s\n" % e)
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

# **first_login**
> first_login()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BannerServiceApi()

try:
    api_instance.first_login()
except ApiException as e:
    print("Exception when calling BannerServiceApi->first_login: %s\n" % e)
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

# **is_first_time_login**
> is_first_time_login()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BannerServiceApi()

try:
    api_instance.is_first_time_login()
except ApiException as e:
    print("Exception when calling BannerServiceApi->is_first_time_login: %s\n" % e)
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

