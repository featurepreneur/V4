from re import X, search
from typing import get_origin
from flask import Flask, render_template
import json

app = Flask(__name__)



@app.route('/')
def index():
    shelf1 = ""
    search1 = ""
    product1 = ""
    di = {}
    with open('scetl_prod_2021_12_31.log', 'r') as log_file:
    
        
        
        for line in log_file:

  
            if line.startswith('INFO:root: Thu Dec 30 23:10:54 2021: time_taken.schedule_shelf'):
                shelf1 = line[65: ]
                # shelf2 = int(shelf1) / 60
                
                shelf2 = shelf1[0:3]
                print(shelf2)
                shelf3 = round(float(shelf2) / 60, 2)
                print(shelf3)


            if line.startswith('INFO:root: Thu Dec 30 23:10:50 2021: time_taken.schedule_search : '):
                search1 = line[65: ]
                search2 = search1[0: 6]
                print(search2)
                search3 = round(float(search2) / 60, 2)
                print(search3)



            if line.startswith('INFO:root: Thu Dec 30 23:07:27 2021: time_taken.schedule_product : '):
                product1 = line[66: ]
                product2 = product1[0: 6]
                print(product2)
                product3 = round(float(product2) / 60, 2)
                print(product3)

            if line.startswith('INFO:root: Thu '):
                date1 = line[14: ]
                date2 = date1[0: 7]
        print(date2)

        #             if line.startswith('INFO:root: Thu Dec 30 23:10:54 2021: time_taken.schedule_shelf : ' ):
                    
        #                 shelf1 = line[65: ]
        #                 print(shelf1)
        #                 # di = {
           
        #                 #     "shelf": shelf1
        #                 # }
            

                        
        # for line in log_file: 
        #             if line.startswith('INFO:root: Thu Dec 30 23:10:50 2021: time_taken.schedule_search : '):
        #                 search1 = line[65: ]
        #                 print(search1)
        #                 # di = {
            
        #                 #     "search": search1
        #                 # }

        # for line in log_file:
        #             if line.startswith('INFO:root: Thu Dec 30 23:07:27 2021: time_taken.schedule_product : '):
                        
       
        #                 product1 = line[66: ]
        #                 print(product1)
                        # di = {
                        #     "product": product1
                        # }
            


        di = {
            "product": product3,
            "shelf": shelf3,
            "search": search3
        }

        json_object = json.dumps(di, indent = 4)

        with open("file.json", "w") as outfile:
            outfile.write(json_object)

        
            

    return render_template("info.html", result1=shelf3, result2=search3, result3=product3, result4= shelf2, result5=search2, result6= product2, date= date2)
            


if __name__ == '__main__':
    app.run(debug=True)

