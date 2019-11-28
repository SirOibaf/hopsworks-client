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
 * HistogramBinDTO
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class HistogramBinDTO {

  @SerializedName("bin")
  private String bin = null;

  @SerializedName("frequency")
  private Integer frequency = null;
  public HistogramBinDTO bin(String bin) {
    this.bin = bin;
    return this;
  }

  

  /**
  * Get bin
  * @return bin
  **/
  @Schema(description = "")
  public String getBin() {
    return bin;
  }
  public void setBin(String bin) {
    this.bin = bin;
  }
  public HistogramBinDTO frequency(Integer frequency) {
    this.frequency = frequency;
    return this;
  }

  

  /**
  * Get frequency
  * @return frequency
  **/
  @Schema(description = "")
  public Integer getFrequency() {
    return frequency;
  }
  public void setFrequency(Integer frequency) {
    this.frequency = frequency;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    HistogramBinDTO histogramBinDTO = (HistogramBinDTO) o;
    return Objects.equals(this.bin, histogramBinDTO.bin) &&
        Objects.equals(this.frequency, histogramBinDTO.frequency);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(bin, frequency);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HistogramBinDTO {\n");
    
    sb.append("    bin: ").append(toIndentedString(bin)).append("\n");
    sb.append("    frequency: ").append(toIndentedString(frequency)).append("\n");
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
