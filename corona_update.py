#get update corona status
from covid import Covid
covid = Covid()
cases= covid.get_status_by_country_name('india')
for i in cases:
    print(i,':', cases[i])