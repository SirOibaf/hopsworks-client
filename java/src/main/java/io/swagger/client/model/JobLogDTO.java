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
 * JobLogDTO
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class JobLogDTO {

  @SerializedName("log")
  private String log = null;

  @SerializedName("path")
  private String path = null;
  /**
   * Gets or Sets type
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    OUT("OUT"),
    ERR("ERR");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static TypeEnum fromValue(String text) {
      for (TypeEnum b : TypeEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return TypeEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("type")
  private TypeEnum type = null;
  /**
   * Gets or Sets retriable
   */
  @JsonAdapter(RetriableEnum.Adapter.class)
  public enum RetriableEnum {
    RETRIEABLE_OUT("RETRIEABLE_OUT"),
    RETRIABLE_ERR("RETRIABLE_ERR");

    private String value;

    RetriableEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static RetriableEnum fromValue(String text) {
      for (RetriableEnum b : RetriableEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<RetriableEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RetriableEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RetriableEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return RetriableEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("retriable")
  private RetriableEnum retriable = null;
  public JobLogDTO log(String log) {
    this.log = log;
    return this;
  }

  

  /**
  * Get log
  * @return log
  **/
  @Schema(description = "")
  public String getLog() {
    return log;
  }
  public void setLog(String log) {
    this.log = log;
  }
  public JobLogDTO path(String path) {
    this.path = path;
    return this;
  }

  

  /**
  * Get path
  * @return path
  **/
  @Schema(description = "")
  public String getPath() {
    return path;
  }
  public void setPath(String path) {
    this.path = path;
  }
  public JobLogDTO type(TypeEnum type) {
    this.type = type;
    return this;
  }

  

  /**
  * Get type
  * @return type
  **/
  @Schema(description = "")
  public TypeEnum getType() {
    return type;
  }
  public void setType(TypeEnum type) {
    this.type = type;
  }
  public JobLogDTO retriable(RetriableEnum retriable) {
    this.retriable = retriable;
    return this;
  }

  

  /**
  * Get retriable
  * @return retriable
  **/
  @Schema(description = "")
  public RetriableEnum getRetriable() {
    return retriable;
  }
  public void setRetriable(RetriableEnum retriable) {
    this.retriable = retriable;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    JobLogDTO jobLogDTO = (JobLogDTO) o;
    return Objects.equals(this.log, jobLogDTO.log) &&
        Objects.equals(this.path, jobLogDTO.path) &&
        Objects.equals(this.type, jobLogDTO.type) &&
        Objects.equals(this.retriable, jobLogDTO.retriable);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(log, path, type, retriable);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class JobLogDTO {\n");
    
    sb.append("    log: ").append(toIndentedString(log)).append("\n");
    sb.append("    path: ").append(toIndentedString(path)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    retriable: ").append(toIndentedString(retriable)).append("\n");
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
