package com.millionvisions.mediafirewall.Model;

import java.util.List;

public class WebhookConfiguration {
    private String userId;
    private List<String> webhooks;

    // Constructor
    public WebhookConfiguration(String userId, List<String> webhooks) {
        this.userId = userId;
        this.webhooks = webhooks;
    }

    // Getters
    public String getUserId() {
        return userId;
    }

    public List<String> getWebhooks() {
        return webhooks;
    }

    // Setters
    public void setUserId(String userId) {
        this.userId = userId;
    }

    public void setWebhooks(List<String> webhooks) {
        this.webhooks = webhooks;
    }

    // toString method
    @Override
    public String toString() {
        return "WebhookConfiguration{" +
                "userId='" + userId + '\'' +
                ", webhooks=" + webhooks +
                '}';
    }
}

