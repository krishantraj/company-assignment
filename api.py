# Request
# {
# “data”:[“A”,”1”,”3”,”4”,”R”,”!”] }
# Response
# {
# “is_success”: true,
# “user_id”: “john_doe_17091999”,
# “count”: “5”,
# “email” : “john@xyz.com”,
# “roll_number”:”ABCD123”,
# “numbers”: [“1”, “3”, “4”],
# “alphabets”: [“A”,”R”]
# }
import numbers
from flask import Flask, request, jsonify ,json
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
  
def frequentdates():
  try:
   
    json_data = request.get_json()
    data = []
    data = json_data['data']

    alpha = []
    num = []
    special = []
    for i in range(len(data)):
        if (data[i].isdigit()):
            num.append(data[i])
        elif((data[i] >= 'A' and data[i] <= 'Z') or
             (data[i] >= 'a' and data[i] <= 'z')):
            alpha.append( data[i])
        else:
            special.append(data[i])
 
    print(alpha)
    print(num )
    print(special)
    
    if true:
      is_success = "true"
    else:
      is_success = "false"
          
    return jsonify({"is_success": is_success, "user_id": "Krishant_19012001", "count": len(data), "email" : "1906030@kiit.ac.in", "roll_number":"1906030","alphabet":alpha,"numbers": num})
  
  except:
    return jsonify({"is_success":"false"})
  finally:
    return jsonify({"is_success":"false"})

if __name__ == '__main__':
  app.run(debug = True,host="0.0.0.0", port=7777)

  ##COMMANDS TO EXECUTE : py app_try.py




