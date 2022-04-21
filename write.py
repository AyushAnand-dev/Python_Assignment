import csv
with open('text2.txt', "r", encoding='utf-8') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('main.csv', 'w', encoding='utf-8') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Name', '           ', 'Phone', '         ', 'Mobile', '               ',
                        'Email', '              ', 'Office_Address', '                     ', 'Residence_Address'))
        writer.writerows(lines)
