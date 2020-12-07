-- Check and see if the school table already exists, if it does, drop it
DROP TABLE IF EXISTS schools;

-- Check and see if the abscences table already exists, if it does, drop it
DROP TABLE IF EXISTS absences;

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

