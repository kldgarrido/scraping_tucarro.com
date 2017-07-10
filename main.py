from mycore import execute
from setting import params

url = params['url']
tag = params['tag']


result = execute(url, tag)

for item in result:
    print(item)

#dataframe.to_csv('output.txt', sep='\t', header=False)