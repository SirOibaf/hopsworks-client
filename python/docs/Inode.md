# Inode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inode_pk** | [**InodePK**](InodePK.md) |  | [optional] 
**id** | **int** |  | 
**modification_time** | **int** |  | [optional] 
**access_time** | **int** |  | [optional] 
**hdfs_user** | [**HdfsUsers**](HdfsUsers.md) |  | [optional] 
**hdfs_group** | [**HdfsGroups**](HdfsGroups.md) |  | [optional] 
**permission** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**client_machine** | **str** |  | [optional] 
**generation_stamp** | **int** |  | [optional] 
**header** | **int** |  | [optional] 
**symlink** | **str** |  | [optional] 
**quota_enabled** | **bool** |  | 
**under_construction** | **bool** |  | 
**subtree_locked** | **bool** |  | [optional] 
**meta_enabled** | **bool** |  | 
**dir** | **bool** |  | 
**subtree_lock_owner** | **int** |  | [optional] 
**size** | **int** |  | 
**templates** | [**list[Template]**](Template.md) |  | [optional] 
**template** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

