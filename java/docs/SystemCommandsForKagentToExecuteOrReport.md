# SystemCommandsForKagentToExecuteOrReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**OpEnum**](#OpEnum) | Operation to be performed | 
**status** | [**StatusEnum**](#StatusEnum) | Status of command | 
**id** | **Integer** | ID of command | 
**arguments** | **String** | Arguments passed to command |  [optional]
**priority** | **Integer** | Priority the command will run, 0 is the lowest priority |  [optional]
**execUser** | **String** | The user command will be executed |  [optional]

<a name="OpEnum"></a>
## Enum: OpEnum
Name | Value
---- | -----
SERVICE_KEY_ROTATION | &quot;SERVICE_KEY_ROTATION&quot;
CONDA_GC | &quot;CONDA_GC&quot;

<a name="StatusEnum"></a>
## Enum: StatusEnum
Name | Value
---- | -----
NEW | &quot;NEW&quot;
ONGOING | &quot;ONGOING&quot;
FINISHED | &quot;FINISHED&quot;
FAILED | &quot;FAILED&quot;
