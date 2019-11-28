# TrainingDatasetDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**featurestoreId** | **Integer** |  |  [optional]
**featurestoreName** | **String** |  |  [optional]
**description** | **String** |  |  [optional]
**created** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional]
**creator** | **String** |  |  [optional]
**version** | **Integer** |  |  [optional]
**descriptiveStatistics** | [**DescriptiveStatsDTO**](DescriptiveStatsDTO.md) |  |  [optional]
**featureCorrelationMatrix** | [**FeatureCorrelationMatrixDTO**](FeatureCorrelationMatrixDTO.md) |  |  [optional]
**featuresHistogram** | [**FeatureDistributionsDTO**](FeatureDistributionsDTO.md) |  |  [optional]
**clusterAnalysis** | [**ClusterAnalysisDTO**](ClusterAnalysisDTO.md) |  |  [optional]
**name** | **String** |  |  [optional]
**id** | **Integer** |  |  [optional]
**features** | [**List&lt;FeatureDTO&gt;**](FeatureDTO.md) |  |  [optional]
**location** | **String** |  |  [optional]
**jobs** | [**List&lt;FeaturestoreJobDTO&gt;**](FeaturestoreJobDTO.md) |  |  [optional]
**dataFormat** | **String** |  |  [optional]
**trainingDatasetType** | [**TrainingDatasetTypeEnum**](#TrainingDatasetTypeEnum) |  |  [optional]

<a name="TrainingDatasetTypeEnum"></a>
## Enum: TrainingDatasetTypeEnum
Name | Value
---- | -----
HOPSFS_TRAINING_DATASET | &quot;HOPSFS_TRAINING_DATASET&quot;
EXTERNAL_TRAINING_DATASET | &quot;EXTERNAL_TRAINING_DATASET&quot;
