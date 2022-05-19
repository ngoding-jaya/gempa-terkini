"""
Aplikasi Informasi Gempa Terkini BMKG 
"""


import gempa


if __name__ == '__main__':
    print("Aplikasi Gempa Terkini")
    result = gempa.ekstraksi_data()
    gempa.tampilkan_data(result)
