SCHTASKS /Create /SC ONLOGON /TN start_server /TR  C:\flask_sbs\app\1.bat
SCHTASKS /Create /SC ONLOGON /TN start_kisok /TR  C:\flask_sbs\app\2.bat