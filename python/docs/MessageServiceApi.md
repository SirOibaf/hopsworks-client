# swagger_client.MessageServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_unread_messages_by_user**](MessageServiceApi.md#count_unread_messages_by_user) | **GET** /message/countUnread | 
[**delete_message**](MessageServiceApi.md#delete_message) | **DELETE** /message/{msgId} | 
[**empty_trash**](MessageServiceApi.md#empty_trash) | **DELETE** /message/empty | 
[**get_all_deleted_messages_by_user**](MessageServiceApi.md#get_all_deleted_messages_by_user) | **GET** /message/deleted | 
[**get_all_messages_by_user**](MessageServiceApi.md#get_all_messages_by_user) | **GET** /message | 
[**mark_as_read**](MessageServiceApi.md#mark_as_read) | **PUT** /message/markAsRead/{msgId} | 
[**move_to_trash**](MessageServiceApi.md#move_to_trash) | **PUT** /message/moveToTrash/{msgId} | 
[**reply**](MessageServiceApi.md#reply) | **POST** /message/reply/{msgId} | 
[**restore_from_trash**](MessageServiceApi.md#restore_from_trash) | **PUT** /message/restoreFromTrash/{msgId} | 

# **count_unread_messages_by_user**
> count_unread_messages_by_user()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageServiceApi()

try:
    api_instance.count_unread_messages_by_user()
except ApiException as e:
    print("Exception when calling MessageServiceApi->count_unread_messages_by_user: %s\n" % e)
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

# **delete_message**
> delete_message(msg_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageServiceApi()
msg_id = 56 # int | 

try:
    api_instance.delete_message(msg_id)
except ApiException as e:
    print("Exception when calling MessageServiceApi->delete_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msg_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **empty_trash**
> empty_trash()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageServiceApi()

try:
    api_instance.empty_trash()
except ApiException as e:
    print("Exception when calling MessageServiceApi->empty_trash: %s\n" % e)
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

# **get_all_deleted_messages_by_user**
> get_all_deleted_messages_by_user()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageServiceApi()

try:
    api_instance.get_all_deleted_messages_by_user()
except ApiException as e:
    print("Exception when calling MessageServiceApi->get_all_deleted_messages_by_user: %s\n" % e)
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

# **get_all_messages_by_user**
> get_all_messages_by_user()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageServiceApi()

try:
    api_instance.get_all_messages_by_user()
except ApiException as e:
    print("Exception when calling MessageServiceApi->get_all_messages_by_user: %s\n" % e)
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

# **mark_as_read**
> mark_as_read(msg_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageServiceApi()
msg_id = 56 # int | 

try:
    api_instance.mark_as_read(msg_id)
except ApiException as e:
    print("Exception when calling MessageServiceApi->mark_as_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msg_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_to_trash**
> move_to_trash(msg_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageServiceApi()
msg_id = 56 # int | 

try:
    api_instance.move_to_trash(msg_id)
except ApiException as e:
    print("Exception when calling MessageServiceApi->move_to_trash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msg_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reply**
> reply(msg_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageServiceApi()
msg_id = 56 # int | 
body = 'body_example' # str |  (optional)

try:
    api_instance.reply(msg_id, body=body)
except ApiException as e:
    print("Exception when calling MessageServiceApi->reply: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msg_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_from_trash**
> restore_from_trash(msg_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageServiceApi()
msg_id = 56 # int | 

try:
    api_instance.restore_from_trash(msg_id)
except ApiException as e:
    print("Exception when calling MessageServiceApi->restore_from_trash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msg_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

