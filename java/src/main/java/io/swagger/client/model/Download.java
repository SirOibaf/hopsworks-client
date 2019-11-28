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
import io.swagger.client.model.ClusterAddressDTO;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Download
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class Download {

  @SerializedName("projectId")
  private Integer projectId = null;

  @SerializedName("publicDSId")
  private String publicDSId = null;

  @SerializedName("name")
  private String name = null;

  @SerializedName("bootstrap")
  private List<ClusterAddressDTO> bootstrap = null;

  @SerializedName("topics")
  private String topics = null;
  public Download projectId(Integer projectId) {
    this.projectId = projectId;
    return this;
  }

  

  /**
  * Get projectId
  * @return projectId
  **/
  @Schema(description = "")
  public Integer getProjectId() {
    return projectId;
  }
  public void setProjectId(Integer projectId) {
    this.projectId = projectId;
  }
  public Download publicDSId(String publicDSId) {
    this.publicDSId = publicDSId;
    return this;
  }

  

  /**
  * Get publicDSId
  * @return publicDSId
  **/
  @Schema(description = "")
  public String getPublicDSId() {
    return publicDSId;
  }
  public void setPublicDSId(String publicDSId) {
    this.publicDSId = publicDSId;
  }
  public Download name(String name) {
    this.name = name;
    return this;
  }

  

  /**
  * Get name
  * @return name
  **/
  @Schema(description = "")
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
  public Download bootstrap(List<ClusterAddressDTO> bootstrap) {
    this.bootstrap = bootstrap;
    return this;
  }

  public Download addBootstrapItem(ClusterAddressDTO bootstrapItem) {
    if (this.bootstrap == null) {
      this.bootstrap = new ArrayList<ClusterAddressDTO>();
    }
    this.bootstrap.add(bootstrapItem);
    return this;
  }

  /**
  * Get bootstrap
  * @return bootstrap
  **/
  @Schema(description = "")
  public List<ClusterAddressDTO> getBootstrap() {
    return bootstrap;
  }
  public void setBootstrap(List<ClusterAddressDTO> bootstrap) {
    this.bootstrap = bootstrap;
  }
  public Download topics(String topics) {
    this.topics = topics;
    return this;
  }

  

  /**
  * Get topics
  * @return topics
  **/
  @Schema(description = "")
  public String getTopics() {
    return topics;
  }
  public void setTopics(String topics) {
    this.topics = topics;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Download download = (Download) o;
    return Objects.equals(this.projectId, download.projectId) &&
        Objects.equals(this.publicDSId, download.publicDSId) &&
        Objects.equals(this.name, download.name) &&
        Objects.equals(this.bootstrap, download.bootstrap) &&
        Objects.equals(this.topics, download.topics);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(projectId, publicDSId, name, bootstrap, topics);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Download {\n");
    
    sb.append("    projectId: ").append(toIndentedString(projectId)).append("\n");
    sb.append("    publicDSId: ").append(toIndentedString(publicDSId)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    bootstrap: ").append(toIndentedString(bootstrap)).append("\n");
    sb.append("    topics: ").append(toIndentedString(topics)).append("\n");
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