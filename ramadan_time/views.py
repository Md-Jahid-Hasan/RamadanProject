from django.shortcuts import render
from .models import District, sehri_iftar_time
import datetime

# Create your views here.
def test(request):

    sehri_district_time = [(1,["Manikganj","Bogura","Sirajganj","Panchagarh","Nilphamari"]),
    (2, ["Bhola","Shariatpur", "Dinajpur", "Thakurgaon", "Joypurhat", "Faridpur", "Madaripur", "Barisharl"]),
    (3, ["Naogoan","Jhalokati"]),
    (4, ["Natore","Pabna","Rajbari", "Magura", "Patuakhali","Gopalganj"]),
    (5, ["Kushtia", "Rajshahi", "Pirojpur", "Borguna", "Narail", "Bagherhat", "Jhenaidah"]),
    (6, ["Chapai Nababganj", "Jessore", "Chuadanga", "Khulna"]),
    (7, ["Meherpur"]),
    (8, ["Satkhira"]),
    (-1,["Gazipur", "Lakshmipur", "Rongpur", "Noakhali", "Gaibandha", "Cox's Bazar"]),
    (-2,["Sherpur", "Jamalpur", "Kurigram", "Lalmonirhat", "Chittagong", "Narsingdi"]),
    (-3,["Comilla", "Mymensingh", "Kishoregonj", "Feni"]),
    (-4, ["Brahmanbaria", "Rangamati", "Bandarban"]),
    (-5, ["Netrakona", "Khagrachari"]),
    (-6, ["Habiganj"]),
    (-7, ["Sunamganj"]),
    (-8, ["Maulvibazar"]),
    (-9, ["Sylhet"])
    ]

    ifatr_dis_time = [(1, ["Gopalganj", "Mymensingh", "Bagherhat"]),
                      (2, ["Narail", "Faridpur", "Khulna", "Manikganj", "Tangail"]),
                      (3, ["Magura", "Sherpur"]),
                      (4, ["Sirajganj", "Jamalpur", "Rajbari", "Satkhira", "Jessore"]),
                      (5, ["Kushtia", "Pabna", "Jhenaidah"]),
                      (6, ["Chuadanga", "Bogura", "Gaibandha"]),
                      (7, ["Natore", "Meherpur", "Kurigram", "Lalmonirhat"]),
                      (8, ["Rajshahi", "Naogaon", "Rangpur", "Jaipurhat"]),
                      (10, ["Nilphamari", "Dinajpur", "Chapai Nababganj"]),
                      (12, ["Panchagarh", "Thakurgaon"]),
                      (-1, ["Shariatpur", "Narsingdi", "Kishoregonj", "Narayanganj", "Munshiganj", "Jhalokati"]),
                      (-2, ["Barishal", "Patuakhali", "Borguna", "Sunamganj", "Chandpur"]),
                      (-3, ["Brahmanbaria", "Lakshmipur", "Bhola", "Habiganj"]),
                      (-4, ["Comilla", "Noakhali", "Sylhet", "Maulvibazar"]),
                      (-5, ["Feni"]),
                      (-8, ["Khagrachari", "Chitagong"]),
                      (-9, ["Rangamati"]),
                      (-10, ["Bandarban", "Cox's Bazar"]),]


    d_name = ""
    flag = False
    if request.method =='POST':
        d_name = request.POST.get('district')
        flag = True
        print(d_name)

    now = datetime.date.today()
    now2 = datetime.date.today()
    clock = datetime.datetime.now()
    hour = clock.hour

    if hour > 18:
        now = now + datetime.timedelta(days=1)

    print(now2)
    time = sehri_iftar_time.objects.get(date=now)
    dist = District.objects.all()

    for (t, dis) in ifatr_dis_time:
        for i in dis:
            if d_name == i:
                time.iftar_minute = time.iftar_minute + t

    for (t, dis) in sehri_district_time:
        for i in dis:
            if d_name == i:
                time.sehri_minute = time.sehri_minute + t

    print(type(time))



    passingvalue = {
        "dist": dist,
        "time": time,
        "now": now,
        "flag": flag

    }
    return render(request, 'home.html', passingvalue)