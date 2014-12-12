package hortus.com.mongo.hortus;

import com.mongodb.*;

import java.net.UnknownHostException;
import java.util.function.Consumer;
import java.util.regex.Pattern;


/**
 * Created by satish on 14-12-05.
 */
public class MongoMain {

    static MongoClient mongoClient;
    static DB db;

    public static void main(String[] args) throws UnknownHostException {
        mongoClient = new MongoClient("54.148.179.83", 27017);
        db = mongoClient.getDB("scrapy");
        DBCollection bppIndia = db.getCollection("bpp_india");
        Pattern regex = Pattern.compile(",", Pattern.CASE_INSENSITIVE | Pattern.UNICODE_CASE);
        BasicDBObject query = new BasicDBObject("price", regex);
        DBCursor cursor = bppIndia.find(query);
        System.out.println("No of documents to fix price for cursor = " + cursor.count());
        /*while (cursor.hasNext()) {
            DBObject dbObject = cursor.next();
            Object price = dbObject.get("price");
            String priceStr = price.toString();

            BasicDBObject update = new BasicDBObject();
            BasicDBObject priceUpdate = new BasicDBObject();
            priceUpdate.put("price", priceStr.replace(",", ""));
            update.put("$set", priceUpdate);
            bppIndia.update(dbObject, update);
        }*/
        cursor.close();
        mongoClient.close();


    }

    public static void printAllDocuments(DBCollection collection) {
        DBCursor cursor = collection.find();
        while (cursor.hasNext()) {
            System.out.println(cursor.next());
        }
    }


}
