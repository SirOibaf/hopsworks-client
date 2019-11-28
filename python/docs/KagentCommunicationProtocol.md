# KagentCommunicationProtocol

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_id** | **str** | ID of the host kagent is running | 
**password** | **str** | Password of kagent&#x27;s REST API | [optional] 
**hadoop_home** | **str** | Path to Hadoop home returned to agent after successful registration | [optional] 
**agent_time** | **int** | Heartbeat timestamp | 
**memory_capacity** | **int** | Total memory capacity of host | 
**cores** | **int** | Number of available cores in host | 
**private_ip** | **str** | Private IP of host | 
**services** | [**StatusReportForRunningServicesOnHost**](StatusReportForRunningServicesOnHost.md) |  | [optional] 
**system_commands** | [**list[SystemCommandsForKagentToExecuteOrReport]**](SystemCommandsForKagentToExecuteOrReport.md) | Status report of running system commands | [optional] 
**conda_commands** | [**list[CondaCommandsForKagentToExecuteOrReport]**](CondaCommandsForKagentToExecuteOrReport.md) | Status report of running conda commands | [optional] 
**conda_report** | **list[str]** | List of Anaconda environments to check for garbage collection | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

