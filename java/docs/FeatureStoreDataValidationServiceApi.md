# FeatureStoreDataValidationServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addValidationRules**](FeatureStoreDataValidationServiceApi.md#addValidationRules) | **POST** /project/{projectId}/featurestores/{featureStoreId}/datavalidation/{featuregroupId}/rules | Write Deequ validation rules to Filesystem so validation job can pick it up
[**getValidationResult**](FeatureStoreDataValidationServiceApi.md#getValidationResult) | **GET** /project/{projectId}/featurestores/{featureStoreId}/datavalidation/{featuregroupId}/result | Fetch the result of a Deequ data validation job
[**getValidationRules**](FeatureStoreDataValidationServiceApi.md#getValidationRules) | **GET** /project/{projectId}/featurestores/{featureStoreId}/datavalidation/{featuregroupId}/rules | Get previously stored Deequ validation rules

<a name="addValidationRules"></a>
# **addValidationRules**
> DataValidationSettingsDTO addValidationRules(featuregroupId, featureStoreId, projectId, body)

Write Deequ validation rules to Filesystem so validation job can pick it up

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeatureStoreDataValidationServiceApi;


FeatureStoreDataValidationServiceApi apiInstance = new FeatureStoreDataValidationServiceApi();
Integer featuregroupId = 56; // Integer | 
Integer featureStoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
ConstraintGroupDTO body = new ConstraintGroupDTO(); // ConstraintGroupDTO | 
try {
    DataValidationSettingsDTO result = apiInstance.addValidationRules(featuregroupId, featureStoreId, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeatureStoreDataValidationServiceApi#addValidationRules");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**|  |
 **featureStoreId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **body** | [**ConstraintGroupDTO**](ConstraintGroupDTO.md)|  | [optional]

### Return type

[**DataValidationSettingsDTO**](DataValidationSettingsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

<a name="getValidationResult"></a>
# **getValidationResult**
> ValidationResult getValidationResult(featuregroupId, featureStoreId, projectId)

Fetch the result of a Deequ data validation job

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeatureStoreDataValidationServiceApi;


FeatureStoreDataValidationServiceApi apiInstance = new FeatureStoreDataValidationServiceApi();
Integer featuregroupId = 56; // Integer | 
Integer featureStoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    ValidationResult result = apiInstance.getValidationResult(featuregroupId, featureStoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeatureStoreDataValidationServiceApi#getValidationResult");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**|  |
 **featureStoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getValidationRules"></a>
# **getValidationRules**
> ConstraintGroupDTO getValidationRules(featuregroupId, featureStoreId, projectId)

Get previously stored Deequ validation rules

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.FeatureStoreDataValidationServiceApi;


FeatureStoreDataValidationServiceApi apiInstance = new FeatureStoreDataValidationServiceApi();
Integer featuregroupId = 56; // Integer | 
Integer featureStoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    ConstraintGroupDTO result = apiInstance.getValidationRules(featuregroupId, featureStoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling FeatureStoreDataValidationServiceApi#getValidationRules");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**|  |
 **featureStoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**ConstraintGroupDTO**](ConstraintGroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

