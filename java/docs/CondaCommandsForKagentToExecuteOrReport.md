# CondaCommandsForKagentToExecuteOrReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**OpEnum**](#OpEnum) | Operation to be performed | 
**user** | **String** | The user command will be executed |  [optional]
**project** | **String** | Name of the project the command is associated with | 
**id** | **Integer** | ID of command | 
**arg** | **String** | Arguments passed to command |  [optional]
**status** | [**StatusEnum**](#StatusEnum) | Status of comamnd | 
**version** | **String** | Python version to be enabled |  [optional]
**channelUrl** | **String** | Pip channel to download a library if not th default |  [optional]
**installType** | [**InstallTypeEnum**](#InstallTypeEnum) | Type of Conda installation |  [optional]
**lib** | **String** | Name of the library to install |  [optional]
**environmentYml** | **String** | Environment exported as a YML file |  [optional]
**installJupyter** | **Boolean** | Whether or not to install Jupyter during the environment creation from a YML file |  [optional]

<a name="OpEnum"></a>
## Enum: OpEnum
Name | Value
---- | -----
CLONE | &quot;CLONE&quot;
CREATE | &quot;CREATE&quot;
BACKUP | &quot;BACKUP&quot;
REMOVE | &quot;REMOVE&quot;
LIST | &quot;LIST&quot;
INSTALL | &quot;INSTALL&quot;
UNINSTALL | &quot;UNINSTALL&quot;
UPGRADE | &quot;UPGRADE&quot;
CLEAN | &quot;CLEAN&quot;
YML | &quot;YML&quot;

<a name="StatusEnum"></a>
## Enum: StatusEnum
Name | Value
---- | -----
NEW | &quot;NEW&quot;
SUCCESS | &quot;SUCCESS&quot;
ONGOING | &quot;ONGOING&quot;
FAILED | &quot;FAILED&quot;

<a name="InstallTypeEnum"></a>
## Enum: InstallTypeEnum
Name | Value
---- | -----
ENVIRONMENT | &quot;ENVIRONMENT&quot;
CONDA | &quot;CONDA&quot;
PIP | &quot;PIP&quot;
