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
import io.swagger.client.model.HdfsGroups;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * HdfsUsers
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class HdfsUsers {

  @SerializedName("id")
  private Integer id = null;

  @SerializedName("name")
  private String name = null;

  @SerializedName("hdfsGroupsCollection")
  private List<HdfsGroups> hdfsGroupsCollection = null;

  @SerializedName("username")
  private String username = null;

  @SerializedName("project")
  private String project = null;
  public HdfsUsers id(Integer id) {
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
  public HdfsUsers name(String name) {
    this.name = name;
    return this;
  }

  

  /**
  * Get name
  * @return name
  **/
  @Schema(required = true, description = "")
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
  public HdfsUsers hdfsGroupsCollection(List<HdfsGroups> hdfsGroupsCollection) {
    this.hdfsGroupsCollection = hdfsGroupsCollection;
    return this;
  }

  public HdfsUsers addHdfsGroupsCollectionItem(HdfsGroups hdfsGroupsCollectionItem) {
    if (this.hdfsGroupsCollection == null) {
      this.hdfsGroupsCollection = new ArrayList<HdfsGroups>();
    }
    this.hdfsGroupsCollection.add(hdfsGroupsCollectionItem);
    return this;
  }

  /**
  * Get hdfsGroupsCollection
  * @return hdfsGroupsCollection
  **/
  @Schema(description = "")
  public List<HdfsGroups> getHdfsGroupsCollection() {
    return hdfsGroupsCollection;
  }
  public void setHdfsGroupsCollection(List<HdfsGroups> hdfsGroupsCollection) {
    this.hdfsGroupsCollection = hdfsGroupsCollection;
  }
  public HdfsUsers username(String username) {
    this.username = username;
    return this;
  }

  

  /**
  * Get username
  * @return username
  **/
  @Schema(description = "")
  public String getUsername() {
    return username;
  }
  public void setUsername(String username) {
    this.username = username;
  }
  public HdfsUsers project(String project) {
    this.project = project;
    return this;
  }

  

  /**
  * Get project
  * @return project
  **/
  @Schema(description = "")
  public String getProject() {
    return project;
  }
  public void setProject(String project) {
    this.project = project;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    HdfsUsers hdfsUsers = (HdfsUsers) o;
    return Objects.equals(this.id, hdfsUsers.id) &&
        Objects.equals(this.name, hdfsUsers.name) &&
        Objects.equals(this.hdfsGroupsCollection, hdfsUsers.hdfsGroupsCollection) &&
        Objects.equals(this.username, hdfsUsers.username) &&
        Objects.equals(this.project, hdfsUsers.project);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(id, name, hdfsGroupsCollection, username, project);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HdfsUsers {\n");
    
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    hdfsGroupsCollection: ").append(toIndentedString(hdfsGroupsCollection)).append("\n");
    sb.append("    username: ").append(toIndentedString(username)).append("\n");
    sb.append("    project: ").append(toIndentedString(project)).append("\n");
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
