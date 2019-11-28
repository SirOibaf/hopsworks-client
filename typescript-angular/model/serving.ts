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
 */import { Project } from './project';
import { ProjectTopics } from './projectTopics';
import { Users } from './users';


export interface Serving { 
    id?: number;
    created?: Date;
    creator?: Users;
    name: string;
    artifactPath: string;
    version: number;
    optimized: boolean;
    instances?: number;
    project?: Project;
    batchingEnabled?: boolean;
    lockIP?: string;
    lockTimestamp?: number;
    kafkaTopic?: ProjectTopics;
    localPort?: number;
    localPid?: number;
    localDir?: string;
    servingType: Serving.ServingTypeEnum;
}
export namespace Serving {
    export type ServingTypeEnum = 'TENSORFLOW' | 'SKLEARN';
    export const ServingTypeEnum = {
        TENSORFLOW: 'TENSORFLOW' as ServingTypeEnum,
        SKLEARN: 'SKLEARN' as ServingTypeEnum
    };
}