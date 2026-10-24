
import json
from datetime import datetime, timezone
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE = "https://www.binance.com/bapi/c2c/v1/public/c2c/agent/ad-list"

def get_offers():
    params = {
        "fiat": "SDG",
        "asset": "USDT",
        "tradeType": "BUY",
        "limit": 20,
        "tradeMethodIdentifiers": "BankofKhartoum",
    }
    url = BASE + "?" + urlencode(params)
    request = Request(url, headers={
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
    })

    with urlopen(request, timeout=25) as response:
        data = json.load(response)

    if data.get("success") is not True:
        raise RuntimeError("Binance request failed")

    offers = []
    for item in data.get("data", {}).get("items", []):
        if "BankofKhartoum" not in item.get("tradeMethods", []):
            continue

        advertiser = item.get("advertiser", {})
        offers.append({
            "price": float(item["price"]),
            "min_transaction_raw": item.get("minTransAmount"),
            "max_transaction_raw": item.get("maxTransAmount"),
            "raw_ad": item,
            "available_usdt": item.get("tradableAmount"),
            "advertiser": advertiser.get("nickName"),
            "completion_rate": advertiser.get("monthFinishRate"),
            "monthly_orders": advertiser.get("monthOrderCount"),
        })

    if not offers:
        raise RuntimeError("No matching offers found")

    offers.sort(key=lambda x: x["price"])

    return {
        "source": "Binance P2P",
        "pair": "USDT/SDG",
        "side": "BUY",
        "payment_method": "BankofKhartoum",
        "updated_at_utc": datetime.now(timezone.utc).isoformat(),
        "offers": offers,
    }

if __name__ == "__main__":
    result = get_offers()
    with open("prices.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print("Updated:", result["updated_at_utc"])
    print("Best price:", result["offers"][0]["price"])
    
