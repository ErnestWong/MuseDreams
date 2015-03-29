package com.example.ernestwong.musedreamandroid;

import android.content.Context;
import android.media.AudioManager;
import android.os.Bundle;
import android.support.v7.app.ActionBarActivity;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;


public class MainActivity extends ActionBarActivity implements OnTaskCompleted {

    String url = "https://shielded-sierra-1551.herokuapp.com/states.json";
    AudioManager am;
    boolean looping;
    int previous = -2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        am = (AudioManager) getSystemService(Context.AUDIO_SERVICE);
        looping = true;
        getRequest(url);

    }

    private void getRequest(String url) {
        new RequestTask(this).execute(url);
    }

    @Override
    protected void onPause() {
        super.onPause();
    }

    @Override
    protected void onStop() {
        super.onStop();
    }

    @Override
    public void onResume() {
        super.onResume();
        getRequest(url);
    }

    @Override
    public void onTaskCompleted(int state) {
        if(previous != state) {
            turnDownVolume(state);
            silencePhone(state);
        }
        previous = state;
        Log.d("callback-state", state + "");

        getRequest(url);

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    public void turnDownVolume(int state) {
        if(state < 1) return;

        if(state >= 4) {
            while(am.getStreamVolume(AudioManager.STREAM_MUSIC) > 0) {
                Log.d("state 4", am.getStreamVolume(AudioManager.STREAM_MUSIC) + "");
                lowerMusicVolume();
            }
        }
    }

    private void lowerMusicVolume() {
        am.adjustStreamVolume(AudioManager.STREAM_MUSIC, AudioManager.ADJUST_LOWER, 0);
    }

    private void raiseMusicVolume() {
        am.adjustStreamVolume(AudioManager.STREAM_MUSIC, AudioManager.ADJUST_RAISE, 0);
    }

    public void silencePhone(int state) {
        if(state < 2) return;

        if(am.getRingerMode() != AudioManager.RINGER_MODE_SILENT) {

            am.setRingerMode(AudioManager.RINGER_MODE_SILENT);
        }
    }

}
