# JobConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appName** | **String** |  |  [optional]
**schedule** | [**ScheduleDTO**](ScheduleDTO.md) |  |  [optional]
**jobType** | [**JobTypeEnum**](#JobTypeEnum) |  |  [optional]
**jobTypeName** | **String** |  |  [optional]

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
