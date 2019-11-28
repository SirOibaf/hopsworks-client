# swagger_client.FeatureStoreDataValidationServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_validation_rules**](FeatureStoreDataValidationServiceApi.md#add_validation_rules) | **POST** /project/{projectId}/featurestores/{featureStoreId}/datavalidation/{featuregroupId}/rules | Write Deequ validation rules to Filesystem so validation job can pick it up
[**get_validation_result**](FeatureStoreDataValidationServiceApi.md#get_validation_result) | **GET** /project/{projectId}/featurestores/{featureStoreId}/datavalidation/{featuregroupId}/result | Fetch the result of a Deequ data validation job
[**get_validation_rules**](FeatureStoreDataValidationServiceApi.md#get_validation_rules) | **GET** /project/{projectId}/featurestores/{featureStoreId}/datavalidation/{featuregroupId}/rules | Get previously stored Deequ validation rules

# **add_validation_rules**
> DataValidationSettingsDTO add_validation_rules(featuregroup_id, feature_store_id, project_id, body=body)

Write Deequ validation rules to Filesystem so validation job can pick it up

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeatureStoreDataValidationServiceApi()
featuregroup_id = 56 # int | 
feature_store_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.ConstraintGroupDTO() # ConstraintGroupDTO |  (optional)

try:
    # Write Deequ validation rules to Filesystem so validation job can pick it up
    api_response = api_instance.add_validation_rules(featuregroup_id, feature_store_id, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureStoreDataValidationServiceApi->add_validation_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**|  | 
 **feature_store_id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**ConstraintGroupDTO**](ConstraintGroupDTO.md)|  | [optional] 

### Return type

[**DataValidationSettingsDTO**](DataValidationSettingsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validation_result**
> ValidationResult get_validation_result(featuregroup_id, feature_store_id, project_id)

Fetch the result of a Deequ data validation job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeatureStoreDataValidationServiceApi()
featuregroup_id = 56 # int | 
feature_store_id = 56 # int | 
project_id = 56 # int | 

try:
    # Fetch the result of a Deequ data validation job
    api_response = api_instance.get_validation_result(featuregroup_id, feature_store_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureStoreDataValidationServiceApi->get_validation_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**|  | 
 **feature_store_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validation_rules**
> ConstraintGroupDTO get_validation_rules(featuregroup_id, feature_store_id, project_id)

Get previously stored Deequ validation rules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeatureStoreDataValidationServiceApi()
featuregroup_id = 56 # int | 
feature_store_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get previously stored Deequ validation rules
    api_response = api_instance.get_validation_rules(featuregroup_id, feature_store_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureStoreDataValidationServiceApi->get_validation_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**|  | 
 **feature_store_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**ConstraintGroupDTO**](ConstraintGroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

