/**
 * Hopsworks api
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.1.0-SNAPSHOT
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */import { HdfsGroups } from './hdfsGroups';
import { HdfsUsers } from './hdfsUsers';
import { InodePK } from './inodePK';
import { Template } from './template';


export interface Inode { 
    inodePK?: InodePK;
    id: number;
    modificationTime?: number;
    accessTime?: number;
    hdfsUser?: HdfsUsers;
    hdfsGroup?: HdfsGroups;
    permission?: number;
    clientName?: string;
    clientMachine?: string;
    generationStamp?: number;
    header?: number;
    symlink?: string;
    quotaEnabled: boolean;
    underConstruction: boolean;
    subtreeLocked?: boolean;
    metaEnabled: boolean;
    dir: boolean;
    subtreeLockOwner?: number;
    size: number;
    templates?: Array<Template>;
    template?: number;
}