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
 */import { Featurestore } from './featurestore';


export interface FeaturestoreS3Connector { 
    id?: number;
    featurestore?: Featurestore;
    accessKey?: string;
    secretKey?: string;
    bucket?: string;
    description?: string;
    name?: string;
}