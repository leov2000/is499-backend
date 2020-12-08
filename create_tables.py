import sqlite3
import csv


def csv_to_list(csv_name):
    with open(csv_name) as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        csv_list = [row for row in reader]

        return csv_list


def connect_and_insert(insert_str):
    conn = sqlite3.connect("schools.db")
    cursor = conn.cursor()

    cursor.executescript(insert_str)
    conn.commit()
    conn.close()


def split_data(csv_list):
    header = csv_list[:1][0]
    data = csv_list[1:]

    return (header, data)


def insert_bullying_data(csv_list):
    (header, data) = split_data(csv_list)
    [dbn_h, school_name_h, complaints_h, material_incidents_h] = header

    for row in data:
        [dbn_r, school_name_r, complaints_r, material_incidents_r] = row

        insert_str = f"""
        INSERT INTO bullying
        (
            {dbn_h},
            {school_name_h},
            {complaints_h},
            {material_incidents_h}
        )
        VALUES
        (
            "{str(dbn_r)}",
            "{str(school_name_r)}",
            "{str(complaints_r)}",
            "{str(material_incidents_r)}"
        )
        """

        connect_and_insert(insert_str)


def query_absences_table():
    conn = sqlite3.connect("schools.db")
    cursor = conn.cursor()

    query_str = """
    SELECT * FROM absences
    WHERE demographic_variable = "All Students" AND "year" = "2017-18";
    """

    cursor.execute(query_str)
    rows = cursor.fetchall()

    for row in rows:
        (
            id,
            dbn_r,
            school_name_r,
            grade_r,
            year_r,
            demographic_category_r,
            demographic_variable_r,
            num_total_days_r,
            num_days_absent_r,
            num_days_present_r,
            percent_attendance_r,
            num_chronically_absent_r,
            percent_chronically_absent_r,
        ) = row

        insert_str = f"""
        INSERT INTO consolidated_absences
        (
            {"dbn"},
            {"school_name"},
            {"grade"},
            {"year"},
            {"demographic_category"},
            {"demographic_variable"},
            {"num_total_days"},
            {"num_days_absent"},
            {"num_days_present"},
            {"percent_attendance"},
            {"num_chronically_absent"},
            {"percent_chronically_absent"}
        )
        VALUES
        (
            "{str(dbn_r)}",
            "{str(school_name_r)}",
            "{str(grade_r)}",
            "{str(year_r)}",
            "{str(demographic_category_r)}",
            "{str(demographic_variable_r)}",
            "{str(num_total_days_r)}",
            "{str(num_days_absent_r)}",
            "{str(num_days_present_r)}",
            "{str(percent_attendance_r)}",
            "{str(num_chronically_absent_r)}",
            "{str(percent_chronically_absent_r)}"
        )
        """

        connect_and_insert(insert_str)

    conn.close()


def insert_dbn_data(csv_list):
    (header, data) = split_data(csv_list)
    [dbn_h, location_h, postal_code_h, coordinates_h] = header

    for row in data:
        [dbn_r, location_r, postal_code_r, coordinates_r] = row

        insert_str = f"""
        INSERT INTO schools
        (
            {dbn_h},
            {location_h},
            {postal_code_h},
            {coordinates_h}
        )
        VALUES
        (
            "{str(dbn_r)}",
            "{str(location_r)}",
            "{str(postal_code_r)}",
            "{str(coordinates_r)}"
        )
        """

        connect_and_insert(insert_str)


def insert_absence_data(csv_list):
    (header, data) = split_data(csv_list)
    [
        dbn_h,
        school_name_h,
        grade_h,
        year_h,
        demographic_category_h,
        demographic_variable_h,
        num_total_days_h,
        num_days_absent_h,
        num_days_present_h,
        percent_attendance_h,
        num_chronically_absent_h,
        percent_chronically_absent_h,
    ] = header

    for row in data:
        [
            dbn_r,
            school_name_r,
            grade_r,
            year_r,
            demographic_category_r,
            demographic_variable_r,
            num_total_days_r,
            num_days_absent_r,
            num_days_present_r,
            percent_attendance_r,
            num_chronically_absent_r,
            percent_chronically_absent_r,
        ] = row

        insert_str = f"""
        INSERT INTO absences
        (
            {dbn_h},
            {school_name_h},
            {grade_h},
            {year_h},
            {demographic_category_h},
            {demographic_variable_h},
            {num_total_days_h},
            {num_days_absent_h},
            {num_days_present_h},
            {percent_attendance_h},
            {num_chronically_absent_h},
            {percent_chronically_absent_h}
        )
        VALUES
        (
            "{str(dbn_r)}",
            "{str(school_name_r)}",
            "{str(grade_r)}",
            "{str(year_r)}",
            "{str(demographic_category_r)}",
            "{str(demographic_variable_r)}",
            "{str(num_total_days_r)}",
            "{str(num_days_absent_r)}",
            "{str(num_days_present_r)}",
            "{str(percent_attendance_r)}",
            "{str(num_chronically_absent_r)}",
            "{str(percent_chronically_absent_r)}"
        )
        """

        connect_and_insert(insert_str)


def create_tables():
    conn = sqlite3.connect("schools.db")
    sql_file = open("schema.sql")
    sql_tables = sql_file.read()

    conn.executescript(sql_tables)
    conn.commit()
    conn.close()

    sql_file.close()


if __name__ == "__main__":
    create_tables()

    dbn_csv = csv_to_list("./data/2018-DBN-ZIP-COORDINATES.csv")
    insert_dbn_data(dbn_csv)

    bullying_csv = csv_to_list("./data/2017-2018_BULLYING_HARASSMENT.csv")
    insert_bullying_data(bullying_csv)

    abscence_csv = csv_to_list("./data/2017-DATA.csv")
    insert_absence_data(abscence_csv)

    query_absences_table()