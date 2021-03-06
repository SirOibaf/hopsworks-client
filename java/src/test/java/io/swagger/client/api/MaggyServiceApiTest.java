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
import io.swagger.client.model.MaggyDriver;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for MaggyServiceApi
 */
@Ignore
public class MaggyServiceApiTest {

    private final MaggyServiceApi api = new MaggyServiceApi();

    /**
     * Get a Maggy Driver Endpoint for this YARN appId
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getDriverTest() throws ApiException {
        String appId = null;
        MaggyDriver response = api.getDriver(appId);

        // TODO: test validations
    }
    /**
     * Register a Maggy Driver Endpoint for this YARN appId (called by Spark Driver in maggy).
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void registerTest() throws ApiException {
        MaggyDriver body = null;
        api.register(body);

        // TODO: test validations
    }
}
