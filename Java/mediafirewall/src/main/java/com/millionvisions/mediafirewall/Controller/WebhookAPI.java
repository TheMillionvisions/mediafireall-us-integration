package com.millionvisions.mediafirewall.Controller;

import com.millionvisions.mediafirewall.Model.Media;
import com.millionvisions.mediafirewall.Service.ModerateService;
import com.millionvisions.mediafirewall.Service.WebhookIntegration;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class WebhookAPI {
    @Autowired
    WebhookIntegration webhookIntegration;


    @PostMapping("/moderate/media/request")
    public ResponseEntity<Media> moderate(@RequestParam String userId , @RequestParam String apikey, @RequestParam String mediaUrl, @RequestParam String filters){
        return new ResponseEntity<>(webhookIntegration.urlRequest(userId, apikey, mediaUrl, filters), HttpStatus.OK);
    }
    @PostMapping("/webhook")
    public ResponseEntity<String> handleWebhook(@RequestBody String payload) {
        System.out.println("Received webhook payload: " + payload);
        webhookIntegration.webhookEventTriggered(payload);
        return ResponseEntity.ok("Webhook received");
    }
}
