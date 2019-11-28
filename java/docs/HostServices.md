# HostServices

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Long** |  |  [optional]
**pid** | **Integer** |  |  [optional]
**group** | **String** |  | 
**service** | **String** |  | 
**status** | [**StatusEnum**](#StatusEnum) |  | 
**uptime** | **Long** |  |  [optional]
**startTime** | **Long** |  |  [optional]
**stopTime** | **Long** |  |  [optional]
**host** | [**Hosts**](Hosts.md) |  |  [optional]
**health** | [**HealthEnum**](#HealthEnum) |  |  [optional]

<a name="StatusEnum"></a>
## Enum: StatusEnum
Name | Value
---- | -----
STARTED | &quot;Started&quot;
STOPPED | &quot;Stopped&quot;
FAILED | &quot;Failed&quot;
TIMEDOUT | &quot;TimedOut&quot;
NONE | &quot;None&quot;

<a name="HealthEnum"></a>
## Enum: HealthEnum
Name | Value
---- | -----
GOOD | &quot;Good&quot;
BAD | &quot;Bad&quot;
