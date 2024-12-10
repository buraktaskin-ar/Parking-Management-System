def dakikayi_gune_ve_saate(otoparkta_kalinan_dakika): # Dakikayı alıp güne saate ve dakikaya çeviren fonksiyon
    gun = otoparkta_kalinan_dakika // 1440
    kalan_dakika = otoparkta_kalinan_dakika % 1440
    saat = kalan_dakika // 60
    dakika = kalan_dakika % 60
    return gun, saat, dakika


def oran_bul(genel_toplam, orani_bulunacak_toplam):
    if genel_toplam > 0:
        oran = 100 * (orani_bulunacak_toplam / genel_toplam)
        return oran
    else:
        return 0


MOTOSIKLET_KOD = 1
BINEK_KOD = 2
MINIBUS_KOD = 3
OTOBUS_KOD = 4
KAMYON_KOD = 5
TIR_KOD = 6

AGIRLIGA_GORE_UCRET_SABITI = 2.5
GAZI_INDIRIM_ORANI = 100
ENGELLI_INDIRIM_ORANI = 50

motosiklet_sayisi = 0
binek_sayisi = 0
minibus_sayisi = 0
otobus_sayisi = 0
kamyon_sayisi = 0
tir_sayisi = 0

motorsiklet_geliri = 0
binek_geliri = 0
minibus_geliri = 0
otobus_geliri = 0
kamyon_geliri = 0
tir_geliri = 0

kalinan_sure_icin_ucret = 0

otoparkin_toplam_geliri = 0
agirligi_1_tondan_az_binek = 0
agirligi_10_tondan_fazla_okt = 0 # okt:otobüs-kamyon-tır
en_fazla_30_dk_mb = 0 # Otoparkta en fazla 30 dakika kalan motosiklet ve binek tipi araçların sayısı
bir_gunden_fazla_mo = 0 # Otoparkta bir günden fazla kalan minibüs ve otobüs sayısı
bir_gun = 1440 # Bir gün 1440 dakikadır.
surucusu_gazi_veya_engelli_olan_arac_sayisi = 0
gazi_arac_sayisi = 0
engelli_arac_sayisi = 0
uc_saatten_fazla_indirimli = 0 # Otoparkta 3 saatten fazla kalan ve indirim uygulanan araçların sayısı
uc_saat = 180
otuz_gun = 30 * 1440 # 30 gün 30*1440 dakikadır.
binden_fazla_gelir_veya_30_gun = 0
en_uzun_sure_otoparkta_kalandan_elde_edilen_gelir = 0
en_cok_gelir_elde_edilen_binek = 0 # En çok gelir elde edilen binek araçtan elde edilen gelir


motosiklet_otoparkta_kalma_suresi = 0
binek_otoparkta_kalma_suresi = 0
minibus_otoparkta_kalma_suresi = 0
otobus_otoparkta_kalma_suresi = 0
kamyon_otoparkta_kalma_suresi = 0
tir_otoparkta_kalma_suresi = 0
gazi_otoparkta_kalma_suresi = 0
engelli_otoparkta_kalma_suresi = 0

