from django.shortcuts import render

def home(request):
    import json
    import requests

    if request.method == "POST":
        station = request.POST['station']

        api_request = requests.get("http://openapi.seoul.go.kr:8088/password/json/bikeList/1/99")
        
        try : 
            api = json.loads(api_request.content) #api_request가 잘 가져왔으면 데이터를 json으로 파싱해서 저장하고,
            api_dict = api["rentBikeStatus"]["row"]
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api':api,'api_dict':api_dict,'station':station})
    else:

        api_request = requests.get("http://openapi.seoul.go.kr:8088/password/json/bikeList/1/99")
        
        try : 
            api = json.loads(api_request.content) #api_request가 잘 가져왔으면 데이터를 json으로 파싱해서 저장하고,
            api_dict = api["rentBikeStatus"]["row"]
        except Exception as e:
            api = "Error..."

    return render(request, 'home.html', {'api':api,'api_dict':api_dict})

def about(request):
    return render(request, 'about.html', {})
