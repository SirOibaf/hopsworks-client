# swagger_client.MetadataServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_metadata_with_schema**](MetadataServiceApi.md#add_metadata_with_schema) | **POST** /metadata/addWithSchema | 
[**attach_schemaless_metadata**](MetadataServiceApi.md#attach_schemaless_metadata) | **PUT** /metadata/schemaless/{xattrName}/{path} | Create or Update a schemaless metadata for a path.
[**detach_schemaless_metadata**](MetadataServiceApi.md#detach_schemaless_metadata) | **DELETE** /metadata/schemaless/{xattrName}/{path} | Delete the schemaless metadata attached to a path.
[**detach_template_from_inode**](MetadataServiceApi.md#detach_template_from_inode) | **GET** /metadata/detachtemplate/{inodeid}/{templateid} | 
[**fetch_available_templates_for_inode**](MetadataServiceApi.md#fetch_available_templates_for_inode) | **GET** /metadata/fetchavailabletemplatesforinode/{inodeid} | 
[**fetch_metadata**](MetadataServiceApi.md#fetch_metadata) | **GET** /metadata/fetchmetadata/{inodepid}/{inodename}/{tableid} | 
[**fetch_metadata_compact**](MetadataServiceApi.md#fetch_metadata_compact) | **GET** /metadata/{inodepid} | 
[**fetch_template**](MetadataServiceApi.md#fetch_template) | **GET** /metadata/fetchtemplate/{templateid}/{sender} | 
[**fetch_templatesfor_inode**](MetadataServiceApi.md#fetch_templatesfor_inode) | **GET** /metadata/fetchtemplatesforinode/{inodeid} | 
[**get_schemaless_metadata**](MetadataServiceApi.md#get_schemaless_metadata) | **GET** /metadata/schemaless/{xattrName}/{path} | Get the schemaless metadata attached to a path.
[**remove_metadata_with_schema**](MetadataServiceApi.md#remove_metadata_with_schema) | **POST** /metadata/removeWithSchema | 
[**test_method**](MetadataServiceApi.md#test_method) | **GET** /metadata/upload | 
[**update_metadata_with_schema**](MetadataServiceApi.md#update_metadata_with_schema) | **POST** /metadata/updateWithSchema | 
[**upload_method**](MetadataServiceApi.md#upload_method) | **POST** /metadata/upload | 

# **add_metadata_with_schema**
> add_metadata_with_schema(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataServiceApi()
body = 'body_example' # str |  (optional)

try:
    api_instance.add_metadata_with_schema(body=body)
except ApiException as e:
    print("Exception when calling MetadataServiceApi->add_metadata_with_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_schemaless_metadata**
> attach_schemaless_metadata(xattr_name, path, body=body)

Create or Update a schemaless metadata for a path.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataServiceApi()
xattr_name = 'xattr_name_example' # str | 
path = 'path_example' # str | 
body = 'body_example' # str |  (optional)

try:
    # Create or Update a schemaless metadata for a path.
    api_instance.attach_schemaless_metadata(xattr_name, path, body=body)
except ApiException as e:
    print("Exception when calling MetadataServiceApi->attach_schemaless_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xattr_name** | **str**|  | 
 **path** | **str**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_schemaless_metadata**
> detach_schemaless_metadata(xattr_name, path)

Delete the schemaless metadata attached to a path.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataServiceApi()
xattr_name = 'xattr_name_example' # str | 
path = 'path_example' # str | 

try:
    # Delete the schemaless metadata attached to a path.
    api_instance.detach_schemaless_metadata(xattr_name, path)
except ApiException as e:
    print("Exception when calling MetadataServiceApi->detach_schemaless_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xattr_name** | **str**|  | 
 **path** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_template_from_inode**
> detach_template_from_inode(inodeid, templateid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataServiceApi()
inodeid = 789 # int | 
templateid = 56 # int | 

try:
    api_instance.detach_template_from_inode(inodeid, templateid)
except ApiException as e:
    print("Exception when calling MetadataServiceApi->detach_template_from_inode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inodeid** | **int**|  | 
 **templateid** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_available_templates_for_inode**
> fetch_available_templates_for_inode(inodeid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataServiceApi()
inodeid = 789 # int | 

try:
    api_instance.fetch_available_templates_for_inode(inodeid)
except ApiException as e:
    print("Exception when calling MetadataServiceApi->fetch_available_templates_for_inode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inodeid** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_metadata**
> fetch_metadata(inodepid, inodename, tableid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataServiceApi()
inodepid = 789 # int | 
inodename = 'inodename_example' # str | 
tableid = 56 # int | 

try:
    api_instance.fetch_metadata(inodepid, inodename, tableid)
except ApiException as e:
    print("Exception when calling MetadataServiceApi->fetch_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inodepid** | **int**|  | 
 **inodename** | **str**|  | 
 **tableid** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_metadata_compact**
> fetch_metadata_compact(inodepid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataServiceApi()
inodepid = 789 # int | 

try:
    api_instance.fetch_metadata_compact(inodepid)
except ApiException as e:
    print("Exception when calling MetadataServiceApi->fetch_metadata_compact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inodepid** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_template**
> fetch_template(templateid, sender)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataServiceApi()
templateid = 56 # int | 
sender = 'sender_example' # str | 

try:
    api_instance.fetch_template(templateid, sender)
except ApiException as e:
    print("Exception when calling MetadataServiceApi->fetch_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateid** | **int**|  | 
 **sender** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_templatesfor_inode**
> fetch_templatesfor_inode(inodeid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataServiceApi()
inodeid = 789 # int | 

try:
    api_instance.fetch_templatesfor_inode(inodeid)
except ApiException as e:
    print("Exception when calling MetadataServiceApi->fetch_templatesfor_inode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inodeid** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schemaless_metadata**
> get_schemaless_metadata(xattr_name, path)

Get the schemaless metadata attached to a path.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataServiceApi()
xattr_name = 'xattr_name_example' # str | 
path = 'path_example' # str | 

try:
    # Get the schemaless metadata attached to a path.
    api_instance.get_schemaless_metadata(xattr_name, path)
except ApiException as e:
    print("Exception when calling MetadataServiceApi->get_schemaless_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xattr_name** | **str**|  | 
 **path** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_metadata_with_schema**
> remove_metadata_with_schema(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataServiceApi()
body = 'body_example' # str |  (optional)

try:
    api_instance.remove_metadata_with_schema(body=body)
except ApiException as e:
    print("Exception when calling MetadataServiceApi->remove_metadata_with_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_method**
> test_method()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataServiceApi()

try:
    api_instance.test_method()
except ApiException as e:
    print("Exception when calling MetadataServiceApi->test_method: %s\n" % e)
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

# **update_metadata_with_schema**
> update_metadata_with_schema(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataServiceApi()
body = 'body_example' # str |  (optional)

try:
    api_instance.update_metadata_with_schema(body=body)
except ApiException as e:
    print("Exception when calling MetadataServiceApi->update_metadata_with_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_method**
> upload_method(file=file, flow_chunk_number=flow_chunk_number, flow_chunk_size=flow_chunk_size, flow_current_chunk_size=flow_current_chunk_size, flow_filename=flow_filename, flow_identifier=flow_identifier, flow_relative_path=flow_relative_path, flow_total_chunks=flow_total_chunks, flow_total_size=flow_total_size)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataServiceApi()
file = 'file_example' # file |  (optional)
flow_chunk_number = 'flow_chunk_number_example' # str |  (optional)
flow_chunk_size = 'flow_chunk_size_example' # str |  (optional)
flow_current_chunk_size = 'flow_current_chunk_size_example' # str |  (optional)
flow_filename = 'flow_filename_example' # str |  (optional)
flow_identifier = 'flow_identifier_example' # str |  (optional)
flow_relative_path = 'flow_relative_path_example' # str |  (optional)
flow_total_chunks = 'flow_total_chunks_example' # str |  (optional)
flow_total_size = 'flow_total_size_example' # str |  (optional)

try:
    api_instance.upload_method(file=file, flow_chunk_number=flow_chunk_number, flow_chunk_size=flow_chunk_size, flow_current_chunk_size=flow_current_chunk_size, flow_filename=flow_filename, flow_identifier=flow_identifier, flow_relative_path=flow_relative_path, flow_total_chunks=flow_total_chunks, flow_total_size=flow_total_size)
except ApiException as e:
    print("Exception when calling MetadataServiceApi->upload_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**|  | [optional] 
 **flow_chunk_number** | [**str**](.md)|  | [optional] 
 **flow_chunk_size** | [**str**](.md)|  | [optional] 
 **flow_current_chunk_size** | [**str**](.md)|  | [optional] 
 **flow_filename** | [**str**](.md)|  | [optional] 
 **flow_identifier** | [**str**](.md)|  | [optional] 
 **flow_relative_path** | [**str**](.md)|  | [optional] 
 **flow_total_chunks** | [**str**](.md)|  | [optional] 
 **flow_total_size** | [**str**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

