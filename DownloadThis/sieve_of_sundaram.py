import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import nth_prime
from sympy import primepi


scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\jacks\\OneDrive\\Desktop\\Coding\\Prime Generator\\secret_key.json', scopes=scopes)

file = gspread.authorize(creds)
workbook = file.open('Prime Generation')
sheet = workbook.worksheet('v_4')

def SieveOfSundaram(n):
    prime_list = [2]
    nNew = int((n - 1) / 2)
    marked = [0] * (nNew + 1)
    start_time = time.perf_counter_ns()
    for i in range(1, (nNew + 1)):
        j = i
        while (i + j + (2 * i * j)) <= nNew:
            marked[i + j + (2 * i * j)] = 1
            j += 1

    for i in range(1, nNew + 1):
        if marked[i] == 0:
            prime_list.append((2 * i + 1))
    end_time = time.perf_counter_ns()
    overall_time = end_time - start_time

    return overall_time

runs = 0
n = 10
while runs < 100:
    start_time = time.perf_counter_ns()
    primes = nth_prime.nth_prime(n)
    lower, upper = nth_prime.bounds(5000)
    previous = primepi(lower)
    num = primes[n - previous - 1]
    SieveOfSundaram(num)
    end_time = time.perf_counter_ns()
    overall_time = end_time - start_time
    cell = f'B{runs + 3}'
    sheet.update_acell(cell, overall_time)
    runs += 1



