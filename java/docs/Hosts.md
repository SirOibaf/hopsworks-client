# Hosts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Integer** |  |  [optional]
**hostname** | **String** |  |  [optional]
**hostIp** | **String** |  |  [optional]
**publicIp** | **String** |  |  [optional]
**privateIp** | **String** |  |  [optional]
**agentPassword** | **String** |  |  [optional]
**cores** | **Integer** |  |  [optional]
**lastHeartbeat** | **Long** |  |  [optional]
**memoryCapacity** | **Long** |  |  [optional]
**numGpus** | **Integer** |  |  [optional]
**registered** | **Boolean** |  |  [optional]
**condaEnabled** | **Boolean** |  |  [optional]
**condaCommands** | [**List&lt;CondaCommands&gt;**](CondaCommands.md) |  |  [optional]
**hostServices** | [**List&lt;HostServices&gt;**](HostServices.md) |  |  [optional]
**publicOrPrivateIp** | **String** |  |  [optional]
**health** | [**HealthEnum**](#HealthEnum) |  |  [optional]
**lastHeartbeatFormatted** | **String** |  |  [optional]

<a name="HealthEnum"></a>
## Enum: HealthEnum
Name | Value
---- | -----
GOOD | &quot;Good&quot;
BAD | &quot;Bad&quot;
