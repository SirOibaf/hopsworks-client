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
 */import { Field } from './field';
import { Template } from './template';


export interface MTable { 
    id?: number;
    name: string;
    templateid: number;
    template?: Template;
    fields?: Array<Field>;
}