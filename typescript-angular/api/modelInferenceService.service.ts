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
 *//* tslint:disable:no-unused-variable member-ordering */

import { Inject, Injectable, Optional }                      from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams,
         HttpResponse, HttpEvent }                           from '@angular/common/http';
import { CustomHttpUrlEncodingCodec }                        from '../encoder';

import { Observable }                                        from 'rxjs/Observable';


import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable()
export class ModelInferenceServiceService {

    protected basePath = '///hopsworks-api/api';
    public defaultHeaders = new HttpHeaders();
    public configuration = new Configuration();

    constructor(protected httpClient: HttpClient, @Optional()@Inject(BASE_PATH) basePath: string, @Optional() configuration: Configuration) {
        if (basePath) {
            this.basePath = basePath;
        }
        if (configuration) {
            this.configuration = configuration;
            this.basePath = basePath || configuration.basePath || this.basePath;
        }
    }

    /**
     * @param consumes string[] mime-types
     * @return true: consumes contains 'multipart/form-data', false: otherwise
     */
    private canConsumeForm(consumes: string[]): boolean {
        const form = 'multipart/form-data';
        for (const consume of consumes) {
            if (form === consume) {
                return true;
            }
        }
        return false;
    }


    /**
     * Make inference
     * 
     * @param modelName Name of the model to query
     * @param version Version of the model to query
     * @param verb Type of query
     * @param projectId 
     * @param body 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public infer(modelName: string, version: string, verb: string, projectId: number, body?: string, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public infer(modelName: string, version: string, verb: string, projectId: number, body?: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public infer(modelName: string, version: string, verb: string, projectId: number, body?: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public infer(modelName: string, version: string, verb: string, projectId: number, body?: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (modelName === null || modelName === undefined) {
            throw new Error('Required parameter modelName was null or undefined when calling infer.');
        }

        if (version === null || version === undefined) {
            throw new Error('Required parameter version was null or undefined when calling infer.');
        }

        if (verb === null || verb === undefined) {
            throw new Error('Required parameter verb was null or undefined when calling infer.');
        }

        if (projectId === null || projectId === undefined) {
            throw new Error('Required parameter projectId was null or undefined when calling infer.');
        }


        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
            'application/json'
        ];
        const httpContentTypeSelected: string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected != undefined) {
            headers = headers.set('Content-Type', httpContentTypeSelected);
        }

        return this.httpClient.post<any>(`${this.basePath}/project/${encodeURIComponent(String(projectId))}/inference/models/${encodeURIComponent(String(modelName))}${encodeURIComponent(String(version))}${encodeURIComponent(String(verb))}`,
            body,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

}