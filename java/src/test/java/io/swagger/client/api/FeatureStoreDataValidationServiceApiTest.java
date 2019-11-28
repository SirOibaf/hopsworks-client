/*
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

package io.swagger.client.api;

import io.swagger.client.ApiException;
import io.swagger.client.model.ConstraintGroupDTO;
import io.swagger.client.model.DataValidationSettingsDTO;
import io.swagger.client.model.ValidationResult;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for FeatureStoreDataValidationServiceApi
 */
@Ignore
public class FeatureStoreDataValidationServiceApiTest {

    private final FeatureStoreDataValidationServiceApi api = new FeatureStoreDataValidationServiceApi();

    /**
     * Write Deequ validation rules to Filesystem so validation job can pick it up
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void addValidationRulesTest() throws ApiException {
        Integer featuregroupId = null;
        Integer featureStoreId = null;
        Integer projectId = null;
        ConstraintGroupDTO body = null;
        DataValidationSettingsDTO response = api.addValidationRules(featuregroupId, featureStoreId, projectId, body);

        // TODO: test validations
    }
    /**
     * Fetch the result of a Deequ data validation job
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getValidationResultTest() throws ApiException {
        Integer featuregroupId = null;
        Integer featureStoreId = null;
        Integer projectId = null;
        ValidationResult response = api.getValidationResult(featuregroupId, featureStoreId, projectId);

        // TODO: test validations
    }
    /**
     * Get previously stored Deequ validation rules
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getValidationRulesTest() throws ApiException {
        Integer featuregroupId = null;
        Integer featureStoreId = null;
        Integer projectId = null;
        ConstraintGroupDTO response = api.getValidationRules(featuregroupId, featureStoreId, projectId);

        // TODO: test validations
    }
}
