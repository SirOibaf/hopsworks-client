# swagger_client.AgentServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle**](AgentServiceApi.md#handle) | **POST** /agentresource | Handle kagent operations such as register, heartbeat, ping

# **handle**
> KagentCommunicationProtocol handle(body, action)

Handle kagent operations such as register, heartbeat, ping

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AgentServiceApi()
body = swagger_client.KagentCommunicationProtocol() # KagentCommunicationProtocol | Agent request
action = 'action_example' # str | Action to be performed on agent resource

try:
    # Handle kagent operations such as register, heartbeat, ping
    api_response = api_instance.handle(body, action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentServiceApi->handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KagentCommunicationProtocol**](KagentCommunicationProtocol.md)| Agent request | 
 **action** | **str**| Action to be performed on agent resource | 

### Return type

[**KagentCommunicationProtocol**](KagentCommunicationProtocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

