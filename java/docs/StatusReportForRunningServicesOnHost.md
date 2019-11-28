# StatusReportForRunningServicesOnHost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **String** | Service name | 
**group** | **String** | Name of the group service belongs to | 
**pid** | **Integer** | Process ID | 
**status** | [**StatusEnum**](#StatusEnum) | Current status of the service |  [optional]

<a name="StatusEnum"></a>
## Enum: StatusEnum
Name | Value
---- | -----
STARTED | &quot;Started&quot;
STOPPED | &quot;Stopped&quot;
FAILED | &quot;Failed&quot;
TIMEDOUT | &quot;TimedOut&quot;
NONE | &quot;None&quot;
