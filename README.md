# mediafirewall-us-integration
Integration Guide: Media Firewall
 1. Authentication:

 To authenticate with the Media Firewall API, follow these steps:

    1.1. Login to Media Firewall Website:

        ● Navigate to the Media Firewall website and login using your credentials.

        ● Click on the User icon-> Account-> Copy the API Key.
        
    1.2. Obtain OAuth Token:
    
        ● Open Postman and set the request method to POST.
        
        ● Use the endpoint: https://{BASE_URL}/oauth/token
        
        ● Include the API Key and UserId in the request body to obtain the OAuth token.
        
        ● Use the obtained access token as a Bearer token for subsequent requests.
        
 2. Request and Response:
    
     2.1 Features:
    
         ● List of available features to apply filters on media content.
    
         ● Features include:
    
               1. MediaLightPerson
    
               2. MediaType(StandardDefinition), MediaType(HighDefinition), 
               MediaType(FullHighDefinition), MediaType(2K), MediaType(4K)
    
               3. Watermark
    
               4. Nudity(HalfNude), Nudity(FullNude), Nudity(SexToys)
    
               5. Tagging
    
               6. PropertyListing
    
               7. ObsceneGesture
    
               8. Disturbing
    
               9. Violence
    
               10. CelebrityDetection
    
               11. MediaLightVehicle
    
               12. VehicleListing(Car), VehicleListing(Truck/Bus), VehicleListing(Motorcycle), 
                   VehicleListing(Car.Truck/Bus.Motorcycle), 
                   VehicleListing(Truck/Bus.Motorcycle),
                   VehicleListing(Car.Motorcycle), VehicleListing(Car.Truck/Bus)

               13. AIGeneratedImage
    
               14. ImageSearch
    
               15. SnapcodeQR
    
               16. Distinguished
    
               17. ProfilePicture(Single), ProfilePicture(Visibility), ProfilePicture(Centered), 
                   ProfilePicture(Single.Visibility.Centered), ProfilePicture(Single.Visibility),
                   ProfilePicture(Visibility.Centered), ProfilePicture(Single.Centered)
    
     2.2 Filtering Media:
    
         ● Use Postman with a POST request to apply filters to media content.
    
         ● Endpoint:
    
         https://{BASE_URL}/moderation/{orgId}/{userId}/url/filters?filters={filters}&
         mediaUrl={mediaUrl}&apikey=
    
         ● Replace {orgId} with your actual orgId.

         ● Replace {userId} with your actual userId.
    
        ● Replace {filters} with the filter keys from 2.1 (for multiple filters, separate keys with
         commas).
    
         ● Replace {mediaUrl} with the URL of the media content.
    
         ● Fill the api key.
    
         ● Add the obtained OAuth token as a Bearer token in the request headers.
    
     2.3 Polling Results:
    
         ● Use a GET  request to poll the results.
    
         ● Endpoint:
    
         https://{BASE_URL}/mfw/model/config/{userId}/{videoId}?apikey=
    
         ● Replace {userId} with your userId.
    
         ● Replace {videoId} with the actual videoId obtained from step 2.2.
    
         ● Fill the api key.
    
         ● Add the obtained OAuth token as a Bearer token in the request headers.
    
     2.4 Integrating Webhook:
    
         ● Integrate your webhook with the Media Firewall to receive results directly.
    
         ● Endpoint:
    
         https://{BASE_URL}/notification/webhook/{userId}?webhookUrl={w
         ebhookUrl}&apikey=
    
         ● Replace {userId} with your actual UserId.
    
         ● Replace {webhookUrl} with your actual webhookUrl.
    
         ● Fill the api key.
    
         ● After posting the webhook, a message will be sent to the webhook. Click on the
         subscribeUrl in the message to subscribe.
    
         ● Content moderation events will be sent to the integrated webhook.
    
         ● Add the obtained OAuth token as a Bearer token in the request headers.
