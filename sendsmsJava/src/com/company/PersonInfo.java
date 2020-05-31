package com.company;
import org.json.simple.JSONObject;
public class PersonInfo {
    public enum Status{
        Guvende(0),
        ZorDurumda(1),
        GidaIhtiyaci(2),
        BezIhtiyaci(3),
        CadirIhtiyaci(4);

        private final int value;
        Status(int i) {
            this.value = i;
        }

        public int getValue() {
            return value;
        }
    }

    public long number;
    public int status;
    public float longitude;
    public float latitude;
    PersonInfo(long userPhoneNumber)
    {
        this.number = userPhoneNumber;
        this.status = 0;
        this.latitude = 36.09f;
        this.longitude = 45.56f;
    }

    public JSONObject toJson()
    {
        JSONObject obj = new JSONObject();
        obj.put("num",this.number);
        obj.put("stat",this.status);
        obj.put("long",this.longitude);
        obj.put("lat",this.latitude);

        return obj;
    }

    public static void main(String[] args) {
        PersonInfo personInfo = new PersonInfo(379125657);
        JSONObject personJson = personInfo.toJson();
        String jsonText = personJson.toString();
        System.out.print(jsonText);
    }

}
