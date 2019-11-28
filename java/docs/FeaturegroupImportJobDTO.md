# FeaturegroupImportJobDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TypeEnum**](#TypeEnum) |  |  [optional]
**storageConnector** | **String** |  |  [optional]
**path** | **String** |  |  [optional]
**featuregroup** | **String** |  |  [optional]
**primaryKey** | **List&lt;String&gt;** |  |  [optional]
**description** | **String** |  |  [optional]
**featurestore** | **String** |  |  [optional]
**featuregroupVersion** | **Integer** |  |  [optional]
**jobs** | **String** |  |  [optional]
**descriptiveStatistics** | **Boolean** |  |  [optional]
**featureCorrelation** | **Boolean** |  |  [optional]
**featureHistograms** | **Boolean** |  |  [optional]
**clusterAnalysis** | **Boolean** |  |  [optional]
**statsColumn** | **List&lt;String&gt;** |  |  [optional]
**numBins** | **Integer** |  |  [optional]
**corrMethod** | **String** |  |  [optional]
**numClusters** | **Integer** |  |  [optional]
**partitionBy** | **List&lt;String&gt;** |  |  [optional]
**dataFormat** | **String** |  |  [optional]
**online** | **Boolean** |  |  [optional]
**onlineTypes** | **Map&lt;String, String&gt;** |  |  [optional]
**offline** | **Boolean** |  |  [optional]
**amCores** | **Integer** |  |  [optional]
**amMemory** | **Integer** |  |  [optional]
**executorCores** | **Integer** |  |  [optional]
**executorMemory** | **Integer** |  |  [optional]
**maxExecutors** | **Integer** |  |  [optional]

<a name="TypeEnum"></a>
## Enum: TypeEnum
Name | Value
---- | -----
S3 | &quot;S3&quot;
REDSHIFT | &quot;REDSHIFT&quot;
