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
export class ElasticServiceService {

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
     * 
     * 
     * @param projectId 
     * @param datasetName 
     * @param searchTerm 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public datasetSearch(projectId: number, datasetName: string, searchTerm: string, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public datasetSearch(projectId: number, datasetName: string, searchTerm: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public datasetSearch(projectId: number, datasetName: string, searchTerm: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public datasetSearch(projectId: number, datasetName: string, searchTerm: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (projectId === null || projectId === undefined) {
            throw new Error('Required parameter projectId was null or undefined when calling datasetSearch.');
        }

        if (datasetName === null || datasetName === undefined) {
            throw new Error('Required parameter datasetName was null or undefined when calling datasetSearch.');
        }

        if (searchTerm === null || searchTerm === undefined) {
            throw new Error('Required parameter searchTerm was null or undefined when calling datasetSearch.');
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
        ];

        return this.httpClient.get<any>(`${this.basePath}/elastic/datasetsearch/${encodeURIComponent(String(projectId))}/${encodeURIComponent(String(datasetName))}/${encodeURIComponent(String(searchTerm))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * 
     * 
     * @param searchTerm 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public globalSearch(searchTerm: string, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public globalSearch(searchTerm: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public globalSearch(searchTerm: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public globalSearch(searchTerm: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (searchTerm === null || searchTerm === undefined) {
            throw new Error('Required parameter searchTerm was null or undefined when calling globalSearch.');
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
        ];

        return this.httpClient.get<any>(`${this.basePath}/elastic/globalsearch/${encodeURIComponent(String(searchTerm))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * 
     * 
     * @param projectId 
     * @param searchTerm 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public projectSearch(projectId: number, searchTerm: string, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public projectSearch(projectId: number, searchTerm: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public projectSearch(projectId: number, searchTerm: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public projectSearch(projectId: number, searchTerm: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (projectId === null || projectId === undefined) {
            throw new Error('Required parameter projectId was null or undefined when calling projectSearch.');
        }

        if (searchTerm === null || searchTerm === undefined) {
            throw new Error('Required parameter searchTerm was null or undefined when calling projectSearch.');
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
        ];

        return this.httpClient.get<any>(`${this.basePath}/elastic/projectsearch/${encodeURIComponent(String(projectId))}/${encodeURIComponent(String(searchTerm))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

}