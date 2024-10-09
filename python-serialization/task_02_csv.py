#!/usr/bin/env python3
"""
Importing csv and json
"""

import csv
import json


def convert_csv_to_json(csvFile):
    """
    Reads a CSV file, converts it to JSON format, and writes it to data.json.
    """

    try:
        with open(csvFile, mode="r", newline="", encoding="utf-8") as csvFile:
            csvReader = csv.DictReader(csvFile)
            data = list(csvReader)

        with open("data.json", mode="w", encoding="utf-8") as jsonFile:
            json.dump(data, jsonFile, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csvFile}' was not found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
