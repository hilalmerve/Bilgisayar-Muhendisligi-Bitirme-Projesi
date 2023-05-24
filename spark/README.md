# Apache Spark
·	**Projede verilerin analizi için PySpark teknolojisi tercih edilmiştir.**

## Apache Spark Kurulumu İçin Yapılması Gerekenler
·	Java indirilir ve kurulumu gerçekleştirilir.\
\
·	Pyhton indirilir ve kurulumu gerçekleştirilir.\
\
·	https://spark.apache.org/downloads.html adresinden Spark indirilir.\
\
·	Windows C dizininde apache-spark adında klasör oluşturulur.\
\
·	İndirilen tar dosyası apache-spark kalsörüne çıkartılır.\
\
·	C dizininde hadoop adında bir klasör oluşturulur.\
\
·	hadoop klasörünün içerisine bin adlı klasör oluşturulur.\
\
·	winutils adlı dosya hadoop klasörünün içerisine kaydedilir.\
\
·	Denetim Masası'nda Gelişmiş Sstem Ayarları içerisinde Ortam Değişkenleri adlı seçeneğe tıklanır.\
\
·	Kullanıcı değişkenleri kısmıdna HADOOP_HOME adlı değişken oluşturulur ve dosya yolu olarak C dizininde oluşturulan hadoop klasörünün yolu verilir. 'C:\hadoop'.\
\
·	Daha sonra SPARK_HOME adlı değişken oluşturulur ve dosya yolu olarak C dizininde oluşturulan apache_spark klasörünün içerisinde indirilen spark dosyasının yolu verilir. Bu proje için 'C:\apache-spark\spark-3.3.2-bin-hadoop3'.\
\
·	Ortam Değişkenlerinin Path kısmına %HADOOP_HOME%\bin ve %SPARK_HOME%\bin eklenir kaydedilir.\
\
·	C dizininde tmp adında bir klasör oluşturulur. İçinde hive adında bir klasör oluşturulur.\
\
·	Bilgisayarda komut ekranına 'winutils chmod 777 C:\tmp\hive' yazılır.\
\
·	Daha sonra komut ekranına pyspark yazılır ve pyspark bilgisayara yüklenmiş ve kurulmuş olur.\
\
·	C dizininde bulunan apache-spark klasöründeki spark klasöründe 'spark-3.3.2-bin-hadoop3' klasörünün içerisindeki conf klasörünün içindeki 'log4j.properties.template' adlı dosya içerisindeki log4j.rootCategory=INFO, ERROR yapılır ve kaydedilir.

## Projenin Çalışması İçin Yapılması Gerekenler
·	'python -m venv env' Python sanal ortamı oluşturulması gerekir.\
\
·	Sanal ortamı aktifleştirmek için '.\env\Scripts\activate' ifadesi yazılmalıdır.\
\
·	Daha sonra proje çalıştırılır.
