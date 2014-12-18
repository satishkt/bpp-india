package com.w205.mongo;

import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.MongoClient;
import org.apache.commons.io.IOUtils;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

/**
 * Created by satish on 14-12-12.
 */
public class PepperFryProductNameFromProductUrl {
    static MongoClient mongoClient;
    static DB db;


    public static void main(String[] args) throws IOException {
        mongoClient = new MongoClient("54.148.179.83", 27017);
        db = mongoClient.getDB("scrapy");
        DBCollection bppIndia = db.getCollection("bpp_india");
        int corePoolSize = 1;
        int maxPoolSize = 10;
        long keepAliveTime = 5000;

        ExecutorService threadPoolExecutor =
                new ThreadPoolExecutor(
                        corePoolSize,
                        maxPoolSize,
                        keepAliveTime,
                        TimeUnit.MILLISECONDS,
                        new LinkedBlockingQueue<Runnable>()
                );
        File file = new File(args[0]);
        List<String> list = IOUtils.readLines(new FileInputStream(file));
        for (String line : list) {
            MongoUpdateRunnable mongoUpdateRunnable = new MongoUpdateRunnable(line, bppIndia);
            //threadPoolExecutor.submit(mongoUpdateRunnable);
            mongoUpdateRunnable.run();
        }


        //threadPoolExecutor.shutdown();
        mongoClient.close();


    }

}
