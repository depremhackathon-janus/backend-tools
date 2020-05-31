package com.company;
import org.json.simple.JSONObject;
public class PersonInfo {
    public enum Status{
        Guvende(1),
        ZorDurumda(2),
        GidaIhtiyaci(4),
        BezIhtiyaci(8),
        CadirIhtiyaci(16),
        EnkazAltindayim(32),
        KomsumdanSesGeliyor(64);

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
    public float longitude; //max character
    public float latitude; // max character
    public String txt;
    PersonInfo(long userPhoneNumber)
    {
        this.number = userPhoneNumber;
        this.status = 0;
        this.latitude = 36.09f;
        this.longitude = 45.56f;
        this.txt = "";
    }

    public JSONObject toJson()
    {
        JSONObject obj = new JSONObject();
        obj.put("num",this.number);
        obj.put("stat",this.status);
        obj.put("long",this.longitude);
        obj.put("lat",this.latitude);
        obj.put("txt",this.txt);
        return obj;
    }

    public static void main(String[] args) {
        PersonInfo personInfo = new PersonInfo(379125657);
        JSONObject personJson = personInfo.toJson();
        String jsonText = personJson.toString();
        System.out.print(jsonText);
    }

}
