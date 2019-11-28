# Activity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Integer** |  |  [optional]
**activity** | **String** |  |  [optional]
**timestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  | 
**flag** | [**FlagEnum**](#FlagEnum) |  | 
**project** | [**Project**](Project.md) |  |  [optional]
**user** | [**Users**](Users.md) |  |  [optional]

<a name="FlagEnum"></a>
## Enum: FlagEnum
Name | Value
---- | -----
MEMBER | &quot;MEMBER&quot;
PROJECT | &quot;PROJECT&quot;
SERVICE | &quot;SERVICE&quot;
DATASET | &quot;DATASET&quot;
JOB | &quot;JOB&quot;
