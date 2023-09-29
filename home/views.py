from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.











def index (request):
    return render(request, 'index.html')
    


def home (request):
    if condition:
         print("Condition is true!")
        # if 'city' in request.GET:
        # if some_condition:
    # USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    # print("This is inside the if block.")
# def get_html_content(city):



    
def home (request):    
    if some_condition:
        city = request.GET.get('city')
        html_content = get_html_content(city)
        print(html_content) 
    # Code block for the if statement
    # print("Correct indentation")
    

        city = city. replace(' ', '+')
        USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        LANGUAGE = "en-US,en;q=0.5"
        session = requests.Session()
        session.headers['User-Agent'] = USER_AGENT
        session.headers['Accept-Language'] = LANGUAGE
        session.headers['Content-Language'] = LANGUAGE
        html_content=session.get(f'https://www.google.com/search?q=weather+{city}').text
        return html_content




    
def home (request):   
    wheather :None 
    if some_condition:
        city = request.GET.get('city')
        html_content = get_html_content(city)
        print(html_content)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        wheather =dict()
        # <span class="BBwThe">New York, NY, USA</span>
        wheather['region'] = soup.find('div', attrs={'id':'wob_loc'}).text
        wheather['dayhour'] = soup.find('div', attrs={'id':'wob_dts'}).text
        wheather['status'] = soup.find('span', attrs={'id':'wob_dc'}).text
        wheather['temp'] = soup.find('div', attrs={'id':'wob_tm'}).text
        print(weather)
       



    return render(request, 'WTR/home.html',{'weather': weather})    


