# tugrul-sualti-pyqtstream
Raspberry pi 4 uzerinden gelen goruntuyu masaustune aktarmak icin uygulama v0.2

tugrul-sualti reposundaki goruntu aktaranin bir ust versiyonu

launcher.py dosyasi sadece dosyalari manuel olarak yurutmek yerine bu isi otomatik gerceklestirmeye yariyor.
ui_main_window.py dosyasi kullanici arayuzunu sagliyor.
video_server.py dosyasi pi`dan gelen goruntuleri aliyor.

video_server.py dosyasindaki "self.ip" degiskeninin adresi: Win+R > cmd > ipconfig > Ethernet adapter Ethernet: > Autoconfiguration IPv4 Address. . : > 169.254.112.175 (bu adres degisebilir(?)) AF_INET kullandigimiz icin IPv4 adresini aliyoruz.

Raspberry pi uzerinde origin.py, masaustunde launcher.py dosyasi calistiriyoruz. (once pi uzerinde origin.py calistirilmasi onemli gelmeyen goruntuyu masaustu uygulama aktaramaz)
