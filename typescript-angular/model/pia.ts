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

export interface Pia { 
    id?: number;
    personalData: string;
    howDataCollected: string;
    specifiedExplicitLegitimate: number;
    consentProcess?: string;
    consentBasis?: string;
    dataMinimized: number;
    dataUptodate: number;
    usersInformedHow: string;
    userControlsDataCollectionRetention: string;
    dataEncrypted: number;
    dataAnonymized: number;
    dataPseudonymized: number;
    dataBackedup: number;
    dataSecurityMeasures: string;
    dataPortabilityMeasure: string;
    subjectAccessRights: string;
    risks: string;
    projectId?: number;
}