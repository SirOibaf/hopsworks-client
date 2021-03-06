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
import io.swagger.client.model.Hosts;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;

/**
 * HostServices
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class HostServices {

  @SerializedName("id")
  private Long id = null;

  @SerializedName("pid")
  private Integer pid = null;

  @SerializedName("group")
  private String group = null;

  @SerializedName("service")
  private String service = null;
  /**
   * Gets or Sets status
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

  @SerializedName("uptime")
  private Long uptime = null;

  @SerializedName("startTime")
  private Long startTime = null;

  @SerializedName("stopTime")
  private Long stopTime = null;

  @SerializedName("host")
  private Hosts host = null;
  /**
   * Gets or Sets health
   */
  @JsonAdapter(HealthEnum.Adapter.class)
  public enum HealthEnum {
    GOOD("Good"),
    BAD("Bad");

    private String value;

    HealthEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static HealthEnum fromValue(String text) {
      for (HealthEnum b : HealthEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<HealthEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final HealthEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public HealthEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return HealthEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("health")
  private HealthEnum health = null;
  public HostServices id(Long id) {
    this.id = id;
    return this;
  }

  

  /**
  * Get id
  * @return id
  **/
  @Schema(description = "")
  public Long getId() {
    return id;
  }
  public void setId(Long id) {
    this.id = id;
  }
  public HostServices pid(Integer pid) {
    this.pid = pid;
    return this;
  }

  

  /**
  * Get pid
  * @return pid
  **/
  @Schema(description = "")
  public Integer getPid() {
    return pid;
  }
  public void setPid(Integer pid) {
    this.pid = pid;
  }
  public HostServices group(String group) {
    this.group = group;
    return this;
  }

  

  /**
  * Get group
  * @return group
  **/
  @Schema(required = true, description = "")
  public String getGroup() {
    return group;
  }
  public void setGroup(String group) {
    this.group = group;
  }
  public HostServices service(String service) {
    this.service = service;
    return this;
  }

  

  /**
  * Get service
  * @return service
  **/
  @Schema(required = true, description = "")
  public String getService() {
    return service;
  }
  public void setService(String service) {
    this.service = service;
  }
  public HostServices status(StatusEnum status) {
    this.status = status;
    return this;
  }

  

  /**
  * Get status
  * @return status
  **/
  @Schema(required = true, description = "")
  public StatusEnum getStatus() {
    return status;
  }
  public void setStatus(StatusEnum status) {
    this.status = status;
  }
  public HostServices uptime(Long uptime) {
    this.uptime = uptime;
    return this;
  }

  

  /**
  * Get uptime
  * @return uptime
  **/
  @Schema(description = "")
  public Long getUptime() {
    return uptime;
  }
  public void setUptime(Long uptime) {
    this.uptime = uptime;
  }
  public HostServices startTime(Long startTime) {
    this.startTime = startTime;
    return this;
  }

  

  /**
  * Get startTime
  * @return startTime
  **/
  @Schema(description = "")
  public Long getStartTime() {
    return startTime;
  }
  public void setStartTime(Long startTime) {
    this.startTime = startTime;
  }
  public HostServices stopTime(Long stopTime) {
    this.stopTime = stopTime;
    return this;
  }

  

  /**
  * Get stopTime
  * @return stopTime
  **/
  @Schema(description = "")
  public Long getStopTime() {
    return stopTime;
  }
  public void setStopTime(Long stopTime) {
    this.stopTime = stopTime;
  }
  public HostServices host(Hosts host) {
    this.host = host;
    return this;
  }

  

  /**
  * Get host
  * @return host
  **/
  @Schema(description = "")
  public Hosts getHost() {
    return host;
  }
  public void setHost(Hosts host) {
    this.host = host;
  }
  public HostServices health(HealthEnum health) {
    this.health = health;
    return this;
  }

  

  /**
  * Get health
  * @return health
  **/
  @Schema(description = "")
  public HealthEnum getHealth() {
    return health;
  }
  public void setHealth(HealthEnum health) {
    this.health = health;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    HostServices hostServices = (HostServices) o;
    return Objects.equals(this.id, hostServices.id) &&
        Objects.equals(this.pid, hostServices.pid) &&
        Objects.equals(this.group, hostServices.group) &&
        Objects.equals(this.service, hostServices.service) &&
        Objects.equals(this.status, hostServices.status) &&
        Objects.equals(this.uptime, hostServices.uptime) &&
        Objects.equals(this.startTime, hostServices.startTime) &&
        Objects.equals(this.stopTime, hostServices.stopTime) &&
        Objects.equals(this.host, hostServices.host) &&
        Objects.equals(this.health, hostServices.health);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(id, pid, group, service, status, uptime, startTime, stopTime, host, health);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HostServices {\n");
    
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    pid: ").append(toIndentedString(pid)).append("\n");
    sb.append("    group: ").append(toIndentedString(group)).append("\n");
    sb.append("    service: ").append(toIndentedString(service)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    uptime: ").append(toIndentedString(uptime)).append("\n");
    sb.append("    startTime: ").append(toIndentedString(startTime)).append("\n");
    sb.append("    stopTime: ").append(toIndentedString(stopTime)).append("\n");
    sb.append("    host: ").append(toIndentedString(host)).append("\n");
    sb.append("    health: ").append(toIndentedString(health)).append("\n");
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
