
def select_bully_table():
    query_str = """SELECT 
    bullying.*, 
    schools.location, 
    schools.postal_code, 
    schools.coordinates 
    FROM bullying 
    JOIN schools ON bullying.dbn = schools.dbn 
    ORDER BY id;
    """

    return query_str

def query_consolidated():
    query_str = """SELECT
    "consolidated_absences".*,
    bullying.complaints,
    bullying.material_incidents,
    schools.location,
    schools.postal_code,
    schools.coordinates
    FROM consolidated_absences 
    LEFT JOIN schools ON schools.dbn = consolidated_absences.dbn
    LEFT JOIN bullying ON schools.dbn = bullying.dbn
    ORDER by id;
    """

    return query_str


def query_all():
    query_str = """SELECT
    "consolidated_absences".*,
    bullying.complaints,
    bullying.material_incidents,
    schools.location,
    schools.postal_code,
    schools.coordinates
    FROM consolidated_absences 
    LEFT JOIN schools ON schools.dbn = consolidated_absences.dbn
    LEFT JOIN bullying ON schools.dbn = bullying.dbn
    WHERE schools.location IS NOT NULL
    ORDER BY id;
    """

    return query_str

def query_absences():
    query_str = """SELECT
    absences.*,
    bullying.complaints,
    bullying.material_incidents,
    schools.location,
    schools.postal_code,
    schools.coordinates
    from absences 
    LEFT JOIN schools ON schools.dbn = absences.dbn
    LEFT JOIN bullying ON schools.dbn = bullying.dbn
    WHERE schools.location IS NOT NULL
    ORDER BY id;
    """

    return query_str