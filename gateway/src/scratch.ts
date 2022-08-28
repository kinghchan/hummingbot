// // @ts-ignore
// import { ethers } from "ethers";
// import { UniswapLPHelper } from './connectors/uniswap/uniswap.lp.helper'
// import {Token} from "@uniswap/sdk-core";
// import {FeeAmount} from "@uniswap/v3-sdk";
// import {Uniswap} from "./connectors/uniswap/uniswap";
//
// const main = async() => {
//   try {
//      console.log('hello');
//     // const provider = new ethers.providers.InfuraProvider("homestead", '9d49173be818436ca54461c87574f508')
//     // provider.getBalance(address).then((balance: any) => {
//     //   // convert a currency unit from wei to ether
//     //   const balanceInEth = ethers.utils.formatEther(balance)
//     //   console.log(`balance: ${balanceInEth} ETH`)
//     // });
//     // @ts-ignore
//     var chainId = 1;
//     var chain = 'ethereum';
//     var network  = 'mainnet';
//     // @ts-ignore
//     const uniswap = Uniswap.getInstance(chain, network);
//     const helper = new UniswapLPHelper(chain, network);
//     const params0 = {
//       // 'chainId': chainId,
//       // 'address': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
//       // 'decimals': 18,
//       // 'symbol': 'WETH'
//       // 'chainId': chainId,
//       // 'address': '0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0',
//       // 'decimals': 18,
//       // 'symbol': 'MATIC'
//       'chainId': chainId,
//       'address': '0x853d955aCEf822Db058eb8505911ED77F175b99e',
//       'decimals': 18,
//       'symbol': 'FRAX'
//     }
//     const params1 = {
//       'chainId': chainId,
//       'address': '0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599',
//       // 'address': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
//       'decimals': 8,
//       // 'decimals': 6,
//       'symbol': 'WBTC'
//       // 'symbol': 'USDC'
//     };
//
//     const token0 = new Token(params0.chainId, params0.address, params0.decimals, params0.symbol);
//     const token1 = new Token(params1.chainId, params1.address, params1.decimals, params1.symbol);
//
//     const feeTier = FeeAmount.HIGH;
//     // @ts-ignore - conflicting 'Token' types. UPDATE - actually need the other type
//     const price = await helper.poolPrice(token1, token0, feeTier);
//     console.log(price);
//
//     // @ts-ignore - conflicting 'Token' types
//     const estimate = await uniswap.estimateBuyTrade(token0, token1, 1);
//     console.log("estimate: ", estimate);
//   } catch (err: any) {
//     console.log(err);
//   }
// }
//
// main();
