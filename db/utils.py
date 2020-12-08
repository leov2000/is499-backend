import sqlite3
import csv

def create_tables():
    conn = sqlite3.connect("schools.db")
    sql_file = open("schema.sql")
    sql_tables = sql_file.read()

    conn.executescript(sql_tables)
    conn.commit()
    conn.close()

    sql_file.close()

def connect_and_insert(insert_str):
    conn = sqlite3.connect("schools.db")
    cursor = conn.cursor()

    cursor.executescript(insert_str)
    conn.commit()
    conn.close()


def csv_to_list(csv_name):
    with open(csv_name) as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        csv_list = [row for row in reader]

        return csv_list


def split_data(csv_list):
    header = csv_list[:1][0]
    data = csv_list[1:]

    return (header, data)


def transform_to_dict(val_list, key_config):
    
    return [
        dict(zip(key_config, val_tup)) for val_tup in val_list 
    ]