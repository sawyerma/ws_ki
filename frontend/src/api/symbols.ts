// API endpoint for symbols data
export interface ApiSymbol {
  symbol: string;
  market: string;
  price: string;
  change: string;
  changePercent: number;
}

export interface ApiResponse {
  symbols: ApiSymbol[];
}

// Mock data that matches the expected API format
const mockSymbols: ApiSymbol[] = [
  {
    symbol: "BTC/USDT",
    market: "spot",
    price: "104,911.62",
    change: "-3.56%",
    changePercent: -3.56,
  },
  {
    symbol: "ETH/USDT",
    market: "spot",
    price: "3,252.10",
    change: "+1.20%",
    changePercent: 1.2,
  },
  {
    symbol: "SOL/USDT",
    market: "spot",
    price: "134.51",
    change: "+0.30%",
    changePercent: 0.3,
  },
  {
    symbol: "BTC/USDT",
    market: "umcbl",
    price: "104,420.00",
    change: "-0.18%",
    changePercent: -0.18,
  },
  {
    symbol: "ADA/USDT",
    market: "spot",
    price: "0.8945",
    change: "+2.15%",
    changePercent: 2.15,
  },
  {
    symbol: "DOT/USDT",
    market: "spot",
    price: "7.23",
    change: "-1.05%",
    changePercent: -1.05,
  },
];

export function getSymbols(): ApiResponse {
  return {
    symbols: mockSymbols,
  };
}