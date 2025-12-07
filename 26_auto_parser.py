import requests
import pandas as pd
from sqlalchemy import create_engine
import logging
import traceback
import os

# 自動建立 log 資料夾
os.makedirs("./log", exist_ok=True)

# 設定 Logging
logging.basicConfig(
    filename="./log/youbike_import.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    encoding="utf-8"
)

def log_error(msg):
    logging.error(msg)
    logging.error(traceback.format_exc())

def main():
    try:
        logging.info("=== YouBike 資料匯入開始 ===")

        # API 網址
        url = "https://api.kcg.gov.tw/api/service/Get/b4dd9c40-9027-4125-8666-06bef1756092"

        # 取得資料
        resp = requests.get(url, timeout=10)

        if resp.status_code != 200:
            raise Exception(f"API 回傳狀態碼異常: {resp.status_code}")

        # 轉成 json
        data = resp.json()

        # 取得 retVal
        records = data.get('data', {}).get('data', {}).get('retVal', {})
        if not records:
            raise Exception("API 回傳資料結構異常或無資料")
        
        # 轉為Df
        df = pd.DataFrame(records)

        # 拆解 sbi_detail
        df["yb2"] = df["sbi_detail"].apply(lambda x: x.get("yb2") if isinstance(x, dict) else None)
        df["eyb"] = df["sbi_detail"].apply(lambda x: x.get("eyb") if isinstance(x, dict) else None)

        # 刪除原本的 dict 欄位（可選）
        df.drop(columns=["sbi_detail"], inplace=True)

        logging.info(f"成功取得 {len(df)} 筆資料")

        # 寫入資料庫
        user = "postgres"
        password = "postgres"
        host = "127.0.0.1"
        port = 5432
        db = "mydb"

        conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
        engine = create_engine(conn_str)

        df.to_sql("youbike_kaohsiung", engine, if_exists="append", index=False)

        logging.info("資料已成功寫入 PostgreSQL")
        logging.info("=== YouBike 資料匯入完成 ===")

    except Exception as e:
        log_error(f"發生錯誤: {str(e)}")
        print("發生錯誤，已寫入 log。")
        return

if __name__ == "__main__":
    main()
    print("程式執行完畢")
