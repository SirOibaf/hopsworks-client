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

package io.swagger.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import org.threeten.bp.OffsetDateTime;

/**
 * MaggyDriver
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class MaggyDriver {

  @SerializedName("id")
  private Integer id = null;

  @SerializedName("appId")
  private String appId = null;

  @SerializedName("hostIp")
  private String hostIp = null;

  @SerializedName("port")
  private Integer port = null;

  @SerializedName("secret")
  private String secret = null;

  @SerializedName("created")
  private OffsetDateTime created = null;
  public MaggyDriver id(Integer id) {
    this.id = id;
    return this;
  }

  

  /**
  * Get id
  * @return id
  **/
  @Schema(description = "")
  public Integer getId() {
    return id;
  }
  public void setId(Integer id) {
    this.id = id;
  }
  public MaggyDriver appId(String appId) {
    this.appId = appId;
    return this;
  }

  

  /**
  * Get appId
  * @return appId
  **/
  @Schema(required = true, description = "")
  public String getAppId() {
    return appId;
  }
  public void setAppId(String appId) {
    this.appId = appId;
  }
  public MaggyDriver hostIp(String hostIp) {
    this.hostIp = hostIp;
    return this;
  }

  

  /**
  * Get hostIp
  * @return hostIp
  **/
  @Schema(required = true, description = "")
  public String getHostIp() {
    return hostIp;
  }
  public void setHostIp(String hostIp) {
    this.hostIp = hostIp;
  }
  public MaggyDriver port(Integer port) {
    this.port = port;
    return this;
  }

  

  /**
  * Get port
  * @return port
  **/
  @Schema(required = true, description = "")
  public Integer getPort() {
    return port;
  }
  public void setPort(Integer port) {
    this.port = port;
  }
  public MaggyDriver secret(String secret) {
    this.secret = secret;
    return this;
  }

  

  /**
  * Get secret
  * @return secret
  **/
  @Schema(required = true, description = "")
  public String getSecret() {
    return secret;
  }
  public void setSecret(String secret) {
    this.secret = secret;
  }
  public MaggyDriver created(OffsetDateTime created) {
    this.created = created;
    return this;
  }

  

  /**
  * Get created
  * @return created
  **/
  @Schema(description = "")
  public OffsetDateTime getCreated() {
    return created;
  }
  public void setCreated(OffsetDateTime created) {
    this.created = created;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    MaggyDriver maggyDriver = (MaggyDriver) o;
    return Objects.equals(this.id, maggyDriver.id) &&
        Objects.equals(this.appId, maggyDriver.appId) &&
        Objects.equals(this.hostIp, maggyDriver.hostIp) &&
        Objects.equals(this.port, maggyDriver.port) &&
        Objects.equals(this.secret, maggyDriver.secret) &&
        Objects.equals(this.created, maggyDriver.created);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(id, appId, hostIp, port, secret, created);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class MaggyDriver {\n");
    
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    appId: ").append(toIndentedString(appId)).append("\n");
    sb.append("    hostIp: ").append(toIndentedString(hostIp)).append("\n");
    sb.append("    port: ").append(toIndentedString(port)).append("\n");
    sb.append("    secret: ").append(toIndentedString(secret)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}