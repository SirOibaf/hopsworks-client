# JupyterSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jupyterSettingsPK** | [**JupyterSettingsPK**](JupyterSettingsPK.md) |  |  [optional]
**secret** | **String** |  | 
**shutdownLevel** | **Integer** |  |  [optional]
**advanced** | **Boolean** |  |  [optional]
**pythonKernel** | **Boolean** |  |  [optional]
**users** | [**Users**](Users.md) |  |  [optional]
**project** | [**Project**](Project.md) |  |  [optional]
**baseDir** | **String** |  | 
**jobConfig** | [**JobConfiguration**](JobConfiguration.md) |  |  [optional]
**privateDir** | **String** |  |  [optional]
**gitAvailable** | **Boolean** |  |  [optional]
**gitBackend** | **Boolean** |  |  [optional]
**gitConfig** | [**GitConfig**](GitConfig.md) |  |  [optional]
**mode** | [**ModeEnum**](#ModeEnum) |  |  [optional]

<a name="ModeEnum"></a>
## Enum: ModeEnum
Name | Value
---- | -----
LAB | &quot;JUPYTER_LAB&quot;
CLASSIC | &quot;JUPYTER_CLASSIC&quot;
