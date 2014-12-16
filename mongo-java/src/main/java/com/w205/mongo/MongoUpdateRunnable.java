package com.w205.mongo;

import com.mongodb.BasicDBObject;
import com.mongodb.DBCollection;
import com.mongodb.DBObject;
import org.bson.types.ObjectId;

import java.util.StringTokenizer;
import java.util.concurrent.Callable;

/**
 * Created by satish on 14-12-16.
 */
public class MongoUpdateRunnable implements Runnable {
    String line;
    DBCollection bppIndia;

    static int counter;

    public MongoUpdateRunnable(String line, DBCollection bppIndia) {
        this.line = line;
        this.bppIndia = bppIndia;
    }

    @Override
    public void run() {
        try {
            StringTokenizer tokenizer = new StringTokenizer(line, ",");
            String objID = tokenizer.nextToken();
            BasicDBObject basicDBObject = new BasicDBObject("_id", new ObjectId(objID));
            DBObject bppIndiaOne = bppIndia.findOne(basicDBObject);
            Object productObj = basicDBObject.get("product");
            String threadName = Thread.currentThread().getName();
            if (productObj == null) {

                String category = tokenizer.nextToken();
                String product = tokenizer.nextToken();
                BasicDBObject update = new BasicDBObject();
                BasicDBObject updateProd = new BasicDBObject();
                updateProd.put("product", product);
                updateProd.put("category", category);
                update.put("$set", updateProd);

                System.out.println("Thread-Name "+ threadName +" Updating product " + product + " category " + category + " in obje ID " + objID);
                bppIndia.update(bppIndiaOne, update);
                System.out.println("Thread-Name "+ threadName +"Inserted counter = " + counter++);
            }else {
                System.out.println("Thread-Name "+ threadName +"Product Exists product.toString() = " + productObj.toString());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
