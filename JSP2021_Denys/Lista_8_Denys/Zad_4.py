import Open_zad4
import Save
file = (Open_zad4.open_file('C:\studia_s3\L_Python\JSP2021_Denys\pesel.txt'))

print(file[1][0:2])
year = []
month = []
day = []
sex = []
for i in range (0,10):
   q = str(1*int(file[i][0]) + 3*int(file[i][1]) + 7*int(file[i][2]) + 9*int(file[i][3]) + 1*int(file[i][4]) + 3*int(file[i][5]) + 7*int(file[i][6]) + 9*int(file[i][7]) + 1*int(file[i][8]) + 3*int(file[i][9]))
   q = int(q[len(q)-1])
   q = str(q-10)
   q = q[len(q)-1]
   if q == file[i][10]:
       year.append(file[i][0:2])
       month.append(file[i][2:4])
       day.append(file[i][4:6])
       sex.append(file[i][9])
Save.save_file_z4(file, day, month, year, sex)