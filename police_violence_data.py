from flask import Flask, request, jsonify
# import pandas as pd

app = Flask(__name__)



data_store = {'incidents' : [
	{'name':'sally','age':15,'gender':'m','img_url':'http://cdn-r2.unilad.co.uk/wp-content/uploads/2015/12/person-of-the-year-2.jpg'},
	{'name':'mike','age':45,'gender':'f','img_url':'http://i.telegraph.co.uk/multimedia/archive/03491/Vladimir_Putin_1_3491835k.jpg'},
	{'name':'justin','age':25,'gender':'m','img_url':'http://images.amcnetworks.com/amc.com/wp-content/uploads/2015/05/MM_714_JM_0623_1545.jpg'},
	{'name':'jim','age':99,'gender':'m','img_url':'https://i.kinja-img.com/gawker-media/image/upload/s--LJ4kR8Aa--/c_scale,fl_progressive,q_80,w_800/197gkt72jr0e1jpg.jpg'}
	]}

# df = pd.read_csv('police_killings_clean.csv')

# Zipcodes is a list, e.g., [11238,90601]
def get_incidents(zipcodes):
	# print(zipcodes)
	# zipcodes = [int(zipcode) for zipcode in zipcodes]
	# incidents = list(df[df.zipcode.isin(zipcodes)].T.to_dict().values())
	# return {'incidents':incidents}
	return data_store


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/police_data", methods=['GET'])
def get_police_data():
	zipcode = request.args.getlist('zipcode')
	incidents = get_incidents(zipcode)
	return jsonify(incidents)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)