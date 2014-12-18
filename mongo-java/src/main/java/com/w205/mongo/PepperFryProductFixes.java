package com.w205.mongo;

import com.mongodb.*;

import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;

/**
 * Created by satish on 14-12-12.
 */
public class PepperFryProductFixes {

    static MongoClient mongoClient;
    static DB db;


    public static void main(String[] args) throws UnknownHostException {
        try {
            mongoClient = new MongoClient("54.148.179.83", 27017);
            db = mongoClient.getDB("scrapy");
            DBCollection bppIndia = db.getCollection("bpp_india");

            List<BasicDBObject> queries = new ArrayList<BasicDBObject>();
            queries.add(new BasicDBObject("vendor", "PepperFry"));
            queries.add(new BasicDBObject("product", null));
            BasicDBObject andQ = new BasicDBObject();
            andQ.put("$and", queries);
            DBCursor cursor = bppIndia.find(andQ);
            System.out.println("No of documents to fix for product name = " + cursor.count());
            int i = 0;
            while (cursor.hasNext()) {
                DBObject dbObject = cursor.next();
                Object prodNameObj = dbObject.get("product_name");
                if (prodNameObj != null) {
                    String prodName = prodNameObj.toString();
                    String prodNameStr = prodName.replace("[", "").replace("]", "").trim();
                    System.out.println("Original prod Name " + prodName + "   ::prodNameStr = " + prodNameStr);
                    BasicDBObject update = new BasicDBObject();
                    BasicDBObject updateProd = new BasicDBObject();
                    updateProd.put("product", prodNameStr);
                    update.put("$set", updateProd);
                    bppIndia.update(dbObject, update);
                    System.out.println("Fixing = " + i++);
                }
            }
            cursor.close();
            mongoClient.close();
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }catch (Exception e){
            e.printStackTrace();
        }


    }
}
