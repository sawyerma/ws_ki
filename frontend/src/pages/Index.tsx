import { useState } from "react";
import TradingNav from "../components/ui/trading-nav";
import PriceDisplay from "../components/ui/price-display";
import TimeButtons from "../components/ui/time-buttons";
import ChartSection from "../components/ui/chart-section";
import CoinSelector from "../components/ui/coin-selector";
import ThemeProvider from "../components/ui/theme-provider";
import Database from "./Database";
import AI from "./AI";
import ML from "./ML";
import Whales from "./Whales";
import News from "./News";
import TradingBot from "./TradingBot";

interface CoinData {
  id: string;
  symbol: string;
  market: string;
  price: string;
  change: string;
  changePercent: number;
  isFavorite: boolean;
  liveStatus: "green" | "red";
  histStatus: "green" | "red";
}

const Index = () => {
  const [viewMode, setViewMode] = useState<
    "trading" | "database" | "ai" | "ml" | "whales" | "news" | "bot"
  >("trading");
  const [selectedCoin, setSelectedCoin] = useState("BTC/USDT");
  const [selectedInterval, setSelectedInterval] = useState("1m");
  const [selectedIndicators, setSelectedIndicators] = useState<string[]>([]);
  const [currentCoinData, setCurrentCoinData] = useState<CoinData>({
    id: "1",
    symbol: "BTC/USDT",
    market: "spot",
    price: "104,911.62",
    change: "-3.56%",
    changePercent: -3.56,
    isFavorite: true,
    liveStatus: "green",
    histStatus: "green",
  });

  // Deine Marktdaten als Variablen - diese kannst du von deinem Programm übergeben
  const [marketData, setMarketData] = useState({
    change24h: "-3.56%", // Variable 1
    high24h: "110.157,20", // Variable 2
    low24h: "99.666,04", // Variable 3
    volume24h: "6.08K", // Variable 4
    turnover24h: "645.65M", // Variable 5
    category: "Public Chain", // Variable 6
  });

  // Trading Mode State (Spot oder Futures-Option)
  const [tradingMode, setTradingMode] = useState("Spot");

  const handleCoinSelect = (coin: CoinData) => {
    setSelectedCoin(coin.symbol);
    setCurrentCoinData(coin);
  };

  const handleIntervalChange = (interval: string) => {
    setSelectedInterval(interval);
  };

  const handleIndicatorSelect = (indicator: string) => {
    setSelectedIndicators(prev => {
      if (prev.includes(indicator)) {
        return prev; // Don't add duplicates
      }
      return [...prev, indicator];
    });
  };

  const handleIndicatorRemove = (indicator: string) => {
    setSelectedIndicators(prev => prev.filter(i => i !== indicator));
  };

  // Show different views based on mode
  if (viewMode === "database") {
    return <Database onBackToTrading={() => setViewMode("trading")} />;
  }
  if (viewMode === "ai") {
    return <AI onBackToTrading={() => setViewMode("trading")} />;
  }
  if (viewMode === "ml") {
    return <ML onBackToTrading={() => setViewMode("trading")} />;
  }
  if (viewMode === "whales") {
    return <Whales onBackToTrading={() => setViewMode("trading")} />;
  }
  if (viewMode === "news") {
    return <News onBackToTrading={() => setViewMode("trading")} />;
  }
  if (viewMode === "bot") {
    return <TradingBot onBackToTrading={() => setViewMode("trading")} />;
  }

  return (
    <ThemeProvider>
      <div
        className="bg-[#fbfcfd] dark:bg-gray-900 text-[#222] dark:text-white min-h-screen px-6 py-5 transition-colors"
        style={{
          fontFamily: "'Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'",
        }}
      >
        {/* Top Navigation */}
        <TradingNav
          onTradingModeChange={setTradingMode}
          onViewChange={setViewMode}
        />

        {/* Market & Price Section */}
        <div className="flex gap-5 max-lg:flex-col max-lg:gap-0">
          {/* Column 1: Coin Selector */}
          <div className="flex flex-col w-[17%] max-lg:w-full max-lg:ml-0">
            <CoinSelector
              selectedCoin={selectedCoin}
              onCoinSelect={handleCoinSelect}
              selectedTradingMode={tradingMode}
              showLiveStatus={true}
              showHistStatus={true}
            />
          </div>

          {/* Column 2: Price Display */}
          <div className="flex flex-col w-[83%] ml-5 max-lg:w-full max-lg:ml-0">
            <PriceDisplay
              currentCoinData={currentCoinData}
              marketData={marketData}
              tradingMode={tradingMode}
            />
          </div>
        </div>

        {/* Time Buttons */}
        <TimeButtons 
          onIntervalChange={handleIntervalChange}
          onIndicatorSelect={handleIndicatorSelect}
        />

        {/* Main Content: Multi-Chart + Orderbook */}
        <ChartSection 
          selectedCoin={selectedCoin}
          selectedMarket={currentCoinData.market}
          selectedInterval={selectedInterval}
          selectedIndicators={selectedIndicators}
          onIndicatorRemove={handleIndicatorRemove}
        />
      </div>
    </ThemeProvider>
  );
};

export default Index;