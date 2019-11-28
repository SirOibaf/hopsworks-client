# AgentServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle**](AgentServiceApi.md#handle) | **POST** /agentresource | Handle kagent operations such as register, heartbeat, ping

<a name="handle"></a>
# **handle**
> KagentCommunicationProtocol handle(body, action)

Handle kagent operations such as register, heartbeat, ping

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.AgentServiceApi;


AgentServiceApi apiInstance = new AgentServiceApi();
KagentCommunicationProtocol body = new KagentCommunicationProtocol(); // KagentCommunicationProtocol | Agent request
String action = "action_example"; // String | Action to be performed on agent resource
try {
    KagentCommunicationProtocol result = apiInstance.handle(body, action);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling AgentServiceApi#handle");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KagentCommunicationProtocol**](KagentCommunicationProtocol.md)| Agent request |
 **action** | **String**| Action to be performed on agent resource | [enum: PING, HEARTBEAT, REGISTER, NONE]

### Return type

[**KagentCommunicationProtocol**](KagentCommunicationProtocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

