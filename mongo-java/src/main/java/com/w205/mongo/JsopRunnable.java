package com.w205.mongo;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.util.List;
import java.util.StringTokenizer;
import java.util.concurrent.Callable;

/**
 * Created by satish on 14-12-16.
 */
public class JsopRunnable implements Callable<String>{

    String line;
    List<String> outs;
    static int counter=0;


    public JsopRunnable(String line, List<String> outs) {
        this.line = line;
        this.outs = outs;
    }

    @Override
    public String call() throws Exception {
        StringTokenizer tokenizer = new StringTokenizer(line, ";;;");
        String url = tokenizer.nextToken();
        String name = Thread.currentThread().getName();
        System.out.println("Thread- Name "+ name +"url = " + url);
        Document doc = null;
        try {
            doc = (Document) Jsoup.connect(url).timeout(0).get();
        } catch (IOException e) {
            e.printStackTrace();
        }
        Element cat_crum = doc.getElementById("cat_crum");
        String category = cat_crum.attr("value");
        System.out.println("Thread- Name "+ name +"category = " + category);
        String objID = tokenizer.nextToken();

        Elements vip_title = doc.getElementsByClass("vip_title");

        if (vip_title == null || vip_title.size() == 0) {
            vip_title = doc.getElementsByClass("vip_title vip_title_fur");
        }
        String title_str = null;
        if (vip_title != null) {
            for (Element title : vip_title) {
                title_str = title.text();
            }
        }

        StringBuffer buff = new StringBuffer();
        buff.append(objID);
        buff.append(",");
        buff.append(category);
        if (title_str != null || title_str.length() > 0) {
            buff.append(",");
            buff.append(title_str);
        }

        System.out.println("counter = " + counter++);
        return buff.toString();

    }
}
