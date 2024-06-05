package com.millionvisions.mediafirewall.Model;

import lombok.Data;

@Data
public class AuthResponse {
    private String api_domain;
    private String access_token;
    private String token_type;
    private long expires_in;
}
