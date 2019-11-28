# FeaturegroupDTO

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
**featuregroupType** | [**FeaturegroupTypeEnum**](#FeaturegroupTypeEnum) |  |  [optional]
**descStatsEnabled** | **Boolean** |  |  [optional]
**featCorrEnabled** | **Boolean** |  |  [optional]
**featHistEnabled** | **Boolean** |  |  [optional]
**clusterAnalysisEnabled** | **Boolean** |  |  [optional]
**statisticColumns** | **List&lt;String&gt;** |  |  [optional]
**numBins** | **Integer** |  |  [optional]
**numClusters** | **Integer** |  |  [optional]
**corrMethod** | **String** |  |  [optional]

<a name="FeaturegroupTypeEnum"></a>
## Enum: FeaturegroupTypeEnum
Name | Value
---- | -----
CACHED_FEATURE_GROUP | &quot;CACHED_FEATURE_GROUP&quot;
ON_DEMAND_FEATURE_GROUP | &quot;ON_DEMAND_FEATURE_GROUP&quot;