otoparkta_kalinan_en_uzun_sure = 0
arac_sinifi_kodu = 1
otoparki_kullanan_toplam_arac = 0
baska_arac = 'e'
while baska_arac == 'e':
    otopark_ucreti = 0
    arac_plakasi = input("Araç plakasını giriniz: ")
    arac_sinifi_kodu = int(input("Araç sınıfı kodunu giriniz: "))
    while arac_sinifi_kodu < 1 or arac_sinifi_kodu > 6:
        print("Araç sınıfı kodu 1 ve 6 değerleri arasında bir tamsayı olmalıdır.")
        arac_sinifi_kodu = int(input("Araç sınıfı kodunu giriniz: "))
    arac_agirligi = int(input("Araç ağırlığını kilogram cinsinden giriniz: "))
    while arac_agirligi <= 0:
        print("Araç ağırlığı 0 dan büyük olmalıdır.")
        arac_agirligi = int(input("Araç ağırlığını kilogram cinsinden giriniz: "))
    otoparkta_kalinan_sure = int(input("Otoparkta kalınan süreyi dakika cinsinden giriniz: "))
    while otoparkta_kalinan_sure <= 0:
        print("Otoparkta kalınan süre 0 dan büyük olmalıdır.")
        otoparkta_kalinan_sure = int(input("Otoparkta kalınan süreyi dakika cinsinden giriniz: "))
    ad_soyad = input("Sürücünün adını soyadını giriniz: ")

    otoparkta_kalinan_gun, otoparkta_kalinan_saat, otoparkta_kalinan_dakika = dakikayi_gune_ve_saate(otoparkta_kalinan_sure)
    otopark_ucreti += (arac_agirligi / 1000) * AGIRLIGA_GORE_UCRET_SABITI

    otoparkta_kalinan_surenin_saat_degeri = otoparkta_kalinan_sure / 60
    ucret_carpani = otoparkta_kalinan_surenin_saat_degeri // 24
    kalan_sure = otoparkta_kalinan_surenin_saat_degeri % 24
    kalinan_sure_icin_ucret = 0
    if ucret_carpani > 0:
        kalinan_sure_icin_ucret += 15 * ucret_carpani
    if kalan_sure > 0:
        if kalan_sure < 1:
            kalinan_sure_icin_ucret += 3
        elif kalan_sure < 3:
            kalinan_sure_icin_ucret += 5
        elif kalan_sure < 5:
            kalinan_sure_icin_ucret += 7
        elif kalan_sure < 10:
            kalinan_sure_icin_ucret += 10
        elif kalan_sure < 24:
            kalinan_sure_icin_ucret += 14
        else:
            kalinan_sure_icin_ucret += 15

    if arac_sinifi_kodu == MOTOSIKLET_KOD:
        arac_sinifi_adi = "Motosiklet"
        katsayi = 1
        motosiklet_sayisi += 1
        otopark_ucreti += kalinan_sure_icin_ucret * katsayi
        motosiklet_otoparkta_kalma_suresi += otoparkta_kalinan_sure

        surucunun_ozel_durumu = input(
            "Sürücünün özel durumu var mı? (Yok :y, Gazi: g, Engelli: e giriniz.): ").lower()
        while surucunun_ozel_durumu != 'y' and surucunun_ozel_durumu != 'g' and surucunun_ozel_durumu != 'e':
            surucunun_ozel_durumu = input(
                "Sürücünün özel durumu var mı? Lütfen yalnızca 'y', 'g' veya 'e' harflerini kullanınız: ").lower()
        if surucunun_ozel_durumu != 'y':
            surucusu_gazi_veya_engelli_olan_arac_sayisi += 1
            if otoparkta_kalinan_sure > uc_saat:
                uc_saatten_fazla_indirimli += 1
            if surucunun_ozel_durumu == "e":
                engelli_arac_sayisi += 1
                surucunun_ozel_durumu = "Engelli"
                uygulanan_indirim_orani = ENGELLI_INDIRIM_ORANI
                engelli_otoparkta_kalma_suresi += otoparkta_kalinan_sure
                otopark_ucreti *= 0.5
            elif surucunun_ozel_durumu == "g":
                gazi_arac_sayisi += 1
                surucunun_ozel_durumu = "Gazi"
                uygulanan_indirim_orani = GAZI_INDIRIM_ORANI
                gazi_otoparkta_kalma_suresi += otoparkta_kalinan_sure
                otopark_ucreti *= 0
            print(f"""
Sürücünün özel durumu: {surucunun_ozel_durumu}
Sürücüye uygulanan indirim oranı: %{uygulanan_indirim_orani}
""")
        motorsiklet_geliri += otopark_ucreti
    elif arac_sinifi_kodu == BINEK_KOD:

        arac_sinifi_adi = "Binek"
        katsayi = 2
        binek_sayisi += 1
        otopark_ucreti += kalinan_sure_icin_ucret * katsayi
        binek_otoparkta_kalma_suresi += otoparkta_kalinan_sure

        surucunun_ozel_durumu = input(
            "Sürücünün özel durumu var mı? (Yok :y, Gazi: g, Engelli: e giriniz.): ").lower()
        while surucunun_ozel_durumu != 'y' and surucunun_ozel_durumu != 'g' and surucunun_ozel_durumu != 'e':
            surucunun_ozel_durumu = input(
                "Sürücünün özel durumu var mı? Lütfen yalnızca 'y', 'g' veya 'e' harflerini kullanınız: ").lower()
        if surucunun_ozel_durumu != 'y':
            surucusu_gazi_veya_engelli_olan_arac_sayisi += 1
            if otoparkta_kalinan_sure > uc_saat:
                uc_saatten_fazla_indirimli += 1
            if surucunun_ozel_durumu == "e":
                engelli_arac_sayisi += 1
                surucunun_ozel_durumu = "Engelli"
                uygulanan_indirim_orani = ENGELLI_INDIRIM_ORANI
                engelli_otoparkta_kalma_suresi += otoparkta_kalinan_sure
                otopark_ucreti *= 0.5
            elif surucunun_ozel_durumu == "g":
                gazi_arac_sayisi += 1
                surucunun_ozel_durumu = "Gazi"
                uygulanan_indirim_orani = GAZI_INDIRIM_ORANI
                gazi_otoparkta_kalma_suresi += otoparkta_kalinan_sure
                otopark_ucreti *= 0
            print(f"""
Sürücünün özel durumu: {surucunun_ozel_durumu}
Sürücüye uygulanan indirim oranı: %{uygulanan_indirim_orani}
""")
        binek_geliri += otopark_ucreti
    elif arac_sinifi_kodu == MINIBUS_KOD:
        arac_sinifi_adi = "Minibüs"
        katsayi = 3
        minibus_sayisi += 1
        otopark_ucreti += kalinan_sure_icin_ucret * katsayi
        minibus_geliri += otopark_ucreti
        minibus_otoparkta_kalma_suresi += otoparkta_kalinan_sure
    elif arac_sinifi_kodu == OTOBUS_KOD:
        arac_sinifi_adi = "Otobüs"
        katsayi = 3
        otobus_sayisi += 1
        otopark_ucreti += kalinan_sure_icin_ucret * katsayi
        otobus_geliri += otopark_ucreti
        otobus_otoparkta_kalma_suresi += otoparkta_kalinan_sure
    elif arac_sinifi_kodu == KAMYON_KOD:
        arac_sinifi_adi = "Kamyon"
        katsayi = 4
        kamyon_sayisi += 1
        otopark_ucreti += kalinan_sure_icin_ucret * katsayi
        kamyon_geliri += otopark_ucreti
        kamyon_otoparkta_kalma_suresi += otoparkta_kalinan_sure
    else:
        arac_sinifi_adi = "Tır"
        katsayi = 4
        tir_sayisi += 1
        otopark_ucreti += kalinan_sure_icin_ucret * katsayi
        tir_geliri += otopark_ucreti
        tir_otoparkta_kalma_suresi += otoparkta_kalinan_sure

    if arac_sinifi_kodu == BINEK_KOD and en_cok_gelir_elde_edilen_binek < otopark_ucreti:
        en_cok_gelir_elde_edilen_binek = otopark_ucreti
        en_uzun_binek_gun, en_uzun_binek_saat, en_uzun_binek_dakika = dakikayi_gune_ve_saate(otoparkta_kalinan_sure)

    if otopark_ucreti > 1000 or otoparkta_kalinan_sure > otuz_gun:
        binden_fazla_gelir_veya_30_gun += 1

    if arac_sinifi_kodu == BINEK_KOD and arac_agirligi < 1000:
        agirligi_1_tondan_az_binek += 1

    if (arac_sinifi_kodu == OTOBUS_KOD or arac_sinifi_kodu == KAMYON_KOD or arac_sinifi_kodu == TIR_KOD) and arac_agirligi > 10000:
        agirligi_10_tondan_fazla_okt += 1

    if otoparkta_kalinan_en_uzun_sure < otoparkta_kalinan_sure:
        otoparkta_kalinan_en_uzun_sure = otoparkta_kalinan_sure
        en_uzun_sure_gun, en_uzun_sure_saat, en_uzun_sure_dakika = dakikayi_gune_ve_saate(otoparkta_kalinan_en_uzun_sure)
        en_uzun_sure_otoparkta_kalandan_elde_edilen_gelir = otopark_ucreti

    if (arac_sinifi_kodu == MOTOSIKLET_KOD or arac_sinifi_kodu == BINEK_KOD) and otoparkta_kalinan_sure <= 30:
        en_fazla_30_dk_mb += 1

    if (arac_sinifi_kodu == MINIBUS_KOD or arac_sinifi_kodu == OTOBUS_KOD) and otoparkta_kalinan_sure > bir_gun:
        bir_gunden_fazla_mo += 1

    otoparki_kullanan_toplam_arac += 1
    otoparkin_toplam_geliri += otopark_ucreti

    print(f"""
Araç plakası: {arac_plakasi}
Araç sınıfının adı: {arac_sinifi_adi}
Araç ağırlığı: {arac_agirligi} kg
Aracın otoparkta kaldığı süre: {otoparkta_kalinan_gun} gün {otoparkta_kalinan_saat} saat {otoparkta_kalinan_dakika} dakika
Sürücünün adı soyadı: {ad_soyad}
Otopark ücreti: {otopark_ucreti:.2f} TL 
        """)
    baska_arac = input("Otoparkta başka araç var mı? (e/h): ").lower()
    while baska_arac != "e" and baska_arac != "h":
        baska_arac = input("Otoparkta başka araç var mı? Lütfen sadece 'e' veya 'h' giriniz. (e/h): ").lower()

