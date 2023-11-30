#!/usr/bin/env node
import redis, { createClient } from "redis";

(function connectRedis() {
  const client = createClient();
  client.on("connect", () =>
    console.log("Redis client connected to the server")
  );
  client.on("error", (err) =>
    console.log("Redis client not connected to the server: ", err)
  );
})();

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  console.log(client.get(schoolName));
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
