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
 */import { TopicsFilterBy } from './topicsFilterBy';
import { TopicsSortBy } from './topicsSortBy';


export interface TopicsBeanParam { 
    sortBy?: string;
    sortBySet?: Array<TopicsSortBy>;
    filter?: Array<TopicsFilterBy>;
}