/*
 Navicat Premium Data Transfer

 Source Server         : test
 Source Server Type    : SQLite
 Source Server Version : 3030001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3030001
 File Encoding         : 65001

 Date: 13/07/2022 02:48:54
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for data20220712_printed
-- ----------------------------
DROP TABLE IF EXISTS "data20220712_printed";
CREATE TABLE "data20220712_printed" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "upc" TEXT,
  "name" TEXT,
  "description" TEXT,
  "image" TEXT,
  "price" REAL,
  "category" TEXT,
  "disc" REAL,
  "stock" INTEGER,
  "employee" TEXT
);

-- ----------------------------
-- Table structure for data20220712_scaned
-- ----------------------------
DROP TABLE IF EXISTS "data20220712_scaned";
CREATE TABLE "data20220712_scaned" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "upc" TEXT,
  "name" TEXT,
  "description" TEXT,
  "image" TEXT,
  "price" REAL,
  "category" TEXT,
  "disc" REAL,
  "stock" INTEGER,
  "employee" TEXT
);

-- ----------------------------
-- Table structure for discounts
-- ----------------------------
DROP TABLE IF EXISTS "discounts";
CREATE TABLE "discounts" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "category_name" TEXT NOT NULL,
  "discount" real NOT NULL
);

-- ----------------------------
-- Table structure for history
-- ----------------------------
DROP TABLE IF EXISTS "history";
CREATE TABLE "history" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "date" text NOT NULL DEFAULT ''
);

-- ----------------------------
-- Table structure for products
-- ----------------------------
DROP TABLE IF EXISTS "products";
CREATE TABLE "products" (
  "id" INTEGER NOT NULL,
  "url" TEXT DEFAULT "",
  "tcin" TEXT,
  "upc" TEXT DEFAULT "",
  "name" TEXT DEFAULT "",
  "description" TEXT DEFAULT "",
  "image" TEXT DEFAULT "",
  "category" TEXT DEFAULT "",
  "price" text DEFAULT "",
  "disc" TEXT DEFAULT "",
  "stock" text DEFAULT 0,
  "employee" TEXT DEFAULT "",
  "open_date" text DEFAULT "0000-00-00",
  "update_date" TEXT DEFAULT "0000-00-00",
  "close_date" TEXT DEFAULT "0000-00-00",
  "is_available" integer DEFAULT 1,
  "last_sold" TEXT DEFAULT "0000-00-00",
  "last_price" text DEFAULT 0,
  PRIMARY KEY ("id")
);

-- ----------------------------
-- Table structure for products_copy1
-- ----------------------------
DROP TABLE IF EXISTS "products_copy1";
CREATE TABLE "products_copy1" (
  "id" INTEGER NOT NULL,
  "url" TEXT DEFAULT "",
  "tcin" TEXT,
  "upc" TEXT DEFAULT "",
  "name" TEXT DEFAULT "",
  "description" TEXT DEFAULT "",
  "image" TEXT DEFAULT "",
  "category" TEXT DEFAULT "",
  "price" text DEFAULT "",
  "disc" TEXT DEFAULT "",
  "stock" text DEFAULT 0,
  "employee" TEXT DEFAULT "",
  "open_date" text DEFAULT "0000-00-00",
  "update_date" TEXT DEFAULT "0000-00-00",
  "close_date" TEXT DEFAULT "0000-00-00",
  "is_available" integer DEFAULT 1,
  "last_sold" TEXT DEFAULT "0000-00-00",
  "last_price" text DEFAULT 0,
  PRIMARY KEY ("id")
);

-- ----------------------------
-- Table structure for sqlite_sequence
-- ----------------------------
DROP TABLE IF EXISTS "sqlite_sequence";
CREATE TABLE "sqlite_sequence" (
  "name",
  "seq"
);

-- ----------------------------
-- Auto increment value for data20220712_printed
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 1 WHERE name = 'data20220712_printed';

-- ----------------------------
-- Auto increment value for data20220712_scaned
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 10 WHERE name = 'data20220712_scaned';

-- ----------------------------
-- Auto increment value for discounts
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 24 WHERE name = 'discounts';

-- ----------------------------
-- Auto increment value for history
-- ----------------------------

PRAGMA foreign_keys = true;
