# tugrul-sualti-pyqtstream
Raspberry pi 4 uzerinden gelen goruntuyu masaustune aktarmak icin uygulama v0.2

tugrul-sualti reposundaki goruntu aktaranin bir ust versiyonu

launcher.py dosyasi sadece dosyalari manuel olarak yurutmek yerine bu isi otomatik gerceklestirmeye yariyor.
ui_main_window.py dosyasi kullanici arayuzunu sagliyor.
video_server.py dosyasi pi`dan gelen goruntuleri aliyor.

video_server.py dosyasindaki "self.ip" degiskeninin adresi: Win+R > cmd > ipconfig > Ethernet adapter Ethernet: > Autoconfiguration IPv4 Address. . : > 169.254.112.175 
(bu adres degisebilir(?)) 
AF_INET kullandigimiz icin IPv4 adresini aliyoruz.

Raspberry pi uzerinde origin.py, masaustunde launcher.py dosyasi calistiriyoruz. 
(once pi uzerinde origin.py calistirilmasi onemli gelmeyen goruntuyu masaustu uygulama aktaramaz)
Hatta baslangicta masaustu uygulama calistirilirsa uygulama yanit vermiyor.

-------
-------RASPBERRY PI-------
raspberry-pi klasorundeki origin.py dosyasi raspberry uzerinde calistirilacak. masaustunde olmasina gerek yok.

raspberry icinde kurulu kutuphaneler icin:
https://www.youtube.com/watch?v=QzVYnG-WaM4
    bu videodaki virtual-env olusturma ve kutuphanelere ek olarak:
        sudo apt-get install libopenblas-dev
        libopenblas-dev'de kurmam gerekti. 

-------

Dipnot: Baslangic kodu olarak > 
https://github.com/abhikesare9/live-streaming-with-opencv 
kullandim.
assets klasöründeki logo/iconlar bana ait değil.
      
