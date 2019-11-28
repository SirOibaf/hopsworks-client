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
 * TopicsSortBy
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class TopicsSortBy {
  /**
   * Gets or Sets param
   */
  @JsonAdapter(ParamEnum.Adapter.class)
  public enum ParamEnum {
    ASC("ASC"),
    DESC("DESC");

    private String value;

    ParamEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static ParamEnum fromValue(String text) {
      for (ParamEnum b : ParamEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<ParamEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ParamEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ParamEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return ParamEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("param")
  private ParamEnum param = null;

  @SerializedName("sql")
  private String sql = null;

  @SerializedName("value")
  private String value = null;
  public TopicsSortBy param(ParamEnum param) {
    this.param = param;
    return this;
  }

  

  /**
  * Get param
  * @return param
  **/
  @Schema(description = "")
  public ParamEnum getParam() {
    return param;
  }
  public void setParam(ParamEnum param) {
    this.param = param;
  }
  public TopicsSortBy sql(String sql) {
    this.sql = sql;
    return this;
  }

  

  /**
  * Get sql
  * @return sql
  **/
  @Schema(description = "")
  public String getSql() {
    return sql;
  }
  public void setSql(String sql) {
    this.sql = sql;
  }
  public TopicsSortBy value(String value) {
    this.value = value;
    return this;
  }

  

  /**
  * Get value
  * @return value
  **/
  @Schema(description = "")
  public String getValue() {
    return value;
  }
  public void setValue(String value) {
    this.value = value;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TopicsSortBy topicsSortBy = (TopicsSortBy) o;
    return Objects.equals(this.param, topicsSortBy.param) &&
        Objects.equals(this.sql, topicsSortBy.sql) &&
        Objects.equals(this.value, topicsSortBy.value);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(param, sql, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TopicsSortBy {\n");
    
    sb.append("    param: ").append(toIndentedString(param)).append("\n");
    sb.append("    sql: ").append(toIndentedString(sql)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
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
