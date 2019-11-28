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
 */import { Hosts } from './hosts';
import { Project } from './project';


export interface CondaCommands { 
    id?: number;
    user: string;
    proj: string;
    channelUrl?: string;
    arg?: string;
    lib?: string;
    version?: string;
    op: CondaCommands.OpEnum;
    status: CondaCommands.StatusEnum;
    installType: CondaCommands.InstallTypeEnum;
    machineType: CondaCommands.MachineTypeEnum;
    created: Date;
    projectId?: Project;
    hostId?: Hosts;
    environmentYml?: string;
    installJupyter?: boolean;
}
export namespace CondaCommands {
    export type OpEnum = 'CLONE' | 'CREATE' | 'BACKUP' | 'REMOVE' | 'LIST' | 'INSTALL' | 'UNINSTALL' | 'UPGRADE' | 'CLEAN' | 'YML';
    export const OpEnum = {
        CLONE: 'CLONE' as OpEnum,
        CREATE: 'CREATE' as OpEnum,
        BACKUP: 'BACKUP' as OpEnum,
        REMOVE: 'REMOVE' as OpEnum,
        LIST: 'LIST' as OpEnum,
        INSTALL: 'INSTALL' as OpEnum,
        UNINSTALL: 'UNINSTALL' as OpEnum,
        UPGRADE: 'UPGRADE' as OpEnum,
        CLEAN: 'CLEAN' as OpEnum,
        YML: 'YML' as OpEnum
    };
    export type StatusEnum = 'NEW' | 'SUCCESS' | 'ONGOING' | 'FAILED';
    export const StatusEnum = {
        NEW: 'NEW' as StatusEnum,
        SUCCESS: 'SUCCESS' as StatusEnum,
        ONGOING: 'ONGOING' as StatusEnum,
        FAILED: 'FAILED' as StatusEnum
    };
    export type InstallTypeEnum = 'ENVIRONMENT' | 'CONDA' | 'PIP';
    export const InstallTypeEnum = {
        ENVIRONMENT: 'ENVIRONMENT' as InstallTypeEnum,
        CONDA: 'CONDA' as InstallTypeEnum,
        PIP: 'PIP' as InstallTypeEnum
    };
    export type MachineTypeEnum = 'ALL' | 'CPU' | 'GPU';
    export const MachineTypeEnum = {
        ALL: 'ALL' as MachineTypeEnum,
        CPU: 'CPU' as MachineTypeEnum,
        GPU: 'GPU' as MachineTypeEnum
    };
}