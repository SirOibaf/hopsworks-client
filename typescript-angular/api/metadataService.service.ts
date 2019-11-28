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
export class MetadataServiceService {

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
     * @param body 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public addMetadataWithSchema(body?: string, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public addMetadataWithSchema(body?: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public addMetadataWithSchema(body?: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public addMetadataWithSchema(body?: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {


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

        return this.httpClient.post<any>(`${this.basePath}/metadata/addWithSchema`,
            body,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Create or Update a schemaless metadata for a path.
     * 
     * @param xattrName 
     * @param path 
     * @param body 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public attachSchemalessMetadata(xattrName: string, path: string, body?: string, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public attachSchemalessMetadata(xattrName: string, path: string, body?: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public attachSchemalessMetadata(xattrName: string, path: string, body?: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public attachSchemalessMetadata(xattrName: string, path: string, body?: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (xattrName === null || xattrName === undefined) {
            throw new Error('Required parameter xattrName was null or undefined when calling attachSchemalessMetadata.');
        }

        if (path === null || path === undefined) {
            throw new Error('Required parameter path was null or undefined when calling attachSchemalessMetadata.');
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

        return this.httpClient.put<any>(`${this.basePath}/metadata/schemaless/${encodeURIComponent(String(xattrName))}/${encodeURIComponent(String(path))}`,
            body,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Delete the schemaless metadata attached to a path.
     * 
     * @param xattrName 
     * @param path 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public detachSchemalessMetadata(xattrName: string, path: string, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public detachSchemalessMetadata(xattrName: string, path: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public detachSchemalessMetadata(xattrName: string, path: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public detachSchemalessMetadata(xattrName: string, path: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (xattrName === null || xattrName === undefined) {
            throw new Error('Required parameter xattrName was null or undefined when calling detachSchemalessMetadata.');
        }

        if (path === null || path === undefined) {
            throw new Error('Required parameter path was null or undefined when calling detachSchemalessMetadata.');
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

        return this.httpClient.delete<any>(`${this.basePath}/metadata/schemaless/${encodeURIComponent(String(xattrName))}/${encodeURIComponent(String(path))}`,
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
     * @param inodeid 
     * @param templateid 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public detachTemplateFromInode(inodeid: number, templateid: number, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public detachTemplateFromInode(inodeid: number, templateid: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public detachTemplateFromInode(inodeid: number, templateid: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public detachTemplateFromInode(inodeid: number, templateid: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (inodeid === null || inodeid === undefined) {
            throw new Error('Required parameter inodeid was null or undefined when calling detachTemplateFromInode.');
        }

        if (templateid === null || templateid === undefined) {
            throw new Error('Required parameter templateid was null or undefined when calling detachTemplateFromInode.');
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

        return this.httpClient.get<any>(`${this.basePath}/metadata/detachtemplate/${encodeURIComponent(String(inodeid))}/${encodeURIComponent(String(templateid))}`,
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
     * @param inodeid 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public fetchAvailableTemplatesForInode(inodeid: number, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public fetchAvailableTemplatesForInode(inodeid: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public fetchAvailableTemplatesForInode(inodeid: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public fetchAvailableTemplatesForInode(inodeid: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (inodeid === null || inodeid === undefined) {
            throw new Error('Required parameter inodeid was null or undefined when calling fetchAvailableTemplatesForInode.');
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

        return this.httpClient.get<any>(`${this.basePath}/metadata/fetchavailabletemplatesforinode/${encodeURIComponent(String(inodeid))}`,
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
     * @param inodepid 
     * @param inodename 
     * @param tableid 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public fetchMetadata(inodepid: number, inodename: string, tableid: number, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public fetchMetadata(inodepid: number, inodename: string, tableid: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public fetchMetadata(inodepid: number, inodename: string, tableid: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public fetchMetadata(inodepid: number, inodename: string, tableid: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (inodepid === null || inodepid === undefined) {
            throw new Error('Required parameter inodepid was null or undefined when calling fetchMetadata.');
        }

        if (inodename === null || inodename === undefined) {
            throw new Error('Required parameter inodename was null or undefined when calling fetchMetadata.');
        }

        if (tableid === null || tableid === undefined) {
            throw new Error('Required parameter tableid was null or undefined when calling fetchMetadata.');
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

        return this.httpClient.get<any>(`${this.basePath}/metadata/fetchmetadata/${encodeURIComponent(String(inodepid))}/${encodeURIComponent(String(inodename))}/${encodeURIComponent(String(tableid))}`,
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
     * @param inodepid 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public fetchMetadataCompact(inodepid: number, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public fetchMetadataCompact(inodepid: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public fetchMetadataCompact(inodepid: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public fetchMetadataCompact(inodepid: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (inodepid === null || inodepid === undefined) {
            throw new Error('Required parameter inodepid was null or undefined when calling fetchMetadataCompact.');
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

        return this.httpClient.get<any>(`${this.basePath}/metadata/${encodeURIComponent(String(inodepid))}`,
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
     * @param templateid 
     * @param sender 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public fetchTemplate(templateid: number, sender: string, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public fetchTemplate(templateid: number, sender: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public fetchTemplate(templateid: number, sender: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public fetchTemplate(templateid: number, sender: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (templateid === null || templateid === undefined) {
            throw new Error('Required parameter templateid was null or undefined when calling fetchTemplate.');
        }

        if (sender === null || sender === undefined) {
            throw new Error('Required parameter sender was null or undefined when calling fetchTemplate.');
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

        return this.httpClient.get<any>(`${this.basePath}/metadata/fetchtemplate/${encodeURIComponent(String(templateid))}/${encodeURIComponent(String(sender))}`,
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
     * @param inodeid 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public fetchTemplatesforInode(inodeid: number, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public fetchTemplatesforInode(inodeid: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public fetchTemplatesforInode(inodeid: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public fetchTemplatesforInode(inodeid: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (inodeid === null || inodeid === undefined) {
            throw new Error('Required parameter inodeid was null or undefined when calling fetchTemplatesforInode.');
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

        return this.httpClient.get<any>(`${this.basePath}/metadata/fetchtemplatesforinode/${encodeURIComponent(String(inodeid))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Get the schemaless metadata attached to a path.
     * 
     * @param xattrName 
     * @param path 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public getSchemalessMetadata(xattrName: string, path: string, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public getSchemalessMetadata(xattrName: string, path: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public getSchemalessMetadata(xattrName: string, path: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public getSchemalessMetadata(xattrName: string, path: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (xattrName === null || xattrName === undefined) {
            throw new Error('Required parameter xattrName was null or undefined when calling getSchemalessMetadata.');
        }

        if (path === null || path === undefined) {
            throw new Error('Required parameter path was null or undefined when calling getSchemalessMetadata.');
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

        return this.httpClient.get<any>(`${this.basePath}/metadata/schemaless/${encodeURIComponent(String(xattrName))}/${encodeURIComponent(String(path))}`,
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
     * @param body 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public removeMetadataWithSchema(body?: string, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public removeMetadataWithSchema(body?: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public removeMetadataWithSchema(body?: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public removeMetadataWithSchema(body?: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {


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

        return this.httpClient.post<any>(`${this.basePath}/metadata/removeWithSchema`,
            body,
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
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public testMethod(observe?: 'body', reportProgress?: boolean): Observable<any>;
    public testMethod(observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public testMethod(observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public testMethod(observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

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

        return this.httpClient.get<any>(`${this.basePath}/metadata/upload`,
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
     * @param body 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public updateMetadataWithSchema(body?: string, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public updateMetadataWithSchema(body?: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public updateMetadataWithSchema(body?: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public updateMetadataWithSchema(body?: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {


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

        return this.httpClient.post<any>(`${this.basePath}/metadata/updateWithSchema`,
            body,
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
     * @param file 
     * @param flowChunkNumber 
     * @param flowChunkSize 
     * @param flowCurrentChunkSize 
     * @param flowFilename 
     * @param flowIdentifier 
     * @param flowRelativePath 
     * @param flowTotalChunks 
     * @param flowTotalSize 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public uploadMethod(file?: Blob, flowChunkNumber?: string, flowChunkSize?: string, flowCurrentChunkSize?: string, flowFilename?: string, flowIdentifier?: string, flowRelativePath?: string, flowTotalChunks?: string, flowTotalSize?: string, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public uploadMethod(file?: Blob, flowChunkNumber?: string, flowChunkSize?: string, flowCurrentChunkSize?: string, flowFilename?: string, flowIdentifier?: string, flowRelativePath?: string, flowTotalChunks?: string, flowTotalSize?: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public uploadMethod(file?: Blob, flowChunkNumber?: string, flowChunkSize?: string, flowCurrentChunkSize?: string, flowFilename?: string, flowIdentifier?: string, flowRelativePath?: string, flowTotalChunks?: string, flowTotalSize?: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public uploadMethod(file?: Blob, flowChunkNumber?: string, flowChunkSize?: string, flowCurrentChunkSize?: string, flowFilename?: string, flowIdentifier?: string, flowRelativePath?: string, flowTotalChunks?: string, flowTotalSize?: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {










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
            'multipart/form-data'
        ];

        const canConsumeForm = this.canConsumeForm(consumes);

        let formParams: { append(param: string, value: any): void; };
        let useForm = false;
        let convertFormParamsToString = false;
        // use FormData to transmit files using content-type "multipart/form-data"
        // see https://stackoverflow.com/questions/4007969/application-x-www-form-urlencoded-or-multipart-form-data
        useForm = canConsumeForm;
        if (useForm) {
            formParams = new FormData();
        } else {
            formParams = new HttpParams({encoder: new CustomHttpUrlEncodingCodec()});
        }

        if (file !== undefined) {
            formParams = formParams.append('file', <any>file) || formParams;
        }
        if (flowChunkNumber !== undefined) {
            formParams = formParams.append('flowChunkNumber', <any>flowChunkNumber) || formParams;
        }
        if (flowChunkSize !== undefined) {
            formParams = formParams.append('flowChunkSize', <any>flowChunkSize) || formParams;
        }
        if (flowCurrentChunkSize !== undefined) {
            formParams = formParams.append('flowCurrentChunkSize', <any>flowCurrentChunkSize) || formParams;
        }
        if (flowFilename !== undefined) {
            formParams = formParams.append('flowFilename', <any>flowFilename) || formParams;
        }
        if (flowIdentifier !== undefined) {
            formParams = formParams.append('flowIdentifier', <any>flowIdentifier) || formParams;
        }
        if (flowRelativePath !== undefined) {
            formParams = formParams.append('flowRelativePath', <any>flowRelativePath) || formParams;
        }
        if (flowTotalChunks !== undefined) {
            formParams = formParams.append('flowTotalChunks', <any>flowTotalChunks) || formParams;
        }
        if (flowTotalSize !== undefined) {
            formParams = formParams.append('flowTotalSize', <any>flowTotalSize) || formParams;
        }

        return this.httpClient.post<any>(`${this.basePath}/metadata/upload`,
            convertFormParamsToString ? formParams.toString() : formParams,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

}