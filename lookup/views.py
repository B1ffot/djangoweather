from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=6FFCEC32-2C6B-4A85-AFFD-4EF379221A19")
		
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
	   			category_description = "Good!"
	   			category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate":
	   			category_description = "moderate"
	   			category_color = "moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
	   			category_description = "Unhealthy For Sensitive Groups"
	   			category_color = "usg"
		elif api[0]['Category']['Name'] == "Unhealthy":
	   	 		category_description = "Unhealthy"
	   	 		category_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy": 
	  	 		category_description = "Very Unhealthy"
	  	 		category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous" :
	  	 		category_description = "Hazardous"
	  	 		category_color = "Hazardous"

	   	


		return render(request, 'home.html', {'api':api,
			'category_description':category_description,
			'category_color':category_color})

		


	else:

		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=6FFCEC32-2C6B-4A85-AFFD-4EF379221A19")
		
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
	   			category_description = "Good!"
	   			category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate":
	   			category_description = "Moderate"
	   			category_color = "moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
	   			category_description = "Unhealthy For Sensitive Groups"
	   			category_color = "usg"
		elif api[0]['Category']['Name'] == "Unhealthy":
	   	 		category_description = "Unhealthy"
	   	 		category_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy": 
	  	 		category_description = "Very Unhealthy"
	  	 		category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous" :
	  	 		category_description = "Hazardous"
	  	 		category_color = "Hazardous"

	   	


		return render(request, 'home.html', {'api':api,
			'category_description':category_description,
			'category_color':category_color})

	