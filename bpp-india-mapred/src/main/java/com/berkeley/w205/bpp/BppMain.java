package com.berkeley.w205.bpp;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.hdfs.DFSClient;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

/**
 * Created by satish on 14-12-09.
 */
public class BppMain extends Configured implements Tool{
    @Override
    public int run(String[] args) throws Exception {
        Configuration conf = getConf();
        Job job = new Job(conf, "disjoint-selector");
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileInputFormat.addInputPath(job, new Path(args[1]));
        FileOutputFormat.setOutputPath(job, new Path(args[2]));
        job.setJarByClass(BppMain.class);
        //job.setMapperClass(MovieMapper.class);
        //job.setReducerClass(MovieReducer.class);
        job.setInputFormatClass(TextInputFormat.class);
        job.setMapOutputKeyClass(IntWritable.class);
        job.setMapOutputValueClass(Text.class);
        boolean succ = job.waitForCompletion(true);
        if (!succ) {
            System.out.println("Job failed, exiting");
            return -1;
        }
        return 0;
    }



    public static void main(String[] args) throws Exception {
        int res= ToolRunner.run(new Configuration(),new BppMain(),args);
        System.exit(res);
    }
}
