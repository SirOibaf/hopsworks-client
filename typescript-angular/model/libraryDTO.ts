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
 */import { CommandDTO } from './commandDTO';


export interface LibraryDTO { 
    href?: string;
    items?: Array<LibraryDTO>;
    count?: number;
    channel?: string;
    packageManager?: LibraryDTO.PackageManagerEnum;
    machine?: LibraryDTO.MachineEnum;
    library?: string;
    version?: string;
    status?: LibraryDTO.StatusEnum;
    preinstalled?: string;
    commands?: CommandDTO;
}
export namespace LibraryDTO {
    export type PackageManagerEnum = 'CONDA' | 'PIP';
    export const PackageManagerEnum = {
        CONDA: 'CONDA' as PackageManagerEnum,
        PIP: 'PIP' as PackageManagerEnum
    };
    export type MachineEnum = 'ALL' | 'CPU' | 'GPU';
    export const MachineEnum = {
        ALL: 'ALL' as MachineEnum,
        CPU: 'CPU' as MachineEnum,
        GPU: 'GPU' as MachineEnum
    };
    export type StatusEnum = 'NEW' | 'SUCCESS' | 'ONGOING' | 'FAILED';
    export const StatusEnum = {
        NEW: 'NEW' as StatusEnum,
        SUCCESS: 'SUCCESS' as StatusEnum,
        ONGOING: 'ONGOING' as StatusEnum,
        FAILED: 'FAILED' as StatusEnum
    };
}