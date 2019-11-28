# FeaturegroupDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**featurestore_id** | **int** |  | [optional] 
**featurestore_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**creator** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**descriptive_statistics** | [**DescriptiveStatsDTO**](DescriptiveStatsDTO.md) |  | [optional] 
**feature_correlation_matrix** | [**FeatureCorrelationMatrixDTO**](FeatureCorrelationMatrixDTO.md) |  | [optional] 
**features_histogram** | [**FeatureDistributionsDTO**](FeatureDistributionsDTO.md) |  | [optional] 
**cluster_analysis** | [**ClusterAnalysisDTO**](ClusterAnalysisDTO.md) |  | [optional] 
**name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**features** | [**list[FeatureDTO]**](FeatureDTO.md) |  | [optional] 
**location** | **str** |  | [optional] 
**jobs** | [**list[FeaturestoreJobDTO]**](FeaturestoreJobDTO.md) |  | [optional] 
**featuregroup_type** | **str** |  | [optional] 
**desc_stats_enabled** | **bool** |  | [optional] 
**feat_corr_enabled** | **bool** |  | [optional] 
**feat_hist_enabled** | **bool** |  | [optional] 
**cluster_analysis_enabled** | **bool** |  | [optional] 
**statistic_columns** | **list[str]** |  | [optional] 
**num_bins** | **int** |  | [optional] 
**num_clusters** | **int** |  | [optional] 
**corr_method** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

