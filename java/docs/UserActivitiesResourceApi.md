# UserActivitiesResourceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findAllById1**](UserActivitiesResourceApi.md#findAllById1) | **GET** /users/activities/{activityId} | Finds an activity for a user by id.
[**findAllByUser1**](UserActivitiesResourceApi.md#findAllByUser1) | **GET** /users/activities | Finds all activities for a user.

<a name="findAllById1"></a>
# **findAllById1**
> ActivitiesDTO findAllById1(activityId, expand)

Finds an activity for a user by id.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UserActivitiesResourceApi;


UserActivitiesResourceApi apiInstance = new UserActivitiesResourceApi();
Integer activityId = 56; // Integer | 
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=creator
try {
    ActivitiesDTO result = apiInstance.findAllById1(activityId, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UserActivitiesResourceApi#findAllById1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activityId** | **Integer**|  |
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;creator | [optional] [enum: expand=creator]

### Return type

[**ActivitiesDTO**](ActivitiesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="findAllByUser1"></a>
# **findAllByUser1**
> ActivitiesDTO findAllByUser1(offset, limit, sortBy, filterBy, expand)

Finds all activities for a user.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.UserActivitiesResourceApi;


UserActivitiesResourceApi apiInstance = new UserActivitiesResourceApi();
Integer offset = 56; // Integer | 
Integer limit = 56; // Integer | 
String sortBy = "sortBy_example"; // String | ex. sort_by=ID:asc,date_created:desc
List<String> filterBy = Arrays.asList("filterBy_example"); // List<String> | ex. filter_by=flag:dataset
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=creator
try {
    ActivitiesDTO result = apiInstance.findAllByUser1(offset, limit, sortBy, filterBy, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UserActivitiesResourceApi#findAllByUser1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **Integer**|  | [optional]
 **limit** | **Integer**|  | [optional]
 **sortBy** | **String**| ex. sort_by&#x3D;ID:asc,date_created:desc | [optional] [enum: id:asc, id:desc, date_created:asc, date_created:desc, flag:asc, flag:desc]
 **filterBy** | [**List&lt;String&gt;**](String.md)| ex. filter_by&#x3D;flag:dataset | [optional] [enum: flag:project, flag:dataset, flag:member, flag:service, flag:job]
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;creator | [optional] [enum: expand=creator]

### Return type

[**ActivitiesDTO**](ActivitiesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

