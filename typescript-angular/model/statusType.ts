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

export interface StatusType { 
    reasonPhrase?: string;
    statusCode?: number;
    family?: StatusType.FamilyEnum;
}
export namespace StatusType {
    export type FamilyEnum = 'INFORMATIONAL' | 'SUCCESSFUL' | 'REDIRECTION' | 'CLIENT_ERROR' | 'SERVER_ERROR' | 'OTHER';
    export const FamilyEnum = {
        INFORMATIONAL: 'INFORMATIONAL' as FamilyEnum,
        SUCCESSFUL: 'SUCCESSFUL' as FamilyEnum,
        REDIRECTION: 'REDIRECTION' as FamilyEnum,
        CLIENTERROR: 'CLIENT_ERROR' as FamilyEnum,
        SERVERERROR: 'SERVER_ERROR' as FamilyEnum,
        OTHER: 'OTHER' as FamilyEnum
    };
}