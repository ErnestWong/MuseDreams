package com.example.ernestwong.musedreamandroid;

import android.util.Log;

import org.json.JSONObject;

/**
 * Created by ernestwong on 2015-03-29.
 */
public class StateResponse {
    public static int getState(String json) {
        try {
            JSONObject obj = new JSONObject(json);
            Log.d("obj", obj.toString());

            String stateObj = obj.getJSONObject("state").toString();
            Log.d("stateobj", stateObj.toString());

            int state = Integer.parseInt(stateObj.replaceAll("[\\D]", ""));
            Log.d("state", state + "");
            return state;
        } catch (Exception e) {
            Log.e("jsonParse", e.toString());
        }
        return -1;
    }
}
