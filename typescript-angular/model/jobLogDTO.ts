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
 */

export interface JobLogDTO { 
    log?: string;
    path?: string;
    type?: JobLogDTO.TypeEnum;
    retriable?: JobLogDTO.RetriableEnum;
}
export namespace JobLogDTO {
    export type TypeEnum = 'OUT' | 'ERR';
    export const TypeEnum = {
        OUT: 'OUT' as TypeEnum,
        ERR: 'ERR' as TypeEnum
    };
    export type RetriableEnum = 'RETRIEABLE_OUT' | 'RETRIABLE_ERR';
    export const RetriableEnum = {
        RETRIEABLEOUT: 'RETRIEABLE_OUT' as RetriableEnum,
        RETRIABLEERR: 'RETRIABLE_ERR' as RetriableEnum
    };
}