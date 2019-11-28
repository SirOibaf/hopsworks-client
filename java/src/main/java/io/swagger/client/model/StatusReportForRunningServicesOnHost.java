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

/**
 * StatusReportForRunningServicesOnHost
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class StatusReportForRunningServicesOnHost {

  @SerializedName("service")
  private String service = null;

  @SerializedName("group")
  private String group = null;

  @SerializedName("pid")
  private Integer pid = null;
  /**
   * Current status of the service
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    STARTED("Started"),
    STOPPED("Stopped"),
    FAILED("Failed"),
    TIMEDOUT("TimedOut"),
    NONE("None");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static StatusEnum fromValue(String text) {
      for (StatusEnum b : StatusEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return StatusEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("status")
  private StatusEnum status = null;
  public StatusReportForRunningServicesOnHost service(String service) {
    this.service = service;
    return this;
  }

  

  /**
  * Service name
  * @return service
  **/
  @Schema(required = true, description = "Service name")
  public String getService() {
    return service;
  }
  public void setService(String service) {
    this.service = service;
  }
  public StatusReportForRunningServicesOnHost group(String group) {
    this.group = group;
    return this;
  }

  

  /**
  * Name of the group service belongs to
  * @return group
  **/
  @Schema(required = true, description = "Name of the group service belongs to")
  public String getGroup() {
    return group;
  }
  public void setGroup(String group) {
    this.group = group;
  }
  public StatusReportForRunningServicesOnHost pid(Integer pid) {
    this.pid = pid;
    return this;
  }

  

  /**
  * Process ID
  * @return pid
  **/
  @Schema(required = true, description = "Process ID")
  public Integer getPid() {
    return pid;
  }
  public void setPid(Integer pid) {
    this.pid = pid;
  }
  public StatusReportForRunningServicesOnHost status(StatusEnum status) {
    this.status = status;
    return this;
  }

  

  /**
  * Current status of the service
  * @return status
  **/
  @Schema(description = "Current status of the service")
  public StatusEnum getStatus() {
    return status;
  }
  public void setStatus(StatusEnum status) {
    this.status = status;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    StatusReportForRunningServicesOnHost statusReportForRunningServicesOnHost = (StatusReportForRunningServicesOnHost) o;
    return Objects.equals(this.service, statusReportForRunningServicesOnHost.service) &&
        Objects.equals(this.group, statusReportForRunningServicesOnHost.group) &&
        Objects.equals(this.pid, statusReportForRunningServicesOnHost.pid) &&
        Objects.equals(this.status, statusReportForRunningServicesOnHost.status);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(service, group, pid, status);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class StatusReportForRunningServicesOnHost {\n");
    
    sb.append("    service: ").append(toIndentedString(service)).append("\n");
    sb.append("    group: ").append(toIndentedString(group)).append("\n");
    sb.append("    pid: ").append(toIndentedString(pid)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
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