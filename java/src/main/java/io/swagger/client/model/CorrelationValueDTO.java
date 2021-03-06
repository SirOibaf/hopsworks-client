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
 * CorrelationValueDTO
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class CorrelationValueDTO {

  @SerializedName("featureName")
  private String featureName = null;

  @SerializedName("correlation")
  private Float correlation = null;
  /**
   * Gets or Sets statisticType
   */
  @JsonAdapter(StatisticTypeEnum.Adapter.class)
  public enum StatisticTypeEnum {
    DESCRIPTIVESTATISTICS("DESCRIPTIVESTATISTICS"),
    CLUSTERANALYSIS("CLUSTERANALYSIS"),
    FEATUREDISTRIBUTIONS("FEATUREDISTRIBUTIONS"),
    FEATURECORRELATIONS("FEATURECORRELATIONS");

    private String value;

    StatisticTypeEnum(String value) {
      this.value = value;
    }
    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }
    public static StatisticTypeEnum fromValue(String text) {
      for (StatisticTypeEnum b : StatisticTypeEnum.values()) {
        if (String.valueOf(b.value).equals(text)) {
          return b;
        }
      }
      return null;
    }
    public static class Adapter extends TypeAdapter<StatisticTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatisticTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatisticTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value = jsonReader.nextString();
        return StatisticTypeEnum.fromValue(String.valueOf(value));
      }
    }
  }
  @SerializedName("statisticType")
  private StatisticTypeEnum statisticType = null;
  public CorrelationValueDTO featureName(String featureName) {
    this.featureName = featureName;
    return this;
  }

  

  /**
  * Get featureName
  * @return featureName
  **/
  @Schema(description = "")
  public String getFeatureName() {
    return featureName;
  }
  public void setFeatureName(String featureName) {
    this.featureName = featureName;
  }
  public CorrelationValueDTO correlation(Float correlation) {
    this.correlation = correlation;
    return this;
  }

  

  /**
  * Get correlation
  * @return correlation
  **/
  @Schema(description = "")
  public Float getCorrelation() {
    return correlation;
  }
  public void setCorrelation(Float correlation) {
    this.correlation = correlation;
  }
  public CorrelationValueDTO statisticType(StatisticTypeEnum statisticType) {
    this.statisticType = statisticType;
    return this;
  }

  

  /**
  * Get statisticType
  * @return statisticType
  **/
  @Schema(description = "")
  public StatisticTypeEnum getStatisticType() {
    return statisticType;
  }
  public void setStatisticType(StatisticTypeEnum statisticType) {
    this.statisticType = statisticType;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CorrelationValueDTO correlationValueDTO = (CorrelationValueDTO) o;
    return Objects.equals(this.featureName, correlationValueDTO.featureName) &&
        Objects.equals(this.correlation, correlationValueDTO.correlation) &&
        Objects.equals(this.statisticType, correlationValueDTO.statisticType);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(featureName, correlation, statisticType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CorrelationValueDTO {\n");
    
    sb.append("    featureName: ").append(toIndentedString(featureName)).append("\n");
    sb.append("    correlation: ").append(toIndentedString(correlation)).append("\n");
    sb.append("    statisticType: ").append(toIndentedString(statisticType)).append("\n");
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
