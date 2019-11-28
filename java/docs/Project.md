# Project

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conda** | **Boolean** |  |  [optional]
**archived** | **Boolean** |  |  [optional]
**logs** | **Boolean** |  |  [optional]
**condaEnv** | **Boolean** |  |  [optional]
**projectTeamCollection** | [**List&lt;ProjectTeam&gt;**](ProjectTeam.md) |  |  [optional]
**activityCollection** | [**List&lt;Activity&gt;**](Activity.md) |  |  [optional]
**projectServicesCollection** | [**List&lt;ProjectServices&gt;**](ProjectServices.md) |  |  [optional]
**datasetCollection** | [**List&lt;Dataset&gt;**](Dataset.md) |  |  [optional]
**condaCommandsCollection** | [**List&lt;CondaCommands&gt;**](CondaCommands.md) |  |  [optional]
**jupyterSettingsCollection** | [**List&lt;JupyterSettings&gt;**](JupyterSettings.md) |  |  [optional]
**servingCollection** | [**List&lt;Serving&gt;**](Serving.md) |  |  [optional]
**tensorBoardCollection** | [**List&lt;TensorBoard&gt;**](TensorBoard.md) |  |  [optional]
**id** | **Integer** |  |  [optional]
**name** | **String** |  | 
**owner** | [**Users**](Users.md) |  |  [optional]
**created** | [**OffsetDateTime**](OffsetDateTime.md) |  | 
**retentionPeriod** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional]
**deleted** | **Boolean** |  |  [optional]
**paymentType** | [**PaymentTypeEnum**](#PaymentTypeEnum) |  | 
**pythonVersion** | **String** |  |  [optional]
**description** | **String** |  |  [optional]
**kafkaMaxNumTopics** | **Integer** |  | 
**lastQuotaUpdate** | [**OffsetDateTime**](OffsetDateTime.md) |  | 
**inode** | [**Inode**](Inode.md) |  |  [optional]
**pythonDepCollection** | [**List&lt;PythonDep&gt;**](PythonDep.md) |  |  [optional]
**jupyterProjectCollection** | [**List&lt;JupyterProject&gt;**](JupyterProject.md) |  |  [optional]
**paymentTypeString** | **String** |  |  [optional]

<a name="PaymentTypeEnum"></a>
## Enum: PaymentTypeEnum
Name | Value
---- | -----
PREPAID | &quot;PREPAID&quot;
NOLIMIT | &quot;NOLIMIT&quot;
