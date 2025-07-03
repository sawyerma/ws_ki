import logging
import traceback
from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException

from exchanges.bitget.rest_utils import (
    fetch_spot_symbols,
    fetch_futures_symbols,
    fetch_spot_tickers,
    fetch_futures_tickers,
)
from db.clickhouse import fetch_symbols

router = APIRouter()
logger = logging.getLogger("trading-api")


@router.get("/symbols")
async def get_symbols():
    """
    Holt alle verfügbaren Symbole von Bitget REST und aus der lokalen Datenbank für Dropdowns etc.
    """
    try:
        spot_symbols = await fetch_spot_symbols()
        usdtm_symbols = await fetch_futures_symbols("USDT-FUTURES")
        coinm_symbols = await fetch_futures_symbols("COIN-FUTURES")
        usdcm_symbols = await fetch_futures_symbols("USDC-FUTURES")
        all_api = spot_symbols + usdtm_symbols + coinm_symbols + usdcm_symbols

        db_symbols = fetch_symbols()
        return {
            "symbols": all_api,
            "db_symbols": db_symbols
        }
    except Exception as e:
        logger.error(f"SYMBOLS-API-ERROR: {e}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Bitget-API-Fehler: {e}")


@router.get("/ticker")
async def get_ticker():
    """
    Holt aktuelle Ticker/Preise für alle Symbole und Märkte von Bitget REST.
    """
    try:
        out: List[Dict[str, Any]] = []

        # Spot-Ticker
        spot_tickers = await fetch_spot_tickers()
        for tk in spot_tickers:
            out.append({
                "symbol":      tk["symbol"],
                "last":        float(tk.get("last", 0)),
                "high24h":     float(tk.get("high24h", 0)),
                "low24h":      float(tk.get("low24h", 0)),
                "changeRate":  float(tk.get("changeRate", 0)),
                "baseVol":     float(tk.get("baseVol", 0)),
                "quoteVol":    float(tk.get("quoteVol", 0)),
                "market_type": "spot",
            })

        # USDT-Margined Futures
        usdtm_tickers = await fetch_futures_tickers("UMCBL")
        for tk in usdtm_tickers:
            out.append({
                "symbol":      tk["symbol"],
                "last":        float(tk.get("last", 0)),
                "high24h":     float(tk.get("high24h", 0)),
                "low24h":      float(tk.get("low24h", 0)),
                "changeRate":  float(tk.get("changeRate", 0)),
                "baseVol":     float(tk.get("baseVol", 0)),
                "quoteVol":    float(tk.get("quoteVol", 0)),
                "market_type": "usdtm",
            })

        # Coin-Margined Futures
        coinm_tickers = await fetch_futures_tickers("DMCBL")
        for tk in coinm_tickers:
            out.append({
                "symbol":      tk["symbol"],
                "last":        float(tk.get("last", 0)),
                "high24h":     float(tk.get("high24h", 0)),
                "low24h":      float(tk.get("low24h", 0)),
                "changeRate":  float(tk.get("changeRate", 0)),
                "baseVol":     float(tk.get("baseVol", 0)),
                "quoteVol":    float(tk.get("quoteVol", 0)),
                "market_type": "coinm",
            })

        # USDC-Margined Futures
        usdcm_tickers = await fetch_futures_tickers("CMCBl")
        for tk in usdcm_tickers:
            out.append({
                "symbol":      tk["symbol"],
                "last":        float(tk.get("last", 0)),
                "high24h":     float(tk.get("high24h", 0)),
                "low24h":      float(tk.get("low24h", 0)),
                "changeRate":  float(tk.get("changeRate", 0)),
                "baseVol":     float(tk.get("baseVol", 0)),
                "quoteVol":    float(tk.get("quoteVol", 0)),
                "market_type": "usdcm",
            })

        return out

    except Exception as e:
        logger.error(f"TICKER-API-ERROR: {e}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Ticker-API-Fehler: {e}")
