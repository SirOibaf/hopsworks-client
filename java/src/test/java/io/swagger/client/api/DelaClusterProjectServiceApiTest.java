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
import io.swagger.client.model.InodeIdDTO;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DelaClusterProjectServiceApi
 */
@Ignore
public class DelaClusterProjectServiceApiTest {

    private final DelaClusterProjectServiceApi api = new DelaClusterProjectServiceApi();

    /**
     * 
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void removePublic1Test() throws ApiException {
        Long inodeId = null;
        Integer projectId = null;
        api.removePublic1(inodeId, projectId);

        // TODO: test validations
    }
    /**
     * 
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void shareTest() throws ApiException {
        Integer projectId = null;
        InodeIdDTO body = null;
        api.share(projectId, body);

        // TODO: test validations
    }
}
