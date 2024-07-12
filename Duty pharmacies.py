from tkinter import *
from tkintermapview import TkinterMapView
import requests
ip_request = requests.get('https://get.geojs.io/v1/ip.json')
ipadd2 =ip_request.json()['ip']
url = 'https://get.geojs.io/v1/ip/geo/'+ipadd2+'.json'
geo = requests.get(url)
geo_data =geo.json()

count =geo_data['country']

root = Tk()
root.geometry('1000x480')
root.title("hospitall الصيدليات المناوبة")

root.configure(background='white')
#========توابع الصيدليات
def markazi():
    map = TkinterMapView(root,width=500,height=400,corner_radius=0)
    map.place(x=470,y=45)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_position(35.364423794563905, 35.933318898319996)
    map.set_zoom(15)
    marker = map.set_marker(35.364423794563905, 35.933318898319996)
    marker.set_text('najm(صيدلية جنان سكيف)')







def cu():
    #country = en.get()
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map.set_address(count,marker=True)






#----------------title-

title1 = Label(root,text='الصيدليات المناوبة',
               fg='white',
               bg='black',
               font=('Tajawal',18),


               )
title1.pack(fill='x')
#--------------------------logo--------



#=============label+entry+button=====
l = Label(root,text='country:',font=('Tajawal 13'),fg='black',bg='white')
l.place(x=10,y=260)

en = Entry(root,font=('Tajawal',14),width=10,relief=GROOVE,bd=1)
en.place(x=140,y=260)

b1 = Button(root,text='get country',bg='black',fg='white',bd=1,relief=SOLID,width=10,
            cursor='hand2',
            command=cu
            )
b1.place(x=260,y=260)

#====================الصيدليات

b= Button(

    root,
    text='صيدلية مركزية',
    cursor='hand2',
    bg='blue',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal',12),
    width=13,
    command=markazi


)
b.place(x=10,y=300)

b1= Button(

    root,
    text='صيدليةمزرعه',
    cursor='hand2',
    bg='blue',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal',12),
    width=13


)
b1.place(x=140,y=300)


b2= Button(

    root,
    text='صيدلية الطحان',
    cursor='hand2',
    bg='blue',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal',12),
    width=13


)
b2.place(x=280,y=300)

b3= Button(

    root,
    text='صيدلية جباصيني',
    cursor='hand2',
    bg='blue',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal',12),
    width=13


)
b3.place(x=10,y=340)

b4= Button(

    root,
    text='صيدليةملقي',
    cursor='hand2',
    bg='blue',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal',12),
    width=13


)
b4.place(x=10,y=380)

b5= Button(

    root,
    text='صيدلية مجتهد',
    cursor='hand2',
    bg='blue',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal',12),
    width=13


)
b5.place(x=140,y=340)

b6= Button(

    root,
    text='صيدلية غزالي',
    cursor='hand2',
    bg='blue',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal',12),
    width=13


)
b6.place(x=280,y=340)

b7= Button(

    root,
    text='صيدلية حفار',
    cursor='hand2',
    bg='blue',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal',12),
    width=13


)
b7.place(x=140,y=380)


b8= Button(

    root,
    text='صيدليةالشهبندر',
    cursor='hand2',
    bg='blue',
    fg='black',
    bd=1,
    relief=SOLID,
    font=('Tajawal',12),
    width=13


)
b8.place(x=280,y=380)


map = TkinterMapView(root , width=500,height=400,corner_radius=0)
map.place(x=470,y=45)







root.mainloop()