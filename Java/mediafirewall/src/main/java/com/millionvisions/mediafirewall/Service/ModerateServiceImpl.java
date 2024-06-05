package com.millionvisions.mediafirewall.Service;

import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.millionvisions.mediafirewall.Model.AuthResponse;
import com.millionvisions.mediafirewall.Model.Media;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.util.UriComponentsBuilder;

import java.net.URI;
import java.util.Objects;

@Service
public class ModerateServiceImpl implements ModerateService{

    AuthResponse authResponse;

    @Override
    public String urlRequest(String userId, String apikey, String mediaUrl, String filters){
        authResponse = getAccessToken(userId,apikey);
        RestTemplate restTemplate = new RestTemplate();
        String baseUrl = authResponse.getApi_domain() + "/mfw/media/" + userId + "/url/filters";
        UriComponentsBuilder uriBuilder = UriComponentsBuilder.fromUriString(baseUrl)
                .queryParam("filters", filters)
                .queryParam("apikey", apikey)
                .queryParam("mediaUrl", mediaUrl);
        HttpHeaders headers = new HttpHeaders();
        headers.set("Authorization", "Bearer " + authResponse.getAccess_token());
        HttpEntity<?> requestEntity = new HttpEntity<>(headers);
        URI uri = uriBuilder.build().toUri();

        ResponseEntity<Media> result = restTemplate.postForEntity(uri, requestEntity, Media.class);

        return checkResults(Objects.requireNonNull(result.getBody()),userId,apikey);
    }
    public String checkResults(Media media,String userId, String apikey){
        JsonObject jsonObject = results(media,userId,apikey);
        while (!jsonObject.getAsJsonObject("processStatus").get("complete").getAsBoolean()) {
                jsonObject = results(media,userId,apikey);
        }
        return jsonObject.toString();
    }

    public JsonObject results(Media media,String userId, String apikey){
        RestTemplate restTemplate = new RestTemplate();
        String uri = "https://apimediafirewall-us.millionvisions.ai"+"/mfw/model/config/" + userId + "/" + media.getVideoId() + "?apikey=" + apikey;

        HttpHeaders headers = new HttpHeaders();
        headers.set("Authorization", "Bearer " + authResponse.getAccess_token());
        HttpEntity<?> requestEntity = new HttpEntity<>(headers);
        ResponseEntity<String> result = restTemplate.exchange(uri, HttpMethod.GET, requestEntity, String.class);
        return JsonParser.parseString(Objects.requireNonNull(result.getBody())).getAsJsonObject();
    }
    @Override
    public AuthResponse getAccessToken(String userId, String apikey) {
        String url = "https://apimediafirewall-us.millionvisions.ai/oauth/token";
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.MULTIPART_FORM_DATA);

        MultiValueMap<String, Object> body = new LinkedMultiValueMap<>();
        body.add("userId", userId);
        body.add("apiKey", apikey);

        HttpEntity<MultiValueMap<String, Object>> requestEntity = new HttpEntity<>(body, headers);
        ResponseEntity<AuthResponse> result = restTemplate.postForEntity(url,requestEntity,AuthResponse.class);
        System.out.println(result.getBody());
        return result.getBody();
    }
}
