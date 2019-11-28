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
import io.swagger.client.model.JWTResponseDTO;
import io.swagger.client.model.ServiceJWTDTO;
import io.swagger.client.model.SpecificationForGeneratingNewJWT;
import io.swagger.client.model.SpecificationToRenewAnExistingJWT;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for JwtServiceApi
 */
@Ignore
public class JwtServiceApiTest {

    private final JwtServiceApi api = new JwtServiceApi();

    /**
     * Create application token
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createTokenTest() throws ApiException {
        SpecificationForGeneratingNewJWT body = null;
        JWTResponseDTO response = api.createToken(body);

        // TODO: test validations
    }
    /**
     * Invalidate a service JWT and also delete the signing key encoded in the token
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void invalidateServiceTokenTest() throws ApiException {
        String token = null;
        api.invalidateServiceToken(token);

        // TODO: test validations
    }
    /**
     * Invalidate application token
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void invalidateTokenTest() throws ApiException {
        String token = null;
        api.invalidateToken(token);

        // TODO: test validations
    }
    /**
     * Delete a JWT signing key
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void removeSigingKeyTest() throws ApiException {
        String keyName = null;
        api.removeSigingKey(keyName);

        // TODO: test validations
    }
    /**
     * Renew a service JWT without invalidating the previous token
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void renewServiceTokenTest() throws ApiException {
        SpecificationToRenewAnExistingJWT body = null;
        ServiceJWTDTO response = api.renewServiceToken(body);

        // TODO: test validations
    }
    /**
     * Renew application token
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void renewTokenTest() throws ApiException {
        SpecificationToRenewAnExistingJWT body = null;
        JWTResponseDTO response = api.renewToken(body);

        // TODO: test validations
    }
}