motosikletlerin_tum_araclar_icindeki_orani = oran_bul(otoparki_kullanan_toplam_arac, motosiklet_sayisi)
bineklerin_tum_araclar_icindeki_orani = oran_bul(otoparki_kullanan_toplam_arac, binek_sayisi)
minibuslerin_tum_araclar_icindeki_orani = oran_bul(otoparki_kullanan_toplam_arac, minibus_sayisi)
otobuslerin_tum_araclar_icindeki_orani = oran_bul(otoparki_kullanan_toplam_arac, otobus_sayisi)
kamyonlarin_tum_araclar_icindeki_orani = oran_bul(otoparki_kullanan_toplam_arac, kamyon_sayisi)
tirlarin_tum_araclar_icindeki_orani = oran_bul(otoparki_kullanan_toplam_arac, tir_sayisi)

motosikletlerin_toplam_gelir_orani = oran_bul(otoparkin_toplam_geliri, motorsiklet_geliri)
bineklerin_toplam_gelir_orani = oran_bul(otoparkin_toplam_geliri, binek_geliri)
minibuslerin_toplam_gelir_orani = oran_bul(otoparkin_toplam_geliri, minibus_geliri)
otobuslerin_toplam_gelir_orani = oran_bul(otoparkin_toplam_geliri, otobus_geliri)
kamyonlarin_toplam_gelir_orani = oran_bul(otoparkin_toplam_geliri, kamyon_geliri)
tirlarin_toplam_gelir_orani = oran_bul(otoparkin_toplam_geliri, tir_geliri)

