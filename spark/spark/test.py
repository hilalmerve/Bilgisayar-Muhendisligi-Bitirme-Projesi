import findspark
findspark.init()
from pyspark.sql.types import StructType,StructField, StringType
from pyspark.ml import PipelineModel
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import os
dataSchema = StructType([
    StructField("description",StringType(),True)
  ])
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0 pyspark-shell'
schema = StructType().add("description", StringType(), True)
spark = SparkSession.builder.config("spark.jars", os.getcwd() + "/jars/spark-sql-kafka-0-10_2.12-3.4.0.jar" + "," + os.getcwd() + "/jars/kafka-clients-2.1.1.jar" + "," + os.getcwd() + "/jars/spark-streaming-kafka-0-10-assembly_2.12-3.4.0").master("local[2]").appName("Class").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

pipelineModel = PipelineModel.load("./resources/model")


df = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "kafka").option("startingOffsets", "latest").load()
df.printSchema()
query = df.selectExpr("CAST(value AS STRING)")
query.printSchema()
df2 = query.selectExpr("value as description")
df2.printSchema()
model = pipelineModel.transform(df2)
prediction = model.select('description', 'predEclassnumber')
result = prediction.select(col("description").cast("string"), col("predEclassnumber").cast("string"))

result1 = model.select(col("predEclassnumber").cast("String"))
result1.printSchema()
query = result1.selectExpr("to_json(struct(*)) AS value").writeStream.outputMode("update").format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("topic", "prediction").option("checkpointLocation", "../checkpoint").start()

query.awaitTermination()