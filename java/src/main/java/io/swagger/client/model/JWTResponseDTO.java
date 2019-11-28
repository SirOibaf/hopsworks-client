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
import org.threeten.bp.OffsetDateTime;

/**
 * JWTResponseDTO
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-11-28T02:09:19.386+01:00[Europe/Stockholm]")public class JWTResponseDTO {

  @SerializedName("token")
  private String token = null;

  @SerializedName("expiresAt")
  private OffsetDateTime expiresAt = null;

  @SerializedName("nbf")
  private OffsetDateTime nbf = null;

  @SerializedName("expLeeway")
  private Integer expLeeway = null;
  public JWTResponseDTO token(String token) {
    this.token = token;
    return this;
  }

  

  /**
  * Get token
  * @return token
  **/
  @Schema(description = "")
  public String getToken() {
    return token;
  }
  public void setToken(String token) {
    this.token = token;
  }
  public JWTResponseDTO expiresAt(OffsetDateTime expiresAt) {
    this.expiresAt = expiresAt;
    return this;
  }

  

  /**
  * Get expiresAt
  * @return expiresAt
  **/
  @Schema(description = "")
  public OffsetDateTime getExpiresAt() {
    return expiresAt;
  }
  public void setExpiresAt(OffsetDateTime expiresAt) {
    this.expiresAt = expiresAt;
  }
  public JWTResponseDTO nbf(OffsetDateTime nbf) {
    this.nbf = nbf;
    return this;
  }

  

  /**
  * Get nbf
  * @return nbf
  **/
  @Schema(description = "")
  public OffsetDateTime getNbf() {
    return nbf;
  }
  public void setNbf(OffsetDateTime nbf) {
    this.nbf = nbf;
  }
  public JWTResponseDTO expLeeway(Integer expLeeway) {
    this.expLeeway = expLeeway;
    return this;
  }

  

  /**
  * Get expLeeway
  * @return expLeeway
  **/
  @Schema(description = "")
  public Integer getExpLeeway() {
    return expLeeway;
  }
  public void setExpLeeway(Integer expLeeway) {
    this.expLeeway = expLeeway;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    JWTResponseDTO jwTResponseDTO = (JWTResponseDTO) o;
    return Objects.equals(this.token, jwTResponseDTO.token) &&
        Objects.equals(this.expiresAt, jwTResponseDTO.expiresAt) &&
        Objects.equals(this.nbf, jwTResponseDTO.nbf) &&
        Objects.equals(this.expLeeway, jwTResponseDTO.expLeeway);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(token, expiresAt, nbf, expLeeway);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class JWTResponseDTO {\n");
    
    sb.append("    token: ").append(toIndentedString(token)).append("\n");
    sb.append("    expiresAt: ").append(toIndentedString(expiresAt)).append("\n");
    sb.append("    nbf: ").append(toIndentedString(nbf)).append("\n");
    sb.append("    expLeeway: ").append(toIndentedString(expLeeway)).append("\n");
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
