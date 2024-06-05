const fetch = require('node-fetch');

const userID = ""; // Provide your userId here
const webhooks = [
    "https://example.com/webhook",
    "https://example1.com/webhook"
];
const url = "https://apimediafirewall-us.millionvisions.ai/notification/webhook";
const body = {
    userId: userID,
    webhooks: webhooks
};
const headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer token'
};
const params = new URLSearchParams({ apikey: '' }); // Provide your apikey here

async function sendPostRequest() {
    try {
        const response = await fetch(`${url}?${params.toString()}`, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(body)
        });
        if (response.ok) {
            console.log("webhooks request sent successfully.");
        } else {
            console.log("Failed to send webhook request. Status code:", response.status);
            const responseText = await response.text();
            console.log("Response content:", responseText);
        }
    } catch (error) {
        console.error("Error occurred:", error);
    }
}

sendPostRequest();
