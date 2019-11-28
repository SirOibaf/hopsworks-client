# RepresentsAServingModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the Serving entry | [optional] 
**name** | **str** | Name of the serving | [optional] 
**artifact_path** | **str** | HOPSFS directory path containing the model (tf) or python script (sklearn) | [optional] 
**model_version** | **int** | Version of the serving | [optional] 
**available_instances** | **int** | Number of Serving instances available for serving | [optional] 
**requested_instances** | **int** | Number of Serving instances to use for serving | [optional] 
**node_port** | **int** | Port on which the Serving instance(s) are listening | [optional] 
**created** | **datetime** | Date on which the Serving entry was created | [optional] 
**batching_enabled** | **bool** | Is request batching enabled | [optional] 
**serving_type** | **str** | Type of serving, sklearn or tfserving | [optional] 
**creator** | **str** | User whom created the Serving entry | [optional] 
**status** | **str** | Status of the Serving entry | [optional] 
**kafka_topic_dto** | [**TopicDTO**](TopicDTO.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

