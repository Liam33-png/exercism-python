"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    treasure, coordinate = record
    return(coordinate)

def convert_coordinate(coordinate):
    return tuple(coordinate)
        

def compare_records(azara_record, rui_record):
    treasure, cordinate = azara_record
    treasure_b, coordinate_b, quadrant_b = rui_record
    return convert_coordinate(cordinate) == convert_coordinate(coordinate_b)


def create_record(azara_record, rui_record):
    if convert_coordinate(azara_record[1]) ==  convert_coordinate(rui_record[1]):
        return azara_record + rui_record
    else:
        return "not a match"

def clean_up(combined_record_group):
    report = []
    for record in combined_record_group:
        report.append(f"{(record[0],record[2], record[3], record[4])}\n")
    return "".join(report)
                
