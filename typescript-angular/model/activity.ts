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
import { Users } from './users';


export interface Activity { 
    id?: number;
    activity?: string;
    timestamp: Date;
    flag: Activity.FlagEnum;
    project?: Project;
    user?: Users;
}
export namespace Activity {
    export type FlagEnum = 'MEMBER' | 'PROJECT' | 'SERVICE' | 'DATASET' | 'JOB';
    export const FlagEnum = {
        MEMBER: 'MEMBER' as FlagEnum,
        PROJECT: 'PROJECT' as FlagEnum,
        SERVICE: 'SERVICE' as FlagEnum,
        DATASET: 'DATASET' as FlagEnum,
        JOB: 'JOB' as FlagEnum
    };
}