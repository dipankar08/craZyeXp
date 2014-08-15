package com.example.fibnative;

import android.support.v7.app.ActionBarActivity;
import android.text.TextUtils;
import android.annotation.SuppressLint;
import android.app.ProgressDialog;
import android.os.AsyncTask;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioGroup;
import android.widget.TextView;


public class MainActivity extends ActionBarActivity implements OnClickListener  {
	
	private EditText input;
	private RadioGroup type;
	private TextView output;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        this.input= (EditText) super.findViewById(R.id.input);
        this.type= (RadioGroup) super.findViewById(R.id.type);
        this.output= (TextView) super.findViewById(R.id.output);
        Button button= (Button) super.findViewById(R.id.button);
        button.setOnClickListener(this); 
    }
    public  void  onClick(View view){
    	String s = this.input.getText().toString();
    	if(TextUtils.isEmpty(s)){
    		return;
    	}
    	final ProgressDialog dialog= ProgressDialog.show(this,"","calculating...",true);
    	final long n = Long.parseLong(s);
    	new AsyncTask<Void, Void, String>() {

			@Override
			protected void onPostExecute(String result) {
				// TODO Auto-generated method stub
				dialog.dismiss();
				MainActivity.this.output.setText(result); 
			}

			@SuppressLint("DefaultLocale") @Override
			protected String doInBackground(Void... params) {
		        long result = 0;
		        long t = System.currentTimeMillis();
		    	switch(MainActivity.this.type.getCheckedRadioButtonId())
		    	{
		    	//System.out.print("dddd"+n);
		    	case R.id.type_fib_jr:
		    		result=FibLib.fibJR(n);
		    		break;
		    	case R.id.type_fib_ji:
		    		result=FibLib.fibJI(n);
		    		break;
		    	case R.id.type_fib_nr:
		    		result=FibLib.fibNR(n);
		    		break;
		    	case R.id.type_fib_ni:
		    		result=FibLib.fibNI(n);
		    		break;
		    	}
		    	t = System.currentTimeMillis()-t;
		    	return String.format("fib(%d)=%d in %d ms", n,result,t);
			}    		
		}.execute();
    	
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (id == R.id.action_settings) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }
}
