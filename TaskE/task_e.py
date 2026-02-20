# Copyright (c) 2026 Chuks isiozor
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

from datetime import datetime, date

DAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

def convert_data(line: list) -> list:
    """
    Convert data types to meet program requirements

    Parameters:
     line (list): Unconverted line -> 7 columns

    Returns:
     (list): Converted data types
    """

    return [
        datetime.fromisoformat(line[0]),
        int(line[1]),
        int(line[2]),
        int(line[3]),
        int(line[4]),
        int(line[5]),
        int(line[6]),
    ]
   # converted = []
   # converted.append(datetime.fromisoformat(line[0]))
   # converted.append(int(line[1]))
   # converted.append(int(line[2]))
   # converted.append(int(line[3]))
   # converted.append(int(line[4]))
   # converted.append(int(line[5]))
   # converted.append(int(line[6]))
   # return converted


def read_data(filename: str) -> list:
    """
    Reads the CSV file and returns the rows in a suitable structure.
    
    Parameters:
     filename (str): Name of the file containing the electricity consumption and production

    Returns:
     reservations (list): Read and converted consumption and production 
    
    """
    cons_prod = []

    with open(filename, "r", encoding="utf-8") as f:
        next(f)
        for line in f:
            line = line.strip()
            fields = line.split(";")
            cons_prod.append(convert_data(fields))
    
    return cons_prod

def day_information(day: date, database: list) -> str:
    """
    Reads the consumption and production per day.
    
    Parameters:
     day (date): Reportable day
     database (list): Consumption and production data + dates

    Returns:
     printable string 
    
    """

    cons_prod = ["day", "date", 0, 0, 0, 0, 0, 0]
    for per_hour in database:
        if per_hour[0].date() == day:
            for i in range(1, len(per_hour)):
                cons_prod[i + 1] += per_hour[i] / 1000
            cons_prod[0] = DAYS[day.weekday()]
            cons_prod[1] = day

    converted_cons_prod = f"{cons_prod[0]:<11}"
    converted_cons_prod += f"{cons_prod[1].strftime("%d.%m.%Y"):<13}"
    for i, element in enumerate(cons_prod):
        if i > 1:
            two_decimal_to_string = f"{element:.2f}".replace(".", ',')
            converted_cons_prod += f"{two_decimal_to_string:<8}"

    return converted_cons_prod + "\n"

def week_header(number: int) -> str:
    """
    Reads the week number

    Parameters:
     number (int): The week number

    Returns:
     printable string based on the week number 
    
    """

    header = f"Week {number} electricity consumption and production (kWh, by phase)\n\n"
    header += "Day        Date         Consumption [kWh]               Production [kWh]\n"
    header += "           (dd.mm.yyyy) v1      v2      v3              v1     v2     v3\n"
    header += "---------------------------------------------------------------------------\n"
    return header

def write_data(content: str):
    """
    Writes the content to the file.

    Parameters:
     content (str): Content
    
    """

    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(content)


    #consumption_phase1 = 0
    #consumption_phase2 = 0
    #consumption_phase3 = 0
    #production_phase1 = 0
    #production_phase2 = 0
    #production_phase3 = 0
    #for per_hour in database:
        #print(type(per_hour[0].date()))
     #   if per_hour[0].date() == day:
     #       consumption_phase1 += per_hour[1]/1000
     #       consumption_phase2 += per_hour[2]/1000
     #       consumption_phase3 += per_hour[3]/1000
     #       production_phase1 += per_hour[4]/1000
     #       production_phase2 += per_hour[5]/1000
     #       production_phase3 += per_hour[6]/1000 

    #cp1 =  f"{consumption_phase1:.2f}".replace(".", ",")
    #cp2 =  f"{consumption_phase2:.2f}".replace(".", ",")
    #cp3 =  f"{consumption_phase3:.2f}".replace(".", ",")
    #pp1 =  f"{production_phase1:.2f}".replace(".", ",")
    #pp2 =  f"{production_phase2:.2f}".replace(".", ",")
    #pp3 =  f"{production_phase3:.2f}".replace(".", ",")           

    #return f'{day.strftime("%d.%m.%Y"):<13}'+f"{cp1:<8}"+f"{cp2:<8}"+f"{cp3:<16}"+f"{pp1:<8}"+f"{pp2:<8}"+f"{pp3:<8}"
    


def main() -> None:
    """
    Main function: reads data, computes daily totals, and prints the report.
    """
    db = read_data("week41.csv")
    file_content = week_header(41)
    for i in range(6, 13):
        file_content += day_information(date(2025, 10, i), db)


    db = read_data("week42.csv")
    file_content += "\n" + week_header(42)
    for i in range(13, 20):
        file_content += day_information(date(2025, 10, i), db)  

    db = read_data("week43.csv")
    file_content += "\n" + week_header(43)
    for i in range(20, 27):
        file_content += day_information(date(2025, 10, i), db)

    write_data(file_content)   
    #print("Week 42 electricity consumption and production (kWh, by phase)", end="\n\n")
    #print("Day        Date         Consumption [kWh]               Production [kWh]")
    #print("           (dd.mm.yyyy) v1      v2      v3              v1     v2     v3")
    #print("---------------------------------------------------------------------------")
    #print(f"{DAYS[0]:<10}", day_information(date(2025, 10, 13), db))
    #print(f"{DAYS[1]:<10}", day_information(date(2025, 10, 14), db))
    #print(f"{DAYS[2]:<10}", day_information(date(2025, 10, 15), db))
    #print(f"{DAYS[3]:<10}", day_information(date(2025, 10, 16), db))
    #print(f"{DAYS[4]:<10}", day_information(date(2025, 10, 17), db))
    #print(f"{DAYS[5]:<10}", day_information(date(2025, 10, 18), db))
    #print(f"{DAYS[6]:<10}", day_information(date(2025, 10, 19), db))

if __name__ == "__main__":
    main()