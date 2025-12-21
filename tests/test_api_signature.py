import asyncio

from api_signature import (
    generate_signature,
    generate_signature_header,
    verify_signature,
    verify_signature_header,
)

appid = "appid"
secret_key = "secret_key"


async def gs():
    sign = await generate_signature(appid, secret_key, "/path", "GET")
    print(sign)


async def gsh():
    sign_header = await generate_signature_header(
        appid, secret_key, "/path", "POST", {"a": "a", "b": 1}, {"_t": "1234567890"}
    )
    print(sign_header)


async def vs():
    signature = await verify_signature(
        url="/path",
        appid=appid,
        secret_key=secret_key,
        nonce="IsJRqILi",
        timestamp="1766335905",
        signature="FCAA034551D699945D5B6FD44562D977B0E924DDE8DA4732D5E8F53A3B929141",
    )
    print(signature)


async def get_secret(appid):
    return secret_key


async def vsh():
    sign = await verify_signature_header(
        url="/path",
        method="POST",
        body={"a": "a", "b": 1},
        query={"_t": "1234567890"},
        header_value="HMAC-SHA256 appid:1766336579:Ob0Fy5Xd:D6F3973B00B7463EDA081284775D4770B60430E620E9C804D8B267290AC5BD4D",
        get_secretkey_by_appid=get_secret,
    )
    print(sign)


if __name__ == "__main__":
    asyncio.run(vsh())