motorsiklet_ortalama_geliri = motorsiklet_geliri / motosiklet_sayisi
binek_ortalama_geliri = binek_geliri / binek_sayisi
minibus_ortalama_geliri = minibus_geliri / minibus_sayisi
otobus_ortalama_geliri = otobus_geliri / otobus_sayisi
kamyon_ortalama_geliri = kamyon_geliri / kamyon_sayisi
tir_ortalama_geliri = tir_geliri / tir_sayisi

agirligi_1_tondan_az_binek_orani = oran_bul(binek_sayisi, agirligi_1_tondan_az_binek)
agirligi_10_tondan_fazla_okt_orani = oran_bul(otobus_sayisi + kamyon_sayisi + tir_sayisi, agirligi_10_tondan_fazla_okt)
otoparkta_30_dk_az_bm_oran = oran_bul(motosiklet_sayisi + binek_sayisi, en_fazla_30_dk_mb)
otoparkta_bir_gunden_fazla_mo_oran = oran_bul(minibus_sayisi + otobus_sayisi, bir_gunden_fazla_mo)
binden_fazla_gelir_veya_30_gun_oran = oran_bul(otoparki_kullanan_toplam_arac, binden_fazla_gelir_veya_30_gun)
gazi_veya_engelli_oran = oran_bul(otoparki_kullanan_toplam_arac, surucusu_gazi_veya_engelli_olan_arac_sayisi)
uc_saatten_fazla_indirimli_oran = oran_bul(surucusu_gazi_veya_engelli_olan_arac_sayisi, uc_saatten_fazla_indirimli)

gazi_oran = oran_bul(otoparki_kullanan_toplam_arac, gazi_arac_sayisi)
engelli_oran = oran_bul(otoparki_kullanan_toplam_arac, engelli_arac_sayisi)

