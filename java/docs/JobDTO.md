# JobDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **String** |  |  [optional]
**items** | [**List&lt;JobDTO&gt;**](JobDTO.md) |  |  [optional]
**count** | **Long** |  |  [optional]
**id** | **Integer** |  |  [optional]
**name** | **String** |  |  [optional]
**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional]
**config** | [**JobConfiguration**](JobConfiguration.md) |  |  [optional]
**jobType** | [**JobTypeEnum**](#JobTypeEnum) |  |  [optional]
**creator** | [**UserDTO**](UserDTO.md) |  |  [optional]
**executions** | [**ExecutionDTO**](ExecutionDTO.md) |  |  [optional]

<a name="JobTypeEnum"></a>
## Enum: JobTypeEnum
Name | Value
---- | -----
YARN | &quot;YARN&quot;
FLINK | &quot;FLINK&quot;
SPARK | &quot;SPARK&quot;
PYSPARK | &quot;PYSPARK&quot;
BEAM_FLINK | &quot;BEAM_FLINK&quot;
BEAM_SPARK | &quot;BEAM_SPARK&quot;
ERASURE_CODING | &quot;ERASURE_CODING&quot;
