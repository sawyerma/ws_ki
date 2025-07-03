import ChartView from "./components/ChartView";
import MarketTrades from "./components/MarketTrades";
import Orderbook from "./components/OrderBook";

export default function App() {
  // Optional: symbol und market als Variable/State – für Dropdown oder Selektion später
  const symbol = "BTCUSDT";
  const market = "spot";

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-[#17181c]">
      <h1 className="text-2xl text-white mb-4 font-bold">BTCUSDT LIVE CHART</h1>
      <ChartView
        wsUrl={`ws://localhost:8000/ws/${symbol}/${market}`}
        width={900}
        height={480}
        symbol={symbol}
        market={market}
      />
      {/* Neue Komponenten unterhalb vom Chart */}
      <div className="flex flex-row gap-8 mt-8">
        <MarketTrades symbol={symbol} market={market} wsBase="ws://localhost:8000" />
        <Orderbook symbol={symbol} market={market} apiBase="http://localhost:8000" />
      </div>
    </div>
  );
}
