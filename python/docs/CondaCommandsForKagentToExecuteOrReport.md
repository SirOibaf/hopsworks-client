# CondaCommandsForKagentToExecuteOrReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | Operation to be performed | 
**user** | **str** | The user command will be executed | [optional] 
**project** | **str** | Name of the project the command is associated with | 
**id** | **int** | ID of command | 
**arg** | **str** | Arguments passed to command | [optional] 
**status** | **str** | Status of comamnd | 
**version** | **str** | Python version to be enabled | [optional] 
**channel_url** | **str** | Pip channel to download a library if not th default | [optional] 
**install_type** | **str** | Type of Conda installation | [optional] 
**lib** | **str** | Name of the library to install | [optional] 
**environment_yml** | **str** | Environment exported as a YML file | [optional] 
**install_jupyter** | **bool** | Whether or not to install Jupyter during the environment creation from a YML file | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

