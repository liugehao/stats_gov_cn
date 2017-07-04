/*
 Navicat Premium Data Transfer

 Source Server         : 192.168.99.100
 Source Server Type    : PostgreSQL
 Source Server Version : 90603
 Source Host           : 192.168.99.100:5432
 Source Catalog        : pgerdb
 Source Schema         : basic

 Target Server Type    : PostgreSQL
 Target Server Version : 90603
 File Encoding         : 65001

 Date: 04/07/2017 09:50:15
*/




-- ----------------------------
-- Table structure for p_city
-- ----------------------------
DROP TABLE IF EXISTS "p_city";
CREATE TABLE "p_city" (
  "city_id" int4 NOT NULL,
  "province_id" int4,
  "name" varchar(100) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "p_city" OWNER TO "postgres";

-- ----------------------------
-- Table structure for p_county
-- ----------------------------
DROP TABLE IF EXISTS "p_county";
CREATE TABLE "p_county" (
  "county_id" int4 NOT NULL ,
  "province_id" int4,
  "city_id" int4,
  "name" varchar(100) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "p_county" OWNER TO "postgres";

-- ----------------------------
-- Table structure for p_province
-- ----------------------------
DROP TABLE IF EXISTS "p_province";
CREATE TABLE "p_province" (
  "province_id" int4 NOT NULL,
  "name" varchar(100) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "p_province" OWNER TO "postgres";

-- ----------------------------
-- Table structure for p_town
-- ----------------------------
DROP TABLE IF EXISTS "p_town";
CREATE TABLE "p_town" (
  "town_id" int4 NOT NULL,
  "province_id" int4,
  "city_id" int4,
  "county_id" int4,
  "name" varchar(100) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "p_town" OWNER TO "postgres";

-- ----------------------------
-- Table structure for p_village
-- ----------------------------
DROP TABLE IF EXISTS "p_village";
CREATE TABLE "p_village" (
  "village_id" int8 NOT NULL,
  "province_id" int4,
  "city_id" int4,
  "county_id" int4,
  "town_id" int4,
  "name" varchar(100) COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "p_village" OWNER TO "postgres";


-- ----------------------------
-- Indexes structure for table device_info
-- ----------------------------
CREATE INDEX "device_info_category_idx" ON "device_info" USING btree (
  "category" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX CONCURRENTLY "device_info_category_idx1" ON "device_info" USING btree (
  "category" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "device_info_category_idx2" ON "device_info" USING btree (
  "category" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table device_info
-- ----------------------------
ALTER TABLE "device_info" ADD CONSTRAINT "device_info_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table p_city
-- ----------------------------
ALTER TABLE "p_city" ADD CONSTRAINT "p_city_pkey" PRIMARY KEY ("city_id");

-- ----------------------------
-- Primary Key structure for table p_county
-- ----------------------------
ALTER TABLE "p_county" ADD CONSTRAINT "p_county_pkey" PRIMARY KEY ("county_id");

-- ----------------------------
-- Primary Key structure for table p_province
-- ----------------------------
ALTER TABLE "p_province" ADD CONSTRAINT "p_province_pkey" PRIMARY KEY ("province_id");

-- ----------------------------
-- Primary Key structure for table p_town
-- ----------------------------
ALTER TABLE "p_town" ADD CONSTRAINT "p_town_pkey" PRIMARY KEY ("town_id");

-- ----------------------------
-- Primary Key structure for table p_village
-- ----------------------------
ALTER TABLE "p_village" ADD CONSTRAINT "p_village_pkey" PRIMARY KEY ("village_id");
