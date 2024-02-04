-- Create the User table
CREATE TABLE auth_user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(150) NOT NULL,
    password VARCHAR(128) NOT NULL,
    first_name VARCHAR(30),
    last_name VARCHAR(150),
    email VARCHAR(254) NOT NULL,
    is_staff BOOLEAN NOT NULL,
    is_active BOOLEAN NOT NULL,
    date_joined TIMESTAMP WITH TIME ZONE NOT NULL,
    department_id INTEGER
);

-- Create the Category table
CREATE TABLE ecommerce_category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Create the Product table
CREATE TABLE ecommerce_product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    category_id INTEGER NOT NULL
);

-- Create the Discount table
CREATE TABLE ecommerce_discount (
    id SERIAL PRIMARY KEY,
    percentage NUMERIC(5, 2) NOT NULL,
    product_category_id INTEGER NOT NULL,
    user_category VARCHAR(50) NOT NULL
);

-- Add foreign key constraints
ALTER TABLE auth_user ADD CONSTRAINT user_department_fk FOREIGN KEY (department_id) REFERENCES ecommerce_department (id);
ALTER TABLE ecommerce_product ADD CONSTRAINT product_category_fk FOREIGN KEY (category_id) REFERENCES ecommerce_category (id);
ALTER TABLE ecommerce_discount ADD CONSTRAINT discount_product_category_fk FOREIGN KEY (product_category_id) REFERENCES ecommerce_category (id);
