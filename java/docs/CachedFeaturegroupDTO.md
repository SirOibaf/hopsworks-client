# CachedFeaturegroupDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hiveTableId** | **Long** |  |  [optional]
**hdfsStorePaths** | **List&lt;String&gt;** |  |  [optional]
**inputFormat** | **String** |  |  [optional]
**hiveTableType** | [**HiveTableTypeEnum**](#HiveTableTypeEnum) |  |  [optional]
**inodeId** | **Long** |  |  [optional]
**onlineFeaturegroupDTO** | [**OnlineFeaturegroupDTO**](OnlineFeaturegroupDTO.md) |  |  [optional]
**onlineFeaturegroupEnabled** | **Boolean** |  |  [optional]

<a name="HiveTableTypeEnum"></a>
## Enum: HiveTableTypeEnum
Name | Value
---- | -----
MANAGED_TABLE | &quot;MANAGED_TABLE&quot;
EXTERNAL_TABLE | &quot;EXTERNAL_TABLE&quot;
