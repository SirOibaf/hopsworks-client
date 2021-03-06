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
 */import { UserDTO } from './userDTO';


export interface ExecutionDTO { 
    href?: string;
    items?: Array<ExecutionDTO>;
    count?: number;
    id?: number;
    submissionTime?: Date;
    state?: ExecutionDTO.StateEnum;
    stdoutPath?: string;
    stderrPath?: string;
    appId?: string;
    hdfsUser?: string;
    finalStatus?: ExecutionDTO.FinalStatusEnum;
    progress?: number;
    user?: UserDTO;
    filesToRemove?: Array<string>;
    duration?: number;
    flinkMasterURL?: string;
}
export namespace ExecutionDTO {
    export type StateEnum = 'INITIALIZING' | 'INITIALIZATION_FAILED' | 'FINISHED' | 'RUNNING' | 'ACCEPTED' | 'FAILED' | 'KILLED' | 'NEW' | 'NEW_SAVING' | 'SUBMITTED' | 'AGGREGATING_LOGS' | 'FRAMEWORK_FAILURE' | 'STARTING_APP_MASTER' | 'APP_MASTER_START_FAILED' | 'GENERATING_SECURITY_MATERIAL';
    export const StateEnum = {
        INITIALIZING: 'INITIALIZING' as StateEnum,
        INITIALIZATIONFAILED: 'INITIALIZATION_FAILED' as StateEnum,
        FINISHED: 'FINISHED' as StateEnum,
        RUNNING: 'RUNNING' as StateEnum,
        ACCEPTED: 'ACCEPTED' as StateEnum,
        FAILED: 'FAILED' as StateEnum,
        KILLED: 'KILLED' as StateEnum,
        NEW: 'NEW' as StateEnum,
        NEWSAVING: 'NEW_SAVING' as StateEnum,
        SUBMITTED: 'SUBMITTED' as StateEnum,
        AGGREGATINGLOGS: 'AGGREGATING_LOGS' as StateEnum,
        FRAMEWORKFAILURE: 'FRAMEWORK_FAILURE' as StateEnum,
        STARTINGAPPMASTER: 'STARTING_APP_MASTER' as StateEnum,
        APPMASTERSTARTFAILED: 'APP_MASTER_START_FAILED' as StateEnum,
        GENERATINGSECURITYMATERIAL: 'GENERATING_SECURITY_MATERIAL' as StateEnum
    };
    export type FinalStatusEnum = 'UNDEFINED' | 'SUCCEEDED' | 'FAILED' | 'KILLED';
    export const FinalStatusEnum = {
        UNDEFINED: 'UNDEFINED' as FinalStatusEnum,
        SUCCEEDED: 'SUCCEEDED' as FinalStatusEnum,
        FAILED: 'FAILED' as FinalStatusEnum,
        KILLED: 'KILLED' as FinalStatusEnum
    };
}