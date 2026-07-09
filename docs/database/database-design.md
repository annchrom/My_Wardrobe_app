# Database Design - My Wardrobe MVP

## Overview

This document describes the database structure for the first version of the My Wardrobe application.

The MVP focuses on basic wardrobe management:

- user accounts
- storing clothing items
- uploading clothing photos
- displaying personal wardrobe collection

The application supports multiple users. Each user has access only to their own wardrobe.

---

# Database Technology

## SQLite

The first version of the application uses SQLite.

Reasons:

- lightweight database
- simple local development
- no additional configuration required
- suitable for MVP

Future versions may migrate to PostgreSQL.

---

# Entity Relationship Diagram

High-level database structure:

```
USER
 |
 | 1:N
 |
CLOTHING_ITEM
```

One user can have many clothing items.

Each clothing item belongs to exactly one user.

---

# Tables

## 1. Users

### Purpose

Stores application users.

### Table name

`users`

### Columns

| Column | Type | Description |
|---|---|---|
| id | INTEGER | Primary key |
| username | VARCHAR | Unique username |
| email | VARCHAR | User email |
| password_hash | VARCHAR | Encrypted password |
| created_at | DATETIME | Account creation date |

---

### Example

| id | username | email |
|---|---|---|
|1|Anna|anna@example.com|
|2|Julia|julia@example.com|

---

# 2. Clothing Items

### Purpose

Stores wardrobe items belonging to users.

### Table name

`clothing_items`

### Columns

| Column | Type | Description |
|---|---|---|
| id | INTEGER | Primary key |
| user_id | INTEGER | Owner of the item |
| name | VARCHAR | Clothing item name |
| category | VARCHAR | Type of clothing |
| color | VARCHAR | Main color |
| season | VARCHAR | Suitable season |
| photo_path | VARCHAR | Location of uploaded photo |
| created_at | DATETIME | Date added |

---

## Example

| id | user_id | name | category | color | season |
|---|---|---|---|---|---|
|1|1|White shirt|Shirt|White|Spring|
|2|1|Black blazer|Jacket|Black|Autumn|

---

# Relationships

## User → Clothing Items

Relationship:

```
User (1) -------- (N) Clothing Items
```

Explanation:

- One user can create many clothing items.
- Each clothing item belongs to one user.
- Users cannot access clothing items belonging to other users.

---

# Data Validation Rules

## Users

- username is required
- email is required
- email must be unique
- password must be stored as a hash

---

## Clothing Items

- name is required
- category is required
- color is required
- season is required
- uploaded photo must have supported format
- user must own the clothing item

---

# Future Database Extensions

The following tables will be added in future versions:

## Outfits

Stores combinations of clothing items.

Possible fields:

- id
- user_id
- name
- rating


## Outfit Items

Many-to-many relationship between outfits and clothing items.


## Wear History

Stores every time an item was worn.

Possible fields:

- id
- clothing_item_id
- outfit_id
- worn_date


## Statistics

Calculated from application data:

- most worn items
- least worn items
- outfit ratings