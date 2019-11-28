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
 */import { EntityTag } from './entityTag';
import { Link } from './link';
import { Locale } from './locale';
import { MediaType } from './mediaType';
import { NewCookie } from './newCookie';
import { StatusType } from './statusType';


export interface Response { 
    statusInfo?: StatusType;
    mediaType?: MediaType;
    allowedMethods?: Array<string>;
    entityTag?: EntityTag;
    links?: Array<Link>;
    stringHeaders?: { [key: string]: Array<string>; };
    cookies?: { [key: string]: NewCookie; };
    metadata?: { [key: string]: Array<any>; };
    entity?: any;
    date?: Date;
    headers?: { [key: string]: Array<any>; };
    lastModified?: Date;
    status?: number;
    length?: number;
    language?: Locale;
    location?: string;
}