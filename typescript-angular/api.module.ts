import { NgModule, ModuleWithProviders, SkipSelf, Optional } from '@angular/core';
import { Configuration } from './configuration';
import { HttpClient } from '@angular/common/http';


import { AdminService } from './api/admin.service';
import { AgentServiceService } from './api/agentService.service';
import { AirflowRelatedEndpointsService } from './api/airflowRelatedEndpoints.service';
import { ApiKeyResourceService } from './api/apiKeyResource.service';
import { AuthService } from './api/auth.service';
import { BannerServiceService } from './api/bannerService.service';
import { ClusterUtilisationServiceService } from './api/clusterUtilisationService.service';
import { CrossDelaServiceService } from './api/crossDelaService.service';
import { DelaClusterProjectServiceService } from './api/delaClusterProjectService.service';
import { DelaClusterServiceService } from './api/delaClusterService.service';
import { DelaServiceService } from './api/delaService.service';
import { ElasticServiceService } from './api/elasticService.service';
import { EndpointServiceService } from './api/endpointService.service';
import { FeatureStoreDataValidationServiceService } from './api/featureStoreDataValidationService.service';
import { FeaturegroupServiceService } from './api/featuregroupService.service';
import { FeaturestoreServiceService } from './api/featurestoreService.service';
import { HopssiteServiceService } from './api/hopssiteService.service';
import { JWTServiceService } from './api/jWTService.service';
import { MachineTypesResourceService } from './api/machineTypesResource.service';
import { MaggyServiceService } from './api/maggyService.service';
import { MessageServiceService } from './api/messageService.service';
import { MetadataServiceService } from './api/metadataService.service';
import { ModelInferenceServiceService } from './api/modelInferenceService.service';
import { MonitorClusterServiceService } from './api/monitorClusterService.service';
import { ProjectActivitiesResourceService } from './api/projectActivitiesResource.service';
import { ProjectServiceService } from './api/projectService.service';
import { PythonService } from './api/python.service';
import { PythonEnvironmentCommandsResourceService } from './api/pythonEnvironmentCommandsResource.service';
import { PythonEnvironmentLibraryCommandsResourceService } from './api/pythonEnvironmentLibraryCommandsResource.service';
import { PythonEnvironmentLibraryResourceService } from './api/pythonEnvironmentLibraryResource.service';
import { PythonEnvironmentsResourceService } from './api/pythonEnvironmentsResource.service';
import { RequestServiceService } from './api/requestService.service';
import { StorageConnectorServiceService } from './api/storageConnectorService.service';
import { TensorFlowServingServiceService } from './api/tensorFlowServingService.service';
import { TrainingDatasetServiceService } from './api/trainingDatasetService.service';
import { UIServingConfigurationService } from './api/uIServingConfiguration.service';
import { UserActivitiesResourceService } from './api/userActivitiesResource.service';
import { UsersService } from './api/users.service';
import { VariablesServiceService } from './api/variablesService.service';

@NgModule({
  imports:      [],
  declarations: [],
  exports:      [],
  providers: [
    AdminService,
    AgentServiceService,
    AirflowRelatedEndpointsService,
    ApiKeyResourceService,
    AuthService,
    BannerServiceService,
    ClusterUtilisationServiceService,
    CrossDelaServiceService,
    DelaClusterProjectServiceService,
    DelaClusterServiceService,
    DelaServiceService,
    ElasticServiceService,
    EndpointServiceService,
    FeatureStoreDataValidationServiceService,
    FeaturegroupServiceService,
    FeaturestoreServiceService,
    HopssiteServiceService,
    JWTServiceService,
    MachineTypesResourceService,
    MaggyServiceService,
    MessageServiceService,
    MetadataServiceService,
    ModelInferenceServiceService,
    MonitorClusterServiceService,
    ProjectActivitiesResourceService,
    ProjectServiceService,
    PythonService,
    PythonEnvironmentCommandsResourceService,
    PythonEnvironmentLibraryCommandsResourceService,
    PythonEnvironmentLibraryResourceService,
    PythonEnvironmentsResourceService,
    RequestServiceService,
    StorageConnectorServiceService,
    TensorFlowServingServiceService,
    TrainingDatasetServiceService,
    UIServingConfigurationService,
    UserActivitiesResourceService,
    UsersService,
    VariablesServiceService ]
})
export class ApiModule {
    public static forRoot(configurationFactory: () => Configuration): ModuleWithProviders {
        return {
            ngModule: ApiModule,
            providers: [ { provide: Configuration, useFactory: configurationFactory } ]
        };
    }

    constructor( @Optional() @SkipSelf() parentModule: ApiModule,
                 @Optional() http: HttpClient) {
        if (parentModule) {
            throw new Error('ApiModule is already loaded. Import in your base AppModule only.');
        }
        if (!http) {
            throw new Error('You need to import the HttpClientModule in your AppModule! \n' +
            'See also https://github.com/angular/angular/issues/20575');
        }
    }
}
