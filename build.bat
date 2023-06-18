@echo off

pip install -r requirements.txt

python konverter_ui.py
pyinstaller --noconfirm --onefile --windowed --icon "stock.ico" --name "InventorySukma"  "app.py"
explorer .\dist