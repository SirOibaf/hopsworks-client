# ExecutionDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **String** |  |  [optional]
**items** | [**List&lt;ExecutionDTO&gt;**](ExecutionDTO.md) |  |  [optional]
**count** | **Long** |  |  [optional]
**id** | **Integer** |  |  [optional]
**submissionTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional]
**state** | [**StateEnum**](#StateEnum) |  |  [optional]
**stdoutPath** | **String** |  |  [optional]
**stderrPath** | **String** |  |  [optional]
**appId** | **String** |  |  [optional]
**hdfsUser** | **String** |  |  [optional]
**finalStatus** | [**FinalStatusEnum**](#FinalStatusEnum) |  |  [optional]
**progress** | **Float** |  |  [optional]
**user** | [**UserDTO**](UserDTO.md) |  |  [optional]
**filesToRemove** | **List&lt;String&gt;** |  |  [optional]
**duration** | **Long** |  |  [optional]
**flinkMasterURL** | **String** |  |  [optional]

<a name="StateEnum"></a>
## Enum: StateEnum
Name | Value
---- | -----
INITIALIZING | &quot;INITIALIZING&quot;
INITIALIZATION_FAILED | &quot;INITIALIZATION_FAILED&quot;
FINISHED | &quot;FINISHED&quot;
RUNNING | &quot;RUNNING&quot;
ACCEPTED | &quot;ACCEPTED&quot;
FAILED | &quot;FAILED&quot;
KILLED | &quot;KILLED&quot;
NEW | &quot;NEW&quot;
NEW_SAVING | &quot;NEW_SAVING&quot;
SUBMITTED | &quot;SUBMITTED&quot;
AGGREGATING_LOGS | &quot;AGGREGATING_LOGS&quot;
FRAMEWORK_FAILURE | &quot;FRAMEWORK_FAILURE&quot;
STARTING_APP_MASTER | &quot;STARTING_APP_MASTER&quot;
APP_MASTER_START_FAILED | &quot;APP_MASTER_START_FAILED&quot;
GENERATING_SECURITY_MATERIAL | &quot;GENERATING_SECURITY_MATERIAL&quot;

<a name="FinalStatusEnum"></a>
## Enum: FinalStatusEnum
Name | Value
---- | -----
UNDEFINED | &quot;UNDEFINED&quot;
SUCCEEDED | &quot;SUCCEEDED&quot;
FAILED | &quot;FAILED&quot;
KILLED | &quot;KILLED&quot;
