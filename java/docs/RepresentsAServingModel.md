# RepresentsAServingModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Integer** | ID of the Serving entry |  [optional]
**name** | **String** | Name of the serving |  [optional]
**artifactPath** | **String** | HOPSFS directory path containing the model (tf) or python script (sklearn) |  [optional]
**modelVersion** | **Integer** | Version of the serving |  [optional]
**availableInstances** | **Integer** | Number of Serving instances available for serving |  [optional]
**requestedInstances** | **Integer** | Number of Serving instances to use for serving |  [optional]
**nodePort** | **Integer** | Port on which the Serving instance(s) are listening |  [optional]
**created** | [**OffsetDateTime**](OffsetDateTime.md) | Date on which the Serving entry was created |  [optional]
**batchingEnabled** | **Boolean** | Is request batching enabled |  [optional]
**servingType** | [**ServingTypeEnum**](#ServingTypeEnum) | Type of serving, sklearn or tfserving |  [optional]
**creator** | **String** | User whom created the Serving entry |  [optional]
**status** | [**StatusEnum**](#StatusEnum) | Status of the Serving entry |  [optional]
**kafkaTopicDTO** | [**TopicDTO**](TopicDTO.md) |  |  [optional]

<a name="ServingTypeEnum"></a>
## Enum: ServingTypeEnum
Name | Value
---- | -----
TENSORFLOW | &quot;TENSORFLOW&quot;
SKLEARN | &quot;SKLEARN&quot;

<a name="StatusEnum"></a>
## Enum: StatusEnum
Name | Value
---- | -----
RUNNING | &quot;RUNNING&quot;
STOPPED | &quot;STOPPED&quot;
STARTING | &quot;STARTING&quot;
UPDATING | &quot;UPDATING&quot;
STOPPING | &quot;STOPPING&quot;
TRANSFORMING | &quot;TRANSFORMING&quot;
