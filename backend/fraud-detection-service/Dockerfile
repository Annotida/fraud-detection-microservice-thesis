FROM eclipse-temurin:21-jdk

WORKDIR /app

COPY . .

RUN chmod +x mvnw

RUN ./mvnw clean package -DskipTests

EXPOSE 5050

CMD ["java","-jar","target/fraud-detection-service-0.0.1-SNAPSHOT.jar"]