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
 * ConstraintResult
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class ConstraintResult {

  @SerializedName("check")
  private String check = null;
  /**
   * Gets or Sets checkLevel
   */
  @JsonAdapter(CheckLevelEnum.Adapter.class)
  public enum CheckLevelEnum {
    WARNING("Warning"),
    ERROR("Error");

    private String value;

    CheckLevelEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static CheckLevelEnum fromValue(String text) {
      for (CheckLevelEnum b : CheckLevelEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<CheckLevelEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CheckLevelEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CheckLevelEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return CheckLevelEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("checkLevel")
  private CheckLevelEnum checkLevel = null;
  /**
   * Gets or Sets checkStatus
   */
  @JsonAdapter(CheckStatusEnum.Adapter.class)
  public enum CheckStatusEnum {
    WARNING("Warning"),
    ERROR("Error");

    private String value;

    CheckStatusEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static CheckStatusEnum fromValue(String text) {
      for (CheckStatusEnum b : CheckStatusEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<CheckStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CheckStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CheckStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return CheckStatusEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("checkStatus")
  private CheckStatusEnum checkStatus = null;

  @SerializedName("constraint")
  private String constraint = null;
  /**
   * Gets or Sets constraintStatus
   */
  @JsonAdapter(ConstraintStatusEnum.Adapter.class)
  public enum ConstraintStatusEnum {
    SUCCESS("Success"),
    WARNING("Warning"),
    FAILURE("Failure"),
    EMPTY("Empty");

    private String value;

    ConstraintStatusEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static ConstraintStatusEnum fromValue(String text) {
      for (ConstraintStatusEnum b : ConstraintStatusEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<ConstraintStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ConstraintStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ConstraintStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return ConstraintStatusEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("constraintStatus")
  private ConstraintStatusEnum constraintStatus = null;

  @SerializedName("constraintMessage")
  private String constraintMessage = null;
  public ConstraintResult check(String check) {
    this.check = check;
    return this;
  }

  

  /**
  * Get check
  * @return check
  **/
  @Schema(description = "")
  public String getCheck() {
    return check;
  }
  public void setCheck(String check) {
    this.check = check;
  }
  public ConstraintResult checkLevel(CheckLevelEnum checkLevel) {
    this.checkLevel = checkLevel;
    return this;
  }

  

  /**
  * Get checkLevel
  * @return checkLevel
  **/
  @Schema(description = "")
  public CheckLevelEnum getCheckLevel() {
    return checkLevel;
  }
  public void setCheckLevel(CheckLevelEnum checkLevel) {
    this.checkLevel = checkLevel;
  }
  public ConstraintResult checkStatus(CheckStatusEnum checkStatus) {
    this.checkStatus = checkStatus;
    return this;
  }

  

  /**
  * Get checkStatus
  * @return checkStatus
  **/
  @Schema(description = "")
  public CheckStatusEnum getCheckStatus() {
    return checkStatus;
  }
  public void setCheckStatus(CheckStatusEnum checkStatus) {
    this.checkStatus = checkStatus;
  }
  public ConstraintResult constraint(String constraint) {
    this.constraint = constraint;
    return this;
  }

  

  /**
  * Get constraint
  * @return constraint
  **/
  @Schema(description = "")
  public String getConstraint() {
    return constraint;
  }
  public void setConstraint(String constraint) {
    this.constraint = constraint;
  }
  public ConstraintResult constraintStatus(ConstraintStatusEnum constraintStatus) {
    this.constraintStatus = constraintStatus;
    return this;
  }

  

  /**
  * Get constraintStatus
  * @return constraintStatus
  **/
  @Schema(description = "")
  public ConstraintStatusEnum getConstraintStatus() {
    return constraintStatus;
  }
  public void setConstraintStatus(ConstraintStatusEnum constraintStatus) {
    this.constraintStatus = constraintStatus;
  }
  public ConstraintResult constraintMessage(String constraintMessage) {
    this.constraintMessage = constraintMessage;
    return this;
  }

  

  /**
  * Get constraintMessage
  * @return constraintMessage
  **/
  @Schema(description = "")
  public String getConstraintMessage() {
    return constraintMessage;
  }
  public void setConstraintMessage(String constraintMessage) {
    this.constraintMessage = constraintMessage;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ConstraintResult constraintResult = (ConstraintResult) o;
    return Objects.equals(this.check, constraintResult.check) &&
        Objects.equals(this.checkLevel, constraintResult.checkLevel) &&
        Objects.equals(this.checkStatus, constraintResult.checkStatus) &&
        Objects.equals(this.constraint, constraintResult.constraint) &&
        Objects.equals(this.constraintStatus, constraintResult.constraintStatus) &&
        Objects.equals(this.constraintMessage, constraintResult.constraintMessage);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(check, checkLevel, checkStatus, constraint, constraintStatus, constraintMessage);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ConstraintResult {\n");
    
    sb.append("    check: ").append(toIndentedString(check)).append("\n");
    sb.append("    checkLevel: ").append(toIndentedString(checkLevel)).append("\n");
    sb.append("    checkStatus: ").append(toIndentedString(checkStatus)).append("\n");
    sb.append("    constraint: ").append(toIndentedString(constraint)).append("\n");
    sb.append("    constraintStatus: ").append(toIndentedString(constraintStatus)).append("\n");
    sb.append("    constraintMessage: ").append(toIndentedString(constraintMessage)).append("\n");
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