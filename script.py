import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(credentials)
sheet = client.open("Ponto IFTTT").get_worksheet(1)

months = {"January": 1,
	"February": 2,
	"March": 3,
	"April": 4,
	"May": 5,
	"June": 6,
	"July": 7,
	"August": 8,
	"September": 9,
	"October": 10,
	"November": 11,
	"December": 12
}

current_day = sheet.findall(str(datetime.now().day))

exit = current_day[-1]
entrance = current_day[-2]

exit_register_occurrence = sheet.cell(exit.row, 1).value
entrance_register_occurrence = sheet.cell(entrance.row, 1).value

exit_time = sheet.cell(exit.row, 6).value
entrance_time = sheet.cell(entrance.row, 6).value

month = sheet.cell(exit.row, 2).value
month_number = months[month]

print("registro: " + exit_register_occurrence + " horário: " + exit_time)
print("registro: " + entrance_register_occurrence + " horário: " + entrance_time)
print("month: " + month + " month number: " + str(month_number))