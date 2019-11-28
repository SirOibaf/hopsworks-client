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
import io.swagger.client.model.ProjectTopics;
import io.swagger.client.model.SchemaTopicsPK;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.threeten.bp.OffsetDateTime;

/**
 * SchemaTopics
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class SchemaTopics {

  @SerializedName("projectTopicsCollection")
  private List<ProjectTopics> projectTopicsCollection = null;

  @SerializedName("schemaTopicsPK")
  private SchemaTopicsPK schemaTopicsPK = null;

  @SerializedName("contents")
  private String contents = null;

  @SerializedName("createdOn")
  private OffsetDateTime createdOn = null;
  public SchemaTopics projectTopicsCollection(List<ProjectTopics> projectTopicsCollection) {
    this.projectTopicsCollection = projectTopicsCollection;
    return this;
  }

  public SchemaTopics addProjectTopicsCollectionItem(ProjectTopics projectTopicsCollectionItem) {
    if (this.projectTopicsCollection == null) {
      this.projectTopicsCollection = new ArrayList<ProjectTopics>();
    }
    this.projectTopicsCollection.add(projectTopicsCollectionItem);
    return this;
  }

  /**
  * Get projectTopicsCollection
  * @return projectTopicsCollection
  **/
  @Schema(description = "")
  public List<ProjectTopics> getProjectTopicsCollection() {
    return projectTopicsCollection;
  }
  public void setProjectTopicsCollection(List<ProjectTopics> projectTopicsCollection) {
    this.projectTopicsCollection = projectTopicsCollection;
  }
  public SchemaTopics schemaTopicsPK(SchemaTopicsPK schemaTopicsPK) {
    this.schemaTopicsPK = schemaTopicsPK;
    return this;
  }

  

  /**
  * Get schemaTopicsPK
  * @return schemaTopicsPK
  **/
  @Schema(description = "")
  public SchemaTopicsPK getSchemaTopicsPK() {
    return schemaTopicsPK;
  }
  public void setSchemaTopicsPK(SchemaTopicsPK schemaTopicsPK) {
    this.schemaTopicsPK = schemaTopicsPK;
  }
  public SchemaTopics contents(String contents) {
    this.contents = contents;
    return this;
  }

  

  /**
  * Get contents
  * @return contents
  **/
  @Schema(required = true, description = "")
  public String getContents() {
    return contents;
  }
  public void setContents(String contents) {
    this.contents = contents;
  }
  public SchemaTopics createdOn(OffsetDateTime createdOn) {
    this.createdOn = createdOn;
    return this;
  }

  

  /**
  * Get createdOn
  * @return createdOn
  **/
  @Schema(required = true, description = "")
  public OffsetDateTime getCreatedOn() {
    return createdOn;
  }
  public void setCreatedOn(OffsetDateTime createdOn) {
    this.createdOn = createdOn;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SchemaTopics schemaTopics = (SchemaTopics) o;
    return Objects.equals(this.projectTopicsCollection, schemaTopics.projectTopicsCollection) &&
        Objects.equals(this.schemaTopicsPK, schemaTopics.schemaTopicsPK) &&
        Objects.equals(this.contents, schemaTopics.contents) &&
        Objects.equals(this.createdOn, schemaTopics.createdOn);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(projectTopicsCollection, schemaTopicsPK, contents, createdOn);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SchemaTopics {\n");
    
    sb.append("    projectTopicsCollection: ").append(toIndentedString(projectTopicsCollection)).append("\n");
    sb.append("    schemaTopicsPK: ").append(toIndentedString(schemaTopicsPK)).append("\n");
    sb.append("    contents: ").append(toIndentedString(contents)).append("\n");
    sb.append("    createdOn: ").append(toIndentedString(createdOn)).append("\n");
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