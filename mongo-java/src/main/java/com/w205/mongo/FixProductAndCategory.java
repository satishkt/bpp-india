package com.w205.mongo;

import org.apache.commons.io.FileUtils;
import org.apache.commons.io.IOUtils;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;

/**
 * Created by satish on 14-12-15.
 */
public class FixProductAndCategory {
    final static String url = "http://www.pepperfry.com/10-metre-long-multi-colored-designer-shell-shaped-led-lights-1215712.html?pos=19:1";
    //*[@id="vip_content_section"]/div[2]/h1

    public static void main(String args[]) throws IOException {

        File file = new File(args[0]);
        File f = new File(args[1]);
        List<String> list = IOUtils.readLines(new FileInputStream(file));
        List<String> outs = new ArrayList<String>();
        int corePoolSize = 5;
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

        for (String line : list) {
            JsopRunnable runnable = new JsopRunnable(line, outs);
            Future<String> submit = threadPoolExecutor.submit(runnable);
            String out_line = "";
            try {
                out_line = submit.get();
            } catch (InterruptedException e) {
                e.printStackTrace();
            } catch (ExecutionException e) {
                e.printStackTrace();
            }

            outs.add(out_line);
            if (outs.size() > 100) {
                System.out.println("Wrote 100");
                FileUtils.writeLines(f, outs, "\n", true);
                outs = new ArrayList<String>();
            }

        }

        FileUtils.writeLines(f, outs, "\n", true);
    }


}
