package com.millionvisions.mediafirewall.Controller;

import com.millionvisions.mediafirewall.Service.ModerateService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(value = "/moderate")
public class ModerateAPI {
    @Autowired
    ModerateService moderateService;

    @PostMapping("/media")
    public ResponseEntity<String> moderate(@RequestParam String userId ,@RequestParam String apikey,@RequestParam String mediaUrl,@RequestParam String filters){
        return new ResponseEntity<>(moderateService.urlRequest(userId, apikey, mediaUrl, filters), HttpStatus.OK);
    }
}
