# Apache Kafka 
· **Projede Kafka Producer ve Consumer NodeJS teknolojisi ile gerçekleştirilmiştir**. Bir web uygulaması üzerinden Producer ve Consumer işlemleri yapılmıştır.

## Apache Kafka Kurulumu İçin Yapılması Gerekenler
· Docker teknolojisinin Windows üzerinde çalışabilmesi için https://www.confluent.io/blog/set-up-and-run-kafka-on-windows-linux-wsl-2/ adresinde tarif edildiği gibi Windows Subsystem for Linux (WSL2) kurulur.\
\
· Docker Desktop indirilir.\
\
·	https://raw.githubusercontent.com/confluentinc/cp-all-in-one/7.3.2-post/cp-all-in-one/docker-compose.yml adresinden docker-compose.yml dosyası indirilir.\
\
·	docker-compose.yml dosyası bir dosya dizinine yerleştirilir.\
\
·	docker-compose.yml dosyasının bulunduğu dosya dizini üzerinde komut ekranı açılarak 'docker-compose up -d' yazılarak docker-compose içerisindeki konfigürasyonlar ve Kafka yüklenir.\
\
·	Yine aynı komut ekranına 'docker-compose ps' yazılarak compose dosyasındaki servisler çalıştırılır.\
\
·	Kafka işlemlerinin bir arayüzde görülmesi için Control Center sayfasını çalıştırabilmek için aynı komut ekranına 'docker-compose restart control-center' yazılır ve Kafka üzerinde yapılan işlemler localhost:9021 no'lu portta çalışan Control Center sayfasında görülür.\
\
·	Kafka'nın çalışmasının durdurulması için komut ekranına 'docker-compose stop' yazılmalıdır.

## VSCode NodeJS Projesi Oluşturmak İçin Yapılması Gerekenler
· Visual Studio Code indirilir.\
\
· https://nodejs.org/ sitesinden NodeJS indirilir.\
\
· Proje için dosya oluşturulur.\
\
· Dosya Visual Studio ile birlikte açılır.\
\
· Terminal kısmına 'npm init' ile proje kurulumuna başlanır, package.json dosyası oluşturulur.\
\
· Terminal kısmına 'npm install' ile gerekli modüller indirilir.\
\
· 'npm install express ejs express-ejs-layouts' ile gerekli kütüphaneler indirilir.\
\
· 

## Projenin Çalıştırılması İçin Yapılması Gerekenler
· 'node index.js' ile proje çalıştırılır.\
\
· 'nodemon index.js' ile proje sürekli bir şekilde çalıştırılabilir.

