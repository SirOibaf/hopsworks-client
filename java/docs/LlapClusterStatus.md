# LlapClusterStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusterStatus** | [**ClusterStatusEnum**](#ClusterStatusEnum) |  |  [optional]
**hosts** | **List&lt;String&gt;** |  |  [optional]
**instanceNumber** | **Integer** |  |  [optional]
**executorsMemory** | **Long** |  |  [optional]
**cacheMemory** | **Long** |  |  [optional]
**executorsPerInstance** | **Integer** |  |  [optional]
**iothreadsPerInstance** | **Integer** |  |  [optional]

<a name="ClusterStatusEnum"></a>
## Enum: ClusterStatusEnum
Name | Value
---- | -----
DOWN | &quot;DOWN&quot;
UP | &quot;UP&quot;
LAUNCHING | &quot;LAUNCHING&quot;
