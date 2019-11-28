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
import io.swagger.client.model.LocalResourceDTO;
import io.swagger.client.model.YarnJobConfiguration;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.List;

/**
 * FlinkJobConfiguration
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class FlinkJobConfiguration extends YarnJobConfiguration {

  @SerializedName("jobManagerMemory")
  private Integer jobManagerMemory = null;

  @SerializedName("numberOfTaskManagers")
  private Integer numberOfTaskManagers = null;

  @SerializedName("numberOfTaskSlots")
  private Integer numberOfTaskSlots = null;

  @SerializedName("taskManagerMemory")
  private Integer taskManagerMemory = null;

  @SerializedName("properties")
  private String properties = null;
  public FlinkJobConfiguration jobManagerMemory(Integer jobManagerMemory) {
    this.jobManagerMemory = jobManagerMemory;
    return this;
  }

  

  /**
  * Get jobManagerMemory
  * @return jobManagerMemory
  **/
  @Schema(description = "")
  public Integer getJobManagerMemory() {
    return jobManagerMemory;
  }
  public void setJobManagerMemory(Integer jobManagerMemory) {
    this.jobManagerMemory = jobManagerMemory;
  }
  public FlinkJobConfiguration numberOfTaskManagers(Integer numberOfTaskManagers) {
    this.numberOfTaskManagers = numberOfTaskManagers;
    return this;
  }

  

  /**
  * Get numberOfTaskManagers
  * @return numberOfTaskManagers
  **/
  @Schema(description = "")
  public Integer getNumberOfTaskManagers() {
    return numberOfTaskManagers;
  }
  public void setNumberOfTaskManagers(Integer numberOfTaskManagers) {
    this.numberOfTaskManagers = numberOfTaskManagers;
  }
  public FlinkJobConfiguration numberOfTaskSlots(Integer numberOfTaskSlots) {
    this.numberOfTaskSlots = numberOfTaskSlots;
    return this;
  }

  

  /**
  * Get numberOfTaskSlots
  * @return numberOfTaskSlots
  **/
  @Schema(description = "")
  public Integer getNumberOfTaskSlots() {
    return numberOfTaskSlots;
  }
  public void setNumberOfTaskSlots(Integer numberOfTaskSlots) {
    this.numberOfTaskSlots = numberOfTaskSlots;
  }
  public FlinkJobConfiguration taskManagerMemory(Integer taskManagerMemory) {
    this.taskManagerMemory = taskManagerMemory;
    return this;
  }

  

  /**
  * Get taskManagerMemory
  * @return taskManagerMemory
  **/
  @Schema(description = "")
  public Integer getTaskManagerMemory() {
    return taskManagerMemory;
  }
  public void setTaskManagerMemory(Integer taskManagerMemory) {
    this.taskManagerMemory = taskManagerMemory;
  }
  public FlinkJobConfiguration properties(String properties) {
    this.properties = properties;
    return this;
  }

  

  /**
  * Get properties
  * @return properties
  **/
  @Schema(description = "")
  public String getProperties() {
    return properties;
  }
  public void setProperties(String properties) {
    this.properties = properties;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FlinkJobConfiguration flinkJobConfiguration = (FlinkJobConfiguration) o;
    return Objects.equals(this.jobManagerMemory, flinkJobConfiguration.jobManagerMemory) &&
        Objects.equals(this.numberOfTaskManagers, flinkJobConfiguration.numberOfTaskManagers) &&
        Objects.equals(this.numberOfTaskSlots, flinkJobConfiguration.numberOfTaskSlots) &&
        Objects.equals(this.taskManagerMemory, flinkJobConfiguration.taskManagerMemory) &&
        Objects.equals(this.properties, flinkJobConfiguration.properties) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(jobManagerMemory, numberOfTaskManagers, numberOfTaskSlots, taskManagerMemory, properties, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FlinkJobConfiguration {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    jobManagerMemory: ").append(toIndentedString(jobManagerMemory)).append("\n");
    sb.append("    numberOfTaskManagers: ").append(toIndentedString(numberOfTaskManagers)).append("\n");
    sb.append("    numberOfTaskSlots: ").append(toIndentedString(numberOfTaskSlots)).append("\n");
    sb.append("    taskManagerMemory: ").append(toIndentedString(taskManagerMemory)).append("\n");
    sb.append("    properties: ").append(toIndentedString(properties)).append("\n");
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