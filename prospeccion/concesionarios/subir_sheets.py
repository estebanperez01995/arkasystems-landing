#!/usr/bin/env python3
"""Crea la pestana 'consecionarias' en CRM PROSPECCION y vuelca el CSV.

    pip install gspread google-auth
    python3 subir_sheets.py concesionarias.csv

Credenciales: variable GOOGLE_APPLICATION_CREDENTIALS apuntando al JSON de una
service account con acceso de edicion a la hoja (compartela con el email de la
service account), o gspread.oauth() si prefieres OAuth de usuario.

Si la pestana ya existe, NO la pisa: aborta y te lo dice. Para reemplazarla,
pasa --reemplazar.
"""
import argparse, csv, os, sys

SHEET_ID = "1C-dFcIQ4rND4DyyLTD2gDF3TklhMBiM0602Oip0XT68"  # CRM PROSPECCION
PESTANA = "consecionarias"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path")
    ap.add_argument("--pestana", default=PESTANA)
    ap.add_argument("--reemplazar", action="store_true")
    args = ap.parse_args()

    import gspread
    from google.oauth2.service_account import Credentials

    ruta = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if ruta:
        creds = Credentials.from_service_account_file(
            ruta, scopes=["https://www.googleapis.com/auth/spreadsheets"])
        gc = gspread.authorize(creds)
    else:
        gc = gspread.oauth()

    sh = gc.open_by_key(SHEET_ID)

    with open(args.csv_path, encoding="utf-8") as f:
        filas = list(csv.reader(f))
    if len(filas) < 2:
        sys.exit("El CSV no tiene datos.")

    existentes = [w.title for w in sh.worksheets()]
    if args.pestana in existentes:
        if not args.reemplazar:
            sys.exit(f"La pestana '{args.pestana}' ya existe. Usa --reemplazar si quieres pisarla.")
        sh.del_worksheet(sh.worksheet(args.pestana))

    ws = sh.add_worksheet(title=args.pestana, rows=len(filas) + 50, cols=len(filas[0]) + 5)
    ws.update(values=filas, range_name="A1")
    ws.freeze(rows=1)
    ws.format("A1:AC1", {"textFormat": {"bold": True}})
    print(f"OK: {len(filas) - 1} filas en la pestana '{args.pestana}'")
    print(f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit#gid={ws.id}")


if __name__ == "__main__":
    main()
