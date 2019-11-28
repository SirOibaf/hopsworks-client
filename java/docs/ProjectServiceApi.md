# ProjectServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acceptRequest**](ProjectServiceApi.md#acceptRequest) | **GET** /project/{projectId}/dataset/accept/{inodeId} | 
[**addAclsToTopic**](ProjectServiceApi.md#addAclsToTopic) | **POST** /project/{projectId}/kafka/topics/{topic}/acls | Add a new ACL for a specified topic.
[**addMembers**](ProjectServiceApi.md#addMembers) | **POST** /project/{projectId}/projectMembers | 
[**addTopicSchema**](ProjectServiceApi.md#addTopicSchema) | **POST** /project/{projectId}/kafka/schema/add | 
[**addValidationRules**](ProjectServiceApi.md#addValidationRules) | **POST** /project/{projectId}/featurestores/{featureStoreId}/datavalidation/{featuregroupId}/rules | Write Deequ validation rules to Filesystem so validation job can pick it up
[**attachTemplate**](ProjectServiceApi.md#attachTemplate) | **POST** /project/{projectId}/dataset/attachTemplate | 
[**checkFileExist**](ProjectServiceApi.md#checkFileExist) | **GET** /project/{projectId}/localfs/fileExists/{path} | 
[**checkFileExists**](ProjectServiceApi.md#checkFileExists) | **GET** /project/{projectId}/dataset/fileExists/{path} | 
[**checkFileForDownload**](ProjectServiceApi.md#checkFileForDownload) | **GET** /project/{projectId}/dataset/checkFileForDownload/{path} | 
[**checkProjectAccess**](ProjectServiceApi.md#checkProjectAccess) | **GET** /project/{projectId}/check | 
[**composeDAG**](ProjectServiceApi.md#composeDAG) | **POST** /project/{projectId}/airflow/dag | Generate an Airflow Python DAG file from a DAG definition
[**convertIPythonNotebook**](ProjectServiceApi.md#convertIPythonNotebook) | **GET** /project/{projectId}/jupyter/convertIPythonNotebook/{path} | 
[**copyFile**](ProjectServiceApi.md#copyFile) | **POST** /project/{projectId}/dataset/copy | 
[**countFileBlocks**](ProjectServiceApi.md#countFileBlocks) | **GET** /project/{projectId}/dataset/countFileBlocks/{path} | 
[**createDataSetDir**](ProjectServiceApi.md#createDataSetDir) | **POST** /project/{projectId}/dataset | 
[**createDataSetDir1**](ProjectServiceApi.md#createDataSetDir1) | **POST** /project/{projectId}/localfs | 
[**createFeaturegroup**](ProjectServiceApi.md#createFeaturegroup) | **POST** /project/{projectId}/featurestores/{featurestoreId}/featuregroups | Create feature group in a featurestore
[**createNewStorageConnectorWithType**](ProjectServiceApi.md#createNewStorageConnectorWithType) | **POST** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType} | Create a new storage connector for the feature store
[**createOrUpdate**](ProjectServiceApi.md#createOrUpdate) | **PUT** /project/{projectId}/serving | Create or update a serving instance
[**createOrUpdateImportJob**](ProjectServiceApi.md#createOrUpdateImportJob) | **PUT** /project/{projectId}/featurestores/importjob | Configure job to import featuregroup
[**createOrUpdateTrainingDatasetJob**](ProjectServiceApi.md#createOrUpdateTrainingDatasetJob) | **POST** /project/{projectId}/featurestores/trainingdatasetjob | Configure job to create training dataset
[**createProject**](ProjectServiceApi.md#createProject) | **POST** /project | 
[**createTopLevelDataSet**](ProjectServiceApi.md#createTopLevelDataSet) | **POST** /project/{projectId}/dataset/createTopLevelDataSet | 
[**createTopic**](ProjectServiceApi.md#createTopic) | **POST** /project/{projectId}/kafka/topics | Create a new Kafka topic.
[**createTrainingDataset**](ProjectServiceApi.md#createTrainingDataset) | **POST** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets | Create training dataset for a featurestore
[**credentials**](ProjectServiceApi.md#credentials) | **GET** /project/{projectId}/credentials | 
[**delete**](ProjectServiceApi.md#delete) | **DELETE** /project/{projectId}/python/environments/{version}/commands | Delete commands for this environment
[**delete1**](ProjectServiceApi.md#delete1) | **DELETE** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Delete commands for this library
[**delete2**](ProjectServiceApi.md#delete2) | **DELETE** /project/{projectId}/python/environments/{version} | Remove the python environment with the specified version for this project
[**delete3**](ProjectServiceApi.md#delete3) | **DELETE** /project/{projectId}/jobs/{name} | Delete the job with the given ID
[**deleteFeatureGroupFromFeatureStore**](ProjectServiceApi.md#deleteFeatureGroupFromFeatureStore) | **DELETE** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId} | Delete specific featuregroup from a specific featurestore
[**deleteFeaturegroupContents**](ProjectServiceApi.md#deleteFeaturegroupContents) | **POST** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId}/clear | Delete featuregroup contents
[**deleteSchema**](ProjectServiceApi.md#deleteSchema) | **DELETE** /project/{projectId}/kafka/removeSchema/{schemaName}/{version} | 
[**deleteServing**](ProjectServiceApi.md#deleteServing) | **DELETE** /project/{projectId}/serving/{servingId} | Delete a serving instance
[**deleteStorageConnectorWithTypeAndId**](ProjectServiceApi.md#deleteStorageConnectorWithTypeAndId) | **DELETE** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType}/{connectorId} | Delete storage connector with a specific id and type from a featurestore
[**deleteTrainingDataset**](ProjectServiceApi.md#deleteTrainingDataset) | **DELETE** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid} | Delete a training datasets with a specific id from a featurestore
[**downloadCerts**](ProjectServiceApi.md#downloadCerts) | **POST** /project/{projectId}/downloadCert | 
[**downloadDatasetHdfs**](ProjectServiceApi.md#downloadDatasetHdfs) | **POST** /project/{projectId}/dela/downloads/{publicDSId}/hdfs | 
[**downloadDatasetKafka**](ProjectServiceApi.md#downloadDatasetKafka) | **POST** /project/{projectId}/dela/downloads/{publicDSId}/kafka | 
[**downloadFromHDFS**](ProjectServiceApi.md#downloadFromHDFS) | **GET** /project/{projectId}/dataset/fileDownload/{path} | 
[**example**](ProjectServiceApi.md#example) | **POST** /project/starterProject/{type} | 
[**execution**](ProjectServiceApi.md#execution) | **POST** /project/{projectId}/jobs/{name}/executions | Start/Stop a job
[**filePreview**](ProjectServiceApi.md#filePreview) | **GET** /project/{projectId}/dataset/filePreview/{path} | 
[**findAllById**](ProjectServiceApi.md#findAllById) | **GET** /project/{projectId}/activities/{activityId} | Finds an activity in project.
[**findAllByProject**](ProjectServiceApi.md#findAllByProject) | **GET** /project/{projectId}/activities | Finds activities in project.
[**findAllByUser**](ProjectServiceApi.md#findAllByUser) | **GET** /project | 
[**findByProjectID**](ProjectServiceApi.md#findByProjectID) | **GET** /project/{projectId} | 
[**findDataSetsInProjectID**](ProjectServiceApi.md#findDataSetsInProjectID) | **GET** /project/{projectId}/dataset/getContent | 
[**findMembersByProjectID**](ProjectServiceApi.md#findMembersByProjectID) | **GET** /project/{projectId}/projectMembers | 
[**get**](ProjectServiceApi.md#get) | **GET** /project/{projectId}/python/environments/{version}/commands | Get commands for this environment
[**get1**](ProjectServiceApi.md#get1) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Get all commands for this library
[**get2**](ProjectServiceApi.md#get2) | **GET** /project/{projectId}/python/environments/{version}/libraries | Get the python libraries installed in this environment
[**get3**](ProjectServiceApi.md#get3) | **GET** /project/{projectId}/python/environments/{version} | Get the python environment for specific python version
[**getAll**](ProjectServiceApi.md#getAll) | **GET** /project/{projectId}/python/environments | Get all python environments for this project
[**getAll1**](ProjectServiceApi.md#getAll1) | **GET** /project/{projectId}/jobs | Get a list of all jobs for this project
[**getAllNotebookServersInProject**](ProjectServiceApi.md#getAllNotebookServersInProject) | **GET** /project/{projectId}/jupyter | 
[**getAllProjects**](ProjectServiceApi.md#getAllProjects) | **GET** /project/getAll | 
[**getAppInfo**](ProjectServiceApi.md#getAppInfo) | **GET** /project/{projectId}/jobs/{appId}/appinfo | 
[**getByName**](ProjectServiceApi.md#getByName) | **GET** /project/{projectId}/python/environments/{version}/commands/{commandId} | Get commands by id
[**getByName1**](ProjectServiceApi.md#getByName1) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library}/commands/{commandId} | Get command by id
[**getByName2**](ProjectServiceApi.md#getByName2) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library} | Get the a python library installed in this environment
[**getCurrentMultiplicator**](ProjectServiceApi.md#getCurrentMultiplicator) | **GET** /project/{projectId}/multiplicators | 
[**getDatasetInfo**](ProjectServiceApi.md#getDatasetInfo) | **GET** /project/getDatasetInfo/{inodeId} | 
[**getDatasetInfo1**](ProjectServiceApi.md#getDatasetInfo1) | **GET** /project/{projectId}/getInodeInfo/{inodeId} | 
[**getDirContent**](ProjectServiceApi.md#getDirContent) | **GET** /project/{projectId}/dataset/getContent/{path} | 
[**getExecution**](ProjectServiceApi.md#getExecution) | **GET** /project/{projectId}/jobs/{name}/executions/{id} | Find Execution by Id
[**getExecutions**](ProjectServiceApi.md#getExecutions) | **GET** /project/{projectId}/jobs/{name}/executions | Get a list of executions for the job.
[**getExtendedDetails**](ProjectServiceApi.md#getExtendedDetails) | **GET** /project/{projectId}/dela/transfers/{publicDSId} | 
[**getFeatureGroupFromFeatureStore**](ProjectServiceApi.md#getFeatureGroupFromFeatureStore) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId} | Get specific featuregroup from a specific featurestore
[**getFeatureGroupPreview**](ProjectServiceApi.md#getFeatureGroupPreview) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId}/preview | Preview feature data of a featuregroup
[**getFeatureGroupSchema**](ProjectServiceApi.md#getFeatureGroupSchema) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId}/schema | Get the SQL schema of a featuregroup
[**getFeaturegroupsForFeaturestore**](ProjectServiceApi.md#getFeaturegroupsForFeaturestore) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups | Get the list of feature groups for a featurestore
[**getFeaturestore**](ProjectServiceApi.md#getFeaturestore) | **GET** /project/{projectId}/featurestores/{featurestoreId} | Get featurestore with specific Id
[**getFeaturestoreByName**](ProjectServiceApi.md#getFeaturestoreByName) | **GET** /project/{projectId}/featurestores/getByName/{featurestoreName} | Get featurestore with specific name
[**getFeaturestoreId**](ProjectServiceApi.md#getFeaturestoreId) | **GET** /project/{projectId}/featurestores/{featurestoreName}/metadata | Get featurestore Metadata
[**getFeaturestoreSettings**](ProjectServiceApi.md#getFeaturestoreSettings) | **GET** /project/{projectId}/featurestores/settings | Get featurestore settings
[**getFeaturestores**](ProjectServiceApi.md#getFeaturestores) | **GET** /project/{projectId}/featurestores | Get the list of feature stores for the project
[**getFile**](ProjectServiceApi.md#getFile) | **GET** /project/{projectId}/dataset/getFile/{path} | 
[**getGitStatusOfJupyterRepo**](ProjectServiceApi.md#getGitStatusOfJupyterRepo) | **GET** /project/{projectId}/jupyter/git/status | 
[**getJob**](ProjectServiceApi.md#getJob) | **GET** /project/{projectId}/jobs/{name} | Get the job with requested ID
[**getJobUI**](ProjectServiceApi.md#getJobUI) | **GET** /project/{projectId}/jobs/{appId}/ui/{isLivy} | 
[**getLog**](ProjectServiceApi.md#getLog) | **GET** /project/{projectId}/jobs/{name}/executions/{id}/log/{type} | Retrieve log of given execution and type
[**getMoreInfo**](ProjectServiceApi.md#getMoreInfo) | **GET** /project/{projectId}/getMoreInfo/{type}/{inodeId} | 
[**getMoreInfo1**](ProjectServiceApi.md#getMoreInfo1) | **GET** /project/getMoreInfo/{type}/{inodeId} | 
[**getMoreInfo2**](ProjectServiceApi.md#getMoreInfo2) | **GET** /project/getMoreInfo/proj/{projectId} | 
[**getOnlineFeaturestoreStorageConnector**](ProjectServiceApi.md#getOnlineFeaturestoreStorageConnector) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/onlinefeaturestore | Get online featurestore storage connector for this feature store
[**getPia**](ProjectServiceApi.md#getPia) | **GET** /project/{projectId}/pia | 
[**getProjectByName**](ProjectServiceApi.md#getProjectByName) | **GET** /project/getProjectInfo/{projectName} | 
[**getProjectContents**](ProjectServiceApi.md#getProjectContents) | **GET** /project/{projectId}/dela/transfers | 
[**getProjectSharedWith**](ProjectServiceApi.md#getProjectSharedWith) | **POST** /project/{projectId}/dataset/projectsSharedWith | 
[**getReadmeByInodeId**](ProjectServiceApi.md#getReadmeByInodeId) | **GET** /project/readme/byInodeId/{inodeId} | 
[**getRemoteGitBranches**](ProjectServiceApi.md#getRemoteGitBranches) | **GET** /project/{projectId}/jupyter/git/branches | 
[**getSchema**](ProjectServiceApi.md#getSchema) | **GET** /project/{projectId}/kafka/{topic}/schema | 
[**getSchemaContent**](ProjectServiceApi.md#getSchemaContent) | **GET** /project/{projectId}/kafka/showSchema/{schemaName}/{schemaVersion} | 
[**getServing**](ProjectServiceApi.md#getServing) | **GET** /project/{projectId}/serving/{servingId} | Get info about a serving instance for the project
[**getServings**](ProjectServiceApi.md#getServings) | **GET** /project/{projectId}/serving | Get the list of serving instances for the project
[**getStorageConnectorWithId**](ProjectServiceApi.md#getStorageConnectorWithId) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType}/{connectorId} | Get a storage connector with a specific id and type from a featurestore
[**getStorageConnectors**](ProjectServiceApi.md#getStorageConnectors) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors | Get all storage connectors of a feature store
[**getStorageConnectorsOfType**](ProjectServiceApi.md#getStorageConnectorsOfType) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType} | Get all storage connectors of a specific type of a feature store
[**getTensorBoard**](ProjectServiceApi.md#getTensorBoard) | **GET** /project/{projectId}/tensorboard | Get the running TensorBoard of the logged in user in this project
[**getTensorBoardUrls**](ProjectServiceApi.md#getTensorBoardUrls) | **GET** /project/{projectId}/jobs/{appId}/tensorboard | 
[**getTopic**](ProjectServiceApi.md#getTopic) | **GET** /project/{projectId}/kafka/topics/{topic} | Get Kafka topic details.
[**getTopicAcl**](ProjectServiceApi.md#getTopicAcl) | **GET** /project/{projectId}/kafka/topics/{topic}/acls/{id} | Get ACL metadata specified by id.
[**getTopicAcls**](ProjectServiceApi.md#getTopicAcls) | **GET** /project/{projectId}/kafka/topics/{topic}/acls | Get all ACLs for a specified topic.
[**getTopics**](ProjectServiceApi.md#getTopics) | **GET** /project/{projectId}/kafka/topics | Retrieve Kafka topics metadata .
[**getTrainingDatasetWithId**](ProjectServiceApi.md#getTrainingDatasetWithId) | **GET** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid} | Get a training datasets with a specific id from a featurestore
[**getTrainingDatasetsForFeaturestore**](ProjectServiceApi.md#getTrainingDatasetsForFeaturestore) | **GET** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets | Get the list of training datasets for a featurestore
[**getValidationResult**](ProjectServiceApi.md#getValidationResult) | **GET** /project/{projectId}/featurestores/{featureStoreId}/datavalidation/{featuregroupId}/result | Fetch the result of a Deequ data validation job
[**getValidationRules**](ProjectServiceApi.md#getValidationRules) | **GET** /project/{projectId}/featurestores/{featureStoreId}/datavalidation/{featuregroupId}/rules | Get previously stored Deequ validation rules
[**getYarnUI**](ProjectServiceApi.md#getYarnUI) | **GET** /project/{projectId}/jobs/{appId}/yarnui | 
[**infer**](ProjectServiceApi.md#infer) | **POST** /project/{projectId}/inference/models/{modelName}{version}{verb} | Make inference
[**inspect**](ProjectServiceApi.md#inspect) | **GET** /project/{projectId}/jobs/{jobtype}/inspection | Inspect Spark user program and return SparkJobConfiguration
[**install**](ProjectServiceApi.md#install) | **POST** /project/{projectId}/python/environments/{version}/libraries/{library} | Install a python library in the environment
[**isDir**](ProjectServiceApi.md#isDir) | **GET** /project/{projectId}/dataset/isDir/{path} | 
[**isDir1**](ProjectServiceApi.md#isDir1) | **GET** /project/{projectId}/localfs/isDir/{path} | 
[**isRunning**](ProjectServiceApi.md#isRunning) | **GET** /project/{projectId}/jupyter/running | 
[**listSchemasForTopics**](ProjectServiceApi.md#listSchemasForTopics) | **GET** /project/{projectId}/kafka/schemas | 
[**livySessions**](ProjectServiceApi.md#livySessions) | **GET** /project/{projectId}/jupyter/livy/sessions | 
[**moveFile**](ProjectServiceApi.md#moveFile) | **POST** /project/{projectId}/dataset/move | 
[**newFeaturestoreUtil**](ProjectServiceApi.md#newFeaturestoreUtil) | **POST** /project/{projectId}/featurestores/util | Upload json input for featurestore-util jobs
[**post**](ProjectServiceApi.md#post) | **POST** /project/{projectId}/python/environments/{version} | Create an environment from version or export an environment as yaml file
[**postYml**](ProjectServiceApi.md#postYml) | **POST** /project/{projectId}/python/environments | Create an environment from yaml file
[**publish**](ProjectServiceApi.md#publish) | **POST** /project/{projectId}/dela/uploads | 
[**put**](ProjectServiceApi.md#put) | **PUT** /project/{projectId}/jobs/{name} | Create or Update a Job.
[**quotasByProjectID**](ProjectServiceApi.md#quotasByProjectID) | **GET** /project/{projectId}/quotas | 
[**quotasByProjectID1**](ProjectServiceApi.md#quotasByProjectID1) | **GET** /project/{projectId}/importPublicDataset/{projectName}/{inodeId} | 
[**rejectRequest**](ProjectServiceApi.md#rejectRequest) | **GET** /project/{projectId}/dataset/reject/{inodeId} | 
[**removeAclsFromTopic**](ProjectServiceApi.md#removeAclsFromTopic) | **DELETE** /project/{projectId}/kafka/topics/{topic}/acls/{id} | Remove ACL specified by id.
[**removeCorrupted**](ProjectServiceApi.md#removeCorrupted) | **DELETE** /project/{projectId}/dataset/corrupted/{fileName} | 
[**removeMembersByID**](ProjectServiceApi.md#removeMembersByID) | **DELETE** /project/{projectId}/projectMembers/{email} | 
[**removeProjectAndFiles**](ProjectServiceApi.md#removeProjectAndFiles) | **POST** /project/{projectId}/delete | 
[**removePublic**](ProjectServiceApi.md#removePublic) | **POST** /project/{projectId}/dela/transfers/{publicDSId}/cancel | 
[**removePublic1**](ProjectServiceApi.md#removePublic1) | **DELETE** /project/{projectId}/delacluster/{inodeId} | 
[**removeTopic**](ProjectServiceApi.md#removeTopic) | **DELETE** /project/{projectId}/kafka/topics/{topic} | Delete a Kafka topic.
[**removedataSetdir**](ProjectServiceApi.md#removedataSetdir) | **DELETE** /project/{projectId}/dataset/{fileName} | 
[**removedataSetdir1**](ProjectServiceApi.md#removedataSetdir1) | **DELETE** /project/{projectId}/localfs/{fileName} | 
[**removefile**](ProjectServiceApi.md#removefile) | **DELETE** /project/{projectId}/dataset/file/{fileName} | 
[**retryLog**](ProjectServiceApi.md#retryLog) | **POST** /project/{projectId}/jobs/{name}/executions/{id}/log/{type} | Retry log aggregation of given execution and type
[**search**](ProjectServiceApi.md#search) | **GET** /project/{projectId}/python/environments/{version}/libraries/{search} | Search for libraries using conda or pip package managers
[**secretDir**](ProjectServiceApi.md#secretDir) | **GET** /project/{projectId}/airflow/secretDir | Create project secret directory in Airflow home
[**setPermissions**](ProjectServiceApi.md#setPermissions) | **PUT** /project/{projectId}/dataset/permissions | Set permissions (potentially with sticky bit) for datasets
[**settings**](ProjectServiceApi.md#settings) | **GET** /project/{projectId}/jupyter/settings | 
[**share**](ProjectServiceApi.md#share) | **POST** /project/{projectId}/delacluster | 
[**shareDataSet**](ProjectServiceApi.md#shareDataSet) | **POST** /project/{projectId}/dataset/shareDataSet | 
[**shareTopic**](ProjectServiceApi.md#shareTopic) | **PUT** /project/{projectId}/kafka/topics/{topic}/shared/{destProjectId} | Share a Kafka topic with a project.
[**showManifest**](ProjectServiceApi.md#showManifest) | **GET** /project/{projectId}/dela/transfers/{publicDSId}/manifest | 
[**startDownload**](ProjectServiceApi.md#startDownload) | **POST** /project/{projectId}/dela/downloads/{publicDSId}/manifest | 
[**startNotebookServer**](ProjectServiceApi.md#startNotebookServer) | **POST** /project/{projectId}/jupyter/start | 
[**startOrStop**](ProjectServiceApi.md#startOrStop) | **POST** /project/{projectId}/serving/{servingId} | Start or stop a Serving instance
[**startTensorBoard**](ProjectServiceApi.md#startTensorBoard) | **POST** /project/{projectId}/tensorboard/{elasticId} | Start a new TensorBoard for the logged in user
[**stopLivySession**](ProjectServiceApi.md#stopLivySession) | **DELETE** /project/{projectId}/jupyter/livy/sessions/{appId} | 
[**stopNotebookServer**](ProjectServiceApi.md#stopNotebookServer) | **GET** /project/{projectId}/jupyter/stop | 
[**stopTensorBoard**](ProjectServiceApi.md#stopTensorBoard) | **DELETE** /project/{projectId}/tensorboard | Stop the running TensorBoard for the logged in user
[**storeAirflowJWT**](ProjectServiceApi.md#storeAirflowJWT) | **POST** /project/{projectId}/airflow/jwt | Generate a JWT for Airflow usage and store it in project&#x27;s secret directory in Airflow
[**syncWithFeaturestore**](ProjectServiceApi.md#syncWithFeaturestore) | **POST** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/sync | Synchornize Hive Table with the feature store
[**testMethod1**](ProjectServiceApi.md#testMethod1) | **GET** /project/{projectId}/dataset/upload/{path} | 
[**topicIsSharedTo**](ProjectServiceApi.md#topicIsSharedTo) | **GET** /project/{projectId}/kafka/topics/{topic}/shared | Get list of projects that a topic has been shared with.
[**uninstall**](ProjectServiceApi.md#uninstall) | **DELETE** /project/{projectId}/python/environments/{version}/libraries/{library} | Uninstall a python library from the environment
[**unscheduleJob**](ProjectServiceApi.md#unscheduleJob) | **DELETE** /project/{projectId}/jobs/{name}/schedule | Cancel a job&#x27;s schedule.
[**unshareDataSet**](ProjectServiceApi.md#unshareDataSet) | **POST** /project/{projectId}/dataset/unshareDataSet | 
[**unshareTopicFromProject**](ProjectServiceApi.md#unshareTopicFromProject) | **DELETE** /project/{projectId}/kafka/topics/{topic}/shared/{destProjectId} | Unshare Kafka topic from a project (specified as destProjectId).
[**unshareTopicFromProjects**](ProjectServiceApi.md#unshareTopicFromProjects) | **DELETE** /project/{projectId}/kafka/topics/{topic}/shared | Unshare Kafka topic from all projects.
[**unzip**](ProjectServiceApi.md#unzip) | **GET** /project/{projectId}/dataset/unzip/{path} | 
[**update**](ProjectServiceApi.md#update) | **PUT** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Update commands for this library
[**updateFeaturegroup**](ProjectServiceApi.md#updateFeaturegroup) | **PUT** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId} | Update featuregroup contents
[**updateNotebookServer**](ProjectServiceApi.md#updateNotebookServer) | **POST** /project/{projectId}/jupyter/update | 
[**updatePia**](ProjectServiceApi.md#updatePia) | **PUT** /project/{projectId}/pia | 
[**updateProject**](ProjectServiceApi.md#updateProject) | **PUT** /project/{projectId} | 
[**updateRoleByEmail**](ProjectServiceApi.md#updateRoleByEmail) | **POST** /project/{projectId}/projectMembers/{email} | 
[**updateSchedule**](ProjectServiceApi.md#updateSchedule) | **PUT** /project/{projectId}/jobs/{name}/schedule | Create/Update job&#x27;s schedule.
[**updateSchemaVersion**](ProjectServiceApi.md#updateSchemaVersion) | **POST** /project/{projectId}/kafka/{topic}/schema/version/{version} | 
[**updateStorageConnectorWithId**](ProjectServiceApi.md#updateStorageConnectorWithId) | **PUT** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType}/{connectorId} | Get a storage connector with a specific id and type from a featurestore
[**updateTopicAcls**](ProjectServiceApi.md#updateTopicAcls) | **PUT** /project/{projectId}/kafka/topics/{topic}/acls/{id} | Update ACL specified by id.
[**updateTrainingDataset**](ProjectServiceApi.md#updateTrainingDataset) | **PUT** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid} | Update a training datasets with a specific id from a featurestore
[**uploadMethod1**](ProjectServiceApi.md#uploadMethod1) | **POST** /project/{projectId}/dataset/upload/{path} | 
[**validateSchemaForTopics**](ProjectServiceApi.md#validateSchemaForTopics) | **POST** /project/{projectId}/kafka/schema/validate | 
[**zip**](ProjectServiceApi.md#zip) | **GET** /project/{projectId}/dataset/zip/{path} | 

<a name="acceptRequest"></a>
# **acceptRequest**
> acceptRequest(inodeId, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Long inodeId = 789L; // Long | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.acceptRequest(inodeId, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#acceptRequest");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inodeId** | **Long**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="addAclsToTopic"></a>
# **addAclsToTopic**
> addAclsToTopic(topic, projectId, body)

Add a new ACL for a specified topic.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String topic = "topic_example"; // String | 
Integer projectId = 56; // Integer | 
AclDTO body = new AclDTO(); // AclDTO | 
try {
    apiInstance.addAclsToTopic(topic, projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#addAclsToTopic");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **String**|  |
 **projectId** | **Integer**|  |
 **body** | [**AclDTO**](AclDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="addMembers"></a>
# **addMembers**
> addMembers(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
MembersDTO body = new MembersDTO(); // MembersDTO | 
try {
    apiInstance.addMembers(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#addMembers");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**MembersDTO**](MembersDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

<a name="addTopicSchema"></a>
# **addTopicSchema**
> addTopicSchema(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
SchemaDTO body = new SchemaDTO(); // SchemaDTO | 
try {
    apiInstance.addTopicSchema(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#addTopicSchema");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**SchemaDTO**](SchemaDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="addValidationRules"></a>
# **addValidationRules**
> DataValidationSettingsDTO addValidationRules(featuregroupId, featureStoreId, projectId, body)

Write Deequ validation rules to Filesystem so validation job can pick it up

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer featuregroupId = 56; // Integer | 
Integer featureStoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
ConstraintGroupDTO body = new ConstraintGroupDTO(); // ConstraintGroupDTO | 
try {
    DataValidationSettingsDTO result = apiInstance.addValidationRules(featuregroupId, featureStoreId, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#addValidationRules");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**|  |
 **featureStoreId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **body** | [**ConstraintGroupDTO**](ConstraintGroupDTO.md)|  | [optional]

### Return type

[**DataValidationSettingsDTO**](DataValidationSettingsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

<a name="attachTemplate"></a>
# **attachTemplate**
> attachTemplate(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
FileTemplateDTO body = new FileTemplateDTO(); // FileTemplateDTO | 
try {
    apiInstance.attachTemplate(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#attachTemplate");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**FileTemplateDTO**](FileTemplateDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

<a name="checkFileExist"></a>
# **checkFileExist**
> checkFileExist(path, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String path = "path_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.checkFileExist(path, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#checkFileExist");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="checkFileExists"></a>
# **checkFileExists**
> checkFileExists(path, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String path = "path_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.checkFileExists(path, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#checkFileExists");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="checkFileForDownload"></a>
# **checkFileForDownload**
> checkFileForDownload(path, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String path = "path_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.checkFileForDownload(path, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#checkFileForDownload");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="checkProjectAccess"></a>
# **checkProjectAccess**
> checkProjectAccess(projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.checkProjectAccess(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#checkProjectAccess");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="composeDAG"></a>
# **composeDAG**
> composeDAG(projectId, body)

Generate an Airflow Python DAG file from a DAG definition

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
AirflowDagDTO body = new AirflowDagDTO(); // AirflowDagDTO | 
try {
    apiInstance.composeDAG(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#composeDAG");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**AirflowDagDTO**](AirflowDagDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

<a name="convertIPythonNotebook"></a>
# **convertIPythonNotebook**
> convertIPythonNotebook(path, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String path = "path_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.convertIPythonNotebook(path, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#convertIPythonNotebook");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="copyFile"></a>
# **copyFile**
> copyFile(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
MoveDTO body = new MoveDTO(); // MoveDTO | 
try {
    apiInstance.copyFile(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#copyFile");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**MoveDTO**](MoveDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="countFileBlocks"></a>
# **countFileBlocks**
> countFileBlocks(path, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String path = "path_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.countFileBlocks(path, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#countFileBlocks");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="createDataSetDir"></a>
# **createDataSetDir**
> createDataSetDir(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
DataSetDTO body = new DataSetDTO(); // DataSetDTO | 
try {
    apiInstance.createDataSetDir(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#createDataSetDir");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**DataSetDTO**](DataSetDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

<a name="createDataSetDir1"></a>
# **createDataSetDir1**
> createDataSetDir1(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
String body = "body_example"; // String | 
try {
    apiInstance.createDataSetDir1(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#createDataSetDir1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**String**](String.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

<a name="createFeaturegroup"></a>
# **createFeaturegroup**
> FeaturegroupDTO createFeaturegroup(featurestoreId, projectId, body)

Create feature group in a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
FeaturegroupDTO body = new FeaturegroupDTO(); // FeaturegroupDTO | 
try {
    FeaturegroupDTO result = apiInstance.createFeaturegroup(featurestoreId, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#createFeaturegroup");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **body** | [**FeaturegroupDTO**](FeaturegroupDTO.md)|  | [optional]

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createNewStorageConnectorWithType"></a>
# **createNewStorageConnectorWithType**
> FeaturestoreStorageConnectorDTO createNewStorageConnectorWithType(connectorType, featurestoreId, projectId, body)

Create a new storage connector for the feature store

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String connectorType = "connectorType_example"; // String | storage connector type
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
FeaturestoreStorageConnectorDTO body = new FeaturestoreStorageConnectorDTO(); // FeaturestoreStorageConnectorDTO | 
try {
    FeaturestoreStorageConnectorDTO result = apiInstance.createNewStorageConnectorWithType(connectorType, featurestoreId, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#createNewStorageConnectorWithType");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectorType** | **String**| storage connector type | [enum: HopsFS, JDBC, S3]
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **body** | [**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)|  | [optional]

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createOrUpdate"></a>
# **createOrUpdate**
> createOrUpdate(body, projectId)

Create or update a serving instance

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
RepresentsAServingModel body = new RepresentsAServingModel(); // RepresentsAServingModel | serving specification
Integer projectId = 56; // Integer | 
try {
    apiInstance.createOrUpdate(body, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#createOrUpdate");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RepresentsAServingModel**](RepresentsAServingModel.md)| serving specification |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="createOrUpdateImportJob"></a>
# **createOrUpdateImportJob**
> JobDTO createOrUpdateImportJob(body, projectId)

Configure job to import featuregroup

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
FeaturegroupImportJobDTO body = new FeaturegroupImportJobDTO(); // FeaturegroupImportJobDTO | Job configuration
Integer projectId = 56; // Integer | 
try {
    JobDTO result = apiInstance.createOrUpdateImportJob(body, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#createOrUpdateImportJob");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeaturegroupImportJobDTO**](FeaturegroupImportJobDTO.md)| Job configuration |
 **projectId** | **Integer**|  |

### Return type

[**JobDTO**](JobDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createOrUpdateTrainingDatasetJob"></a>
# **createOrUpdateTrainingDatasetJob**
> JobDTO createOrUpdateTrainingDatasetJob(body, projectId)

Configure job to create training dataset

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
TrainingDatasetJobDTO body = new TrainingDatasetJobDTO(); // TrainingDatasetJobDTO | Job configuration
Integer projectId = 56; // Integer | 
try {
    JobDTO result = apiInstance.createOrUpdateTrainingDatasetJob(body, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#createOrUpdateTrainingDatasetJob");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrainingDatasetJobDTO**](TrainingDatasetJobDTO.md)| Job configuration |
 **projectId** | **Integer**|  |

### Return type

[**JobDTO**](JobDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createProject"></a>
# **createProject**
> createProject(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
ProjectDTO body = new ProjectDTO(); // ProjectDTO | 
try {
    apiInstance.createProject(body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#createProject");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectDTO**](ProjectDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="createTopLevelDataSet"></a>
# **createTopLevelDataSet**
> createTopLevelDataSet(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
DataSetDTO body = new DataSetDTO(); // DataSetDTO | 
try {
    apiInstance.createTopLevelDataSet(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#createTopLevelDataSet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**DataSetDTO**](DataSetDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

<a name="createTopic"></a>
# **createTopic**
> createTopic(projectId, body)

Create a new Kafka topic.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
TopicDTO body = new TopicDTO(); // TopicDTO | 
try {
    apiInstance.createTopic(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#createTopic");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**TopicDTO**](TopicDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="createTrainingDataset"></a>
# **createTrainingDataset**
> TrainingDatasetDTO createTrainingDataset(featurestoreId, projectId, body)

Create training dataset for a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
TrainingDatasetDTO body = new TrainingDatasetDTO(); // TrainingDatasetDTO | 
try {
    TrainingDatasetDTO result = apiInstance.createTrainingDataset(featurestoreId, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#createTrainingDataset");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **body** | [**TrainingDatasetDTO**](TrainingDatasetDTO.md)|  | [optional]

### Return type

[**TrainingDatasetDTO**](TrainingDatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="credentials"></a>
# **credentials**
> credentials(projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.credentials(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#credentials");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="delete"></a>
# **delete**
> delete(version, projectId)

Delete commands for this environment

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.delete(version, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#delete");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="delete1"></a>
# **delete1**
> delete1(library, version, projectId)

Delete commands for this library

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String library = "library_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.delete1(library, version, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#delete1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **String**|  |
 **version** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="delete2"></a>
# **delete2**
> EnvironmentDTO delete2(version, projectId)

Remove the python environment with the specified version for this project

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    EnvironmentDTO result = apiInstance.delete2(version, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#delete2");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="delete3"></a>
# **delete3**
> delete3(name, projectId)

Delete the job with the given ID

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String name = "name_example"; // String | id
Integer projectId = 56; // Integer | 
try {
    apiInstance.delete3(name, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#delete3");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| id |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="deleteFeatureGroupFromFeatureStore"></a>
# **deleteFeatureGroupFromFeatureStore**
> FeaturegroupDTO deleteFeatureGroupFromFeatureStore(featuregroupId, featurestoreId, projectId)

Delete specific featuregroup from a specific featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer featuregroupId = 56; // Integer | Id of the featuregroup
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    FeaturegroupDTO result = apiInstance.deleteFeatureGroupFromFeatureStore(featuregroupId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#deleteFeatureGroupFromFeatureStore");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**| Id of the featuregroup |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteFeaturegroupContents"></a>
# **deleteFeaturegroupContents**
> FeaturegroupDTO deleteFeaturegroupContents(featuregroupId, featurestoreId, projectId)

Delete featuregroup contents

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer featuregroupId = 56; // Integer | Id of the featuregroup
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    FeaturegroupDTO result = apiInstance.deleteFeaturegroupContents(featuregroupId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#deleteFeaturegroupContents");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**| Id of the featuregroup |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteSchema"></a>
# **deleteSchema**
> deleteSchema(schemaName, version, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String schemaName = "schemaName_example"; // String | 
Integer version = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.deleteSchema(schemaName, version, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#deleteSchema");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schemaName** | **String**|  |
 **version** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="deleteServing"></a>
# **deleteServing**
> deleteServing(servingId, projectId)

Delete a serving instance

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer servingId = 56; // Integer | Id of the serving instance
Integer projectId = 56; // Integer | 
try {
    apiInstance.deleteServing(servingId, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#deleteServing");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **servingId** | **Integer**| Id of the serving instance |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="deleteStorageConnectorWithTypeAndId"></a>
# **deleteStorageConnectorWithTypeAndId**
> FeaturestoreStorageConnectorDTO deleteStorageConnectorWithTypeAndId(connectorType, connectorId, featurestoreId, projectId)

Delete storage connector with a specific id and type from a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String connectorType = "connectorType_example"; // String | storage connector type
Integer connectorId = 56; // Integer | Id of the storage connector
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    FeaturestoreStorageConnectorDTO result = apiInstance.deleteStorageConnectorWithTypeAndId(connectorType, connectorId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#deleteStorageConnectorWithTypeAndId");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectorType** | **String**| storage connector type | [enum: HopsFS, JDBC, S3]
 **connectorId** | **Integer**| Id of the storage connector |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteTrainingDataset"></a>
# **deleteTrainingDataset**
> TrainingDatasetDTO deleteTrainingDataset(trainingdatasetid, featurestoreId, projectId)

Delete a training datasets with a specific id from a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer trainingdatasetid = 56; // Integer | Id of the training dataset
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    TrainingDatasetDTO result = apiInstance.deleteTrainingDataset(trainingdatasetid, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#deleteTrainingDataset");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trainingdatasetid** | **Integer**| Id of the training dataset |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**TrainingDatasetDTO**](TrainingDatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="downloadCerts"></a>
# **downloadCerts**
> downloadCerts(projectId, password)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
String password = "password_example"; // String | 
try {
    apiInstance.downloadCerts(projectId, password);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#downloadCerts");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **password** | [**String**](.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

<a name="downloadDatasetHdfs"></a>
# **downloadDatasetHdfs**
> downloadDatasetHdfs(publicDSId, projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String publicDSId = "publicDSId_example"; // String | 
Integer projectId = 56; // Integer | 
Download body = new Download(); // Download | 
try {
    apiInstance.downloadDatasetHdfs(publicDSId, projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#downloadDatasetHdfs");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicDSId** | **String**|  |
 **projectId** | **Integer**|  |
 **body** | [**Download**](Download.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="downloadDatasetKafka"></a>
# **downloadDatasetKafka**
> downloadDatasetKafka(publicDSId, projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String publicDSId = "publicDSId_example"; // String | 
Integer projectId = 56; // Integer | 
Download body = new Download(); // Download | 
try {
    apiInstance.downloadDatasetKafka(publicDSId, projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#downloadDatasetKafka");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicDSId** | **String**|  |
 **projectId** | **Integer**|  |
 **body** | [**Download**](Download.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="downloadFromHDFS"></a>
# **downloadFromHDFS**
> downloadFromHDFS(path, projectId, token)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String path = "path_example"; // String | 
Integer projectId = 56; // Integer | 
String token = "token_example"; // String | 
try {
    apiInstance.downloadFromHDFS(path, projectId, token);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#downloadFromHDFS");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **String**|  |
 **projectId** | **Integer**|  |
 **token** | **String**|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="example"></a>
# **example**
> example(type)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String type = "type_example"; // String | 
try {
    apiInstance.example(type);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#example");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="execution"></a>
# **execution**
> execution(action, name, projectId)

Start/Stop a job

Starts a job by creating and starting an Execution, stops a job by stopping the Execution.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String action = "action_example"; // String | start or stop
String name = "name_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.execution(action, name, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#execution");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **String**| start or stop | [enum: START, STOP]
 **name** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="filePreview"></a>
# **filePreview**
> filePreview(path, projectId, mode)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String path = "path_example"; // String | 
Integer projectId = 56; // Integer | 
String mode = "mode_example"; // String | 
try {
    apiInstance.filePreview(path, projectId, mode);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#filePreview");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **String**|  |
 **projectId** | **Integer**|  |
 **mode** | **String**|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="findAllById"></a>
# **findAllById**
> ActivitiesDTO findAllById(activityId, projectId, expand)

Finds an activity in project.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer activityId = 56; // Integer | 
Integer projectId = 56; // Integer | 
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=creator
try {
    ActivitiesDTO result = apiInstance.findAllById(activityId, projectId, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#findAllById");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activityId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;creator | [optional] [enum: expand=creator]

### Return type

[**ActivitiesDTO**](ActivitiesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="findAllByProject"></a>
# **findAllByProject**
> ActivitiesDTO findAllByProject(projectId, offset, limit, sortBy, filterBy, expand)

Finds activities in project.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
Integer offset = 56; // Integer | 
Integer limit = 56; // Integer | 
String sortBy = "sortBy_example"; // String | ex. sort_by=ID:asc,date_created:desc
List<String> filterBy = Arrays.asList("filterBy_example"); // List<String> | ex. filter_by=flag:dataset
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=creator
try {
    ActivitiesDTO result = apiInstance.findAllByProject(projectId, offset, limit, sortBy, filterBy, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#findAllByProject");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **offset** | **Integer**|  | [optional]
 **limit** | **Integer**|  | [optional]
 **sortBy** | **String**| ex. sort_by&#x3D;ID:asc,date_created:desc | [optional] [enum: id:asc, id:desc, date_created:asc, date_created:desc, flag:asc, flag:desc]
 **filterBy** | [**List&lt;String&gt;**](String.md)| ex. filter_by&#x3D;flag:dataset | [optional] [enum: flag:project, flag:dataset, flag:member, flag:service, flag:job]
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;creator | [optional] [enum: expand=creator]

### Return type

[**ActivitiesDTO**](ActivitiesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="findAllByUser"></a>
# **findAllByUser**
> findAllByUser()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
try {
    apiInstance.findAllByUser();
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#findAllByUser");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="findByProjectID"></a>
# **findByProjectID**
> findByProjectID(projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.findByProjectID(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#findByProjectID");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="findDataSetsInProjectID"></a>
# **findDataSetsInProjectID**
> findDataSetsInProjectID(projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.findDataSetsInProjectID(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#findDataSetsInProjectID");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="findMembersByProjectID"></a>
# **findMembersByProjectID**
> findMembersByProjectID(projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.findMembersByProjectID(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#findMembersByProjectID");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="get"></a>
# **get**
> get(version, projectId, offset, limit, sortBy, filterBy)

Get commands for this environment

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
Integer offset = 56; // Integer | 
Integer limit = 56; // Integer | 
String sortBy = "sortBy_example"; // String | ex. sort_by=ID:asc,date_created:desc
List<String> filterBy = Arrays.asList("filterBy_example"); // List<String> | ex. filter_by=op:create
try {
    apiInstance.get(version, projectId, offset, limit, sortBy, filterBy);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#get");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **String**|  |
 **projectId** | **Integer**|  |
 **offset** | **Integer**|  | [optional]
 **limit** | **Integer**|  | [optional]
 **sortBy** | **String**| ex. sort_by&#x3D;ID:asc,date_created:desc | [optional] [enum: id:asc, id:desc, status:asc, status:desc, date_created:asc, date_created:desc, host:asc, host:desc]
 **filterBy** | [**List&lt;String&gt;**](String.md)| ex. filter_by&#x3D;op:create | [optional] [enum: op:CLONE, op:CREATE, op:BACKUP, op:REMOVE, op:LIST, op:INSTALL, op:UNINSTALL, op:UPGRADE, op:CLEAN, op:YML, status:NEW, status:SUCCESS, status:ONGOING, status:FAILED, machine_type:ALL, machine_type:CPU, machine_type:GPU, host_in:1, host_nin:4, host_lt:5, host_gt:3]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="get1"></a>
# **get1**
> CommandDTO get1(library, version, projectId, offset, limit, sortBy, filterBy)

Get all commands for this library

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String library = "library_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
Integer offset = 56; // Integer | 
Integer limit = 56; // Integer | 
String sortBy = "sortBy_example"; // String | ex. sort_by=ID:asc,date_created:desc
List<String> filterBy = Arrays.asList("filterBy_example"); // List<String> | ex. filter_by=op:create
try {
    CommandDTO result = apiInstance.get1(library, version, projectId, offset, limit, sortBy, filterBy);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#get1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **String**|  |
 **version** | **String**|  |
 **projectId** | **Integer**|  |
 **offset** | **Integer**|  | [optional]
 **limit** | **Integer**|  | [optional]
 **sortBy** | **String**| ex. sort_by&#x3D;ID:asc,date_created:desc | [optional] [enum: id:asc, id:desc, status:asc, status:desc, date_created:asc, date_created:desc, host:asc, host:desc]
 **filterBy** | [**List&lt;String&gt;**](String.md)| ex. filter_by&#x3D;op:create | [optional] [enum: op:CLONE, op:CREATE, op:BACKUP, op:REMOVE, op:LIST, op:INSTALL, op:UNINSTALL, op:UPGRADE, op:CLEAN, op:YML, status:NEW, status:SUCCESS, status:ONGOING, status:FAILED, machine_type:ALL, machine_type:CPU, machine_type:GPU, host_in:1, host_nin:4, host_lt:5, host_gt:3]

### Return type

[**CommandDTO**](CommandDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="get2"></a>
# **get2**
> LibraryDTO get2(version, projectId, offset, limit, sortBy, filterBy, expand)

Get the python libraries installed in this environment

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
Integer offset = 56; // Integer | 
Integer limit = 56; // Integer | 
String sortBy = "sortBy_example"; // String | ex. sort_by=ID:asc,dependency:desc
List<String> filterBy = Arrays.asList("filterBy_example"); // List<String> | ex. filter_by=preinstalled:1
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=commands
try {
    LibraryDTO result = apiInstance.get2(version, projectId, offset, limit, sortBy, filterBy, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#get2");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **String**|  |
 **projectId** | **Integer**|  |
 **offset** | **Integer**|  | [optional]
 **limit** | **Integer**|  | [optional]
 **sortBy** | **String**| ex. sort_by&#x3D;ID:asc,dependency:desc | [optional] [enum: id:asc, id:desc, dependency:asc, dependency:desc, status:asc, status:desc]
 **filterBy** | [**List&lt;String&gt;**](String.md)| ex. filter_by&#x3D;preinstalled:1 | [optional] [enum: preinstalled:1, preinstalled:0, status:new, status:success, status:ongoing, status:failed]
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;commands | [optional] [enum: commands]

### Return type

[**LibraryDTO**](LibraryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="get3"></a>
# **get3**
> EnvironmentDTO get3(version, projectId, expand)

Get the python environment for specific python version

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=commands
try {
    EnvironmentDTO result = apiInstance.get3(version, projectId, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#get3");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **String**|  |
 **projectId** | **Integer**|  |
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;commands | [optional] [enum: commands, libraries]

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getAll"></a>
# **getAll**
> EnvironmentDTO getAll(projectId, expand)

Get all python environments for this project

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=commands
try {
    EnvironmentDTO result = apiInstance.getAll(projectId, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getAll");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;commands | [optional] [enum: commands, libraries]

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getAll1"></a>
# **getAll1**
> JobDTO getAll1(projectId, offset, limit, sortBy, filterBy, expand)

Get a list of all jobs for this project

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
Integer offset = 56; // Integer | 
Integer limit = 56; // Integer | 
String sortBy = "sortBy_example"; // String | ex. sort_by=date_created:desc,name:asc
List<String> filterBy = Arrays.asList("filterBy_example"); // List<String> | ex. filter_by=jobtype:spark&filter_by=date_created_gt:2018-12-25T17:12:10
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=creator
try {
    JobDTO result = apiInstance.getAll1(projectId, offset, limit, sortBy, filterBy, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getAll1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **offset** | **Integer**|  | [optional]
 **limit** | **Integer**|  | [optional]
 **sortBy** | **String**| ex. sort_by&#x3D;date_created:desc,name:asc | [optional] [enum: id:asc, id:desc, name:asc, name:desc, date_created:asc, date_created:desc, jobtype:asc, jobtype:desc, creator:asc, creator:desc, creator_firstname:asc, creator_firstname:desc, creator_lastname:asc, creator_lastname:desc, state:asc, state:desc, finalstatus:asc, finalstatus:desc, progress:asc, progress:desc, submissiontime:asc, submissiontime:desc, duration:asc, duration:desc]
 **filterBy** | [**List&lt;String&gt;**](String.md)| ex. filter_by&#x3D;jobtype:spark&amp;filter_by&#x3D;date_created_gt:2018-12-25T17:12:10 | [optional] [enum: filter_by=jobtype:spark, filter_by=jobtype:pyspark, filter_by=jobtype:flink, filter_by=jobtype:beam_flink, filter_by=jobtype_neq:spark, filter_by=jobtype_neq:pyspark, filter_by=jobtype_neq:flink, filter_by=jobtype_neq:beam_flink, filter_by=date_created:2018-12-25T17:12:10.058, filter_by=date_created_gt:2018-12-25T17:12:10.058, filter_by=date_created_lt:2018-12-25T17:12:10.058, filter_by=name:myetl, filter_by=creator:john, filter_by=latest_execution:finished]
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;creator | [optional] [enum: expand=creator, expand=executions]

### Return type

[**JobDTO**](JobDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getAllNotebookServersInProject"></a>
# **getAllNotebookServersInProject**
> getAllNotebookServersInProject(projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.getAllNotebookServersInProject(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getAllNotebookServersInProject");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getAllProjects"></a>
# **getAllProjects**
> getAllProjects()



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
try {
    apiInstance.getAllProjects();
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getAllProjects");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getAppInfo"></a>
# **getAppInfo**
> getAppInfo(appId, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String appId = "appId_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.getAppInfo(appId, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getAppInfo");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getByName"></a>
# **getByName**
> CommandDTO getByName(commandId, version, projectId)

Get commands by id

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer commandId = 56; // Integer | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    CommandDTO result = apiInstance.getByName(commandId, version, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getByName");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commandId** | **Integer**|  |
 **version** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

[**CommandDTO**](CommandDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getByName1"></a>
# **getByName1**
> CommandDTO getByName1(library, commandId, version, projectId)

Get command by id

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String library = "library_example"; // String | 
Integer commandId = 56; // Integer | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    CommandDTO result = apiInstance.getByName1(library, commandId, version, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getByName1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **String**|  |
 **commandId** | **Integer**|  |
 **version** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

[**CommandDTO**](CommandDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getByName2"></a>
# **getByName2**
> LibraryDTO getByName2(library, version, projectId, expand)

Get the a python library installed in this environment

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String library = "library_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=commands
try {
    LibraryDTO result = apiInstance.getByName2(library, version, projectId, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getByName2");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **String**|  |
 **version** | **String**|  |
 **projectId** | **Integer**|  |
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;commands | [optional] [enum: commands]

### Return type

[**LibraryDTO**](LibraryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getCurrentMultiplicator"></a>
# **getCurrentMultiplicator**
> getCurrentMultiplicator(projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.getCurrentMultiplicator(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getCurrentMultiplicator");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getDatasetInfo"></a>
# **getDatasetInfo**
> getDatasetInfo(inodeId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Long inodeId = 789L; // Long | 
try {
    apiInstance.getDatasetInfo(inodeId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getDatasetInfo");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inodeId** | **Long**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getDatasetInfo1"></a>
# **getDatasetInfo1**
> getDatasetInfo1(projectId, inodeId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
Long inodeId = 789L; // Long | 
try {
    apiInstance.getDatasetInfo1(projectId, inodeId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getDatasetInfo1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **inodeId** | **Long**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getDirContent"></a>
# **getDirContent**
> getDirContent(path, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String path = "path_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.getDirContent(path, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getDirContent");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getExecution"></a>
# **getExecution**
> ExecutionDTO getExecution(id, name, projectId, sortBy, filterBy, expand)

Find Execution by Id

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer id = 56; // Integer | execution id
String name = "name_example"; // String | 
Integer projectId = 56; // Integer | 
String sortBy = "sortBy_example"; // String | ex. sort_by=submissiontime:desc,id:asc
List<String> filterBy = Arrays.asList("filterBy_example"); // List<String> | state and finalstatus accept also neq (not equals) ex. filter_by=state:running&filter_by=state_neq:new&filter_by=submissiontime:2018-12-25T17:12:10.058
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=creator
try {
    ExecutionDTO result = apiInstance.getExecution(id, name, projectId, sortBy, filterBy, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getExecution");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**| execution id |
 **name** | **String**|  |
 **projectId** | **Integer**|  |
 **sortBy** | **String**| ex. sort_by&#x3D;submissiontime:desc,id:asc | [optional] [enum: id:asc, id:desc, name, submissiontime:asc, submissiontime:desc, state:asc, state:desc, finalstatus:asc, finalstatus:desc, appId:asc, appId:desc, progress:asc, progress:desc, duration:asc, duration:desc]
 **filterBy** | [**List&lt;String&gt;**](String.md)| state and finalstatus accept also neq (not equals) ex. filter_by&#x3D;state:running&amp;filter_by&#x3D;state_neq:new&amp;filter_by&#x3D;submissiontime:2018-12-25T17:12:10.058 | [optional] [enum: state:initializing, state:initialization_failed, state:finished, state:running, state:accepted, state:failed, state:killed, state:new, state:new_saving, state:submitted, state:aggregating_logs, state:framework_failure, state:starting_app_master, state:app_master_start_failed, finalstatus:undefined, finalstatus:succeeded, finalstatus:failed, finalstatus:killed, submissiontime:2018-12-25T17:12:10.058, submissiontime_gt:2018-12-25T17:12:10.058, submissiontime_lt:2018-12-25T17:12:10.058]
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;creator | [optional] [enum: expand=creator]

### Return type

[**ExecutionDTO**](ExecutionDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getExecutions"></a>
# **getExecutions**
> ExecutionDTO getExecutions(name, projectId, offset, limit, sortBy, filterBy, expand)

Get a list of executions for the job.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String name = "name_example"; // String | 
Integer projectId = 56; // Integer | 
Integer offset = 56; // Integer | 
Integer limit = 56; // Integer | 
String sortBy = "sortBy_example"; // String | ex. sort_by=submissiontime:desc,id:asc
List<String> filterBy = Arrays.asList("filterBy_example"); // List<String> | state and finalstatus accept also neq (not equals) ex. filter_by=state:running&filter_by=state_neq:new&filter_by=submissiontime:2018-12-25T17:12:10.058
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=creator
try {
    ExecutionDTO result = apiInstance.getExecutions(name, projectId, offset, limit, sortBy, filterBy, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getExecutions");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**|  |
 **projectId** | **Integer**|  |
 **offset** | **Integer**|  | [optional]
 **limit** | **Integer**|  | [optional]
 **sortBy** | **String**| ex. sort_by&#x3D;submissiontime:desc,id:asc | [optional] [enum: id:asc, id:desc, name, submissiontime:asc, submissiontime:desc, state:asc, state:desc, finalstatus:asc, finalstatus:desc, appId:asc, appId:desc, progress:asc, progress:desc, duration:asc, duration:desc]
 **filterBy** | [**List&lt;String&gt;**](String.md)| state and finalstatus accept also neq (not equals) ex. filter_by&#x3D;state:running&amp;filter_by&#x3D;state_neq:new&amp;filter_by&#x3D;submissiontime:2018-12-25T17:12:10.058 | [optional] [enum: state:initializing, state:initialization_failed, state:finished, state:running, state:accepted, state:failed, state:killed, state:new, state:new_saving, state:submitted, state:aggregating_logs, state:framework_failure, state:starting_app_master, state:app_master_start_failed, finalstatus:undefined, finalstatus:succeeded, finalstatus:failed, finalstatus:killed, submissiontime:2018-12-25T17:12:10.058, submissiontime_gt:2018-12-25T17:12:10.058, submissiontime_lt:2018-12-25T17:12:10.058]
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;creator | [optional] [enum: expand=creator]

### Return type

[**ExecutionDTO**](ExecutionDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getExtendedDetails"></a>
# **getExtendedDetails**
> getExtendedDetails(publicDSId, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String publicDSId = "publicDSId_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.getExtendedDetails(publicDSId, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getExtendedDetails");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicDSId** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getFeatureGroupFromFeatureStore"></a>
# **getFeatureGroupFromFeatureStore**
> FeaturegroupDTO getFeatureGroupFromFeatureStore(featuregroupId, featurestoreId, projectId)

Get specific featuregroup from a specific featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer featuregroupId = 56; // Integer | Id of the featuregroup
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    FeaturegroupDTO result = apiInstance.getFeatureGroupFromFeatureStore(featuregroupId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getFeatureGroupFromFeatureStore");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**| Id of the featuregroup |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getFeatureGroupPreview"></a>
# **getFeatureGroupPreview**
> List&lt;FeaturegroupPreview&gt; getFeatureGroupPreview(featuregroupId, featurestoreId, projectId)

Preview feature data of a featuregroup

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer featuregroupId = 56; // Integer | Id of the featuregroup
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    List<FeaturegroupPreview> result = apiInstance.getFeatureGroupPreview(featuregroupId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getFeatureGroupPreview");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**| Id of the featuregroup |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**List&lt;FeaturegroupPreview&gt;**](FeaturegroupPreview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getFeatureGroupSchema"></a>
# **getFeatureGroupSchema**
> RowValueQueryResult getFeatureGroupSchema(featuregroupId, featurestoreId, projectId)

Get the SQL schema of a featuregroup

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer featuregroupId = 56; // Integer | Id of the featuregroup
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    RowValueQueryResult result = apiInstance.getFeatureGroupSchema(featuregroupId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getFeatureGroupSchema");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**| Id of the featuregroup |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**RowValueQueryResult**](RowValueQueryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getFeaturegroupsForFeaturestore"></a>
# **getFeaturegroupsForFeaturestore**
> List&lt;FeaturegroupDTO&gt; getFeaturegroupsForFeaturestore(featurestoreId, projectId)

Get the list of feature groups for a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    List<FeaturegroupDTO> result = apiInstance.getFeaturegroupsForFeaturestore(featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getFeaturegroupsForFeaturestore");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**List&lt;FeaturegroupDTO&gt;**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getFeaturestore"></a>
# **getFeaturestore**
> FeaturestoreDTO getFeaturestore(featurestoreId, projectId)

Get featurestore with specific Id

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer featurestoreId = 56; // Integer | Id of the featurestore
Integer projectId = 56; // Integer | 
try {
    FeaturestoreDTO result = apiInstance.getFeaturestore(featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getFeaturestore");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreId** | **Integer**| Id of the featurestore |
 **projectId** | **Integer**|  |

### Return type

[**FeaturestoreDTO**](FeaturestoreDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getFeaturestoreByName"></a>
# **getFeaturestoreByName**
> FeaturestoreDTO getFeaturestoreByName(featurestoreName, projectId)

Get featurestore with specific name

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String featurestoreName = "featurestoreName_example"; // String | Id of the featurestore
Integer projectId = 56; // Integer | 
try {
    FeaturestoreDTO result = apiInstance.getFeaturestoreByName(featurestoreName, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getFeaturestoreByName");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreName** | **String**| Id of the featurestore |
 **projectId** | **Integer**|  |

### Return type

[**FeaturestoreDTO**](FeaturestoreDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getFeaturestoreId"></a>
# **getFeaturestoreId**
> FeaturestoreClientSettingsDTO getFeaturestoreId(featurestoreName, projectId)

Get featurestore Metadata

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String featurestoreName = "featurestoreName_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    FeaturestoreClientSettingsDTO result = apiInstance.getFeaturestoreId(featurestoreName, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getFeaturestoreId");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreName** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

[**FeaturestoreClientSettingsDTO**](FeaturestoreClientSettingsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getFeaturestoreSettings"></a>
# **getFeaturestoreSettings**
> FeaturestoreClientSettingsDTO getFeaturestoreSettings(projectId)

Get featurestore settings

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    FeaturestoreClientSettingsDTO result = apiInstance.getFeaturestoreSettings(projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getFeaturestoreSettings");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

[**FeaturestoreClientSettingsDTO**](FeaturestoreClientSettingsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getFeaturestores"></a>
# **getFeaturestores**
> List&lt;FeaturestoreDTO&gt; getFeaturestores(projectId)

Get the list of feature stores for the project

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    List<FeaturestoreDTO> result = apiInstance.getFeaturestores(projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getFeaturestores");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

[**List&lt;FeaturestoreDTO&gt;**](FeaturestoreDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getFile"></a>
# **getFile**
> getFile(path, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String path = "path_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.getFile(path, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getFile");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getGitStatusOfJupyterRepo"></a>
# **getGitStatusOfJupyterRepo**
> getGitStatusOfJupyterRepo(projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.getGitStatusOfJupyterRepo(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getGitStatusOfJupyterRepo");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getJob"></a>
# **getJob**
> JobDTO getJob(name, projectId, sortBy, filterBy, expand)

Get the job with requested ID

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String name = "name_example"; // String | 
Integer projectId = 56; // Integer | 
String sortBy = "sortBy_example"; // String | ex. sort_by=date_created:desc,name:asc
List<String> filterBy = Arrays.asList("filterBy_example"); // List<String> | ex. filter_by=jobtype:spark&filter_by=date_created_gt:2018-12-25T17:12:10
List<String> expand = Arrays.asList("expand_example"); // List<String> | ex. expand=creator
try {
    JobDTO result = apiInstance.getJob(name, projectId, sortBy, filterBy, expand);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getJob");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**|  |
 **projectId** | **Integer**|  |
 **sortBy** | **String**| ex. sort_by&#x3D;date_created:desc,name:asc | [optional] [enum: id:asc, id:desc, name:asc, name:desc, date_created:asc, date_created:desc, jobtype:asc, jobtype:desc, creator:asc, creator:desc, creator_firstname:asc, creator_firstname:desc, creator_lastname:asc, creator_lastname:desc, state:asc, state:desc, finalstatus:asc, finalstatus:desc, progress:asc, progress:desc, submissiontime:asc, submissiontime:desc, duration:asc, duration:desc]
 **filterBy** | [**List&lt;String&gt;**](String.md)| ex. filter_by&#x3D;jobtype:spark&amp;filter_by&#x3D;date_created_gt:2018-12-25T17:12:10 | [optional] [enum: filter_by=jobtype:spark, filter_by=jobtype:pyspark, filter_by=jobtype:flink, filter_by=jobtype:beam_flink, filter_by=jobtype_neq:spark, filter_by=jobtype_neq:pyspark, filter_by=jobtype_neq:flink, filter_by=jobtype_neq:beam_flink, filter_by=date_created:2018-12-25T17:12:10.058, filter_by=date_created_gt:2018-12-25T17:12:10.058, filter_by=date_created_lt:2018-12-25T17:12:10.058, filter_by=name:myetl, filter_by=creator:john, filter_by=latest_execution:finished]
 **expand** | [**List&lt;String&gt;**](String.md)| ex. expand&#x3D;creator | [optional] [enum: expand=creator, expand=executions]

### Return type

[**JobDTO**](JobDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getJobUI"></a>
# **getJobUI**
> getJobUI(appId, isLivy, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String appId = "appId_example"; // String | 
String isLivy = "isLivy_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.getJobUI(appId, isLivy, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getJobUI");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**|  |
 **isLivy** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getLog"></a>
# **getLog**
> JobLogDTO getLog(id, type, name, projectId)

Retrieve log of given execution and type

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer id = 56; // Integer | 
String type = "type_example"; // String | 
String name = "name_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    JobLogDTO result = apiInstance.getLog(id, type, name, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getLog");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**|  |
 **type** | **String**|  | [enum: OUT, ERR]
 **name** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

[**JobLogDTO**](JobLogDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getMoreInfo"></a>
# **getMoreInfo**
> getMoreInfo(projectId, inodeId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
Long inodeId = 789L; // Long | 
try {
    apiInstance.getMoreInfo(projectId, inodeId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getMoreInfo");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **inodeId** | **Long**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getMoreInfo1"></a>
# **getMoreInfo1**
> getMoreInfo1(inodeId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Long inodeId = 789L; // Long | 
try {
    apiInstance.getMoreInfo1(inodeId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getMoreInfo1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inodeId** | **Long**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getMoreInfo2"></a>
# **getMoreInfo2**
> getMoreInfo2(projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.getMoreInfo2(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getMoreInfo2");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getOnlineFeaturestoreStorageConnector"></a>
# **getOnlineFeaturestoreStorageConnector**
> FeaturestoreStorageConnectorDTO getOnlineFeaturestoreStorageConnector(featurestoreId, projectId)

Get online featurestore storage connector for this feature store

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    FeaturestoreStorageConnectorDTO result = apiInstance.getOnlineFeaturestoreStorageConnector(featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getOnlineFeaturestoreStorageConnector");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getPia"></a>
# **getPia**
> getPia(projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.getPia(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getPia");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getProjectByName"></a>
# **getProjectByName**
> getProjectByName(projectName)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String projectName = "projectName_example"; // String | 
try {
    apiInstance.getProjectByName(projectName);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getProjectByName");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectName** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getProjectContents"></a>
# **getProjectContents**
> getProjectContents(projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.getProjectContents(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getProjectContents");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getProjectSharedWith"></a>
# **getProjectSharedWith**
> getProjectSharedWith(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
DataSetDTO body = new DataSetDTO(); // DataSetDTO | 
try {
    apiInstance.getProjectSharedWith(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getProjectSharedWith");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**DataSetDTO**](DataSetDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

<a name="getReadmeByInodeId"></a>
# **getReadmeByInodeId**
> getReadmeByInodeId(inodeId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Long inodeId = 789L; // Long | 
try {
    apiInstance.getReadmeByInodeId(inodeId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getReadmeByInodeId");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inodeId** | **Long**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getRemoteGitBranches"></a>
# **getRemoteGitBranches**
> getRemoteGitBranches(projectId, remoteURI, keyName)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
String remoteURI = "remoteURI_example"; // String | 
String keyName = "keyName_example"; // String | 
try {
    apiInstance.getRemoteGitBranches(projectId, remoteURI, keyName);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getRemoteGitBranches");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **remoteURI** | **String**|  | [optional]
 **keyName** | **String**|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getSchema"></a>
# **getSchema**
> getSchema(topic, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String topic = "topic_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.getSchema(topic, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getSchema");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getSchemaContent"></a>
# **getSchemaContent**
> getSchemaContent(schemaName, schemaVersion, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String schemaName = "schemaName_example"; // String | 
Integer schemaVersion = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.getSchemaContent(schemaName, schemaVersion, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getSchemaContent");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schemaName** | **String**|  |
 **schemaVersion** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getServing"></a>
# **getServing**
> RepresentsAServingModel getServing(servingId, projectId)

Get info about a serving instance for the project

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer servingId = 56; // Integer | Id of the Serving instance
Integer projectId = 56; // Integer | 
try {
    RepresentsAServingModel result = apiInstance.getServing(servingId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getServing");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **servingId** | **Integer**| Id of the Serving instance |
 **projectId** | **Integer**|  |

### Return type

[**RepresentsAServingModel**](RepresentsAServingModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getServings"></a>
# **getServings**
> List&lt;RepresentsAServingModel&gt; getServings(projectId)

Get the list of serving instances for the project

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    List<RepresentsAServingModel> result = apiInstance.getServings(projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getServings");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

[**List&lt;RepresentsAServingModel&gt;**](RepresentsAServingModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getStorageConnectorWithId"></a>
# **getStorageConnectorWithId**
> FeaturestoreStorageConnectorDTO getStorageConnectorWithId(connectorType, connectorId, featurestoreId, projectId)

Get a storage connector with a specific id and type from a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String connectorType = "connectorType_example"; // String | storage connector type
Integer connectorId = 56; // Integer | Id of the storage connector
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    FeaturestoreStorageConnectorDTO result = apiInstance.getStorageConnectorWithId(connectorType, connectorId, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getStorageConnectorWithId");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectorType** | **String**| storage connector type | [enum: HopsFS, JDBC, S3]
 **connectorId** | **Integer**| Id of the storage connector |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getStorageConnectors"></a>
# **getStorageConnectors**
> List&lt;FeaturestoreStorageConnectorDTO&gt; getStorageConnectors(featurestoreId, projectId)

Get all storage connectors of a feature store

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    List<FeaturestoreStorageConnectorDTO> result = apiInstance.getStorageConnectors(featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getStorageConnectors");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**List&lt;FeaturestoreStorageConnectorDTO&gt;**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getStorageConnectorsOfType"></a>
# **getStorageConnectorsOfType**
> List&lt;FeaturestoreStorageConnectorDTO&gt; getStorageConnectorsOfType(connectorType, featurestoreId, projectId)

Get all storage connectors of a specific type of a feature store

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String connectorType = "connectorType_example"; // String | storage connector type
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    List<FeaturestoreStorageConnectorDTO> result = apiInstance.getStorageConnectorsOfType(connectorType, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getStorageConnectorsOfType");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectorType** | **String**| storage connector type | [enum: HopsFS, JDBC, S3]
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**List&lt;FeaturestoreStorageConnectorDTO&gt;**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getTensorBoard"></a>
# **getTensorBoard**
> getTensorBoard(projectId)

Get the running TensorBoard of the logged in user in this project

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.getTensorBoard(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getTensorBoard");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getTensorBoardUrls"></a>
# **getTensorBoardUrls**
> getTensorBoardUrls(appId, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String appId = "appId_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.getTensorBoardUrls(appId, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getTensorBoardUrls");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getTopic"></a>
# **getTopic**
> getTopic(topic, projectId)

Get Kafka topic details.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String topic = "topic_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.getTopic(topic, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getTopic");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getTopicAcl"></a>
# **getTopicAcl**
> getTopicAcl(topic, id, projectId)

Get ACL metadata specified by id.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String topic = "topic_example"; // String | 
Integer id = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.getTopicAcl(topic, id, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getTopicAcl");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **String**|  |
 **id** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getTopicAcls"></a>
# **getTopicAcls**
> getTopicAcls(topic, projectId, body, offset, limit)

Get all ACLs for a specified topic.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String topic = "topic_example"; // String | 
Integer projectId = 56; // Integer | 
AclsBeanParam body = new AclsBeanParam(); // AclsBeanParam | 
Integer offset = 56; // Integer | 
Integer limit = 56; // Integer | 
try {
    apiInstance.getTopicAcls(topic, projectId, body, offset, limit);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getTopicAcls");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **String**|  |
 **projectId** | **Integer**|  |
 **body** | [**AclsBeanParam**](AclsBeanParam.md)|  | [optional]
 **offset** | **Integer**|  | [optional]
 **limit** | **Integer**|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

<a name="getTopics"></a>
# **getTopics**
> getTopics(projectId, body, offset, limit)

Retrieve Kafka topics metadata .

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
TopicsBeanParam body = new TopicsBeanParam(); // TopicsBeanParam | 
Integer offset = 56; // Integer | 
Integer limit = 56; // Integer | 
try {
    apiInstance.getTopics(projectId, body, offset, limit);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getTopics");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**TopicsBeanParam**](TopicsBeanParam.md)|  | [optional]
 **offset** | **Integer**|  | [optional]
 **limit** | **Integer**|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

<a name="getTrainingDatasetWithId"></a>
# **getTrainingDatasetWithId**
> TrainingDatasetDTO getTrainingDatasetWithId(trainingdatasetid, featurestoreId, projectId)

Get a training datasets with a specific id from a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer trainingdatasetid = 56; // Integer | Id of the training dataset
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    TrainingDatasetDTO result = apiInstance.getTrainingDatasetWithId(trainingdatasetid, featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getTrainingDatasetWithId");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trainingdatasetid** | **Integer**| Id of the training dataset |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**TrainingDatasetDTO**](TrainingDatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getTrainingDatasetsForFeaturestore"></a>
# **getTrainingDatasetsForFeaturestore**
> List&lt;TrainingDatasetDTO&gt; getTrainingDatasetsForFeaturestore(featurestoreId, projectId)

Get the list of training datasets for a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    List<TrainingDatasetDTO> result = apiInstance.getTrainingDatasetsForFeaturestore(featurestoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getTrainingDatasetsForFeaturestore");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**List&lt;TrainingDatasetDTO&gt;**](TrainingDatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getValidationResult"></a>
# **getValidationResult**
> ValidationResult getValidationResult(featuregroupId, featureStoreId, projectId)

Fetch the result of a Deequ data validation job

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer featuregroupId = 56; // Integer | 
Integer featureStoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    ValidationResult result = apiInstance.getValidationResult(featuregroupId, featureStoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getValidationResult");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**|  |
 **featureStoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getValidationRules"></a>
# **getValidationRules**
> ConstraintGroupDTO getValidationRules(featuregroupId, featureStoreId, projectId)

Get previously stored Deequ validation rules

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer featuregroupId = 56; // Integer | 
Integer featureStoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    ConstraintGroupDTO result = apiInstance.getValidationRules(featuregroupId, featureStoreId, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getValidationRules");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**|  |
 **featureStoreId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

[**ConstraintGroupDTO**](ConstraintGroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getYarnUI"></a>
# **getYarnUI**
> getYarnUI(appId, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String appId = "appId_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.getYarnUI(appId, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#getYarnUI");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="infer"></a>
# **infer**
> infer(modelName, version, verb, projectId, body)

Make inference

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String modelName = "modelName_example"; // String | Name of the model to query
String version = "version_example"; // String | Version of the model to query
String verb = "verb_example"; // String | Type of query
Integer projectId = 56; // Integer | 
String body = "body_example"; // String | 
try {
    apiInstance.infer(modelName, version, verb, projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#infer");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modelName** | **String**| Name of the model to query |
 **version** | **String**| Version of the model to query |
 **verb** | **String**| Type of query |
 **projectId** | **Integer**|  |
 **body** | [**String**](String.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="inspect"></a>
# **inspect**
> SparkJobConfiguration inspect(jobtype, path, projectId)

Inspect Spark user program and return SparkJobConfiguration

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String jobtype = "jobtype_example"; // String | spark job type
String path = "path_example"; // String | path
Integer projectId = 56; // Integer | 
try {
    SparkJobConfiguration result = apiInstance.inspect(jobtype, path, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#inspect");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobtype** | **String**| spark job type | [enum: YARN, FLINK, SPARK, PYSPARK, BEAM_FLINK, BEAM_SPARK, ERASURE_CODING]
 **path** | **String**| path |
 **projectId** | **Integer**|  |

### Return type

[**SparkJobConfiguration**](SparkJobConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="install"></a>
# **install**
> install(library, version2, projectId, packageManager, version, channel, machine)

Install a python library in the environment

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String library = "library_example"; // String | 
String version2 = "version_example"; // String | 
Integer projectId = 56; // Integer | 
String packageManager = "packageManager_example"; // String | 
String version = "version_example"; // String | 
String channel = "channel_example"; // String | 
String machine = "machine_example"; // String | 
try {
    apiInstance.install(library, version2, projectId, packageManager, version, channel, machine);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#install");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **String**|  |
 **version2** | **String**|  |
 **projectId** | **Integer**|  |
 **packageManager** | **String**|  | [optional] [enum: CONDA, PIP]
 **version** | **String**|  | [optional]
 **channel** | **String**|  | [optional]
 **machine** | **String**|  | [optional] [enum: ALL, CPU, GPU]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="isDir"></a>
# **isDir**
> isDir(path, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String path = "path_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.isDir(path, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#isDir");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="isDir1"></a>
# **isDir1**
> isDir1(path, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String path = "path_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.isDir1(path, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#isDir1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="isRunning"></a>
# **isRunning**
> isRunning(projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.isRunning(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#isRunning");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="listSchemasForTopics"></a>
# **listSchemasForTopics**
> listSchemasForTopics(projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.listSchemasForTopics(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#listSchemasForTopics");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="livySessions"></a>
# **livySessions**
> livySessions(projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.livySessions(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#livySessions");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="moveFile"></a>
# **moveFile**
> moveFile(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
MoveDTO body = new MoveDTO(); // MoveDTO | 
try {
    apiInstance.moveFile(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#moveFile");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**MoveDTO**](MoveDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="newFeaturestoreUtil"></a>
# **newFeaturestoreUtil**
> newFeaturestoreUtil(projectId, body)

Upload json input for featurestore-util jobs

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
FeaturestoreUtilJobDTO body = new FeaturestoreUtilJobDTO(); // FeaturestoreUtilJobDTO | 
try {
    apiInstance.newFeaturestoreUtil(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#newFeaturestoreUtil");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**FeaturestoreUtilJobDTO**](FeaturestoreUtilJobDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="post"></a>
# **post**
> EnvironmentDTO post(version, projectId, action)

Create an environment from version or export an environment as yaml file

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
String action = "action_example"; // String | 
try {
    EnvironmentDTO result = apiInstance.post(version, projectId, action);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#post");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **String**|  |
 **projectId** | **Integer**|  |
 **action** | **String**|  | [optional] [enum: CREATE, EXPORT]

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="postYml"></a>
# **postYml**
> EnvironmentDTO postYml(projectId, body)

Create an environment from yaml file

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
EnvironmentYmlDTO body = new EnvironmentYmlDTO(); // EnvironmentYmlDTO | 
try {
    EnvironmentDTO result = apiInstance.postYml(projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#postYml");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**EnvironmentYmlDTO**](EnvironmentYmlDTO.md)|  | [optional]

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

<a name="publish"></a>
# **publish**
> publish(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
InodeIdDTO body = new InodeIdDTO(); // InodeIdDTO | 
try {
    apiInstance.publish(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#publish");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**InodeIdDTO**](InodeIdDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="put"></a>
# **put**
> JobDTO put(name, projectId, body)

Create or Update a Job.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String name = "name_example"; // String | name
Integer projectId = 56; // Integer | 
JobConfiguration body = new JobConfiguration(); // JobConfiguration | 
try {
    JobDTO result = apiInstance.put(name, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#put");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| name |
 **projectId** | **Integer**|  |
 **body** | [**JobConfiguration**](JobConfiguration.md)|  | [optional]

### Return type

[**JobDTO**](JobDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="quotasByProjectID"></a>
# **quotasByProjectID**
> quotasByProjectID(projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.quotasByProjectID(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#quotasByProjectID");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="quotasByProjectID1"></a>
# **quotasByProjectID1**
> quotasByProjectID1(projectId, projectName, inodeId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
String projectName = "projectName_example"; // String | 
Long inodeId = 789L; // Long | 
try {
    apiInstance.quotasByProjectID1(projectId, projectName, inodeId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#quotasByProjectID1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **projectName** | **String**|  |
 **inodeId** | **Long**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="rejectRequest"></a>
# **rejectRequest**
> rejectRequest(inodeId, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Long inodeId = 789L; // Long | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.rejectRequest(inodeId, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#rejectRequest");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inodeId** | **Long**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="removeAclsFromTopic"></a>
# **removeAclsFromTopic**
> removeAclsFromTopic(topic, id, projectId)

Remove ACL specified by id.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String topic = "topic_example"; // String | 
Integer id = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.removeAclsFromTopic(topic, id, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#removeAclsFromTopic");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **String**|  |
 **id** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="removeCorrupted"></a>
# **removeCorrupted**
> removeCorrupted(fileName, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String fileName = "fileName_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.removeCorrupted(fileName, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#removeCorrupted");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fileName** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="removeMembersByID"></a>
# **removeMembersByID**
> removeMembersByID(email, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String email = "email_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.removeMembersByID(email, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#removeMembersByID");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="removeProjectAndFiles"></a>
# **removeProjectAndFiles**
> removeProjectAndFiles(projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.removeProjectAndFiles(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#removeProjectAndFiles");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="removePublic"></a>
# **removePublic**
> removePublic(publicDSId, clean, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String publicDSId = "publicDSId_example"; // String | 
Boolean clean = true; // Boolean | delete dataset
Integer projectId = 56; // Integer | 
try {
    apiInstance.removePublic(publicDSId, clean, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#removePublic");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicDSId** | **String**|  |
 **clean** | **Boolean**| delete dataset |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="removePublic1"></a>
# **removePublic1**
> removePublic1(inodeId, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Long inodeId = 789L; // Long | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.removePublic1(inodeId, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#removePublic1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inodeId** | **Long**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="removeTopic"></a>
# **removeTopic**
> removeTopic(topic, projectId)

Delete a Kafka topic.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String topic = "topic_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.removeTopic(topic, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#removeTopic");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="removedataSetdir"></a>
# **removedataSetdir**
> removedataSetdir(fileName, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String fileName = "fileName_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.removedataSetdir(fileName, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#removedataSetdir");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fileName** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="removedataSetdir1"></a>
# **removedataSetdir1**
> removedataSetdir1(fileName, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String fileName = "fileName_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.removedataSetdir1(fileName, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#removedataSetdir1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fileName** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="removefile"></a>
# **removefile**
> removefile(fileName, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String fileName = "fileName_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.removefile(fileName, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#removefile");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fileName** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="retryLog"></a>
# **retryLog**
> JobLogDTO retryLog(id, type, name, projectId)

Retry log aggregation of given execution and type

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer id = 56; // Integer | 
String type = "type_example"; // String | 
String name = "name_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    JobLogDTO result = apiInstance.retryLog(id, type, name, projectId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#retryLog");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Integer**|  |
 **type** | **String**|  | [enum: OUT, ERR]
 **name** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

[**JobLogDTO**](JobLogDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="search"></a>
# **search**
> LibrarySearchDTO search(search, version, projectId, query, channel)

Search for libraries using conda or pip package managers

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String search = "search_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
String query = "query_example"; // String | 
String channel = "channel_example"; // String | 
try {
    LibrarySearchDTO result = apiInstance.search(search, version, projectId, query, channel);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#search");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **String**|  |
 **version** | **String**|  |
 **projectId** | **Integer**|  |
 **query** | **String**|  | [optional]
 **channel** | **String**|  | [optional]

### Return type

[**LibrarySearchDTO**](LibrarySearchDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="secretDir"></a>
# **secretDir**
> secretDir(projectId)

Create project secret directory in Airflow home

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.secretDir(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#secretDir");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="setPermissions"></a>
# **setPermissions**
> setPermissions(projectId, body)

Set permissions (potentially with sticky bit) for datasets

Allow data scientists to create and modify own files in dataset.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
DataSetDTO body = new DataSetDTO(); // DataSetDTO | 
try {
    apiInstance.setPermissions(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#setPermissions");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**DataSetDTO**](DataSetDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

<a name="settings"></a>
# **settings**
> settings(projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.settings(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#settings");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="share"></a>
# **share**
> share(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
InodeIdDTO body = new InodeIdDTO(); // InodeIdDTO | 
try {
    apiInstance.share(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#share");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**InodeIdDTO**](InodeIdDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="shareDataSet"></a>
# **shareDataSet**
> shareDataSet(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
DataSetDTO body = new DataSetDTO(); // DataSetDTO | 
try {
    apiInstance.shareDataSet(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#shareDataSet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**DataSetDTO**](DataSetDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

<a name="shareTopic"></a>
# **shareTopic**
> shareTopic(topic, destProjectId, projectId)

Share a Kafka topic with a project.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String topic = "topic_example"; // String | 
Integer destProjectId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.shareTopic(topic, destProjectId, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#shareTopic");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **String**|  |
 **destProjectId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="showManifest"></a>
# **showManifest**
> showManifest(publicDSId, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String publicDSId = "publicDSId_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.showManifest(publicDSId, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#showManifest");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicDSId** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="startDownload"></a>
# **startDownload**
> startDownload(publicDSId, projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String publicDSId = "publicDSId_example"; // String | 
Integer projectId = 56; // Integer | 
Download body = new Download(); // Download | 
try {
    apiInstance.startDownload(publicDSId, projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#startDownload");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicDSId** | **String**|  |
 **projectId** | **Integer**|  |
 **body** | [**Download**](Download.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="startNotebookServer"></a>
# **startNotebookServer**
> startNotebookServer(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
JupyterSettings body = new JupyterSettings(); // JupyterSettings | 
try {
    apiInstance.startNotebookServer(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#startNotebookServer");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**JupyterSettings**](JupyterSettings.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="startOrStop"></a>
# **startOrStop**
> startOrStop(servingId, action, projectId)

Start or stop a Serving instance

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer servingId = 56; // Integer | ID of the Serving instance to start/stop
String action = "action_example"; // String | Action
Integer projectId = 56; // Integer | 
try {
    apiInstance.startOrStop(servingId, action, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#startOrStop");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **servingId** | **Integer**| ID of the Serving instance to start/stop |
 **action** | **String**| Action | [enum: START, STOP]
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="startTensorBoard"></a>
# **startTensorBoard**
> startTensorBoard(elasticId, projectId)

Start a new TensorBoard for the logged in user

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String elasticId = "elasticId_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.startTensorBoard(elasticId, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#startTensorBoard");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **elasticId** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="stopLivySession"></a>
# **stopLivySession**
> stopLivySession(appId, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String appId = "appId_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.stopLivySession(appId, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#stopLivySession");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="stopNotebookServer"></a>
# **stopNotebookServer**
> stopNotebookServer(projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.stopNotebookServer(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#stopNotebookServer");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="stopTensorBoard"></a>
# **stopTensorBoard**
> stopTensorBoard(projectId)

Stop the running TensorBoard for the logged in user

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.stopTensorBoard(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#stopTensorBoard");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="storeAirflowJWT"></a>
# **storeAirflowJWT**
> storeAirflowJWT(projectId)

Generate a JWT for Airflow usage and store it in project&#x27;s secret directory in Airflow

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
try {
    apiInstance.storeAirflowJWT(projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#storeAirflowJWT");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="syncWithFeaturestore"></a>
# **syncWithFeaturestore**
> FeaturegroupDTO syncWithFeaturestore(featurestoreId, projectId, body)

Synchornize Hive Table with the feature store

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
FeaturegroupDTO body = new FeaturegroupDTO(); // FeaturegroupDTO | 
try {
    FeaturegroupDTO result = apiInstance.syncWithFeaturestore(featurestoreId, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#syncWithFeaturestore");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **body** | [**FeaturegroupDTO**](FeaturegroupDTO.md)|  | [optional]

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

<a name="testMethod1"></a>
# **testMethod1**
> testMethod1(path, projectId, templateId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String path = "path_example"; // String | 
Integer projectId = 56; // Integer | 
Integer templateId = 56; // Integer | 
try {
    apiInstance.testMethod1(path, projectId, templateId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#testMethod1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **String**|  |
 **projectId** | **Integer**|  |
 **templateId** | **Integer**|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="topicIsSharedTo"></a>
# **topicIsSharedTo**
> topicIsSharedTo(topic, projectId)

Get list of projects that a topic has been shared with.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String topic = "topic_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.topicIsSharedTo(topic, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#topicIsSharedTo");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="uninstall"></a>
# **uninstall**
> uninstall(library, version, projectId)

Uninstall a python library from the environment

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String library = "library_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.uninstall(library, version, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#uninstall");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **String**|  |
 **version** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="unscheduleJob"></a>
# **unscheduleJob**
> unscheduleJob(name, projectId)

Cancel a job&#x27;s schedule.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String name = "name_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.unscheduleJob(name, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#unscheduleJob");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="unshareDataSet"></a>
# **unshareDataSet**
> unshareDataSet(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
DataSetDTO body = new DataSetDTO(); // DataSetDTO | 
try {
    apiInstance.unshareDataSet(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#unshareDataSet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**DataSetDTO**](DataSetDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

<a name="unshareTopicFromProject"></a>
# **unshareTopicFromProject**
> unshareTopicFromProject(topic, destProjectId, projectId)

Unshare Kafka topic from a project (specified as destProjectId).

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String topic = "topic_example"; // String | 
Integer destProjectId = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.unshareTopicFromProject(topic, destProjectId, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#unshareTopicFromProject");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **String**|  |
 **destProjectId** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="unshareTopicFromProjects"></a>
# **unshareTopicFromProjects**
> unshareTopicFromProjects(topic, projectId)

Unshare Kafka topic from all projects.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String topic = "topic_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.unshareTopicFromProjects(topic, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#unshareTopicFromProjects");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="unzip"></a>
# **unzip**
> unzip(path, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String path = "path_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.unzip(path, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#unzip");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="update"></a>
# **update**
> update(library, version, projectId)

Update commands for this library

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String library = "library_example"; // String | 
String version = "version_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.update(library, version, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#update");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **String**|  |
 **version** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="updateFeaturegroup"></a>
# **updateFeaturegroup**
> FeaturegroupDTO updateFeaturegroup(featuregroupId, featurestoreId, projectId, body, updateMetadata, updateStats, enableOnline, disableOnline, updateStatsSettings)

Update featuregroup contents

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer featuregroupId = 56; // Integer | Id of the featuregroup
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
FeaturegroupDTO body = new FeaturegroupDTO(); // FeaturegroupDTO | 
Boolean updateMetadata = true; // Boolean | updateMetadata
Boolean updateStats = true; // Boolean | updateStats
Boolean enableOnline = true; // Boolean | enableOnline
Boolean disableOnline = true; // Boolean | disableOnline
Boolean updateStatsSettings = true; // Boolean | updateStatsSettings
try {
    FeaturegroupDTO result = apiInstance.updateFeaturegroup(featuregroupId, featurestoreId, projectId, body, updateMetadata, updateStats, enableOnline, disableOnline, updateStatsSettings);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#updateFeaturegroup");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroupId** | **Integer**| Id of the featuregroup |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **body** | [**FeaturegroupDTO**](FeaturegroupDTO.md)|  | [optional]
 **updateMetadata** | **Boolean**| updateMetadata | [optional]
 **updateStats** | **Boolean**| updateStats | [optional]
 **enableOnline** | **Boolean**| enableOnline | [optional]
 **disableOnline** | **Boolean**| disableOnline | [optional]
 **updateStatsSettings** | **Boolean**| updateStatsSettings | [optional]

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateNotebookServer"></a>
# **updateNotebookServer**
> updateNotebookServer(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
JupyterSettings body = new JupyterSettings(); // JupyterSettings | 
try {
    apiInstance.updateNotebookServer(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#updateNotebookServer");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**JupyterSettings**](JupyterSettings.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="updatePia"></a>
# **updatePia**
> updatePia(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
Pia body = new Pia(); // Pia | 
try {
    apiInstance.updatePia(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#updatePia");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**Pia**](Pia.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="updateProject"></a>
# **updateProject**
> updateProject(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
ProjectDTO body = new ProjectDTO(); // ProjectDTO | 
try {
    apiInstance.updateProject(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#updateProject");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**ProjectDTO**](ProjectDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="updateRoleByEmail"></a>
# **updateRoleByEmail**
> updateRoleByEmail(email, projectId, role)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String email = "email_example"; // String | 
Integer projectId = 56; // Integer | 
String role = "role_example"; // String | 
try {
    apiInstance.updateRoleByEmail(email, projectId, role);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#updateRoleByEmail");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **String**|  |
 **projectId** | **Integer**|  |
 **role** | [**String**](.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

<a name="updateSchedule"></a>
# **updateSchedule**
> updateSchedule(name, projectId, body)

Create/Update job&#x27;s schedule.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String name = "name_example"; // String | 
Integer projectId = 56; // Integer | 
ScheduleDTO body = new ScheduleDTO(); // ScheduleDTO | 
try {
    apiInstance.updateSchedule(name, projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#updateSchedule");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**|  |
 **projectId** | **Integer**|  |
 **body** | [**ScheduleDTO**](ScheduleDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="updateSchemaVersion"></a>
# **updateSchemaVersion**
> updateSchemaVersion(topic, version, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String topic = "topic_example"; // String | 
Integer version = 56; // Integer | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.updateSchemaVersion(topic, version, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#updateSchemaVersion");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **String**|  |
 **version** | **Integer**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="updateStorageConnectorWithId"></a>
# **updateStorageConnectorWithId**
> FeaturestoreStorageConnectorDTO updateStorageConnectorWithId(connectorType, connectorId, featurestoreId, projectId, body)

Get a storage connector with a specific id and type from a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String connectorType = "connectorType_example"; // String | storage connector type
Integer connectorId = 56; // Integer | Id of the storage connector
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
FeaturestoreStorageConnectorDTO body = new FeaturestoreStorageConnectorDTO(); // FeaturestoreStorageConnectorDTO | 
try {
    FeaturestoreStorageConnectorDTO result = apiInstance.updateStorageConnectorWithId(connectorType, connectorId, featurestoreId, projectId, body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#updateStorageConnectorWithId");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectorType** | **String**| storage connector type | [enum: HopsFS, JDBC, S3]
 **connectorId** | **Integer**| Id of the storage connector |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **body** | [**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)|  | [optional]

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateTopicAcls"></a>
# **updateTopicAcls**
> updateTopicAcls(topic, id, projectId, body)

Update ACL specified by id.

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String topic = "topic_example"; // String | 
Integer id = 56; // Integer | 
Integer projectId = 56; // Integer | 
AclDTO body = new AclDTO(); // AclDTO | 
try {
    apiInstance.updateTopicAcls(topic, id, projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#updateTopicAcls");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **String**|  |
 **id** | **Integer**|  |
 **projectId** | **Integer**|  |
 **body** | [**AclDTO**](AclDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="updateTrainingDataset"></a>
# **updateTrainingDataset**
> TrainingDatasetDTO updateTrainingDataset(trainingdatasetid, featurestoreId, projectId, body, updateMetadata, updateStats)

Update a training datasets with a specific id from a featurestore

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer trainingdatasetid = 56; // Integer | Id of the training dataset
Integer featurestoreId = 56; // Integer | 
Integer projectId = 56; // Integer | 
TrainingDatasetDTO body = new TrainingDatasetDTO(); // TrainingDatasetDTO | 
Boolean updateMetadata = true; // Boolean | updateMetadata
Boolean updateStats = true; // Boolean | updateStats
try {
    TrainingDatasetDTO result = apiInstance.updateTrainingDataset(trainingdatasetid, featurestoreId, projectId, body, updateMetadata, updateStats);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#updateTrainingDataset");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trainingdatasetid** | **Integer**| Id of the training dataset |
 **featurestoreId** | **Integer**|  |
 **projectId** | **Integer**|  |
 **body** | [**TrainingDatasetDTO**](TrainingDatasetDTO.md)|  | [optional]
 **updateMetadata** | **Boolean**| updateMetadata | [optional]
 **updateStats** | **Boolean**| updateStats | [optional]

### Return type

[**TrainingDatasetDTO**](TrainingDatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="uploadMethod1"></a>
# **uploadMethod1**
> uploadMethod1(path, projectId, file, flowChunkNumber, flowChunkSize, flowCurrentChunkSize, flowFilename, flowIdentifier, flowRelativePath, flowTotalChunks, flowTotalSize, templateId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String path = "path_example"; // String | 
Integer projectId = 56; // Integer | 
File file = new File("file_example"); // File | 
String flowChunkNumber = "flowChunkNumber_example"; // String | 
String flowChunkSize = "flowChunkSize_example"; // String | 
String flowCurrentChunkSize = "flowCurrentChunkSize_example"; // String | 
String flowFilename = "flowFilename_example"; // String | 
String flowIdentifier = "flowIdentifier_example"; // String | 
String flowRelativePath = "flowRelativePath_example"; // String | 
String flowTotalChunks = "flowTotalChunks_example"; // String | 
String flowTotalSize = "flowTotalSize_example"; // String | 
Integer templateId = 56; // Integer | 
try {
    apiInstance.uploadMethod1(path, projectId, file, flowChunkNumber, flowChunkSize, flowCurrentChunkSize, flowFilename, flowIdentifier, flowRelativePath, flowTotalChunks, flowTotalSize, templateId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#uploadMethod1");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **String**|  |
 **projectId** | **Integer**|  |
 **file** | **File**|  | [optional]
 **flowChunkNumber** | [**String**](.md)|  | [optional]
 **flowChunkSize** | [**String**](.md)|  | [optional]
 **flowCurrentChunkSize** | [**String**](.md)|  | [optional]
 **flowFilename** | [**String**](.md)|  | [optional]
 **flowIdentifier** | [**String**](.md)|  | [optional]
 **flowRelativePath** | [**String**](.md)|  | [optional]
 **flowTotalChunks** | [**String**](.md)|  | [optional]
 **flowTotalSize** | [**String**](.md)|  | [optional]
 **templateId** | **Integer**|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

<a name="validateSchemaForTopics"></a>
# **validateSchemaForTopics**
> validateSchemaForTopics(projectId, body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
Integer projectId = 56; // Integer | 
SchemaDTO body = new SchemaDTO(); // SchemaDTO | 
try {
    apiInstance.validateSchemaForTopics(projectId, body);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#validateSchemaForTopics");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectId** | **Integer**|  |
 **body** | [**SchemaDTO**](SchemaDTO.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

<a name="zip"></a>
# **zip**
> zip(path, projectId)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.ProjectServiceApi;


ProjectServiceApi apiInstance = new ProjectServiceApi();
String path = "path_example"; // String | 
Integer projectId = 56; // Integer | 
try {
    apiInstance.zip(path, projectId);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectServiceApi#zip");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **String**|  |
 **projectId** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

