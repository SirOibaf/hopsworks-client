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
 * SystemCommandsForKagentToExecuteOrReport
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class SystemCommandsForKagentToExecuteOrReport {
  /**
   * Operation to be performed
   */
  @JsonAdapter(OpEnum.Adapter.class)
  public enum OpEnum {
    SERVICE_KEY_ROTATION("SERVICE_KEY_ROTATION"),
    CONDA_GC("CONDA_GC");

    private String value;

    OpEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static OpEnum fromValue(String text) {
      for (OpEnum b : OpEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<OpEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final OpEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public OpEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return OpEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("op")
  private OpEnum op = null;
  /**
   * Status of command
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    NEW("NEW"),
    ONGOING("ONGOING"),
    FINISHED("FINISHED"),
    FAILED("FAILED");

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

  @SerializedName("id")
  private Integer id = null;

  @SerializedName("arguments")
  private String arguments = null;

  @SerializedName("priority")
  private Integer priority = null;

  @SerializedName("execUser")
  private String execUser = null;
  public SystemCommandsForKagentToExecuteOrReport op(OpEnum op) {
    this.op = op;
    return this;
  }

  

  /**
  * Operation to be performed
  * @return op
  **/
  @Schema(required = true, description = "Operation to be performed")
  public OpEnum getOp() {
    return op;
  }
  public void setOp(OpEnum op) {
    this.op = op;
  }
  public SystemCommandsForKagentToExecuteOrReport status(StatusEnum status) {
    this.status = status;
    return this;
  }

  

  /**
  * Status of command
  * @return status
  **/
  @Schema(required = true, description = "Status of command")
  public StatusEnum getStatus() {
    return status;
  }
  public void setStatus(StatusEnum status) {
    this.status = status;
  }
  public SystemCommandsForKagentToExecuteOrReport id(Integer id) {
    this.id = id;
    return this;
  }

  

  /**
  * ID of command
  * @return id
  **/
  @Schema(required = true, description = "ID of command")
  public Integer getId() {
    return id;
  }
  public void setId(Integer id) {
    this.id = id;
  }
  public SystemCommandsForKagentToExecuteOrReport arguments(String arguments) {
    this.arguments = arguments;
    return this;
  }

  

  /**
  * Arguments passed to command
  * @return arguments
  **/
  @Schema(description = "Arguments passed to command")
  public String getArguments() {
    return arguments;
  }
  public void setArguments(String arguments) {
    this.arguments = arguments;
  }
  public SystemCommandsForKagentToExecuteOrReport priority(Integer priority) {
    this.priority = priority;
    return this;
  }

  

  /**
  * Priority the command will run, 0 is the lowest priority
  * @return priority
  **/
  @Schema(description = "Priority the command will run, 0 is the lowest priority")
  public Integer getPriority() {
    return priority;
  }
  public void setPriority(Integer priority) {
    this.priority = priority;
  }
  public SystemCommandsForKagentToExecuteOrReport execUser(String execUser) {
    this.execUser = execUser;
    return this;
  }

  

  /**
  * The user command will be executed
  * @return execUser
  **/
  @Schema(description = "The user command will be executed")
  public String getExecUser() {
    return execUser;
  }
  public void setExecUser(String execUser) {
    this.execUser = execUser;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SystemCommandsForKagentToExecuteOrReport systemCommandsForKagentToExecuteOrReport = (SystemCommandsForKagentToExecuteOrReport) o;
    return Objects.equals(this.op, systemCommandsForKagentToExecuteOrReport.op) &&
        Objects.equals(this.status, systemCommandsForKagentToExecuteOrReport.status) &&
        Objects.equals(this.id, systemCommandsForKagentToExecuteOrReport.id) &&
        Objects.equals(this.arguments, systemCommandsForKagentToExecuteOrReport.arguments) &&
        Objects.equals(this.priority, systemCommandsForKagentToExecuteOrReport.priority) &&
        Objects.equals(this.execUser, systemCommandsForKagentToExecuteOrReport.execUser);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(op, status, id, arguments, priority, execUser);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SystemCommandsForKagentToExecuteOrReport {\n");
    
    sb.append("    op: ").append(toIndentedString(op)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    arguments: ").append(toIndentedString(arguments)).append("\n");
    sb.append("    priority: ").append(toIndentedString(priority)).append("\n");
    sb.append("    execUser: ").append(toIndentedString(execUser)).append("\n");
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
