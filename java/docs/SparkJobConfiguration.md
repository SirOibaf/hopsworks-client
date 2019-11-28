# SparkJobConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appPath** | **String** |  |  [optional]
**mainClass** | **String** |  |  [optional]
**args** | **String** |  |  [optional]
**properties** | **String** |  |  [optional]
**experimentType** | [**ExperimentTypeEnum**](#ExperimentTypeEnum) |  |  [optional]
**distributionStrategy** | [**DistributionStrategyEnum**](#DistributionStrategyEnum) |  |  [optional]
**executorInstances** | **Integer** |  |  [optional]
**executorCores** | **Integer** |  |  [optional]
**executorMemory** | **Integer** |  |  [optional]
**executorGpus** | **Integer** |  |  [optional]
**numPs** | **Integer** |  |  [optional]
**dynamicAllocationEnabled** | **Boolean** |  |  [optional]
**dynamicAllocationMinExecutors** | **Integer** |  |  [optional]
**dynamicAllocationMaxExecutors** | **Integer** |  |  [optional]
**dynamicAllocationInitialExecutors** | **Integer** |  |  [optional]
**blacklistingEnabled** | **Boolean** |  |  [optional]
**pyFiles** | **String** |  |  [optional]
**files** | **String** |  |  [optional]
**jars** | **String** |  |  [optional]
**archives** | **String** |  |  [optional]

<a name="ExperimentTypeEnum"></a>
## Enum: ExperimentTypeEnum
Name | Value
---- | -----
EXPERIMENT | &quot;EXPERIMENT&quot;
PARALLEL_EXPERIMENTS | &quot;PARALLEL_EXPERIMENTS&quot;
DISTRIBUTED_TRAINING | &quot;DISTRIBUTED_TRAINING&quot;

<a name="DistributionStrategyEnum"></a>
## Enum: DistributionStrategyEnum
Name | Value
---- | -----
MIRRORED | &quot;MIRRORED&quot;
PARAMETER_SERVER | &quot;PARAMETER_SERVER&quot;
COLLECTIVE_ALL_REDUCE | &quot;COLLECTIVE_ALL_REDUCE&quot;