motorsiklet_otoparkta_kalma_gun, motorsiklet_otoparkta_kalma_saat, motorsiklet_otoparkta_kalma_dakika = dakikayi_gune_ve_saate(motosiklet_otoparkta_kalma_suresi // motosiklet_sayisi)
binek_otoparkta_kalma_gun, binek_otoparkta_kalma_saat, binek_otoparkta_kalma_dakika = dakikayi_gune_ve_saate(binek_otoparkta_kalma_suresi // binek_sayisi)
minibus_otoparkta_kalma_gun, minibus_otoparkta_kalma_saat, minibus_otoparkta_kalma_dakika = dakikayi_gune_ve_saate(minibus_otoparkta_kalma_suresi // minibus_sayisi)
otobus_otoparkta_kalma_gun, otobus_otoparkta_kalma_saat, otobus_otoparkta_kalma_dakika = dakikayi_gune_ve_saate(otobus_otoparkta_kalma_suresi // otobus_sayisi)
kamyon_otoparkta_kalma_gun, kamyon_otoparkta_kalma_saat, kamyon_otoparkta_kalma_dakika = dakikayi_gune_ve_saate(kamyon_otoparkta_kalma_suresi // kamyon_sayisi)
tir_otoparkta_kalma_gun, tir_otoparkta_kalma_saat, tir_otoparkta_kalma_dakika = dakikayi_gune_ve_saate(tir_otoparkta_kalma_suresi // tir_sayisi)
gazi_otoparkta_kalma_gun, gazi_otoparkta_kalma_saat, gazi_otoparkta_kalma_dakika = dakikayi_gune_ve_saate(gazi_otoparkta_kalma_suresi // gazi_arac_sayisi)
engelli_otoparkta_kalma_gun, engelli_otoparkta_kalma_saat, engelli_otoparkta_kalma_dakika = dakikayi_gune_ve_saate(engelli_otoparkta_kalma_suresi // engelli_arac_sayisi)

print(f"""
Otoparkı kullanan toplam araç sayısı: {otoparki_kullanan_toplam_arac} araç

Motorsiklet sayısı: {motosiklet_sayisi} tane. Motorsikletlerin tüm araçlar içindeki oranı: %{motosikletlerin_tum_araclar_icindeki_orani:.2f}
Binek araç sayısı: {binek_sayisi} tane. Binek araçların tüm araçlar içindeki oranı: %{bineklerin_tum_araclar_icindeki_orani:.2f} 
Minibüs sayısı: {minibus_sayisi} tane. Minibüslerin tüm araçlar içindeki oranı: %{minibuslerin_tum_araclar_icindeki_orani:.2f}
Otobüs sayısı: {otobus_sayisi} tane. Otobüslerin tüm araçlar içindeki oranı: % {otobuslerin_tum_araclar_icindeki_orani:.2f}
Kamyon sayısı: {kamyon_sayisi} tane. Kamyonların tüm araçlar içindeki oranı: %{kamyonlarin_tum_araclar_icindeki_orani:.2f}
Tır sayısı: {tir_sayisi} tane. Tırların tüm araçlar içindeki oranı: %{tirlarin_tum_araclar_icindeki_orani:.2f}

Otoparkın toplam geliri: {otoparkin_toplam_geliri:.2f} TL 

Motorsikletlerden elde edilen toplam gelir: {motorsiklet_geliri:.2f} TL. Bu gelirin otopark geliri içerisindeki oranı: %{motosikletlerin_toplam_gelir_orani:.2f}
Binek araçlardan elde edilen toplam gelir: {binek_geliri:.2f} TL. Bu gelirin otopark geliri içerisindeki oranı: %{bineklerin_toplam_gelir_orani:.2f}
Minibüslerden elde edilen toplam gelir: {minibus_geliri:.2f} TL. Bu gelirin otopark geliri içerisindeki oranı: %{minibuslerin_toplam_gelir_orani:.2f}
Otobüslerden elde edilen toplam gelir: {otobus_geliri:.2f} TL. Bu gelirin otopark geliri içerisindeki oranı: %{otobuslerin_toplam_gelir_orani:.2f}
Kamyonlardan elde edilen toplam gelir: {kamyon_geliri:.2f} TL. Bu gelirin otopark geliri içerisindeki oranı: %{kamyonlarin_toplam_gelir_orani:.2f}
Tırlardan elde edilen toplam gelir: {tir_geliri:.2f} TL. Bu gelirin otopark geliri içerisindeki oranı: %{tirlarin_toplam_gelir_orani:.2f}

Motorsikletlerin ortalama otoparkta kalma süresi: {motorsiklet_otoparkta_kalma_gun} gün {motorsiklet_otoparkta_kalma_saat} saat {motorsiklet_otoparkta_kalma_dakika:.2f} dakika
Binek araçların ortalama otoparkta kalma süresi: {binek_otoparkta_kalma_gun} gün {binek_otoparkta_kalma_saat} saat {binek_otoparkta_kalma_dakika:.2f} dakika
Minibüslerin ortalama otoparkta kalma süresi: {minibus_otoparkta_kalma_gun} gün {minibus_otoparkta_kalma_saat} saat {minibus_otoparkta_kalma_dakika:.2f} dakika
Otobüslerin ortalama otoparkta kalma süresi: {otobus_otoparkta_kalma_gun} gün {otobus_otoparkta_kalma_saat} saat {otobus_otoparkta_kalma_dakika:.2f} dakika
Kamyonların ortalama otoparkta kalma süresi: {kamyon_otoparkta_kalma_gun} gün {kamyon_otoparkta_kalma_saat} saat {kamyon_otoparkta_kalma_dakika:.2f} dakika
Tırların ortalama otoparkta kalma süresi: {tir_otoparkta_kalma_gun} gün {tir_otoparkta_kalma_saat} saat {tir_otoparkta_kalma_dakika:.2f} dakika

Motorsikletlerden araç başına elde edilen ortalama gelir: {motorsiklet_ortalama_geliri:.2f} TL.
Binek araçlardan araç başına elde edilen ortalama gelir: {binek_ortalama_geliri:.2f} TL.
Mibibüslerden araç başına elde edilen ortalama gelir: {minibus_ortalama_geliri:.2f} TL.
Otobüslerden araç başına elde edilen ortalama gelir: {otobus_ortalama_geliri:.2f} TL.
Kamyonlardan araç başına elde edilen ortalama gelir: {kamyon_ortalama_geliri:.2f} TL.
Tırlardan araç başına elde edilen ortalama gelir: {tir_ortalama_geliri:.2f} TL.

Ağırlığı 1 tondan az binek araçların tüm binek araçlar içerisindeki oranı: %{agirligi_1_tondan_az_binek_orani:.2f}
Ağırlığı 10 tondan fazla olan otobüs, kamyon ve tır sınıfı araçların, tüm otobüs, kamyon ve tır sınıfı araçlar içindeki oranı: %{agirligi_10_tondan_fazla_okt_orani:.2f}
Otoparkta 30 dakika veya daha kısa süre kalan motosiklet ve binek tipi araçların, tüm motosiklet ve binek tipi araçlar içindeki oranı: %{otoparkta_30_dk_az_bm_oran:.2f}
Otoparkta 1 günden daha uzun süre kalan minibüs ve otobüs tipi araçların, tüm minibüs ve otobüs tipi araçlar içindeki oranı: %{otoparkta_bir_gunden_fazla_mo_oran:.2f}
Otoparkta 30 günden daha uzun süre kalan veya 1000 TL’den daha yüksek gelir edilen araçların, tüm araçlar içindeki oranı: %{binden_fazla_gelir_veya_30_gun_oran:.2f}
Sürücüsü gazi olan araç sayısı: {gazi_arac_sayisi} tane. Bu araçların tüm araçlar içindeki oranları: %{gazi_oran:.2f}
Sürücüsü engelli olan araç sayısı: {engelli_arac_sayisi} tane. Bu araçların tüm araçlar içindeki oranları: %{engelli_oran:.2f}
Sürücüsü gazi olan araçların araç başına ortalama otoparkta kalma süreleri: {gazi_otoparkta_kalma_gun} gün {gazi_otoparkta_kalma_saat} saat {gazi_otoparkta_kalma_dakika:.2f} dakika
Sürücüsü engelli olan araçların araç başına ortalama otoparkta kalma süreleri: {engelli_otoparkta_kalma_gun} gün {engelli_otoparkta_kalma_saat} saat {engelli_otoparkta_kalma_dakika:.2f} dakika 
Otoparkta 3 saatten daha uzun süre kalan indirim uygulanan araçların, tüm indirim uygulanan araçlar içindeki oranı: %{uc_saatten_fazla_indirimli_oran:.2f}
En uzun süre otoparkta kalan aracın otoparkta kaldığı süre: {en_uzun_sure_gun} gün {en_uzun_sure_saat} saat {en_uzun_sure_dakika:.2f} dakika. Bu araçtan elde edilen gelir {en_uzun_sure_otoparkta_kalandan_elde_edilen_gelir:.2f} TL
En çok gelir elde edilen binek aracın otoparkta kaldığı süre: {en_uzun_binek_gun} gün {en_uzun_binek_saat} saat {en_uzun_binek_dakika:.2f} dakika. Bu araçtan elde edilen gelir {en_cok_gelir_elde_edilen_binek:.2f} TL
""")
