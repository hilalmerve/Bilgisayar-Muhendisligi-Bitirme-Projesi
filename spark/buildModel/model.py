import findspark
findspark.init()
from pyspark.sql.types import StructType,StructField, StringType, LongType, IntegerType
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace
from pyspark.ml.feature import Tokenizer,StopWordsRemover,CountVectorizer,IDF
from pyspark.ml.feature import StringIndexer, IndexToString
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline 
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql.types import StringType
from pyspark.sql.functions import col
from pyspark.ml.feature import RegexTokenizer, StopWordsRemover, CountVectorizer
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

dataSchema = StructType([
    StructField("id",LongType(),True),
    StructField("description",StringType(),True),
    StructField("eclassnumber",StringType(),True)
  ])

spark = SparkSession.builder.master("local[*]").appName("TextClassification").getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

df = spark.read.option("header", True).option("inferSchema", True).option("multiLine", True).json("./resources/dataset/")
df.printSchema()
df.show(5)

df2 = df.select("id", "description", regexp_replace("eclassnumber", "-", "").alias('eclassnumber'))
df2.printSchema()
df2.show()
df3 = df2.withColumn("eclassnumber",df2.eclassnumber.cast(IntegerType()))
df3.printSchema()
df3.select("description", "eclassnumber").show()

df = df3.select("description", "eclassnumber")
df.groupBy("eclassnumber") \
    .count() \
    .orderBy(col("count").desc()) \
    .show()

tokenizer = Tokenizer(inputCol='description',outputCol='mytokens')
stopwords_remover = StopWordsRemover(inputCol='mytokens',outputCol='filtered_tokens')
vectorizer = CountVectorizer(inputCol='filtered_tokens',outputCol='rawFeatures')
idf = IDF(inputCol='rawFeatures',outputCol='vectorizedFeatures')

labelEncoder = StringIndexer(inputCol='eclassnumber',outputCol='label').fit(df)
labelEncoder.transform(df).show(10)

df = labelEncoder.transform(df)

(trainDF,testDF) = df.randomSplit((0.7,0.3),seed=42)
print("Training Dataset Count: " + str(trainDF.count()))
print("Test Dataset Count: " + str(testDF.count()))

lr = LogisticRegression(featuresCol='vectorizedFeatures',labelCol='label')
labelConverter = IndexToString(inputCol="prediction", outputCol="predEclassnumber",labels=labelEncoder.labels)
pipeline = Pipeline(stages=[tokenizer,stopwords_remover,vectorizer,idf,lr,labelConverter])
lr_model = pipeline.fit(trainDF)

predictions = lr_model.transform(testDF)
predictions.show()

predictions.select('rawPrediction','probability','eclassnumber','label','prediction','predEclassnumber').show(10)

evaluator = MulticlassClassificationEvaluator(labelCol='label',predictionCol='prediction',metricName='accuracy')
accuracy = evaluator.evaluate(predictions)
accuracy

ex1 = spark.createDataFrame([
    ("Concept development Development",StringType())
],
["description"])

ex1.show()
pred_ex1 = lr_model.transform(ex1)
pred_ex1.show()

tahmin = pred_ex1.select('description', 'rawPrediction','probability','prediction', 'predEclassnumber')
tahmin.show()

lr_model.write().overwrite().save("./resources/model")