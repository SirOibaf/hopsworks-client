# InodeView

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** |  |  [optional]
**dir** | **Boolean** |  |  [optional]
**parent** | **Boolean** |  |  [optional]
**path** | **String** |  |  [optional]
**size** | **Long** |  |  [optional]
**shared** | **Boolean** |  |  [optional]
**owningProjectName** | **String** |  |  [optional]
**modification** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional]
**accessTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional]
**id** | **Long** |  |  [optional]
**parentId** | **Long** |  |  [optional]
**template** | **Integer** |  |  [optional]
**description** | **String** |  |  [optional]
**status** | **Boolean** |  |  [optional]
**underConstruction** | **Boolean** |  |  [optional]
**owner** | **String** |  |  [optional]
**permission** | **String** |  |  [optional]
**email** | **String** |  |  [optional]
**publicDs** | **Integer** |  |  [optional]
**sharedWith** | **Integer** |  |  [optional]
**searchable** | **Boolean** |  |  [optional]
**zipState** | **String** |  |  [optional]
**publicId** | **String** |  |  [optional]
**type** | [**TypeEnum**](#TypeEnum) |  |  [optional]
**publicDataset** | **Boolean** |  |  [optional]

<a name="TypeEnum"></a>
## Enum: TypeEnum
Name | Value
---- | -----
DATASET | &quot;DATASET&quot;
HIVEDB | &quot;HIVEDB&quot;
FEATURESTORE | &quot;FEATURESTORE&quot;
