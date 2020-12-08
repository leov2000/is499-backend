-- Check and see if the school table already exists, if it does, drop it
DROP TABLE IF EXISTS schools;

-- Check and see if the abscences table already exists, if it does, drop it
DROP TABLE IF EXISTS absences;

-- Check and see if the consolidated_absences table already exists, if it does, drop it
DROP TABLE IF EXISTS consolidated_absences;

-- Check and see if the bullying table already exists, if it does, drop it
DROP TABLE IF EXISTS bullying;

-- Create schools table
CREATE TABLE schools (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    dbn TEXT NOT NULL,
    "location" TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    coordinates TEXT NOT NULL
);

-- Create absences table
CREATE TABLE absences (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    dbn TEXT NOT NULL,
    school_name TEXT NOT NULL,
    grade TEXT NOT NULL,
    "year" TEXT NOT NULL,
    demographic_category TEXT NOT NULL,
    demographic_variable TEXT NOT NULL,
    num_total_days TEXT NOT NULL,
    num_days_absent TEXT NOT NULL,
    num_days_present TEXT NOT NULL,
    percent_attendance TEXT NOT NULL,
    num_chronically_absent TEXT NOT NULL,
    percent_chronically_absent TEXT NOT NULL
);

-- Create consolidated_absences table
CREATE TABLE consolidated_absences (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    dbn TEXT NOT NULL,
    school_name TEXT NOT NULL,
    grade TEXT NOT NULL,
    "year" TEXT NOT NULL,
    demographic_category TEXT NOT NULL,
    demographic_variable TEXT NOT NULL,
    num_total_days TEXT NOT NULL,
    num_days_absent TEXT NOT NULL,
    num_days_present TEXT NOT NULL,
    percent_attendance TEXT NOT NULL,
    num_chronically_absent TEXT NOT NULL,
    percent_chronically_absent TEXT NOT NULL
);

-- Create bullying table
CREATE TABLE bullying (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    dbn TEXT NOT NULL,
    school_name TEXT NOT NULL,
    complaints TEXT NOT NULL,
    material_incidents TEXT NOT NULL
);

