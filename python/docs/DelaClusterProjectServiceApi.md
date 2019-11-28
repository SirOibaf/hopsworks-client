# swagger_client.DelaClusterProjectServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remove_public1**](DelaClusterProjectServiceApi.md#remove_public1) | **DELETE** /project/{projectId}/delacluster/{inodeId} | 
[**share**](DelaClusterProjectServiceApi.md#share) | **POST** /project/{projectId}/delacluster | 

# **remove_public1**
> remove_public1(inode_id, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DelaClusterProjectServiceApi()
inode_id = 789 # int | 
project_id = 56 # int | 

try:
    api_instance.remove_public1(inode_id, project_id)
except ApiException as e:
    print("Exception when calling DelaClusterProjectServiceApi->remove_public1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inode_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share**
> share(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DelaClusterProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.InodeIdDTO() # InodeIdDTO |  (optional)

try:
    api_instance.share(project_id, body=body)
except ApiException as e:
    print("Exception when calling DelaClusterProjectServiceApi->share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**InodeIdDTO**](InodeIdDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

