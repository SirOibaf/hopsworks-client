# DataSetDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inodeId** | **Long** |  |  [optional]
**name** | **String** |  |  [optional]
**description** | **String** |  |  [optional]
**isPublic** | **Boolean** |  |  [optional]
**searchable** | **Boolean** |  |  [optional]
**generateReadme** | **Boolean** |  |  [optional]
**permissions** | [**PermissionsEnum**](#PermissionsEnum) |  |  [optional]
**template** | **Integer** |  |  [optional]
**projectId** | **Integer** |  |  [optional]
**projectIds** | **List&lt;Integer&gt;** |  |  [optional]
**projectName** | **String** |  |  [optional]
**templateName** | **String** |  |  [optional]
**projectTeam** | [**List&lt;UserCardDTO&gt;**](UserCardDTO.md) |  |  [optional]
**sharedWith** | **List&lt;String&gt;** |  |  [optional]
**type** | [**TypeEnum**](#TypeEnum) |  |  [optional]
**members** | [**List&lt;UserCardDTO&gt;**](UserCardDTO.md) |  |  [optional]

<a name="PermissionsEnum"></a>
## Enum: PermissionsEnum
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
