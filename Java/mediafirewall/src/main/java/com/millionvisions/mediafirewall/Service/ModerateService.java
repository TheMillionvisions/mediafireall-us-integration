package com.millionvisions.mediafirewall.Service;


import com.millionvisions.mediafirewall.Model.AuthResponse;

public interface ModerateService {

    String urlRequest(String userId, String apikey,String mediaUrl,String filters);
    AuthResponse getAccessToken(String userId, String apikey);
}
