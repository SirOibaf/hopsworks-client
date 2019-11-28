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
import io.swagger.client.model.Hosts;
import io.swagger.client.model.LlapClusterStatus;
import io.swagger.client.model.ProjectAdminInfoDTO;
import io.swagger.client.model.ProjectDTO;
import io.swagger.client.model.Users;
import io.swagger.client.model.VariablesRequest;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AdminApi
 */
@Ignore
public class AdminApiTest {

    private final AdminApi api = new AdminApi();

    /**
     * 
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void acceptUserTest() throws ApiException {
        String email = null;
        Users body = null;
        api.acceptUser(email, body);

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
    public void addNewClusterNodeTest() throws ApiException {
        Hosts body = null;
        api.addNewClusterNode(body);

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
    public void changeClusterStatusTest() throws ApiException {
        LlapClusterStatus body = null;
        api.changeClusterStatus(body);

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
    public void changeMasterEncryptionPasswordTest() throws ApiException {
        String oldPassword = null;
        String newPassword = null;
        api.changeMasterEncryptionPassword(oldPassword, newPassword);

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
    public void clusterStatusTest() throws ApiException {
        api.clusterStatus();

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
    public void createProjectAsUserTest() throws ApiException {
        ProjectDTO body = null;
        api.createProjectAsUser(body);

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
    public void deleteNodeTest() throws ApiException {
        String hostid = null;
        api.deleteNode(hostid);

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
    public void deleteProjectTest() throws ApiException {
        Integer id = null;
        api.deleteProject(id);

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
    public void forceDeleteProjectTest() throws ApiException {
        String name = null;
        api.forceDeleteProject(name);

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
    public void getAllClusterNodesTest() throws ApiException {
        api.getAllClusterNodes();

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
    public void getAllGroupsTest() throws ApiException {
        api.getAllGroups();

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
    public void getAllUsersTest() throws ApiException {
        String status = null;
        api.getAllUsers(status);

        // TODO: test validations
    }
    /**
     * Get kafka system settings
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getKafkaSettingsTest() throws ApiException {
        api.getKafkaSettings();

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
    public void getMaterializerStateTest() throws ApiException {
        api.getMaterializerState();

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
    public void getProjectAdminInfoTest() throws ApiException {
        Integer id = null;
        api.getProjectAdminInfo(id);

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
    public void getProjectsAdminInfoTest() throws ApiException {
        api.getProjectsAdminInfo();

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
    public void getUpdatePasswordStatusTest() throws ApiException {
        Integer opId = null;
        api.getUpdatePasswordStatus(opId);

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
    public void getUserTest() throws ApiException {
        String email = null;
        api.getUser(email);

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
    public void pendingUserTest() throws ApiException {
        String email = null;
        api.pendingUser(email);

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
    public void refreshVariablesTest() throws ApiException {
        api.refreshVariables();

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
    public void rejectUserTest() throws ApiException {
        String email = null;
        api.rejectUser(email);

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
    public void removeLocalMaterializedCryptoTest() throws ApiException {
        String name = null;
        String directory = null;
        api.removeLocalMaterializedCrypto(name, directory);

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
    public void removeRemoteMaterializedCryptoTest() throws ApiException {
        String name = null;
        String directory = null;
        api.removeRemoteMaterializedCrypto(name, directory);

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
    public void renewServiceJWTTest() throws ApiException {
        api.renewServiceJWT();

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
    public void restartAgentTest() throws ApiException {
        String hostname = null;
        api.restartAgent(hostname);

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
    public void serviceKeyRotateTest() throws ApiException {
        api.serviceKeyRotate();

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
    public void setProjectAdminInfoTest() throws ApiException {
        ProjectAdminInfoDTO body = null;
        api.setProjectAdminInfo(body);

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
    public void startAgentTest() throws ApiException {
        String hostname = null;
        api.startAgent(hostname);

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
    public void stopAgentTest() throws ApiException {
        String hostname = null;
        api.stopAgent(hostname);

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
    public void updateClusterNodeTest() throws ApiException {
        Hosts body = null;
        api.updateClusterNode(body);

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
    public void updateUserTest() throws ApiException {
        String email = null;
        Users body = null;
        api.updateUser(email, body);

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
    public void updateVariablesTest() throws ApiException {
        VariablesRequest body = null;
        api.updateVariables(body);

        // TODO: test validations
    }
}