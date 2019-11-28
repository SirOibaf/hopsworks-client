# swagger_client.AdminApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_user**](AdminApi.md#accept_user) | **POST** /admin/users/{email}/accepted | 
[**add_new_cluster_node**](AdminApi.md#add_new_cluster_node) | **POST** /admin/hosts | 
[**change_cluster_status**](AdminApi.md#change_cluster_status) | **POST** /admin/llap | 
[**change_master_encryption_password**](AdminApi.md#change_master_encryption_password) | **PUT** /admin/encryptionPass | 
[**cluster_status**](AdminApi.md#cluster_status) | **GET** /admin/llap | 
[**create_project_as_user**](AdminApi.md#create_project_as_user) | **POST** /admin/projects/createas | 
[**delete_node**](AdminApi.md#delete_node) | **DELETE** /admin/hosts/{hostid} | 
[**delete_project**](AdminApi.md#delete_project) | **DELETE** /admin/projects/{id} | 
[**force_delete_project**](AdminApi.md#force_delete_project) | **DELETE** /admin/projects/{name}/force | 
[**get_all_cluster_nodes**](AdminApi.md#get_all_cluster_nodes) | **GET** /admin/hosts | 
[**get_all_groups**](AdminApi.md#get_all_groups) | **GET** /admin/usergroups | 
[**get_all_users**](AdminApi.md#get_all_users) | **GET** /admin/users | 
[**get_kafka_settings**](AdminApi.md#get_kafka_settings) | **GET** /admin/kafka/settings | Get kafka system settings
[**get_materializer_state**](AdminApi.md#get_materializer_state) | **GET** /admin/materializer | 
[**get_project_admin_info**](AdminApi.md#get_project_admin_info) | **GET** /admin/projects/{id} | 
[**get_projects_admin_info**](AdminApi.md#get_projects_admin_info) | **GET** /admin/projects | 
[**get_update_password_status**](AdminApi.md#get_update_password_status) | **GET** /admin/encryptionPass/{opId} | 
[**get_user**](AdminApi.md#get_user) | **GET** /admin/users/{email} | 
[**pending_user**](AdminApi.md#pending_user) | **POST** /admin/users/{email}/pending | 
[**refresh_variables**](AdminApi.md#refresh_variables) | **POST** /admin/variables/refresh | 
[**reject_user**](AdminApi.md#reject_user) | **POST** /admin/users/{email}/rejected | 
[**remove_local_materialized_crypto**](AdminApi.md#remove_local_materialized_crypto) | **DELETE** /admin/materializer/local/{name}/{directory} | 
[**remove_remote_materialized_crypto**](AdminApi.md#remove_remote_materialized_crypto) | **DELETE** /admin/materializer/remote/{name}/{directory} | 
[**renew_service_jwt**](AdminApi.md#renew_service_jwt) | **PUT** /admin/servicetoken | 
[**restart_agent**](AdminApi.md#restart_agent) | **PUT** /admin/kagent/{hostname} | 
[**service_key_rotate**](AdminApi.md#service_key_rotate) | **POST** /admin/rotate | 
[**set_project_admin_info**](AdminApi.md#set_project_admin_info) | **PUT** /admin/projects | 
[**start_agent**](AdminApi.md#start_agent) | **POST** /admin/kagent/{hostname} | 
[**stop_agent**](AdminApi.md#stop_agent) | **DELETE** /admin/kagent/{hostname} | 
[**update_cluster_node**](AdminApi.md#update_cluster_node) | **PUT** /admin/hosts | 
[**update_user**](AdminApi.md#update_user) | **POST** /admin/users/{email} | 
[**update_variables**](AdminApi.md#update_variables) | **POST** /admin/variables | 

# **accept_user**
> accept_user(email, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
email = 'email_example' # str | 
body = swagger_client.Users() # Users |  (optional)

try:
    api_instance.accept_user(email, body=body)
except ApiException as e:
    print("Exception when calling AdminApi->accept_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **body** | [**Users**](Users.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_new_cluster_node**
> add_new_cluster_node(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
body = swagger_client.Hosts() # Hosts |  (optional)

try:
    api_instance.add_new_cluster_node(body=body)
except ApiException as e:
    print("Exception when calling AdminApi->add_new_cluster_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Hosts**](Hosts.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_cluster_status**
> change_cluster_status(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
body = swagger_client.LlapClusterStatus() # LlapClusterStatus |  (optional)

try:
    api_instance.change_cluster_status(body=body)
except ApiException as e:
    print("Exception when calling AdminApi->change_cluster_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LlapClusterStatus**](LlapClusterStatus.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_master_encryption_password**
> change_master_encryption_password(old_password=old_password, new_password=new_password)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
old_password = 'old_password_example' # str |  (optional)
new_password = 'new_password_example' # str |  (optional)

try:
    api_instance.change_master_encryption_password(old_password=old_password, new_password=new_password)
except ApiException as e:
    print("Exception when calling AdminApi->change_master_encryption_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **old_password** | [**str**](.md)|  | [optional] 
 **new_password** | [**str**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_status**
> cluster_status()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()

try:
    api_instance.cluster_status()
except ApiException as e:
    print("Exception when calling AdminApi->cluster_status: %s\n" % e)
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

# **create_project_as_user**
> create_project_as_user(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
body = swagger_client.ProjectDTO() # ProjectDTO |  (optional)

try:
    api_instance.create_project_as_user(body=body)
except ApiException as e:
    print("Exception when calling AdminApi->create_project_as_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectDTO**](ProjectDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node**
> delete_node(hostid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
hostid = 'hostid_example' # str | 

try:
    api_instance.delete_node(hostid)
except ApiException as e:
    print("Exception when calling AdminApi->delete_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
id = 56 # int | 

try:
    api_instance.delete_project(id)
except ApiException as e:
    print("Exception when calling AdminApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **force_delete_project**
> force_delete_project(name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
name = 'name_example' # str | 

try:
    api_instance.force_delete_project(name)
except ApiException as e:
    print("Exception when calling AdminApi->force_delete_project: %s\n" % e)
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

# **get_all_cluster_nodes**
> get_all_cluster_nodes()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()

try:
    api_instance.get_all_cluster_nodes()
except ApiException as e:
    print("Exception when calling AdminApi->get_all_cluster_nodes: %s\n" % e)
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

# **get_all_groups**
> get_all_groups()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()

try:
    api_instance.get_all_groups()
except ApiException as e:
    print("Exception when calling AdminApi->get_all_groups: %s\n" % e)
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

# **get_all_users**
> get_all_users(status=status)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
status = 'status_example' # str |  (optional)

try:
    api_instance.get_all_users(status=status)
except ApiException as e:
    print("Exception when calling AdminApi->get_all_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kafka_settings**
> get_kafka_settings()

Get kafka system settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()

try:
    # Get kafka system settings
    api_instance.get_kafka_settings()
except ApiException as e:
    print("Exception when calling AdminApi->get_kafka_settings: %s\n" % e)
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

# **get_materializer_state**
> get_materializer_state()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()

try:
    api_instance.get_materializer_state()
except ApiException as e:
    print("Exception when calling AdminApi->get_materializer_state: %s\n" % e)
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

# **get_project_admin_info**
> get_project_admin_info(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
id = 56 # int | 

try:
    api_instance.get_project_admin_info(id)
except ApiException as e:
    print("Exception when calling AdminApi->get_project_admin_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects_admin_info**
> get_projects_admin_info()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()

try:
    api_instance.get_projects_admin_info()
except ApiException as e:
    print("Exception when calling AdminApi->get_projects_admin_info: %s\n" % e)
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

# **get_update_password_status**
> get_update_password_status(op_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
op_id = 56 # int | 

try:
    api_instance.get_update_password_status(op_id)
except ApiException as e:
    print("Exception when calling AdminApi->get_update_password_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **op_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> get_user(email)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
email = 'email_example' # str | 

try:
    api_instance.get_user(email)
except ApiException as e:
    print("Exception when calling AdminApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pending_user**
> pending_user(email)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
email = 'email_example' # str | 

try:
    api_instance.pending_user(email)
except ApiException as e:
    print("Exception when calling AdminApi->pending_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_variables**
> refresh_variables()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()

try:
    api_instance.refresh_variables()
except ApiException as e:
    print("Exception when calling AdminApi->refresh_variables: %s\n" % e)
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

# **reject_user**
> reject_user(email)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
email = 'email_example' # str | 

try:
    api_instance.reject_user(email)
except ApiException as e:
    print("Exception when calling AdminApi->reject_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_local_materialized_crypto**
> remove_local_materialized_crypto(name, directory)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
name = 'name_example' # str | 
directory = 'directory_example' # str | 

try:
    api_instance.remove_local_materialized_crypto(name, directory)
except ApiException as e:
    print("Exception when calling AdminApi->remove_local_materialized_crypto: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **directory** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_remote_materialized_crypto**
> remove_remote_materialized_crypto(name, directory)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
name = 'name_example' # str | 
directory = 'directory_example' # str | 

try:
    api_instance.remove_remote_materialized_crypto(name, directory)
except ApiException as e:
    print("Exception when calling AdminApi->remove_remote_materialized_crypto: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **directory** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_service_jwt**
> renew_service_jwt()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()

try:
    api_instance.renew_service_jwt()
except ApiException as e:
    print("Exception when calling AdminApi->renew_service_jwt: %s\n" % e)
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

# **restart_agent**
> restart_agent(hostname)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
hostname = 'hostname_example' # str | 

try:
    api_instance.restart_agent(hostname)
except ApiException as e:
    print("Exception when calling AdminApi->restart_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_key_rotate**
> service_key_rotate()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()

try:
    api_instance.service_key_rotate()
except ApiException as e:
    print("Exception when calling AdminApi->service_key_rotate: %s\n" % e)
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

# **set_project_admin_info**
> set_project_admin_info(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
body = swagger_client.ProjectAdminInfoDTO() # ProjectAdminInfoDTO |  (optional)

try:
    api_instance.set_project_admin_info(body=body)
except ApiException as e:
    print("Exception when calling AdminApi->set_project_admin_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectAdminInfoDTO**](ProjectAdminInfoDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_agent**
> start_agent(hostname)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
hostname = 'hostname_example' # str | 

try:
    api_instance.start_agent(hostname)
except ApiException as e:
    print("Exception when calling AdminApi->start_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_agent**
> stop_agent(hostname)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
hostname = 'hostname_example' # str | 

try:
    api_instance.stop_agent(hostname)
except ApiException as e:
    print("Exception when calling AdminApi->stop_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_node**
> update_cluster_node(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
body = swagger_client.Hosts() # Hosts |  (optional)

try:
    api_instance.update_cluster_node(body=body)
except ApiException as e:
    print("Exception when calling AdminApi->update_cluster_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Hosts**](Hosts.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(email, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
email = 'email_example' # str | 
body = swagger_client.Users() # Users |  (optional)

try:
    api_instance.update_user(email, body=body)
except ApiException as e:
    print("Exception when calling AdminApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **body** | [**Users**](Users.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_variables**
> update_variables(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
body = swagger_client.VariablesRequest() # VariablesRequest |  (optional)

try:
    api_instance.update_variables(body=body)
except ApiException as e:
    print("Exception when calling AdminApi->update_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VariablesRequest**](VariablesRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

