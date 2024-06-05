package com.millionvisions.mediafirewall.Service;

import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.millionvisions.mediafirewall.Model.AuthResponse;
import com.millionvisions.mediafirewall.Model.Media;
import com.millionvisions.mediafirewall.Model.WebhookConfiguration;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.util.UriComponentsBuilder;

import java.net.URI;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

@Service
public class WebhookIntegration {
    AuthResponse authResponse;
    public Media urlRequest(String userId, String apikey, String mediaUrl, String filters){
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
        return result.getBody();
    }
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
    //webhook payload response
    public void webhookEventTriggered(String payload){
        JsonObject jsonObject = JsonParser.parseString(payload).getAsJsonObject();
        // Extract the subscribe URL field
        if (jsonObject.has("SubscribeURL")) {
            String subscribeUrl = jsonObject.get("SubscribeURL").getAsString();
            RestTemplate restTemplate = new RestTemplate();
            ResponseEntity<String> response = restTemplate.getForEntity(subscribeUrl, String.class);
        }else {
            System.out.println(jsonObject.get("Message"));
        }
    }


    public void sendPostRequest(WebhookConfiguration webhookConfig, String url,String accessToken) {
        // Create RestTemplate instance
        RestTemplate restTemplate = new RestTemplate();
        // Set headers
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        headers.set("Authorization", "Bearer " + accessToken);
        // Create request entity with JSON payload and headers
        HttpEntity<WebhookConfiguration> requestEntity = new HttpEntity<>(webhookConfig, headers);

        // Send POST request
        ResponseEntity<String> response = restTemplate.exchange(
                url,
                HttpMethod.POST,
                requestEntity,
                String.class
        );

        // Handle response
        HttpStatusCode statusCode = response.getStatusCode();
        if (statusCode == HttpStatus.OK) {
            System.out.println("Request successful");
            System.out.println("Response body: " + response.getBody());
        } else {
            System.out.println("Request failed with status code: " + statusCode);
        }
    }

    public static void main(String[] args) {
        // Example JSON payload
        String userId = "example@email.com";
        String apikey = ""; //you can find the apikey in https://mediafirewall.ai website account section
        List<String> webhooks = Arrays.asList("https://example.com/webhook","https://example1.com/webhook");
        WebhookConfiguration webhookConfig = new WebhookConfiguration(userId, webhooks);
        //URL
        String url = "https://apimediafirewall-us.millionvisions.ai/notification/webhook?apikey=" + apikey;

        // Send POST request
        WebhookIntegration restClient = new WebhookIntegration();
        AuthResponse auth = restClient.getAccessToken(userId,apikey);
        restClient.sendPostRequest(webhookConfig, url,auth.getAccess_token());
    }
}
