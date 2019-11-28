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
import io.swagger.client.model.TopicDTO;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * TopicDTO
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class TopicDTO {

  @SerializedName("href")
  private String href = null;

  @SerializedName("items")
  private List<TopicDTO> items = null;

  @SerializedName("count")
  private Long count = null;

  @SerializedName("name")
  private String name = null;

  @SerializedName("numOfReplicas")
  private Integer numOfReplicas = null;

  @SerializedName("numOfPartitions")
  private Integer numOfPartitions = null;

  @SerializedName("schemaName")
  private String schemaName = null;

  @SerializedName("schemaVersion")
  private Integer schemaVersion = null;

  @SerializedName("ownerProjectId")
  private Integer ownerProjectId = null;

  @SerializedName("shared")
  private Boolean shared = null;
  public TopicDTO href(String href) {
    this.href = href;
    return this;
  }

  

  /**
  * Get href
  * @return href
  **/
  @Schema(description = "")
  public String getHref() {
    return href;
  }
  public void setHref(String href) {
    this.href = href;
  }
  public TopicDTO items(List<TopicDTO> items) {
    this.items = items;
    return this;
  }

  public TopicDTO addItemsItem(TopicDTO itemsItem) {
    if (this.items == null) {
      this.items = new ArrayList<TopicDTO>();
    }
    this.items.add(itemsItem);
    return this;
  }

  /**
  * Get items
  * @return items
  **/
  @Schema(description = "")
  public List<TopicDTO> getItems() {
    return items;
  }
  public void setItems(List<TopicDTO> items) {
    this.items = items;
  }
  public TopicDTO count(Long count) {
    this.count = count;
    return this;
  }

  

  /**
  * Get count
  * @return count
  **/
  @Schema(description = "")
  public Long getCount() {
    return count;
  }
  public void setCount(Long count) {
    this.count = count;
  }
  public TopicDTO name(String name) {
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
  public TopicDTO numOfReplicas(Integer numOfReplicas) {
    this.numOfReplicas = numOfReplicas;
    return this;
  }

  

  /**
  * Get numOfReplicas
  * @return numOfReplicas
  **/
  @Schema(description = "")
  public Integer getNumOfReplicas() {
    return numOfReplicas;
  }
  public void setNumOfReplicas(Integer numOfReplicas) {
    this.numOfReplicas = numOfReplicas;
  }
  public TopicDTO numOfPartitions(Integer numOfPartitions) {
    this.numOfPartitions = numOfPartitions;
    return this;
  }

  

  /**
  * Get numOfPartitions
  * @return numOfPartitions
  **/
  @Schema(description = "")
  public Integer getNumOfPartitions() {
    return numOfPartitions;
  }
  public void setNumOfPartitions(Integer numOfPartitions) {
    this.numOfPartitions = numOfPartitions;
  }
  public TopicDTO schemaName(String schemaName) {
    this.schemaName = schemaName;
    return this;
  }

  

  /**
  * Get schemaName
  * @return schemaName
  **/
  @Schema(description = "")
  public String getSchemaName() {
    return schemaName;
  }
  public void setSchemaName(String schemaName) {
    this.schemaName = schemaName;
  }
  public TopicDTO schemaVersion(Integer schemaVersion) {
    this.schemaVersion = schemaVersion;
    return this;
  }

  

  /**
  * Get schemaVersion
  * @return schemaVersion
  **/
  @Schema(description = "")
  public Integer getSchemaVersion() {
    return schemaVersion;
  }
  public void setSchemaVersion(Integer schemaVersion) {
    this.schemaVersion = schemaVersion;
  }
  public TopicDTO ownerProjectId(Integer ownerProjectId) {
    this.ownerProjectId = ownerProjectId;
    return this;
  }

  

  /**
  * Get ownerProjectId
  * @return ownerProjectId
  **/
  @Schema(description = "")
  public Integer getOwnerProjectId() {
    return ownerProjectId;
  }
  public void setOwnerProjectId(Integer ownerProjectId) {
    this.ownerProjectId = ownerProjectId;
  }
  public TopicDTO shared(Boolean shared) {
    this.shared = shared;
    return this;
  }

  

  /**
  * Get shared
  * @return shared
  **/
  @Schema(description = "")
  public Boolean isShared() {
    return shared;
  }
  public void setShared(Boolean shared) {
    this.shared = shared;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TopicDTO topicDTO = (TopicDTO) o;
    return Objects.equals(this.href, topicDTO.href) &&
        Objects.equals(this.items, topicDTO.items) &&
        Objects.equals(this.count, topicDTO.count) &&
        Objects.equals(this.name, topicDTO.name) &&
        Objects.equals(this.numOfReplicas, topicDTO.numOfReplicas) &&
        Objects.equals(this.numOfPartitions, topicDTO.numOfPartitions) &&
        Objects.equals(this.schemaName, topicDTO.schemaName) &&
        Objects.equals(this.schemaVersion, topicDTO.schemaVersion) &&
        Objects.equals(this.ownerProjectId, topicDTO.ownerProjectId) &&
        Objects.equals(this.shared, topicDTO.shared);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(href, items, count, name, numOfReplicas, numOfPartitions, schemaName, schemaVersion, ownerProjectId, shared);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TopicDTO {\n");
    
    sb.append("    href: ").append(toIndentedString(href)).append("\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
    sb.append("    count: ").append(toIndentedString(count)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    numOfReplicas: ").append(toIndentedString(numOfReplicas)).append("\n");
    sb.append("    numOfPartitions: ").append(toIndentedString(numOfPartitions)).append("\n");
    sb.append("    schemaName: ").append(toIndentedString(schemaName)).append("\n");
    sb.append("    schemaVersion: ").append(toIndentedString(schemaVersion)).append("\n");
    sb.append("    ownerProjectId: ").append(toIndentedString(ownerProjectId)).append("\n");
    sb.append("    shared: ").append(toIndentedString(shared)).append("\n");
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
