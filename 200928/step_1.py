f = open('nginx_logs_head.txt', 'r', encoding='utf-8')

file_data = f.readlines()
#for row in file_data:
#    row = row.strip()
for row in file_data:
    row = row.strip()
    print(row)