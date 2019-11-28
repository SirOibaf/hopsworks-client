# swagger_client.ProjectServiceApi

All URIs are relative to *///hopsworks-api/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_request**](ProjectServiceApi.md#accept_request) | **GET** /project/{projectId}/dataset/accept/{inodeId} | 
[**add_acls_to_topic**](ProjectServiceApi.md#add_acls_to_topic) | **POST** /project/{projectId}/kafka/topics/{topic}/acls | Add a new ACL for a specified topic.
[**add_members**](ProjectServiceApi.md#add_members) | **POST** /project/{projectId}/projectMembers | 
[**add_topic_schema**](ProjectServiceApi.md#add_topic_schema) | **POST** /project/{projectId}/kafka/schema/add | 
[**add_validation_rules**](ProjectServiceApi.md#add_validation_rules) | **POST** /project/{projectId}/featurestores/{featureStoreId}/datavalidation/{featuregroupId}/rules | Write Deequ validation rules to Filesystem so validation job can pick it up
[**attach_template**](ProjectServiceApi.md#attach_template) | **POST** /project/{projectId}/dataset/attachTemplate | 
[**check_file_exist**](ProjectServiceApi.md#check_file_exist) | **GET** /project/{projectId}/localfs/fileExists/{path} | 
[**check_file_exists**](ProjectServiceApi.md#check_file_exists) | **GET** /project/{projectId}/dataset/fileExists/{path} | 
[**check_file_for_download**](ProjectServiceApi.md#check_file_for_download) | **GET** /project/{projectId}/dataset/checkFileForDownload/{path} | 
[**check_project_access**](ProjectServiceApi.md#check_project_access) | **GET** /project/{projectId}/check | 
[**compose_dag**](ProjectServiceApi.md#compose_dag) | **POST** /project/{projectId}/airflow/dag | Generate an Airflow Python DAG file from a DAG definition
[**convert_i_python_notebook**](ProjectServiceApi.md#convert_i_python_notebook) | **GET** /project/{projectId}/jupyter/convertIPythonNotebook/{path} | 
[**copy_file**](ProjectServiceApi.md#copy_file) | **POST** /project/{projectId}/dataset/copy | 
[**count_file_blocks**](ProjectServiceApi.md#count_file_blocks) | **GET** /project/{projectId}/dataset/countFileBlocks/{path} | 
[**create_data_set_dir**](ProjectServiceApi.md#create_data_set_dir) | **POST** /project/{projectId}/dataset | 
[**create_data_set_dir1**](ProjectServiceApi.md#create_data_set_dir1) | **POST** /project/{projectId}/localfs | 
[**create_featuregroup**](ProjectServiceApi.md#create_featuregroup) | **POST** /project/{projectId}/featurestores/{featurestoreId}/featuregroups | Create feature group in a featurestore
[**create_new_storage_connector_with_type**](ProjectServiceApi.md#create_new_storage_connector_with_type) | **POST** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType} | Create a new storage connector for the feature store
[**create_or_update**](ProjectServiceApi.md#create_or_update) | **PUT** /project/{projectId}/serving | Create or update a serving instance
[**create_or_update_import_job**](ProjectServiceApi.md#create_or_update_import_job) | **PUT** /project/{projectId}/featurestores/importjob | Configure job to import featuregroup
[**create_or_update_training_dataset_job**](ProjectServiceApi.md#create_or_update_training_dataset_job) | **POST** /project/{projectId}/featurestores/trainingdatasetjob | Configure job to create training dataset
[**create_project**](ProjectServiceApi.md#create_project) | **POST** /project | 
[**create_top_level_data_set**](ProjectServiceApi.md#create_top_level_data_set) | **POST** /project/{projectId}/dataset/createTopLevelDataSet | 
[**create_topic**](ProjectServiceApi.md#create_topic) | **POST** /project/{projectId}/kafka/topics | Create a new Kafka topic.
[**create_training_dataset**](ProjectServiceApi.md#create_training_dataset) | **POST** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets | Create training dataset for a featurestore
[**credentials**](ProjectServiceApi.md#credentials) | **GET** /project/{projectId}/credentials | 
[**delete**](ProjectServiceApi.md#delete) | **DELETE** /project/{projectId}/python/environments/{version}/commands | Delete commands for this environment
[**delete1**](ProjectServiceApi.md#delete1) | **DELETE** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Delete commands for this library
[**delete2**](ProjectServiceApi.md#delete2) | **DELETE** /project/{projectId}/python/environments/{version} | Remove the python environment with the specified version for this project
[**delete3**](ProjectServiceApi.md#delete3) | **DELETE** /project/{projectId}/jobs/{name} | Delete the job with the given ID
[**delete_feature_group_from_feature_store**](ProjectServiceApi.md#delete_feature_group_from_feature_store) | **DELETE** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId} | Delete specific featuregroup from a specific featurestore
[**delete_featuregroup_contents**](ProjectServiceApi.md#delete_featuregroup_contents) | **POST** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId}/clear | Delete featuregroup contents
[**delete_schema**](ProjectServiceApi.md#delete_schema) | **DELETE** /project/{projectId}/kafka/removeSchema/{schemaName}/{version} | 
[**delete_serving**](ProjectServiceApi.md#delete_serving) | **DELETE** /project/{projectId}/serving/{servingId} | Delete a serving instance
[**delete_storage_connector_with_type_and_id**](ProjectServiceApi.md#delete_storage_connector_with_type_and_id) | **DELETE** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType}/{connectorId} | Delete storage connector with a specific id and type from a featurestore
[**delete_training_dataset**](ProjectServiceApi.md#delete_training_dataset) | **DELETE** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid} | Delete a training datasets with a specific id from a featurestore
[**download_certs**](ProjectServiceApi.md#download_certs) | **POST** /project/{projectId}/downloadCert | 
[**download_dataset_hdfs**](ProjectServiceApi.md#download_dataset_hdfs) | **POST** /project/{projectId}/dela/downloads/{publicDSId}/hdfs | 
[**download_dataset_kafka**](ProjectServiceApi.md#download_dataset_kafka) | **POST** /project/{projectId}/dela/downloads/{publicDSId}/kafka | 
[**download_from_hdfs**](ProjectServiceApi.md#download_from_hdfs) | **GET** /project/{projectId}/dataset/fileDownload/{path} | 
[**example**](ProjectServiceApi.md#example) | **POST** /project/starterProject/{type} | 
[**execution**](ProjectServiceApi.md#execution) | **POST** /project/{projectId}/jobs/{name}/executions | Start/Stop a job
[**file_preview**](ProjectServiceApi.md#file_preview) | **GET** /project/{projectId}/dataset/filePreview/{path} | 
[**find_all_by_id**](ProjectServiceApi.md#find_all_by_id) | **GET** /project/{projectId}/activities/{activityId} | Finds an activity in project.
[**find_all_by_project**](ProjectServiceApi.md#find_all_by_project) | **GET** /project/{projectId}/activities | Finds activities in project.
[**find_all_by_user**](ProjectServiceApi.md#find_all_by_user) | **GET** /project | 
[**find_by_project_id**](ProjectServiceApi.md#find_by_project_id) | **GET** /project/{projectId} | 
[**find_data_sets_in_project_id**](ProjectServiceApi.md#find_data_sets_in_project_id) | **GET** /project/{projectId}/dataset/getContent | 
[**find_members_by_project_id**](ProjectServiceApi.md#find_members_by_project_id) | **GET** /project/{projectId}/projectMembers | 
[**get**](ProjectServiceApi.md#get) | **GET** /project/{projectId}/python/environments/{version}/commands | Get commands for this environment
[**get1**](ProjectServiceApi.md#get1) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Get all commands for this library
[**get2**](ProjectServiceApi.md#get2) | **GET** /project/{projectId}/python/environments/{version}/libraries | Get the python libraries installed in this environment
[**get3**](ProjectServiceApi.md#get3) | **GET** /project/{projectId}/python/environments/{version} | Get the python environment for specific python version
[**get_all**](ProjectServiceApi.md#get_all) | **GET** /project/{projectId}/python/environments | Get all python environments for this project
[**get_all1**](ProjectServiceApi.md#get_all1) | **GET** /project/{projectId}/jobs | Get a list of all jobs for this project
[**get_all_notebook_servers_in_project**](ProjectServiceApi.md#get_all_notebook_servers_in_project) | **GET** /project/{projectId}/jupyter | 
[**get_all_projects**](ProjectServiceApi.md#get_all_projects) | **GET** /project/getAll | 
[**get_app_info**](ProjectServiceApi.md#get_app_info) | **GET** /project/{projectId}/jobs/{appId}/appinfo | 
[**get_by_name**](ProjectServiceApi.md#get_by_name) | **GET** /project/{projectId}/python/environments/{version}/commands/{commandId} | Get commands by id
[**get_by_name1**](ProjectServiceApi.md#get_by_name1) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library}/commands/{commandId} | Get command by id
[**get_by_name2**](ProjectServiceApi.md#get_by_name2) | **GET** /project/{projectId}/python/environments/{version}/libraries/{library} | Get the a python library installed in this environment
[**get_current_multiplicator**](ProjectServiceApi.md#get_current_multiplicator) | **GET** /project/{projectId}/multiplicators | 
[**get_dataset_info**](ProjectServiceApi.md#get_dataset_info) | **GET** /project/getDatasetInfo/{inodeId} | 
[**get_dataset_info1**](ProjectServiceApi.md#get_dataset_info1) | **GET** /project/{projectId}/getInodeInfo/{inodeId} | 
[**get_dir_content**](ProjectServiceApi.md#get_dir_content) | **GET** /project/{projectId}/dataset/getContent/{path} | 
[**get_execution**](ProjectServiceApi.md#get_execution) | **GET** /project/{projectId}/jobs/{name}/executions/{id} | Find Execution by Id
[**get_executions**](ProjectServiceApi.md#get_executions) | **GET** /project/{projectId}/jobs/{name}/executions | Get a list of executions for the job.
[**get_extended_details**](ProjectServiceApi.md#get_extended_details) | **GET** /project/{projectId}/dela/transfers/{publicDSId} | 
[**get_feature_group_from_feature_store**](ProjectServiceApi.md#get_feature_group_from_feature_store) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId} | Get specific featuregroup from a specific featurestore
[**get_feature_group_preview**](ProjectServiceApi.md#get_feature_group_preview) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId}/preview | Preview feature data of a featuregroup
[**get_feature_group_schema**](ProjectServiceApi.md#get_feature_group_schema) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId}/schema | Get the SQL schema of a featuregroup
[**get_featuregroups_for_featurestore**](ProjectServiceApi.md#get_featuregroups_for_featurestore) | **GET** /project/{projectId}/featurestores/{featurestoreId}/featuregroups | Get the list of feature groups for a featurestore
[**get_featurestore**](ProjectServiceApi.md#get_featurestore) | **GET** /project/{projectId}/featurestores/{featurestoreId} | Get featurestore with specific Id
[**get_featurestore_by_name**](ProjectServiceApi.md#get_featurestore_by_name) | **GET** /project/{projectId}/featurestores/getByName/{featurestoreName} | Get featurestore with specific name
[**get_featurestore_id**](ProjectServiceApi.md#get_featurestore_id) | **GET** /project/{projectId}/featurestores/{featurestoreName}/metadata | Get featurestore Metadata
[**get_featurestore_settings**](ProjectServiceApi.md#get_featurestore_settings) | **GET** /project/{projectId}/featurestores/settings | Get featurestore settings
[**get_featurestores**](ProjectServiceApi.md#get_featurestores) | **GET** /project/{projectId}/featurestores | Get the list of feature stores for the project
[**get_file**](ProjectServiceApi.md#get_file) | **GET** /project/{projectId}/dataset/getFile/{path} | 
[**get_git_status_of_jupyter_repo**](ProjectServiceApi.md#get_git_status_of_jupyter_repo) | **GET** /project/{projectId}/jupyter/git/status | 
[**get_job**](ProjectServiceApi.md#get_job) | **GET** /project/{projectId}/jobs/{name} | Get the job with requested ID
[**get_job_ui**](ProjectServiceApi.md#get_job_ui) | **GET** /project/{projectId}/jobs/{appId}/ui/{isLivy} | 
[**get_log**](ProjectServiceApi.md#get_log) | **GET** /project/{projectId}/jobs/{name}/executions/{id}/log/{type} | Retrieve log of given execution and type
[**get_more_info**](ProjectServiceApi.md#get_more_info) | **GET** /project/{projectId}/getMoreInfo/{type}/{inodeId} | 
[**get_more_info1**](ProjectServiceApi.md#get_more_info1) | **GET** /project/getMoreInfo/{type}/{inodeId} | 
[**get_more_info2**](ProjectServiceApi.md#get_more_info2) | **GET** /project/getMoreInfo/proj/{projectId} | 
[**get_online_featurestore_storage_connector**](ProjectServiceApi.md#get_online_featurestore_storage_connector) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/onlinefeaturestore | Get online featurestore storage connector for this feature store
[**get_pia**](ProjectServiceApi.md#get_pia) | **GET** /project/{projectId}/pia | 
[**get_project_by_name**](ProjectServiceApi.md#get_project_by_name) | **GET** /project/getProjectInfo/{projectName} | 
[**get_project_contents**](ProjectServiceApi.md#get_project_contents) | **GET** /project/{projectId}/dela/transfers | 
[**get_project_shared_with**](ProjectServiceApi.md#get_project_shared_with) | **POST** /project/{projectId}/dataset/projectsSharedWith | 
[**get_readme_by_inode_id**](ProjectServiceApi.md#get_readme_by_inode_id) | **GET** /project/readme/byInodeId/{inodeId} | 
[**get_remote_git_branches**](ProjectServiceApi.md#get_remote_git_branches) | **GET** /project/{projectId}/jupyter/git/branches | 
[**get_schema**](ProjectServiceApi.md#get_schema) | **GET** /project/{projectId}/kafka/{topic}/schema | 
[**get_schema_content**](ProjectServiceApi.md#get_schema_content) | **GET** /project/{projectId}/kafka/showSchema/{schemaName}/{schemaVersion} | 
[**get_serving**](ProjectServiceApi.md#get_serving) | **GET** /project/{projectId}/serving/{servingId} | Get info about a serving instance for the project
[**get_servings**](ProjectServiceApi.md#get_servings) | **GET** /project/{projectId}/serving | Get the list of serving instances for the project
[**get_storage_connector_with_id**](ProjectServiceApi.md#get_storage_connector_with_id) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType}/{connectorId} | Get a storage connector with a specific id and type from a featurestore
[**get_storage_connectors**](ProjectServiceApi.md#get_storage_connectors) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors | Get all storage connectors of a feature store
[**get_storage_connectors_of_type**](ProjectServiceApi.md#get_storage_connectors_of_type) | **GET** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType} | Get all storage connectors of a specific type of a feature store
[**get_tensor_board**](ProjectServiceApi.md#get_tensor_board) | **GET** /project/{projectId}/tensorboard | Get the running TensorBoard of the logged in user in this project
[**get_tensor_board_urls**](ProjectServiceApi.md#get_tensor_board_urls) | **GET** /project/{projectId}/jobs/{appId}/tensorboard | 
[**get_topic**](ProjectServiceApi.md#get_topic) | **GET** /project/{projectId}/kafka/topics/{topic} | Get Kafka topic details.
[**get_topic_acl**](ProjectServiceApi.md#get_topic_acl) | **GET** /project/{projectId}/kafka/topics/{topic}/acls/{id} | Get ACL metadata specified by id.
[**get_topic_acls**](ProjectServiceApi.md#get_topic_acls) | **GET** /project/{projectId}/kafka/topics/{topic}/acls | Get all ACLs for a specified topic.
[**get_topics**](ProjectServiceApi.md#get_topics) | **GET** /project/{projectId}/kafka/topics | Retrieve Kafka topics metadata .
[**get_training_dataset_with_id**](ProjectServiceApi.md#get_training_dataset_with_id) | **GET** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid} | Get a training datasets with a specific id from a featurestore
[**get_training_datasets_for_featurestore**](ProjectServiceApi.md#get_training_datasets_for_featurestore) | **GET** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets | Get the list of training datasets for a featurestore
[**get_validation_result**](ProjectServiceApi.md#get_validation_result) | **GET** /project/{projectId}/featurestores/{featureStoreId}/datavalidation/{featuregroupId}/result | Fetch the result of a Deequ data validation job
[**get_validation_rules**](ProjectServiceApi.md#get_validation_rules) | **GET** /project/{projectId}/featurestores/{featureStoreId}/datavalidation/{featuregroupId}/rules | Get previously stored Deequ validation rules
[**get_yarn_ui**](ProjectServiceApi.md#get_yarn_ui) | **GET** /project/{projectId}/jobs/{appId}/yarnui | 
[**infer**](ProjectServiceApi.md#infer) | **POST** /project/{projectId}/inference/models/{modelName}{version}{verb} | Make inference
[**inspect**](ProjectServiceApi.md#inspect) | **GET** /project/{projectId}/jobs/{jobtype}/inspection | Inspect Spark user program and return SparkJobConfiguration
[**install**](ProjectServiceApi.md#install) | **POST** /project/{projectId}/python/environments/{version}/libraries/{library} | Install a python library in the environment
[**is_dir**](ProjectServiceApi.md#is_dir) | **GET** /project/{projectId}/dataset/isDir/{path} | 
[**is_dir1**](ProjectServiceApi.md#is_dir1) | **GET** /project/{projectId}/localfs/isDir/{path} | 
[**is_running**](ProjectServiceApi.md#is_running) | **GET** /project/{projectId}/jupyter/running | 
[**list_schemas_for_topics**](ProjectServiceApi.md#list_schemas_for_topics) | **GET** /project/{projectId}/kafka/schemas | 
[**livy_sessions**](ProjectServiceApi.md#livy_sessions) | **GET** /project/{projectId}/jupyter/livy/sessions | 
[**move_file**](ProjectServiceApi.md#move_file) | **POST** /project/{projectId}/dataset/move | 
[**new_featurestore_util**](ProjectServiceApi.md#new_featurestore_util) | **POST** /project/{projectId}/featurestores/util | Upload json input for featurestore-util jobs
[**post**](ProjectServiceApi.md#post) | **POST** /project/{projectId}/python/environments/{version} | Create an environment from version or export an environment as yaml file
[**post_yml**](ProjectServiceApi.md#post_yml) | **POST** /project/{projectId}/python/environments | Create an environment from yaml file
[**publish**](ProjectServiceApi.md#publish) | **POST** /project/{projectId}/dela/uploads | 
[**put**](ProjectServiceApi.md#put) | **PUT** /project/{projectId}/jobs/{name} | Create or Update a Job.
[**quotas_by_project_id**](ProjectServiceApi.md#quotas_by_project_id) | **GET** /project/{projectId}/quotas | 
[**quotas_by_project_id1**](ProjectServiceApi.md#quotas_by_project_id1) | **GET** /project/{projectId}/importPublicDataset/{projectName}/{inodeId} | 
[**reject_request**](ProjectServiceApi.md#reject_request) | **GET** /project/{projectId}/dataset/reject/{inodeId} | 
[**remove_acls_from_topic**](ProjectServiceApi.md#remove_acls_from_topic) | **DELETE** /project/{projectId}/kafka/topics/{topic}/acls/{id} | Remove ACL specified by id.
[**remove_corrupted**](ProjectServiceApi.md#remove_corrupted) | **DELETE** /project/{projectId}/dataset/corrupted/{fileName} | 
[**remove_members_by_id**](ProjectServiceApi.md#remove_members_by_id) | **DELETE** /project/{projectId}/projectMembers/{email} | 
[**remove_project_and_files**](ProjectServiceApi.md#remove_project_and_files) | **POST** /project/{projectId}/delete | 
[**remove_public**](ProjectServiceApi.md#remove_public) | **POST** /project/{projectId}/dela/transfers/{publicDSId}/cancel | 
[**remove_public1**](ProjectServiceApi.md#remove_public1) | **DELETE** /project/{projectId}/delacluster/{inodeId} | 
[**remove_topic**](ProjectServiceApi.md#remove_topic) | **DELETE** /project/{projectId}/kafka/topics/{topic} | Delete a Kafka topic.
[**removedata_setdir**](ProjectServiceApi.md#removedata_setdir) | **DELETE** /project/{projectId}/dataset/{fileName} | 
[**removedata_setdir1**](ProjectServiceApi.md#removedata_setdir1) | **DELETE** /project/{projectId}/localfs/{fileName} | 
[**removefile**](ProjectServiceApi.md#removefile) | **DELETE** /project/{projectId}/dataset/file/{fileName} | 
[**retry_log**](ProjectServiceApi.md#retry_log) | **POST** /project/{projectId}/jobs/{name}/executions/{id}/log/{type} | Retry log aggregation of given execution and type
[**search**](ProjectServiceApi.md#search) | **GET** /project/{projectId}/python/environments/{version}/libraries/{search} | Search for libraries using conda or pip package managers
[**secret_dir**](ProjectServiceApi.md#secret_dir) | **GET** /project/{projectId}/airflow/secretDir | Create project secret directory in Airflow home
[**set_permissions**](ProjectServiceApi.md#set_permissions) | **PUT** /project/{projectId}/dataset/permissions | Set permissions (potentially with sticky bit) for datasets
[**settings**](ProjectServiceApi.md#settings) | **GET** /project/{projectId}/jupyter/settings | 
[**share**](ProjectServiceApi.md#share) | **POST** /project/{projectId}/delacluster | 
[**share_data_set**](ProjectServiceApi.md#share_data_set) | **POST** /project/{projectId}/dataset/shareDataSet | 
[**share_topic**](ProjectServiceApi.md#share_topic) | **PUT** /project/{projectId}/kafka/topics/{topic}/shared/{destProjectId} | Share a Kafka topic with a project.
[**show_manifest**](ProjectServiceApi.md#show_manifest) | **GET** /project/{projectId}/dela/transfers/{publicDSId}/manifest | 
[**start_download**](ProjectServiceApi.md#start_download) | **POST** /project/{projectId}/dela/downloads/{publicDSId}/manifest | 
[**start_notebook_server**](ProjectServiceApi.md#start_notebook_server) | **POST** /project/{projectId}/jupyter/start | 
[**start_or_stop**](ProjectServiceApi.md#start_or_stop) | **POST** /project/{projectId}/serving/{servingId} | Start or stop a Serving instance
[**start_tensor_board**](ProjectServiceApi.md#start_tensor_board) | **POST** /project/{projectId}/tensorboard/{elasticId} | Start a new TensorBoard for the logged in user
[**stop_livy_session**](ProjectServiceApi.md#stop_livy_session) | **DELETE** /project/{projectId}/jupyter/livy/sessions/{appId} | 
[**stop_notebook_server**](ProjectServiceApi.md#stop_notebook_server) | **GET** /project/{projectId}/jupyter/stop | 
[**stop_tensor_board**](ProjectServiceApi.md#stop_tensor_board) | **DELETE** /project/{projectId}/tensorboard | Stop the running TensorBoard for the logged in user
[**store_airflow_jwt**](ProjectServiceApi.md#store_airflow_jwt) | **POST** /project/{projectId}/airflow/jwt | Generate a JWT for Airflow usage and store it in project&#x27;s secret directory in Airflow
[**sync_with_featurestore**](ProjectServiceApi.md#sync_with_featurestore) | **POST** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/sync | Synchornize Hive Table with the feature store
[**test_method1**](ProjectServiceApi.md#test_method1) | **GET** /project/{projectId}/dataset/upload/{path} | 
[**topic_is_shared_to**](ProjectServiceApi.md#topic_is_shared_to) | **GET** /project/{projectId}/kafka/topics/{topic}/shared | Get list of projects that a topic has been shared with.
[**uninstall**](ProjectServiceApi.md#uninstall) | **DELETE** /project/{projectId}/python/environments/{version}/libraries/{library} | Uninstall a python library from the environment
[**unschedule_job**](ProjectServiceApi.md#unschedule_job) | **DELETE** /project/{projectId}/jobs/{name}/schedule | Cancel a job&#x27;s schedule.
[**unshare_data_set**](ProjectServiceApi.md#unshare_data_set) | **POST** /project/{projectId}/dataset/unshareDataSet | 
[**unshare_topic_from_project**](ProjectServiceApi.md#unshare_topic_from_project) | **DELETE** /project/{projectId}/kafka/topics/{topic}/shared/{destProjectId} | Unshare Kafka topic from a project (specified as destProjectId).
[**unshare_topic_from_projects**](ProjectServiceApi.md#unshare_topic_from_projects) | **DELETE** /project/{projectId}/kafka/topics/{topic}/shared | Unshare Kafka topic from all projects.
[**unzip**](ProjectServiceApi.md#unzip) | **GET** /project/{projectId}/dataset/unzip/{path} | 
[**update**](ProjectServiceApi.md#update) | **PUT** /project/{projectId}/python/environments/{version}/libraries/{library}/commands | Update commands for this library
[**update_featuregroup**](ProjectServiceApi.md#update_featuregroup) | **PUT** /project/{projectId}/featurestores/{featurestoreId}/featuregroups/{featuregroupId} | Update featuregroup contents
[**update_notebook_server**](ProjectServiceApi.md#update_notebook_server) | **POST** /project/{projectId}/jupyter/update | 
[**update_pia**](ProjectServiceApi.md#update_pia) | **PUT** /project/{projectId}/pia | 
[**update_project**](ProjectServiceApi.md#update_project) | **PUT** /project/{projectId} | 
[**update_role_by_email**](ProjectServiceApi.md#update_role_by_email) | **POST** /project/{projectId}/projectMembers/{email} | 
[**update_schedule**](ProjectServiceApi.md#update_schedule) | **PUT** /project/{projectId}/jobs/{name}/schedule | Create/Update job&#x27;s schedule.
[**update_schema_version**](ProjectServiceApi.md#update_schema_version) | **POST** /project/{projectId}/kafka/{topic}/schema/version/{version} | 
[**update_storage_connector_with_id**](ProjectServiceApi.md#update_storage_connector_with_id) | **PUT** /project/{projectId}/featurestores/{featurestoreId}/storageconnectors/{connectorType}/{connectorId} | Get a storage connector with a specific id and type from a featurestore
[**update_topic_acls**](ProjectServiceApi.md#update_topic_acls) | **PUT** /project/{projectId}/kafka/topics/{topic}/acls/{id} | Update ACL specified by id.
[**update_training_dataset**](ProjectServiceApi.md#update_training_dataset) | **PUT** /project/{projectId}/featurestores/{featurestoreId}/trainingdatasets/{trainingdatasetid} | Update a training datasets with a specific id from a featurestore
[**upload_method1**](ProjectServiceApi.md#upload_method1) | **POST** /project/{projectId}/dataset/upload/{path} | 
[**validate_schema_for_topics**](ProjectServiceApi.md#validate_schema_for_topics) | **POST** /project/{projectId}/kafka/schema/validate | 
[**zip**](ProjectServiceApi.md#zip) | **GET** /project/{projectId}/dataset/zip/{path} | 

# **accept_request**
> accept_request(inode_id, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
inode_id = 789 # int | 
project_id = 56 # int | 

try:
    api_instance.accept_request(inode_id, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->accept_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inode_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_acls_to_topic**
> add_acls_to_topic(topic, project_id, body=body)

Add a new ACL for a specified topic.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
topic = 'topic_example' # str | 
project_id = 56 # int | 
body = swagger_client.AclDTO() # AclDTO |  (optional)

try:
    # Add a new ACL for a specified topic.
    api_instance.add_acls_to_topic(topic, project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->add_acls_to_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**|  | 
 **project_id** | **int**|  | 
 **body** | [**AclDTO**](AclDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_members**
> add_members(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.MembersDTO() # MembersDTO |  (optional)

try:
    api_instance.add_members(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->add_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**MembersDTO**](MembersDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_topic_schema**
> add_topic_schema(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.SchemaDTO() # SchemaDTO |  (optional)

try:
    api_instance.add_topic_schema(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->add_topic_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**SchemaDTO**](SchemaDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_validation_rules**
> DataValidationSettingsDTO add_validation_rules(featuregroup_id, feature_store_id, project_id, body=body)

Write Deequ validation rules to Filesystem so validation job can pick it up

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featuregroup_id = 56 # int | 
feature_store_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.ConstraintGroupDTO() # ConstraintGroupDTO |  (optional)

try:
    # Write Deequ validation rules to Filesystem so validation job can pick it up
    api_response = api_instance.add_validation_rules(featuregroup_id, feature_store_id, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->add_validation_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**|  | 
 **feature_store_id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**ConstraintGroupDTO**](ConstraintGroupDTO.md)|  | [optional] 

### Return type

[**DataValidationSettingsDTO**](DataValidationSettingsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_template**
> attach_template(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.FileTemplateDTO() # FileTemplateDTO |  (optional)

try:
    api_instance.attach_template(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->attach_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**FileTemplateDTO**](FileTemplateDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_file_exist**
> check_file_exist(path, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
path = 'path_example' # str | 
project_id = 56 # int | 

try:
    api_instance.check_file_exist(path, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->check_file_exist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_file_exists**
> check_file_exists(path, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
path = 'path_example' # str | 
project_id = 56 # int | 

try:
    api_instance.check_file_exists(path, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->check_file_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_file_for_download**
> check_file_for_download(path, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
path = 'path_example' # str | 
project_id = 56 # int | 

try:
    api_instance.check_file_for_download(path, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->check_file_for_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_project_access**
> check_project_access(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    api_instance.check_project_access(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->check_project_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compose_dag**
> compose_dag(project_id, body=body)

Generate an Airflow Python DAG file from a DAG definition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.AirflowDagDTO() # AirflowDagDTO |  (optional)

try:
    # Generate an Airflow Python DAG file from a DAG definition
    api_instance.compose_dag(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->compose_dag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**AirflowDagDTO**](AirflowDagDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_i_python_notebook**
> convert_i_python_notebook(path, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
path = 'path_example' # str | 
project_id = 56 # int | 

try:
    api_instance.convert_i_python_notebook(path, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->convert_i_python_notebook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_file**
> copy_file(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.MoveDTO() # MoveDTO |  (optional)

try:
    api_instance.copy_file(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->copy_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**MoveDTO**](MoveDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_file_blocks**
> count_file_blocks(path, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
path = 'path_example' # str | 
project_id = 56 # int | 

try:
    api_instance.count_file_blocks(path, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->count_file_blocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_data_set_dir**
> create_data_set_dir(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.DataSetDTO() # DataSetDTO |  (optional)

try:
    api_instance.create_data_set_dir(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->create_data_set_dir: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**DataSetDTO**](DataSetDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_data_set_dir1**
> create_data_set_dir1(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = 'body_example' # str |  (optional)

try:
    api_instance.create_data_set_dir1(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->create_data_set_dir1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_featuregroup**
> FeaturegroupDTO create_featuregroup(featurestore_id, project_id, body=body)

Create feature group in a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.FeaturegroupDTO() # FeaturegroupDTO |  (optional)

try:
    # Create feature group in a featurestore
    api_response = api_instance.create_featuregroup(featurestore_id, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->create_featuregroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**FeaturegroupDTO**](FeaturegroupDTO.md)|  | [optional] 

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_storage_connector_with_type**
> FeaturestoreStorageConnectorDTO create_new_storage_connector_with_type(connector_type, featurestore_id, project_id, body=body)

Create a new storage connector for the feature store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
connector_type = 'connector_type_example' # str | storage connector type
featurestore_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.FeaturestoreStorageConnectorDTO() # FeaturestoreStorageConnectorDTO |  (optional)

try:
    # Create a new storage connector for the feature store
    api_response = api_instance.create_new_storage_connector_with_type(connector_type, featurestore_id, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->create_new_storage_connector_with_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_type** | **str**| storage connector type | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)|  | [optional] 

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update**
> create_or_update(body, project_id)

Create or update a serving instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
body = swagger_client.RepresentsAServingModel() # RepresentsAServingModel | serving specification
project_id = 56 # int | 

try:
    # Create or update a serving instance
    api_instance.create_or_update(body, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->create_or_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RepresentsAServingModel**](RepresentsAServingModel.md)| serving specification | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_import_job**
> JobDTO create_or_update_import_job(body, project_id)

Configure job to import featuregroup

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
body = swagger_client.FeaturegroupImportJobDTO() # FeaturegroupImportJobDTO | Job configuration
project_id = 56 # int | 

try:
    # Configure job to import featuregroup
    api_response = api_instance.create_or_update_import_job(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->create_or_update_import_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeaturegroupImportJobDTO**](FeaturegroupImportJobDTO.md)| Job configuration | 
 **project_id** | **int**|  | 

### Return type

[**JobDTO**](JobDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_training_dataset_job**
> JobDTO create_or_update_training_dataset_job(body, project_id)

Configure job to create training dataset

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
body = swagger_client.TrainingDatasetJobDTO() # TrainingDatasetJobDTO | Job configuration
project_id = 56 # int | 

try:
    # Configure job to create training dataset
    api_response = api_instance.create_or_update_training_dataset_job(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->create_or_update_training_dataset_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrainingDatasetJobDTO**](TrainingDatasetJobDTO.md)| Job configuration | 
 **project_id** | **int**|  | 

### Return type

[**JobDTO**](JobDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> create_project(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
body = swagger_client.ProjectDTO() # ProjectDTO |  (optional)

try:
    api_instance.create_project(body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectDTO**](ProjectDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_top_level_data_set**
> create_top_level_data_set(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.DataSetDTO() # DataSetDTO |  (optional)

try:
    api_instance.create_top_level_data_set(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->create_top_level_data_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**DataSetDTO**](DataSetDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_topic**
> create_topic(project_id, body=body)

Create a new Kafka topic.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.TopicDTO() # TopicDTO |  (optional)

try:
    # Create a new Kafka topic.
    api_instance.create_topic(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->create_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**TopicDTO**](TopicDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_training_dataset**
> TrainingDatasetDTO create_training_dataset(featurestore_id, project_id, body=body)

Create training dataset for a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.TrainingDatasetDTO() # TrainingDatasetDTO |  (optional)

try:
    # Create training dataset for a featurestore
    api_response = api_instance.create_training_dataset(featurestore_id, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->create_training_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**TrainingDatasetDTO**](TrainingDatasetDTO.md)|  | [optional] 

### Return type

[**TrainingDatasetDTO**](TrainingDatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials**
> credentials(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    api_instance.credentials(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(version, project_id)

Delete commands for this environment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Delete commands for this environment
    api_instance.delete(version, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete1**
> delete1(library, version, project_id)

Delete commands for this library

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
library = 'library_example' # str | 
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Delete commands for this library
    api_instance.delete1(library, version, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **str**|  | 
 **version** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete2**
> EnvironmentDTO delete2(version, project_id)

Remove the python environment with the specified version for this project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Remove the python environment with the specified version for this project
    api_response = api_instance.delete2(version, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->delete2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete3**
> delete3(name, project_id)

Delete the job with the given ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
name = 'name_example' # str | id
project_id = 56 # int | 

try:
    # Delete the job with the given ID
    api_instance.delete3(name, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->delete3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| id | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feature_group_from_feature_store**
> FeaturegroupDTO delete_feature_group_from_feature_store(featuregroup_id, featurestore_id, project_id)

Delete specific featuregroup from a specific featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featuregroup_id = 56 # int | Id of the featuregroup
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Delete specific featuregroup from a specific featurestore
    api_response = api_instance.delete_feature_group_from_feature_store(featuregroup_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->delete_feature_group_from_feature_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**| Id of the featuregroup | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_featuregroup_contents**
> FeaturegroupDTO delete_featuregroup_contents(featuregroup_id, featurestore_id, project_id)

Delete featuregroup contents

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featuregroup_id = 56 # int | Id of the featuregroup
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Delete featuregroup contents
    api_response = api_instance.delete_featuregroup_contents(featuregroup_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->delete_featuregroup_contents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**| Id of the featuregroup | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_schema**
> delete_schema(schema_name, version, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
schema_name = 'schema_name_example' # str | 
version = 56 # int | 
project_id = 56 # int | 

try:
    api_instance.delete_schema(schema_name, version, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->delete_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_name** | **str**|  | 
 **version** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_serving**
> delete_serving(serving_id, project_id)

Delete a serving instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
serving_id = 56 # int | Id of the serving instance
project_id = 56 # int | 

try:
    # Delete a serving instance
    api_instance.delete_serving(serving_id, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->delete_serving: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serving_id** | **int**| Id of the serving instance | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storage_connector_with_type_and_id**
> FeaturestoreStorageConnectorDTO delete_storage_connector_with_type_and_id(connector_type, connector_id, featurestore_id, project_id)

Delete storage connector with a specific id and type from a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
connector_type = 'connector_type_example' # str | storage connector type
connector_id = 56 # int | Id of the storage connector
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Delete storage connector with a specific id and type from a featurestore
    api_response = api_instance.delete_storage_connector_with_type_and_id(connector_type, connector_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->delete_storage_connector_with_type_and_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_type** | **str**| storage connector type | 
 **connector_id** | **int**| Id of the storage connector | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_training_dataset**
> TrainingDatasetDTO delete_training_dataset(trainingdatasetid, featurestore_id, project_id)

Delete a training datasets with a specific id from a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
trainingdatasetid = 56 # int | Id of the training dataset
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Delete a training datasets with a specific id from a featurestore
    api_response = api_instance.delete_training_dataset(trainingdatasetid, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->delete_training_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trainingdatasetid** | **int**| Id of the training dataset | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**TrainingDatasetDTO**](TrainingDatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_certs**
> download_certs(project_id, password=password)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
password = 'password_example' # str |  (optional)

try:
    api_instance.download_certs(project_id, password=password)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->download_certs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **password** | [**str**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_dataset_hdfs**
> download_dataset_hdfs(public_ds_id, project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
public_ds_id = 'public_ds_id_example' # str | 
project_id = 56 # int | 
body = swagger_client.Download() # Download |  (optional)

try:
    api_instance.download_dataset_hdfs(public_ds_id, project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->download_dataset_hdfs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_ds_id** | **str**|  | 
 **project_id** | **int**|  | 
 **body** | [**Download**](Download.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_dataset_kafka**
> download_dataset_kafka(public_ds_id, project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
public_ds_id = 'public_ds_id_example' # str | 
project_id = 56 # int | 
body = swagger_client.Download() # Download |  (optional)

try:
    api_instance.download_dataset_kafka(public_ds_id, project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->download_dataset_kafka: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_ds_id** | **str**|  | 
 **project_id** | **int**|  | 
 **body** | [**Download**](Download.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_from_hdfs**
> download_from_hdfs(path, project_id, token=token)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
path = 'path_example' # str | 
project_id = 56 # int | 
token = 'token_example' # str |  (optional)

try:
    api_instance.download_from_hdfs(path, project_id, token=token)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->download_from_hdfs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **project_id** | **int**|  | 
 **token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **example**
> example(type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
type = 'type_example' # str | 

try:
    api_instance.example(type)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->example: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execution**
> execution(action, name, project_id)

Start/Stop a job

Starts a job by creating and starting an Execution, stops a job by stopping the Execution.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
action = 'action_example' # str | start or stop
name = 'name_example' # str | 
project_id = 56 # int | 

try:
    # Start/Stop a job
    api_instance.execution(action, name, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| start or stop | 
 **name** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_preview**
> file_preview(path, project_id, mode=mode)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
path = 'path_example' # str | 
project_id = 56 # int | 
mode = 'mode_example' # str |  (optional)

try:
    api_instance.file_preview(path, project_id, mode=mode)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->file_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **project_id** | **int**|  | 
 **mode** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_by_id**
> ActivitiesDTO find_all_by_id(activity_id, project_id, expand=expand)

Finds an activity in project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
activity_id = 56 # int | 
project_id = 56 # int | 
expand = ['expand_example'] # list[str] | ex. expand=creator (optional)

try:
    # Finds an activity in project.
    api_response = api_instance.find_all_by_id(activity_id, project_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->find_all_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**|  | 
 **project_id** | **int**|  | 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;creator | [optional] 

### Return type

[**ActivitiesDTO**](ActivitiesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_by_project**
> ActivitiesDTO find_all_by_project(project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by, expand=expand)

Finds activities in project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
sort_by = 'sort_by_example' # str | ex. sort_by=ID:asc,date_created:desc (optional)
filter_by = ['filter_by_example'] # list[str] | ex. filter_by=flag:dataset (optional)
expand = ['expand_example'] # list[str] | ex. expand=creator (optional)

try:
    # Finds activities in project.
    api_response = api_instance.find_all_by_project(project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->find_all_by_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort_by** | **str**| ex. sort_by&#x3D;ID:asc,date_created:desc | [optional] 
 **filter_by** | [**list[str]**](str.md)| ex. filter_by&#x3D;flag:dataset | [optional] 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;creator | [optional] 

### Return type

[**ActivitiesDTO**](ActivitiesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_by_user**
> find_all_by_user()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()

try:
    api_instance.find_all_by_user()
except ApiException as e:
    print("Exception when calling ProjectServiceApi->find_all_by_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_project_id**
> find_by_project_id(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    api_instance.find_by_project_id(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->find_by_project_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_data_sets_in_project_id**
> find_data_sets_in_project_id(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    api_instance.find_data_sets_in_project_id(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->find_data_sets_in_project_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_members_by_project_id**
> find_members_by_project_id(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    api_instance.find_members_by_project_id(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->find_members_by_project_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> get(version, project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by)

Get commands for this environment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
version = 'version_example' # str | 
project_id = 56 # int | 
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
sort_by = 'sort_by_example' # str | ex. sort_by=ID:asc,date_created:desc (optional)
filter_by = ['filter_by_example'] # list[str] | ex. filter_by=op:create (optional)

try:
    # Get commands for this environment
    api_instance.get(version, project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **project_id** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort_by** | **str**| ex. sort_by&#x3D;ID:asc,date_created:desc | [optional] 
 **filter_by** | [**list[str]**](str.md)| ex. filter_by&#x3D;op:create | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get1**
> CommandDTO get1(library, version, project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by)

Get all commands for this library

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
library = 'library_example' # str | 
version = 'version_example' # str | 
project_id = 56 # int | 
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
sort_by = 'sort_by_example' # str | ex. sort_by=ID:asc,date_created:desc (optional)
filter_by = ['filter_by_example'] # list[str] | ex. filter_by=op:create (optional)

try:
    # Get all commands for this library
    api_response = api_instance.get1(library, version, project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **str**|  | 
 **version** | **str**|  | 
 **project_id** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort_by** | **str**| ex. sort_by&#x3D;ID:asc,date_created:desc | [optional] 
 **filter_by** | [**list[str]**](str.md)| ex. filter_by&#x3D;op:create | [optional] 

### Return type

[**CommandDTO**](CommandDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get2**
> LibraryDTO get2(version, project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by, expand=expand)

Get the python libraries installed in this environment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
version = 'version_example' # str | 
project_id = 56 # int | 
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
sort_by = 'sort_by_example' # str | ex. sort_by=ID:asc,dependency:desc (optional)
filter_by = ['filter_by_example'] # list[str] | ex. filter_by=preinstalled:1 (optional)
expand = ['expand_example'] # list[str] | ex. expand=commands (optional)

try:
    # Get the python libraries installed in this environment
    api_response = api_instance.get2(version, project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **project_id** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort_by** | **str**| ex. sort_by&#x3D;ID:asc,dependency:desc | [optional] 
 **filter_by** | [**list[str]**](str.md)| ex. filter_by&#x3D;preinstalled:1 | [optional] 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;commands | [optional] 

### Return type

[**LibraryDTO**](LibraryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get3**
> EnvironmentDTO get3(version, project_id, expand=expand)

Get the python environment for specific python version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
version = 'version_example' # str | 
project_id = 56 # int | 
expand = ['expand_example'] # list[str] | ex. expand=commands (optional)

try:
    # Get the python environment for specific python version
    api_response = api_instance.get3(version, project_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **project_id** | **int**|  | 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;commands | [optional] 

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> EnvironmentDTO get_all(project_id, expand=expand)

Get all python environments for this project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
expand = ['expand_example'] # list[str] | ex. expand=commands (optional)

try:
    # Get all python environments for this project
    api_response = api_instance.get_all(project_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;commands | [optional] 

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all1**
> JobDTO get_all1(project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by, expand=expand)

Get a list of all jobs for this project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
sort_by = 'sort_by_example' # str | ex. sort_by=date_created:desc,name:asc (optional)
filter_by = ['filter_by_example'] # list[str] | ex. filter_by=jobtype:spark&filter_by=date_created_gt:2018-12-25T17:12:10 (optional)
expand = ['expand_example'] # list[str] | ex. expand=creator (optional)

try:
    # Get a list of all jobs for this project
    api_response = api_instance.get_all1(project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_all1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort_by** | **str**| ex. sort_by&#x3D;date_created:desc,name:asc | [optional] 
 **filter_by** | [**list[str]**](str.md)| ex. filter_by&#x3D;jobtype:spark&amp;filter_by&#x3D;date_created_gt:2018-12-25T17:12:10 | [optional] 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;creator | [optional] 

### Return type

[**JobDTO**](JobDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_notebook_servers_in_project**
> get_all_notebook_servers_in_project(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    api_instance.get_all_notebook_servers_in_project(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_all_notebook_servers_in_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_projects**
> get_all_projects()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()

try:
    api_instance.get_all_projects()
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_all_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_info**
> get_app_info(app_id, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
app_id = 'app_id_example' # str | 
project_id = 56 # int | 

try:
    api_instance.get_app_info(app_id, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_app_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_name**
> CommandDTO get_by_name(command_id, version, project_id)

Get commands by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
command_id = 56 # int | 
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Get commands by id
    api_response = api_instance.get_by_name(command_id, version, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **int**|  | 
 **version** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

[**CommandDTO**](CommandDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_name1**
> CommandDTO get_by_name1(library, command_id, version, project_id)

Get command by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
library = 'library_example' # str | 
command_id = 56 # int | 
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Get command by id
    api_response = api_instance.get_by_name1(library, command_id, version, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_by_name1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **str**|  | 
 **command_id** | **int**|  | 
 **version** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

[**CommandDTO**](CommandDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_name2**
> LibraryDTO get_by_name2(library, version, project_id, expand=expand)

Get the a python library installed in this environment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
library = 'library_example' # str | 
version = 'version_example' # str | 
project_id = 56 # int | 
expand = ['expand_example'] # list[str] | ex. expand=commands (optional)

try:
    # Get the a python library installed in this environment
    api_response = api_instance.get_by_name2(library, version, project_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_by_name2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **str**|  | 
 **version** | **str**|  | 
 **project_id** | **int**|  | 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;commands | [optional] 

### Return type

[**LibraryDTO**](LibraryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_multiplicator**
> get_current_multiplicator(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    api_instance.get_current_multiplicator(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_current_multiplicator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_info**
> get_dataset_info(inode_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
inode_id = 789 # int | 

try:
    api_instance.get_dataset_info(inode_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_dataset_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inode_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_info1**
> get_dataset_info1(project_id, inode_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
inode_id = 789 # int | 

try:
    api_instance.get_dataset_info1(project_id, inode_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_dataset_info1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **inode_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dir_content**
> get_dir_content(path, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
path = 'path_example' # str | 
project_id = 56 # int | 

try:
    api_instance.get_dir_content(path, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_dir_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution**
> ExecutionDTO get_execution(id, name, project_id, sort_by=sort_by, filter_by=filter_by, expand=expand)

Find Execution by Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
id = 56 # int | execution id
name = 'name_example' # str | 
project_id = 56 # int | 
sort_by = 'sort_by_example' # str | ex. sort_by=submissiontime:desc,id:asc (optional)
filter_by = ['filter_by_example'] # list[str] | state and finalstatus accept also neq (not equals) ex. filter_by=state:running&filter_by=state_neq:new&filter_by=submissiontime:2018-12-25T17:12:10.058 (optional)
expand = ['expand_example'] # list[str] | ex. expand=creator (optional)

try:
    # Find Execution by Id
    api_response = api_instance.get_execution(id, name, project_id, sort_by=sort_by, filter_by=filter_by, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| execution id | 
 **name** | **str**|  | 
 **project_id** | **int**|  | 
 **sort_by** | **str**| ex. sort_by&#x3D;submissiontime:desc,id:asc | [optional] 
 **filter_by** | [**list[str]**](str.md)| state and finalstatus accept also neq (not equals) ex. filter_by&#x3D;state:running&amp;filter_by&#x3D;state_neq:new&amp;filter_by&#x3D;submissiontime:2018-12-25T17:12:10.058 | [optional] 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;creator | [optional] 

### Return type

[**ExecutionDTO**](ExecutionDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_executions**
> ExecutionDTO get_executions(name, project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by, expand=expand)

Get a list of executions for the job.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
name = 'name_example' # str | 
project_id = 56 # int | 
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
sort_by = 'sort_by_example' # str | ex. sort_by=submissiontime:desc,id:asc (optional)
filter_by = ['filter_by_example'] # list[str] | state and finalstatus accept also neq (not equals) ex. filter_by=state:running&filter_by=state_neq:new&filter_by=submissiontime:2018-12-25T17:12:10.058 (optional)
expand = ['expand_example'] # list[str] | ex. expand=creator (optional)

try:
    # Get a list of executions for the job.
    api_response = api_instance.get_executions(name, project_id, offset=offset, limit=limit, sort_by=sort_by, filter_by=filter_by, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **project_id** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort_by** | **str**| ex. sort_by&#x3D;submissiontime:desc,id:asc | [optional] 
 **filter_by** | [**list[str]**](str.md)| state and finalstatus accept also neq (not equals) ex. filter_by&#x3D;state:running&amp;filter_by&#x3D;state_neq:new&amp;filter_by&#x3D;submissiontime:2018-12-25T17:12:10.058 | [optional] 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;creator | [optional] 

### Return type

[**ExecutionDTO**](ExecutionDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extended_details**
> get_extended_details(public_ds_id, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
public_ds_id = 'public_ds_id_example' # str | 
project_id = 56 # int | 

try:
    api_instance.get_extended_details(public_ds_id, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_extended_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_ds_id** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_group_from_feature_store**
> FeaturegroupDTO get_feature_group_from_feature_store(featuregroup_id, featurestore_id, project_id)

Get specific featuregroup from a specific featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featuregroup_id = 56 # int | Id of the featuregroup
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get specific featuregroup from a specific featurestore
    api_response = api_instance.get_feature_group_from_feature_store(featuregroup_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_feature_group_from_feature_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**| Id of the featuregroup | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_group_preview**
> list[FeaturegroupPreview] get_feature_group_preview(featuregroup_id, featurestore_id, project_id)

Preview feature data of a featuregroup

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featuregroup_id = 56 # int | Id of the featuregroup
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Preview feature data of a featuregroup
    api_response = api_instance.get_feature_group_preview(featuregroup_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_feature_group_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**| Id of the featuregroup | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**list[FeaturegroupPreview]**](FeaturegroupPreview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_group_schema**
> RowValueQueryResult get_feature_group_schema(featuregroup_id, featurestore_id, project_id)

Get the SQL schema of a featuregroup

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featuregroup_id = 56 # int | Id of the featuregroup
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get the SQL schema of a featuregroup
    api_response = api_instance.get_feature_group_schema(featuregroup_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_feature_group_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**| Id of the featuregroup | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**RowValueQueryResult**](RowValueQueryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_featuregroups_for_featurestore**
> list[FeaturegroupDTO] get_featuregroups_for_featurestore(featurestore_id, project_id)

Get the list of feature groups for a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get the list of feature groups for a featurestore
    api_response = api_instance.get_featuregroups_for_featurestore(featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_featuregroups_for_featurestore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**list[FeaturegroupDTO]**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_featurestore**
> FeaturestoreDTO get_featurestore(featurestore_id, project_id)

Get featurestore with specific Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featurestore_id = 56 # int | Id of the featurestore
project_id = 56 # int | 

try:
    # Get featurestore with specific Id
    api_response = api_instance.get_featurestore(featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_featurestore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_id** | **int**| Id of the featurestore | 
 **project_id** | **int**|  | 

### Return type

[**FeaturestoreDTO**](FeaturestoreDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_featurestore_by_name**
> FeaturestoreDTO get_featurestore_by_name(featurestore_name, project_id)

Get featurestore with specific name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featurestore_name = 'featurestore_name_example' # str | Id of the featurestore
project_id = 56 # int | 

try:
    # Get featurestore with specific name
    api_response = api_instance.get_featurestore_by_name(featurestore_name, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_featurestore_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_name** | **str**| Id of the featurestore | 
 **project_id** | **int**|  | 

### Return type

[**FeaturestoreDTO**](FeaturestoreDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_featurestore_id**
> FeaturestoreClientSettingsDTO get_featurestore_id(featurestore_name, project_id)

Get featurestore Metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featurestore_name = 'featurestore_name_example' # str | 
project_id = 56 # int | 

try:
    # Get featurestore Metadata
    api_response = api_instance.get_featurestore_id(featurestore_name, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_featurestore_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_name** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

[**FeaturestoreClientSettingsDTO**](FeaturestoreClientSettingsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_featurestore_settings**
> FeaturestoreClientSettingsDTO get_featurestore_settings(project_id)

Get featurestore settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    # Get featurestore settings
    api_response = api_instance.get_featurestore_settings(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_featurestore_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**FeaturestoreClientSettingsDTO**](FeaturestoreClientSettingsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_featurestores**
> list[FeaturestoreDTO] get_featurestores(project_id)

Get the list of feature stores for the project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    # Get the list of feature stores for the project
    api_response = api_instance.get_featurestores(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_featurestores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**list[FeaturestoreDTO]**](FeaturestoreDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> get_file(path, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
path = 'path_example' # str | 
project_id = 56 # int | 

try:
    api_instance.get_file(path, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_git_status_of_jupyter_repo**
> get_git_status_of_jupyter_repo(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    api_instance.get_git_status_of_jupyter_repo(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_git_status_of_jupyter_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> JobDTO get_job(name, project_id, sort_by=sort_by, filter_by=filter_by, expand=expand)

Get the job with requested ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
name = 'name_example' # str | 
project_id = 56 # int | 
sort_by = 'sort_by_example' # str | ex. sort_by=date_created:desc,name:asc (optional)
filter_by = ['filter_by_example'] # list[str] | ex. filter_by=jobtype:spark&filter_by=date_created_gt:2018-12-25T17:12:10 (optional)
expand = ['expand_example'] # list[str] | ex. expand=creator (optional)

try:
    # Get the job with requested ID
    api_response = api_instance.get_job(name, project_id, sort_by=sort_by, filter_by=filter_by, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **project_id** | **int**|  | 
 **sort_by** | **str**| ex. sort_by&#x3D;date_created:desc,name:asc | [optional] 
 **filter_by** | [**list[str]**](str.md)| ex. filter_by&#x3D;jobtype:spark&amp;filter_by&#x3D;date_created_gt:2018-12-25T17:12:10 | [optional] 
 **expand** | [**list[str]**](str.md)| ex. expand&#x3D;creator | [optional] 

### Return type

[**JobDTO**](JobDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_ui**
> get_job_ui(app_id, is_livy, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
app_id = 'app_id_example' # str | 
is_livy = 'is_livy_example' # str | 
project_id = 56 # int | 

try:
    api_instance.get_job_ui(app_id, is_livy, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_job_ui: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **is_livy** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log**
> JobLogDTO get_log(id, type, name, project_id)

Retrieve log of given execution and type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
id = 56 # int | 
type = 'type_example' # str | 
name = 'name_example' # str | 
project_id = 56 # int | 

try:
    # Retrieve log of given execution and type
    api_response = api_instance.get_log(id, type, name, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **type** | **str**|  | 
 **name** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

[**JobLogDTO**](JobLogDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_more_info**
> get_more_info(project_id, inode_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
inode_id = 789 # int | 

try:
    api_instance.get_more_info(project_id, inode_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_more_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **inode_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_more_info1**
> get_more_info1(inode_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
inode_id = 789 # int | 

try:
    api_instance.get_more_info1(inode_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_more_info1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inode_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_more_info2**
> get_more_info2(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    api_instance.get_more_info2(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_more_info2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_online_featurestore_storage_connector**
> FeaturestoreStorageConnectorDTO get_online_featurestore_storage_connector(featurestore_id, project_id)

Get online featurestore storage connector for this feature store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get online featurestore storage connector for this feature store
    api_response = api_instance.get_online_featurestore_storage_connector(featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_online_featurestore_storage_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pia**
> get_pia(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    api_instance.get_pia(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_pia: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_by_name**
> get_project_by_name(project_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_name = 'project_name_example' # str | 

try:
    api_instance.get_project_by_name(project_name)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_project_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_contents**
> get_project_contents(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    api_instance.get_project_contents(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_project_contents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_shared_with**
> get_project_shared_with(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.DataSetDTO() # DataSetDTO |  (optional)

try:
    api_instance.get_project_shared_with(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_project_shared_with: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**DataSetDTO**](DataSetDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_readme_by_inode_id**
> get_readme_by_inode_id(inode_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
inode_id = 789 # int | 

try:
    api_instance.get_readme_by_inode_id(inode_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_readme_by_inode_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inode_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_git_branches**
> get_remote_git_branches(project_id, remote_uri=remote_uri, key_name=key_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
remote_uri = 'remote_uri_example' # str |  (optional)
key_name = 'key_name_example' # str |  (optional)

try:
    api_instance.get_remote_git_branches(project_id, remote_uri=remote_uri, key_name=key_name)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_remote_git_branches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **remote_uri** | **str**|  | [optional] 
 **key_name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema**
> get_schema(topic, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
topic = 'topic_example' # str | 
project_id = 56 # int | 

try:
    api_instance.get_schema(topic, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_content**
> get_schema_content(schema_name, schema_version, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
schema_name = 'schema_name_example' # str | 
schema_version = 56 # int | 
project_id = 56 # int | 

try:
    api_instance.get_schema_content(schema_name, schema_version, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_schema_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_name** | **str**|  | 
 **schema_version** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_serving**
> RepresentsAServingModel get_serving(serving_id, project_id)

Get info about a serving instance for the project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
serving_id = 56 # int | Id of the Serving instance
project_id = 56 # int | 

try:
    # Get info about a serving instance for the project
    api_response = api_instance.get_serving(serving_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_serving: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serving_id** | **int**| Id of the Serving instance | 
 **project_id** | **int**|  | 

### Return type

[**RepresentsAServingModel**](RepresentsAServingModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_servings**
> list[RepresentsAServingModel] get_servings(project_id)

Get the list of serving instances for the project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    # Get the list of serving instances for the project
    api_response = api_instance.get_servings(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_servings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**list[RepresentsAServingModel]**](RepresentsAServingModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_connector_with_id**
> FeaturestoreStorageConnectorDTO get_storage_connector_with_id(connector_type, connector_id, featurestore_id, project_id)

Get a storage connector with a specific id and type from a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
connector_type = 'connector_type_example' # str | storage connector type
connector_id = 56 # int | Id of the storage connector
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get a storage connector with a specific id and type from a featurestore
    api_response = api_instance.get_storage_connector_with_id(connector_type, connector_id, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_storage_connector_with_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_type** | **str**| storage connector type | 
 **connector_id** | **int**| Id of the storage connector | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_connectors**
> list[FeaturestoreStorageConnectorDTO] get_storage_connectors(featurestore_id, project_id)

Get all storage connectors of a feature store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get all storage connectors of a feature store
    api_response = api_instance.get_storage_connectors(featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_storage_connectors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**list[FeaturestoreStorageConnectorDTO]**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_connectors_of_type**
> list[FeaturestoreStorageConnectorDTO] get_storage_connectors_of_type(connector_type, featurestore_id, project_id)

Get all storage connectors of a specific type of a feature store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
connector_type = 'connector_type_example' # str | storage connector type
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get all storage connectors of a specific type of a feature store
    api_response = api_instance.get_storage_connectors_of_type(connector_type, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_storage_connectors_of_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_type** | **str**| storage connector type | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**list[FeaturestoreStorageConnectorDTO]**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tensor_board**
> get_tensor_board(project_id)

Get the running TensorBoard of the logged in user in this project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    # Get the running TensorBoard of the logged in user in this project
    api_instance.get_tensor_board(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_tensor_board: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tensor_board_urls**
> get_tensor_board_urls(app_id, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
app_id = 'app_id_example' # str | 
project_id = 56 # int | 

try:
    api_instance.get_tensor_board_urls(app_id, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_tensor_board_urls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic**
> get_topic(topic, project_id)

Get Kafka topic details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
topic = 'topic_example' # str | 
project_id = 56 # int | 

try:
    # Get Kafka topic details.
    api_instance.get_topic(topic, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_acl**
> get_topic_acl(topic, id, project_id)

Get ACL metadata specified by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
topic = 'topic_example' # str | 
id = 56 # int | 
project_id = 56 # int | 

try:
    # Get ACL metadata specified by id.
    api_instance.get_topic_acl(topic, id, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_topic_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**|  | 
 **id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_acls**
> get_topic_acls(topic, project_id, body=body, offset=offset, limit=limit)

Get all ACLs for a specified topic.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
topic = 'topic_example' # str | 
project_id = 56 # int | 
body = swagger_client.AclsBeanParam() # AclsBeanParam |  (optional)
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # Get all ACLs for a specified topic.
    api_instance.get_topic_acls(topic, project_id, body=body, offset=offset, limit=limit)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_topic_acls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**|  | 
 **project_id** | **int**|  | 
 **body** | [**AclsBeanParam**](AclsBeanParam.md)|  | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topics**
> get_topics(project_id, body=body, offset=offset, limit=limit)

Retrieve Kafka topics metadata .

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.TopicsBeanParam() # TopicsBeanParam |  (optional)
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # Retrieve Kafka topics metadata .
    api_instance.get_topics(project_id, body=body, offset=offset, limit=limit)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_topics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**TopicsBeanParam**](TopicsBeanParam.md)|  | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_training_dataset_with_id**
> TrainingDatasetDTO get_training_dataset_with_id(trainingdatasetid, featurestore_id, project_id)

Get a training datasets with a specific id from a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
trainingdatasetid = 56 # int | Id of the training dataset
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get a training datasets with a specific id from a featurestore
    api_response = api_instance.get_training_dataset_with_id(trainingdatasetid, featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_training_dataset_with_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trainingdatasetid** | **int**| Id of the training dataset | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**TrainingDatasetDTO**](TrainingDatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_training_datasets_for_featurestore**
> list[TrainingDatasetDTO] get_training_datasets_for_featurestore(featurestore_id, project_id)

Get the list of training datasets for a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get the list of training datasets for a featurestore
    api_response = api_instance.get_training_datasets_for_featurestore(featurestore_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_training_datasets_for_featurestore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**list[TrainingDatasetDTO]**](TrainingDatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validation_result**
> ValidationResult get_validation_result(featuregroup_id, feature_store_id, project_id)

Fetch the result of a Deequ data validation job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featuregroup_id = 56 # int | 
feature_store_id = 56 # int | 
project_id = 56 # int | 

try:
    # Fetch the result of a Deequ data validation job
    api_response = api_instance.get_validation_result(featuregroup_id, feature_store_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_validation_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**|  | 
 **feature_store_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validation_rules**
> ConstraintGroupDTO get_validation_rules(featuregroup_id, feature_store_id, project_id)

Get previously stored Deequ validation rules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featuregroup_id = 56 # int | 
feature_store_id = 56 # int | 
project_id = 56 # int | 

try:
    # Get previously stored Deequ validation rules
    api_response = api_instance.get_validation_rules(featuregroup_id, feature_store_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_validation_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**|  | 
 **feature_store_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**ConstraintGroupDTO**](ConstraintGroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_yarn_ui**
> get_yarn_ui(app_id, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
app_id = 'app_id_example' # str | 
project_id = 56 # int | 

try:
    api_instance.get_yarn_ui(app_id, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->get_yarn_ui: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **infer**
> infer(model_name, version, verb, project_id, body=body)

Make inference

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
model_name = 'model_name_example' # str | Name of the model to query
version = 'version_example' # str | Version of the model to query
verb = 'verb_example' # str | Type of query
project_id = 56 # int | 
body = 'body_example' # str |  (optional)

try:
    # Make inference
    api_instance.infer(model_name, version, verb, project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->infer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**| Name of the model to query | 
 **version** | **str**| Version of the model to query | 
 **verb** | **str**| Type of query | 
 **project_id** | **int**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspect**
> SparkJobConfiguration inspect(jobtype, path, project_id)

Inspect Spark user program and return SparkJobConfiguration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
jobtype = 'jobtype_example' # str | spark job type
path = 'path_example' # str | path
project_id = 56 # int | 

try:
    # Inspect Spark user program and return SparkJobConfiguration
    api_response = api_instance.inspect(jobtype, path, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobtype** | **str**| spark job type | 
 **path** | **str**| path | 
 **project_id** | **int**|  | 

### Return type

[**SparkJobConfiguration**](SparkJobConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install**
> install(library, version2, project_id, package_manager=package_manager, version=version, channel=channel, machine=machine)

Install a python library in the environment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
library = 'library_example' # str | 
version2 = 'version_example' # str | 
project_id = 56 # int | 
package_manager = 'package_manager_example' # str |  (optional)
version = 'version_example' # str |  (optional)
channel = 'channel_example' # str |  (optional)
machine = 'machine_example' # str |  (optional)

try:
    # Install a python library in the environment
    api_instance.install(library, version2, project_id, package_manager=package_manager, version=version, channel=channel, machine=machine)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->install: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **str**|  | 
 **version2** | **str**|  | 
 **project_id** | **int**|  | 
 **package_manager** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **channel** | **str**|  | [optional] 
 **machine** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_dir**
> is_dir(path, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
path = 'path_example' # str | 
project_id = 56 # int | 

try:
    api_instance.is_dir(path, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->is_dir: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_dir1**
> is_dir1(path, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
path = 'path_example' # str | 
project_id = 56 # int | 

try:
    api_instance.is_dir1(path, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->is_dir1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_running**
> is_running(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    api_instance.is_running(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->is_running: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schemas_for_topics**
> list_schemas_for_topics(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    api_instance.list_schemas_for_topics(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->list_schemas_for_topics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **livy_sessions**
> livy_sessions(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    api_instance.livy_sessions(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->livy_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_file**
> move_file(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.MoveDTO() # MoveDTO |  (optional)

try:
    api_instance.move_file(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->move_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**MoveDTO**](MoveDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_featurestore_util**
> new_featurestore_util(project_id, body=body)

Upload json input for featurestore-util jobs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.FeaturestoreUtilJobDTO() # FeaturestoreUtilJobDTO |  (optional)

try:
    # Upload json input for featurestore-util jobs
    api_instance.new_featurestore_util(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->new_featurestore_util: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**FeaturestoreUtilJobDTO**](FeaturestoreUtilJobDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post**
> EnvironmentDTO post(version, project_id, action=action)

Create an environment from version or export an environment as yaml file

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
version = 'version_example' # str | 
project_id = 56 # int | 
action = 'action_example' # str |  (optional)

try:
    # Create an environment from version or export an environment as yaml file
    api_response = api_instance.post(version, project_id, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **project_id** | **int**|  | 
 **action** | **str**|  | [optional] 

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_yml**
> EnvironmentDTO post_yml(project_id, body=body)

Create an environment from yaml file

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.EnvironmentYmlDTO() # EnvironmentYmlDTO |  (optional)

try:
    # Create an environment from yaml file
    api_response = api_instance.post_yml(project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->post_yml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**EnvironmentYmlDTO**](EnvironmentYmlDTO.md)|  | [optional] 

### Return type

[**EnvironmentDTO**](EnvironmentDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish**
> publish(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.InodeIdDTO() # InodeIdDTO |  (optional)

try:
    api_instance.publish(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->publish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**InodeIdDTO**](InodeIdDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put**
> JobDTO put(name, project_id, body=body)

Create or Update a Job.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
name = 'name_example' # str | name
project_id = 56 # int | 
body = swagger_client.JobConfiguration() # JobConfiguration |  (optional)

try:
    # Create or Update a Job.
    api_response = api_instance.put(name, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 
 **project_id** | **int**|  | 
 **body** | [**JobConfiguration**](JobConfiguration.md)|  | [optional] 

### Return type

[**JobDTO**](JobDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotas_by_project_id**
> quotas_by_project_id(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    api_instance.quotas_by_project_id(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->quotas_by_project_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotas_by_project_id1**
> quotas_by_project_id1(project_id, project_name, inode_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
project_name = 'project_name_example' # str | 
inode_id = 789 # int | 

try:
    api_instance.quotas_by_project_id1(project_id, project_name, inode_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->quotas_by_project_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **project_name** | **str**|  | 
 **inode_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_request**
> reject_request(inode_id, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
inode_id = 789 # int | 
project_id = 56 # int | 

try:
    api_instance.reject_request(inode_id, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->reject_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inode_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_acls_from_topic**
> remove_acls_from_topic(topic, id, project_id)

Remove ACL specified by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
topic = 'topic_example' # str | 
id = 56 # int | 
project_id = 56 # int | 

try:
    # Remove ACL specified by id.
    api_instance.remove_acls_from_topic(topic, id, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->remove_acls_from_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**|  | 
 **id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_corrupted**
> remove_corrupted(file_name, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
file_name = 'file_name_example' # str | 
project_id = 56 # int | 

try:
    api_instance.remove_corrupted(file_name, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->remove_corrupted: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_members_by_id**
> remove_members_by_id(email, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
email = 'email_example' # str | 
project_id = 56 # int | 

try:
    api_instance.remove_members_by_id(email, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->remove_members_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_project_and_files**
> remove_project_and_files(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    api_instance.remove_project_and_files(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->remove_project_and_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_public**
> remove_public(public_ds_id, clean, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
public_ds_id = 'public_ds_id_example' # str | 
clean = true # bool | delete dataset
project_id = 56 # int | 

try:
    api_instance.remove_public(public_ds_id, clean, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->remove_public: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_ds_id** | **str**|  | 
 **clean** | **bool**| delete dataset | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_public1**
> remove_public1(inode_id, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
inode_id = 789 # int | 
project_id = 56 # int | 

try:
    api_instance.remove_public1(inode_id, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->remove_public1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inode_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_topic**
> remove_topic(topic, project_id)

Delete a Kafka topic.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
topic = 'topic_example' # str | 
project_id = 56 # int | 

try:
    # Delete a Kafka topic.
    api_instance.remove_topic(topic, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->remove_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **removedata_setdir**
> removedata_setdir(file_name, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
file_name = 'file_name_example' # str | 
project_id = 56 # int | 

try:
    api_instance.removedata_setdir(file_name, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->removedata_setdir: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **removedata_setdir1**
> removedata_setdir1(file_name, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
file_name = 'file_name_example' # str | 
project_id = 56 # int | 

try:
    api_instance.removedata_setdir1(file_name, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->removedata_setdir1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **removefile**
> removefile(file_name, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
file_name = 'file_name_example' # str | 
project_id = 56 # int | 

try:
    api_instance.removefile(file_name, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->removefile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_log**
> JobLogDTO retry_log(id, type, name, project_id)

Retry log aggregation of given execution and type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
id = 56 # int | 
type = 'type_example' # str | 
name = 'name_example' # str | 
project_id = 56 # int | 

try:
    # Retry log aggregation of given execution and type
    api_response = api_instance.retry_log(id, type, name, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->retry_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **type** | **str**|  | 
 **name** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

[**JobLogDTO**](JobLogDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> LibrarySearchDTO search(search, version, project_id, query=query, channel=channel)

Search for libraries using conda or pip package managers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
search = 'search_example' # str | 
version = 'version_example' # str | 
project_id = 56 # int | 
query = 'query_example' # str |  (optional)
channel = 'channel_example' # str |  (optional)

try:
    # Search for libraries using conda or pip package managers
    api_response = api_instance.search(search, version, project_id, query=query, channel=channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | 
 **version** | **str**|  | 
 **project_id** | **int**|  | 
 **query** | **str**|  | [optional] 
 **channel** | **str**|  | [optional] 

### Return type

[**LibrarySearchDTO**](LibrarySearchDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_dir**
> secret_dir(project_id)

Create project secret directory in Airflow home

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    # Create project secret directory in Airflow home
    api_instance.secret_dir(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->secret_dir: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_permissions**
> set_permissions(project_id, body=body)

Set permissions (potentially with sticky bit) for datasets

Allow data scientists to create and modify own files in dataset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.DataSetDTO() # DataSetDTO |  (optional)

try:
    # Set permissions (potentially with sticky bit) for datasets
    api_instance.set_permissions(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->set_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**DataSetDTO**](DataSetDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings**
> settings(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    api_instance.settings(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share**
> share(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.InodeIdDTO() # InodeIdDTO |  (optional)

try:
    api_instance.share(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**InodeIdDTO**](InodeIdDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_data_set**
> share_data_set(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.DataSetDTO() # DataSetDTO |  (optional)

try:
    api_instance.share_data_set(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->share_data_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**DataSetDTO**](DataSetDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_topic**
> share_topic(topic, dest_project_id, project_id)

Share a Kafka topic with a project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
topic = 'topic_example' # str | 
dest_project_id = 56 # int | 
project_id = 56 # int | 

try:
    # Share a Kafka topic with a project.
    api_instance.share_topic(topic, dest_project_id, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->share_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**|  | 
 **dest_project_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_manifest**
> show_manifest(public_ds_id, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
public_ds_id = 'public_ds_id_example' # str | 
project_id = 56 # int | 

try:
    api_instance.show_manifest(public_ds_id, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->show_manifest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_ds_id** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_download**
> start_download(public_ds_id, project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
public_ds_id = 'public_ds_id_example' # str | 
project_id = 56 # int | 
body = swagger_client.Download() # Download |  (optional)

try:
    api_instance.start_download(public_ds_id, project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->start_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_ds_id** | **str**|  | 
 **project_id** | **int**|  | 
 **body** | [**Download**](Download.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_notebook_server**
> start_notebook_server(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.JupyterSettings() # JupyterSettings |  (optional)

try:
    api_instance.start_notebook_server(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->start_notebook_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**JupyterSettings**](JupyterSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_or_stop**
> start_or_stop(serving_id, action, project_id)

Start or stop a Serving instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
serving_id = 56 # int | ID of the Serving instance to start/stop
action = 'action_example' # str | Action
project_id = 56 # int | 

try:
    # Start or stop a Serving instance
    api_instance.start_or_stop(serving_id, action, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->start_or_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serving_id** | **int**| ID of the Serving instance to start/stop | 
 **action** | **str**| Action | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_tensor_board**
> start_tensor_board(elastic_id, project_id)

Start a new TensorBoard for the logged in user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
elastic_id = 'elastic_id_example' # str | 
project_id = 56 # int | 

try:
    # Start a new TensorBoard for the logged in user
    api_instance.start_tensor_board(elastic_id, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->start_tensor_board: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **elastic_id** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_livy_session**
> stop_livy_session(app_id, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
app_id = 'app_id_example' # str | 
project_id = 56 # int | 

try:
    api_instance.stop_livy_session(app_id, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->stop_livy_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_notebook_server**
> stop_notebook_server(project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    api_instance.stop_notebook_server(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->stop_notebook_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_tensor_board**
> stop_tensor_board(project_id)

Stop the running TensorBoard for the logged in user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    # Stop the running TensorBoard for the logged in user
    api_instance.stop_tensor_board(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->stop_tensor_board: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_airflow_jwt**
> store_airflow_jwt(project_id)

Generate a JWT for Airflow usage and store it in project's secret directory in Airflow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 

try:
    # Generate a JWT for Airflow usage and store it in project's secret directory in Airflow
    api_instance.store_airflow_jwt(project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->store_airflow_jwt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_with_featurestore**
> FeaturegroupDTO sync_with_featurestore(featurestore_id, project_id, body=body)

Synchornize Hive Table with the feature store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featurestore_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.FeaturegroupDTO() # FeaturegroupDTO |  (optional)

try:
    # Synchornize Hive Table with the feature store
    api_response = api_instance.sync_with_featurestore(featurestore_id, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->sync_with_featurestore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**FeaturegroupDTO**](FeaturegroupDTO.md)|  | [optional] 

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_method1**
> test_method1(path, project_id, template_id=template_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
path = 'path_example' # str | 
project_id = 56 # int | 
template_id = 56 # int |  (optional)

try:
    api_instance.test_method1(path, project_id, template_id=template_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->test_method1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **project_id** | **int**|  | 
 **template_id** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topic_is_shared_to**
> topic_is_shared_to(topic, project_id)

Get list of projects that a topic has been shared with.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
topic = 'topic_example' # str | 
project_id = 56 # int | 

try:
    # Get list of projects that a topic has been shared with.
    api_instance.topic_is_shared_to(topic, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->topic_is_shared_to: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uninstall**
> uninstall(library, version, project_id)

Uninstall a python library from the environment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
library = 'library_example' # str | 
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Uninstall a python library from the environment
    api_instance.uninstall(library, version, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->uninstall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **str**|  | 
 **version** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unschedule_job**
> unschedule_job(name, project_id)

Cancel a job's schedule.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
name = 'name_example' # str | 
project_id = 56 # int | 

try:
    # Cancel a job's schedule.
    api_instance.unschedule_job(name, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->unschedule_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unshare_data_set**
> unshare_data_set(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.DataSetDTO() # DataSetDTO |  (optional)

try:
    api_instance.unshare_data_set(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->unshare_data_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**DataSetDTO**](DataSetDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unshare_topic_from_project**
> unshare_topic_from_project(topic, dest_project_id, project_id)

Unshare Kafka topic from a project (specified as destProjectId).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
topic = 'topic_example' # str | 
dest_project_id = 56 # int | 
project_id = 56 # int | 

try:
    # Unshare Kafka topic from a project (specified as destProjectId).
    api_instance.unshare_topic_from_project(topic, dest_project_id, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->unshare_topic_from_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**|  | 
 **dest_project_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unshare_topic_from_projects**
> unshare_topic_from_projects(topic, project_id)

Unshare Kafka topic from all projects.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
topic = 'topic_example' # str | 
project_id = 56 # int | 

try:
    # Unshare Kafka topic from all projects.
    api_instance.unshare_topic_from_projects(topic, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->unshare_topic_from_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unzip**
> unzip(path, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
path = 'path_example' # str | 
project_id = 56 # int | 

try:
    api_instance.unzip(path, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->unzip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> update(library, version, project_id)

Update commands for this library

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
library = 'library_example' # str | 
version = 'version_example' # str | 
project_id = 56 # int | 

try:
    # Update commands for this library
    api_instance.update(library, version, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library** | **str**|  | 
 **version** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_featuregroup**
> FeaturegroupDTO update_featuregroup(featuregroup_id, featurestore_id, project_id, body=body, update_metadata=update_metadata, update_stats=update_stats, enable_online=enable_online, disable_online=disable_online, update_stats_settings=update_stats_settings)

Update featuregroup contents

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
featuregroup_id = 56 # int | Id of the featuregroup
featurestore_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.FeaturegroupDTO() # FeaturegroupDTO |  (optional)
update_metadata = true # bool | updateMetadata (optional)
update_stats = true # bool | updateStats (optional)
enable_online = true # bool | enableOnline (optional)
disable_online = true # bool | disableOnline (optional)
update_stats_settings = true # bool | updateStatsSettings (optional)

try:
    # Update featuregroup contents
    api_response = api_instance.update_featuregroup(featuregroup_id, featurestore_id, project_id, body=body, update_metadata=update_metadata, update_stats=update_stats, enable_online=enable_online, disable_online=disable_online, update_stats_settings=update_stats_settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->update_featuregroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featuregroup_id** | **int**| Id of the featuregroup | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**FeaturegroupDTO**](FeaturegroupDTO.md)|  | [optional] 
 **update_metadata** | **bool**| updateMetadata | [optional] 
 **update_stats** | **bool**| updateStats | [optional] 
 **enable_online** | **bool**| enableOnline | [optional] 
 **disable_online** | **bool**| disableOnline | [optional] 
 **update_stats_settings** | **bool**| updateStatsSettings | [optional] 

### Return type

[**FeaturegroupDTO**](FeaturegroupDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notebook_server**
> update_notebook_server(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.JupyterSettings() # JupyterSettings |  (optional)

try:
    api_instance.update_notebook_server(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->update_notebook_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**JupyterSettings**](JupyterSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pia**
> update_pia(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.Pia() # Pia |  (optional)

try:
    api_instance.update_pia(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->update_pia: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**Pia**](Pia.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> update_project(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.ProjectDTO() # ProjectDTO |  (optional)

try:
    api_instance.update_project(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**ProjectDTO**](ProjectDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role_by_email**
> update_role_by_email(email, project_id, role=role)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
email = 'email_example' # str | 
project_id = 56 # int | 
role = 'role_example' # str |  (optional)

try:
    api_instance.update_role_by_email(email, project_id, role=role)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->update_role_by_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **project_id** | **int**|  | 
 **role** | [**str**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_schedule**
> update_schedule(name, project_id, body=body)

Create/Update job's schedule.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
name = 'name_example' # str | 
project_id = 56 # int | 
body = swagger_client.ScheduleDTO() # ScheduleDTO |  (optional)

try:
    # Create/Update job's schedule.
    api_instance.update_schedule(name, project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->update_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **project_id** | **int**|  | 
 **body** | [**ScheduleDTO**](ScheduleDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_schema_version**
> update_schema_version(topic, version, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
topic = 'topic_example' # str | 
version = 56 # int | 
project_id = 56 # int | 

try:
    api_instance.update_schema_version(topic, version, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->update_schema_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**|  | 
 **version** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storage_connector_with_id**
> FeaturestoreStorageConnectorDTO update_storage_connector_with_id(connector_type, connector_id, featurestore_id, project_id, body=body)

Get a storage connector with a specific id and type from a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
connector_type = 'connector_type_example' # str | storage connector type
connector_id = 56 # int | Id of the storage connector
featurestore_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.FeaturestoreStorageConnectorDTO() # FeaturestoreStorageConnectorDTO |  (optional)

try:
    # Get a storage connector with a specific id and type from a featurestore
    api_response = api_instance.update_storage_connector_with_id(connector_type, connector_id, featurestore_id, project_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->update_storage_connector_with_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_type** | **str**| storage connector type | 
 **connector_id** | **int**| Id of the storage connector | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)|  | [optional] 

### Return type

[**FeaturestoreStorageConnectorDTO**](FeaturestoreStorageConnectorDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_topic_acls**
> update_topic_acls(topic, id, project_id, body=body)

Update ACL specified by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
topic = 'topic_example' # str | 
id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.AclDTO() # AclDTO |  (optional)

try:
    # Update ACL specified by id.
    api_instance.update_topic_acls(topic, id, project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->update_topic_acls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**|  | 
 **id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**AclDTO**](AclDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_training_dataset**
> TrainingDatasetDTO update_training_dataset(trainingdatasetid, featurestore_id, project_id, body=body, update_metadata=update_metadata, update_stats=update_stats)

Update a training datasets with a specific id from a featurestore

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
trainingdatasetid = 56 # int | Id of the training dataset
featurestore_id = 56 # int | 
project_id = 56 # int | 
body = swagger_client.TrainingDatasetDTO() # TrainingDatasetDTO |  (optional)
update_metadata = true # bool | updateMetadata (optional)
update_stats = true # bool | updateStats (optional)

try:
    # Update a training datasets with a specific id from a featurestore
    api_response = api_instance.update_training_dataset(trainingdatasetid, featurestore_id, project_id, body=body, update_metadata=update_metadata, update_stats=update_stats)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->update_training_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trainingdatasetid** | **int**| Id of the training dataset | 
 **featurestore_id** | **int**|  | 
 **project_id** | **int**|  | 
 **body** | [**TrainingDatasetDTO**](TrainingDatasetDTO.md)|  | [optional] 
 **update_metadata** | **bool**| updateMetadata | [optional] 
 **update_stats** | **bool**| updateStats | [optional] 

### Return type

[**TrainingDatasetDTO**](TrainingDatasetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_method1**
> upload_method1(path, project_id, file=file, flow_chunk_number=flow_chunk_number, flow_chunk_size=flow_chunk_size, flow_current_chunk_size=flow_current_chunk_size, flow_filename=flow_filename, flow_identifier=flow_identifier, flow_relative_path=flow_relative_path, flow_total_chunks=flow_total_chunks, flow_total_size=flow_total_size, template_id=template_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
path = 'path_example' # str | 
project_id = 56 # int | 
file = 'file_example' # file |  (optional)
flow_chunk_number = 'flow_chunk_number_example' # str |  (optional)
flow_chunk_size = 'flow_chunk_size_example' # str |  (optional)
flow_current_chunk_size = 'flow_current_chunk_size_example' # str |  (optional)
flow_filename = 'flow_filename_example' # str |  (optional)
flow_identifier = 'flow_identifier_example' # str |  (optional)
flow_relative_path = 'flow_relative_path_example' # str |  (optional)
flow_total_chunks = 'flow_total_chunks_example' # str |  (optional)
flow_total_size = 'flow_total_size_example' # str |  (optional)
template_id = 56 # int |  (optional)

try:
    api_instance.upload_method1(path, project_id, file=file, flow_chunk_number=flow_chunk_number, flow_chunk_size=flow_chunk_size, flow_current_chunk_size=flow_current_chunk_size, flow_filename=flow_filename, flow_identifier=flow_identifier, flow_relative_path=flow_relative_path, flow_total_chunks=flow_total_chunks, flow_total_size=flow_total_size, template_id=template_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->upload_method1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **project_id** | **int**|  | 
 **file** | **file**|  | [optional] 
 **flow_chunk_number** | [**str**](.md)|  | [optional] 
 **flow_chunk_size** | [**str**](.md)|  | [optional] 
 **flow_current_chunk_size** | [**str**](.md)|  | [optional] 
 **flow_filename** | [**str**](.md)|  | [optional] 
 **flow_identifier** | [**str**](.md)|  | [optional] 
 **flow_relative_path** | [**str**](.md)|  | [optional] 
 **flow_total_chunks** | [**str**](.md)|  | [optional] 
 **flow_total_size** | [**str**](.md)|  | [optional] 
 **template_id** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_schema_for_topics**
> validate_schema_for_topics(project_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
project_id = 56 # int | 
body = swagger_client.SchemaDTO() # SchemaDTO |  (optional)

try:
    api_instance.validate_schema_for_topics(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->validate_schema_for_topics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **body** | [**SchemaDTO**](SchemaDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zip**
> zip(path, project_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectServiceApi()
path = 'path_example' # str | 
project_id = 56 # int | 

try:
    api_instance.zip(path, project_id)
except ApiException as e:
    print("Exception when calling ProjectServiceApi->zip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

