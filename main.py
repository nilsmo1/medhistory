import json
import sys

from datetime import datetime
from os.path import exists

def display_history(record):
    print("\nPrevious entries:")
    for r in record[-3:][::-1]:
        r_time = r["time"]
        r_substance = r["substance"]
        r_dosage = r["dosage"]
        print(f"({r_time})\t{r_substance}, {r_dosage}")
    print()

def main():
    record_path = "record.json"
    now = datetime.utcnow().strftime("%d/%m/%Y %H:%M")
    
    record = []
    if exists(record_path):
        with open(record_path) as record_read: 
            record = json.load(record_read)
    
    if record:
        display_history(record)

    substance = ""
    while not substance:
        substance = input("Which substance did you take? ")
    dosage = input("What dosage? (mg): ")
    units = "mg" if dosage else ""
    record_obj = {"time": now, "substance": substance.capitalize(), "dosage": f"{dosage or '-'}{units}"}
    
    print()
    for item, value in record_obj.items():
        print(f"{item:>9} : {value}")
    print()
    submit = input("Submit record? [y/n] ")
    if not submit.lower().startswith("y") and submit:
        print("aborting submission..")
        sys.exit()
       
    record.append(record_obj)
    with open(record_path, "w") as record_write:
        json.dump(record, record_write, indent=4, separators=(",",": "))

    display_history(record)

if __name__ == "__main__": main()
