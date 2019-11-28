# CondaCommands

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Integer** |  |  [optional]
**user** | **String** |  | 
**proj** | **String** |  | 
**channelUrl** | **String** |  |  [optional]
**arg** | **String** |  |  [optional]
**lib** | **String** |  |  [optional]
**version** | **String** |  |  [optional]
**op** | [**OpEnum**](#OpEnum) |  | 
**status** | [**StatusEnum**](#StatusEnum) |  | 
**installType** | [**InstallTypeEnum**](#InstallTypeEnum) |  | 
**machineType** | [**MachineTypeEnum**](#MachineTypeEnum) |  | 
**created** | [**OffsetDateTime**](OffsetDateTime.md) |  | 
**projectId** | [**Project**](Project.md) |  |  [optional]
**hostId** | [**Hosts**](Hosts.md) |  |  [optional]
**environmentYml** | **String** |  |  [optional]
**installJupyter** | **Boolean** |  |  [optional]

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

<a name="MachineTypeEnum"></a>
## Enum: MachineTypeEnum
Name | Value
---- | -----
ALL | &quot;ALL&quot;
CPU | &quot;CPU&quot;
GPU | &quot;GPU&quot;
