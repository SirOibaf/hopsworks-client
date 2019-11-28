# ProjectActivitiesResourceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findAllById**](ProjectActivitiesResourceApi.md#findAllById) | **GET** /project/{projectId}/activities/{activityId} | Finds an activity in project.
[**findAllByProject**](ProjectActivitiesResourceApi.md#findAllByProject) | **GET** /project/{projectId}/activities | Finds activities in project.

<a name="findAllById"></a>
# **findAllById**
> ActivitiesDTO findAllById(activityId, projectId, expand)

Finds an activity in project.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectActivitiesResourceApi;


ProjectActivitiesResourceApi apiInstance = new ProjectActivitiesResourceApi();
Integer activityId = 56; // Integer | 
Integer projectId = 56; // Integer | 
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=creator
try {
    ActivitiesDTO result = apiInstance.findAllById(activityId, projectId, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectActivitiesResourceApi#findAllById");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activityId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;creator | [optional] [enum: expand=creator]

### Return type

[**ActivitiesDTO**](ActivitiesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="findAllByProject"></a>
# **findAllByProject**
> ActivitiesDTO findAllByProject(projectId, offset, limit, sortBy, filterBy, expand)

Finds activities in project.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectActivitiesResourceApi;


ProjectActivitiesResourceApi apiInstance = new ProjectActivitiesResourceApi();
Integer projectId = 56; // Integer | 
Integer offset = 56; // Integer | 
Integer limit = 56; // Integer | 
String sortBy = "sortBy_example"; // String | ex. sort_by=ID:asc,date_created:desc
List<String> filterBy = Arrays.asList("filterBy_example"); // List<String> | ex. filter_by=flag:dataset
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=creator
try {
    ActivitiesDTO result = apiInstance.findAllByProject(projectId, offset, limit, sortBy, filterBy, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectActivitiesResourceApi#findAllByProject");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
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

