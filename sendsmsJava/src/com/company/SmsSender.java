package com.company;

import com.twilio.Twilio;
import com.twilio.rest.api.v2010.account.Message;
import com.twilio.type.PhoneNumber;
import com.company.PersonInfo;
import org.json.simple.JSONObject;

public class SmsSender {
    // Find your Account Sid and Auth Token at twilio.com/console
    public static final String ACCOUNT_SID =
            "ACe7472d8673290c0e203b61d9bcf1c0a5";
    public static final String AUTH_TOKEN =
            "98a73ec711d7412a864223e16f02c05c";

    public static void main(String[] args) {
        Twilio.init(ACCOUNT_SID, AUTH_TOKEN);

        // create a person info
        PersonInfo personInfo = new PersonInfo(379125657);
        personInfo.longitude = 44.33f;
        personInfo.latitude = 33.44f;
        personInfo.status =  PersonInfo.Status.Guvende.getValue() + PersonInfo.Status.BezIhtiyaci.getValue();
        JSONObject personJson = personInfo.toJson();
        String personStringJson = personJson.toString();
        String replaceString=personStringJson.replace('\"','\'');//replaces all occurrences of 'a' to 'e'
        System.out.println(replaceString);

        Message message = Message
                .creator(new PhoneNumber("+12029329036"), // to
                        new PhoneNumber("+12029329036"), // from
                        "test")
                .create();

        System.out.println(message.getSid());
    }
}