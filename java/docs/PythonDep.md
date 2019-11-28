# PythonDep

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Integer** |  |  [optional]
**dependency** | **String** |  | 
**version** | **String** |  | 
**preinstalled** | **Boolean** |  |  [optional]
**projectCollection** | [**List&lt;Project&gt;**](Project.md) |  |  [optional]
**repoUrl** | [**AnacondaRepo**](AnacondaRepo.md) |  |  [optional]
**installType** | [**InstallTypeEnum**](#InstallTypeEnum) |  |  [optional]
**machineType** | [**MachineTypeEnum**](#MachineTypeEnum) |  |  [optional]

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
