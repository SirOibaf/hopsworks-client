# Dataset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Integer** |  |  [optional]
**inode** | [**Inode**](Inode.md) |  |  [optional]
**name** | **String** |  |  [optional]
**description** | **String** |  |  [optional]
**project** | [**Project**](Project.md) |  |  [optional]
**editable** | [**EditableEnum**](#EditableEnum) |  | 
**searchable** | **Boolean** |  | 
**status** | **Boolean** |  | 
**publicDs** | **Integer** |  | 
**publicDsId** | **String** |  |  [optional]
**shared** | **Boolean** |  | 
**type** | [**TypeEnum**](#TypeEnum) |  | 
**featurestore** | [**Featurestore**](Featurestore.md) |  |  [optional]
**datasetRequestCollection** | [**List&lt;DatasetRequest&gt;**](DatasetRequest.md) |  |  [optional]
**inodeId** | **Long** |  |  [optional]
**publicDsState** | [**PublicDsStateEnum**](#PublicDsStateEnum) |  |  [optional]

<a name="EditableEnum"></a>
## Enum: EditableEnum
Name | Value
---- | -----
GROUP_WRITABLE_SB | &quot;GROUP_WRITABLE_SB&quot;
GROUP_WRITABLE | &quot;GROUP_WRITABLE&quot;
OWNER_ONLY | &quot;OWNER_ONLY&quot;

<a name="TypeEnum"></a>
## Enum: TypeEnum
Name | Value
---- | -----
DATASET | &quot;DATASET&quot;
HIVEDB | &quot;HIVEDB&quot;
FEATURESTORE | &quot;FEATURESTORE&quot;

<a name="PublicDsStateEnum"></a>
## Enum: PublicDsStateEnum
Name | Value
---- | -----
PRIVATE | &quot;PRIVATE&quot;
CLUSTER | &quot;CLUSTER&quot;
HOPS | &quot;HOPS&quot;
