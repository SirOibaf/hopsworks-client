# MachineTypesResourceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMachineType**](MachineTypesResourceApi.md#getMachineType) | **GET** /machines/{type} | Get number of machines for a machine type
[**getMachineTypes**](MachineTypesResourceApi.md#getMachineTypes) | **GET** /machines | Get all types of machines for conda

<a name="getMachineType"></a>
# **getMachineType**
> MachineTypeDTO getMachineType(type)

Get number of machines for a machine type

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MachineTypesResourceApi;


MachineTypesResourceApi apiInstance = new MachineTypesResourceApi();
String type = "type_example"; // String | 
try {
    MachineTypeDTO result = apiInstance.getMachineType(type);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling MachineTypesResourceApi#getMachineType");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **String**|  | [enum: ALL, CPU, GPU]

### Return type

[**MachineTypeDTO**](MachineTypeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getMachineTypes"></a>
# **getMachineTypes**
> MachineTypeDTO getMachineTypes()

Get all types of machines for conda

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.MachineTypesResourceApi;


MachineTypesResourceApi apiInstance = new MachineTypesResourceApi();
try {
    MachineTypeDTO result = apiInstance.getMachineTypes();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling MachineTypesResourceApi#getMachineTypes");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MachineTypeDTO**](MachineTypeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

