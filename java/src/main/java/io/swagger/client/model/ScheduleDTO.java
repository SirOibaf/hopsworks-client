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
 * ScheduleDTO
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class ScheduleDTO {

  @SerializedName("start")
  private Long start = null;

  @SerializedName("number")
  private Integer number = null;
  /**
   * Gets or Sets unit
   */
  @JsonAdapter(UnitEnum.Adapter.class)
  public enum UnitEnum {
    SECOND("SECOND"),
    MINUTE("MINUTE"),
    HOUR("HOUR"),
    DAY("DAY"),
    WEEK("WEEK"),
    MONTH("MONTH");

    private String value;

    UnitEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static UnitEnum fromValue(String text) {
      for (UnitEnum b : UnitEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<UnitEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final UnitEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public UnitEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return UnitEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("unit")
  private UnitEnum unit = null;
  public ScheduleDTO start(Long start) {
    this.start = start;
    return this;
  }

  

  /**
  * Get start
  * @return start
  **/
  @Schema(description = "")
  public Long getStart() {
    return start;
  }
  public void setStart(Long start) {
    this.start = start;
  }
  public ScheduleDTO number(Integer number) {
    this.number = number;
    return this;
  }

  

  /**
  * Get number
  * @return number
  **/
  @Schema(description = "")
  public Integer getNumber() {
    return number;
  }
  public void setNumber(Integer number) {
    this.number = number;
  }
  public ScheduleDTO unit(UnitEnum unit) {
    this.unit = unit;
    return this;
  }

  

  /**
  * Get unit
  * @return unit
  **/
  @Schema(description = "")
  public UnitEnum getUnit() {
    return unit;
  }
  public void setUnit(UnitEnum unit) {
    this.unit = unit;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ScheduleDTO scheduleDTO = (ScheduleDTO) o;
    return Objects.equals(this.start, scheduleDTO.start) &&
        Objects.equals(this.number, scheduleDTO.number) &&
        Objects.equals(this.unit, scheduleDTO.unit);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(start, number, unit);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ScheduleDTO {\n");
    
    sb.append("    start: ").append(toIndentedString(start)).append("\n");
    sb.append("    number: ").append(toIndentedString(number)).append("\n");
    sb.append("    unit: ").append(toIndentedString(unit)).append("\n");
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
