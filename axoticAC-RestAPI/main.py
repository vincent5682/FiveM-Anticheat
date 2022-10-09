from fastapi import FastAPI, Request
import pymysql
from datetime import datetime
import uvicorn
import asyncio
from pydantic import BaseModel


class Scan(BaseModel):
    steamid: str
    ip: str
    verify: bool

# database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="axoticac")
cursor = connection.cursor()

app = FastAPI()

async def main():
    config = uvicorn.Config("main:app", port=8000, host="0.0.0.0")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())


@app.get("/ip")
async def index(request: Request):
    return request.client.host.replace('"', '')


@app.post("/scan")
async def addScan(scan: Scan):
    retrieve = "Select * from user WHERE steamid = %s AND ip = %s;"
    tuple1 = (scan.steamid, scan.ip)

    # executing the quires
    cursor.execute(retrieve, tuple1)
    rows = cursor.fetchall()
    if len(rows) == 0:
        insert = "INSERT INTO user(steamid, ip, verify) VALUES(%s, %s, %s);"
        tuple2 = (scan.steamid, scan.ip, scan.verify)
        cursor.execute(insert, tuple2)
        connection.commit()
    else:
        updateSql = "UPDATE user SET verify = %s, lastupdated = %s WHERE steamid = %s AND ip = %s;"
        tuple3 = (scan.verify, datetime.now(), scan.steamid, scan.ip)
        cursor.execute(updateSql, tuple3)
        connection.commit()
    return {"success": True}
