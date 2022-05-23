"""
Package Gempa
"""
import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    tanggal: 19 Mei 2022
    waktu: 04:12:08 WIB
    magnitudo: 2.9
    kedalaman: 10 km
    koordinat: ls: 3.63, bt: 128.17
    lokasi: Pusat gempa berada di darat 7 km Utara Ambon
    dirasakan: Dirasakan (Skala MMI): III Ambon
    :return:
    """
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, "html.parser")
        tanggal = soup.find("span", {"class": "waktu"}).text.split(", ")
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None
        i = 0

        result = soup.find("div", {"class": "col-md-6 col-xs-6 gempabumi-detail no-padding"}).findChildren("li")
        for res in result:
            if i == 1:
                magnitudo = res.text
            if i == 2:
                kedalaman = res.text
            if i == 3:
                koordinat = res.text.split("-")
                ls = koordinat[0]
                bt = koordinat[1]
            if i == 4:
                lokasi = res.text
            if i == 5:
                dirasakan = res.text

            i += 1

        hasil = dict()
        hasil["tanggal"] = tanggal[0]
        hasil["waktu"] = tanggal[1]
        hasil["magnitudo"] = magnitudo
        hasil["kedalaman"] = kedalaman
        hasil["koordinat"] = {"ls": ls, "bt": bt}
        hasil["lokasi"] = lokasi
        hasil["dirasakan"] = dirasakan

        return hasil


def tampilkan_data(result):
    if result is None:
        print("Data gempa tidak ditemukan.")
        return
    print("Gempa Terkini berdasarkan informasi dari BMKG terjadi pada:")
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Koordinat: {result['koordinat']['ls']}{result['koordinat']['bt']}")
    print(f"{result['lokasi']}")
    print(f"{result['dirasakan']}")