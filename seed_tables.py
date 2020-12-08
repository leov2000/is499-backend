import sqlite3
from db_utils import connect_and_insert, csv_to_list, split_data, create_tables


def seed_consolidated_absences():
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


def seed_bullying_data(csv_list):
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


def seed_dbn_data(csv_list):
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


def seed_absence_data(csv_list):
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

if __name__ == "__main__":
    create_tables()

    dbn_csv = csv_to_list("./data/2018-DBN-ZIP-COORDINATES.csv")
    seed_dbn_data(dbn_csv)

    bullying_csv = csv_to_list("./data/2017-2018_BULLYING_HARASSMENT.csv")
    seed_bullying_data(bullying_csv)

    abscence_csv = csv_to_list("./data/2017-DATA.csv")
    seed_absence_data(abscence_csv)

    seed_consolidated_absences()