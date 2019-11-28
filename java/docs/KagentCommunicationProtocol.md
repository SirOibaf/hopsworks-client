# KagentCommunicationProtocol

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostId** | **String** | ID of the host kagent is running | 
**password** | **String** | Password of kagent&#x27;s REST API |  [optional]
**hadoopHome** | **String** | Path to Hadoop home returned to agent after successful registration |  [optional]
**agentTime** | **Long** | Heartbeat timestamp | 
**memoryCapacity** | **Long** | Total memory capacity of host | 
**cores** | **Integer** | Number of available cores in host | 
**privateIp** | **String** | Private IP of host | 
**services** | [**StatusReportForRunningServicesOnHost**](StatusReportForRunningServicesOnHost.md) |  |  [optional]
**systemCommands** | [**List&lt;SystemCommandsForKagentToExecuteOrReport&gt;**](SystemCommandsForKagentToExecuteOrReport.md) | Status report of running system commands |  [optional]
**condaCommands** | [**List&lt;CondaCommandsForKagentToExecuteOrReport&gt;**](CondaCommandsForKagentToExecuteOrReport.md) | Status report of running conda commands |  [optional]
**condaReport** | **List&lt;String&gt;** | List of Anaconda environments to check for garbage collection |  [optional]
