import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\jacks\\OneDrive\\Desktop\\Coding\\Prime Generator\\secret_key.json', scopes=scopes)

file = gspread.authorize(creds)
workbook = file.open('Prime Generation')
sheet = workbook.worksheet('v_2')

runs = 0
while runs < 16:
    num = 100
    prime_list = [2, 3]
    primes = 2
    start_time = time.perf_counter_ns()
    while primes < num:
        for i in range(5, (2 ** num)):
            sum = 0
            for prime in prime_list:
                if i % prime == 0:
                    sum += 1
            if sum == 0:
                prime_list.append(i)
                primes += 1
            if len(prime_list) == num:
                break
    end_time = time.perf_counter_ns()
    overall_time = end_time - start_time
    cell = f'C{(runs + 87)}'
    sheet.update_acell(cell, overall_time)
    runs += 1