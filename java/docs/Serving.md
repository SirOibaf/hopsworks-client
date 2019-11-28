# Serving

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Integer** |  |  [optional]
**created** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional]
**creator** | [**Users**](Users.md) |  |  [optional]
**name** | **String** |  | 
**artifactPath** | **String** |  | 
**version** | **Integer** |  | 
**optimized** | **Boolean** |  | 
**instances** | **Integer** |  |  [optional]
**project** | [**Project**](Project.md) |  |  [optional]
**batchingEnabled** | **Boolean** |  |  [optional]
**lockIP** | **String** |  |  [optional]
**lockTimestamp** | **Long** |  |  [optional]
**kafkaTopic** | [**ProjectTopics**](ProjectTopics.md) |  |  [optional]
**localPort** | **Integer** |  |  [optional]
**localPid** | **Integer** |  |  [optional]
**localDir** | **String** |  |  [optional]
**servingType** | [**ServingTypeEnum**](#ServingTypeEnum) |  | 

<a name="ServingTypeEnum"></a>
## Enum: ServingTypeEnum
Name | Value
---- | -----
TENSORFLOW | &quot;TENSORFLOW&quot;
SKLEARN | &quot;SKLEARN&quot;
