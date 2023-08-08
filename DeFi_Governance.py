# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='DeFi In Danger, Can Governance Provide the Remedy?',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('DeFi In Danger, Can Governance Provide the Remedy?')
st.text(" \n")
st.text(" \n")
st.text(" \n")


# Content
c1, c2, c3 = st.columns(3)


with c1:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/curve.jpeg'))

with c2:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/curve_debt.png'))
with c3:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/stability.jpeg'))

st.text(" \n")
st.text(" \n")


st.write("""
### Attackers Steal $61.7 Million From Several DeFi Projects in Curve Pool Exploits ###
Several decentralized finance protocols were hit on Sunday by attackers who stole more than \$61.7 million worth of crypto. The attackers leveraged a vulnerability in liquidity pools on Curve, the automated market maker platform. The vulnerability was traced back to Vyper, an alternative, third-party programming language for Ethereum smart contracts, according to Curve on Twitter. Curve said other liquidity pools that don’t leverage the language are fine. A number of stablepools (alETH/msETH/pETH) using Vyper 0.2.15 have been exploited as a result of a malfunctioning reentrancy lock. We are assessing the situation and will update the community as things develop. Other pools are safe.     
In a now-deleted Tweet, Curve initially described the vulnerability as a run-of-the-mill, read-only "re-entrancy" attack that could’ve been avoided. A re-entrancy attack happens when a smart contract interacts with another contract, which in turn calls back to the first contract before fully executing.[[1]](https://decrypt.co/150606/attackers-steal-24-million-from-several-defi-projects-in-curve-pool-exploits) """)

st.write(""" ### Assessing the Current State of DeFi: Is DeFi Dead already ?
The commentariat said decentralized finance is in danger amid the crypto winter and recent spate of hacks. They're dead wrong. I’ve seen a couple articles in the past few days about the death and decay of decentralized finance (DeFi). The impetus has been the recent issues in DeFi caused by an exploit and crypto founder who is a horrible risk manager. In short: The founder of a prominent automated market maker (AMM) Curve Finance loaned out nearly half of the protocol’s CRV tokens on a few DeFi lenders, and was almost liquidated after an unexpected but somewhat predictable DeFi exploit depreciated the price of CRV.   
The first article was a great op-ed in CoinDesk, written by Daniel Kuhn, who said DeFi is “dead inside.” The second was a report from JPMorgan, which argued the overall sector is in “shrinking or stalling mode.” These commentators couldn't be further from the truth, however.The idea of what DeFi was during the summer of 2020 is certainly, and thankfully dead. It was a time of too much bribery, liquidity and talk of yield. “Yield farming,” the fuel to DeFi Summer’s fire, eventually calmed down and a few decentralized platforms emerged as market leaders – many of which took professional “white glove” services in aim for expansion.    
But the sector is not perfect. As Daniel noted, we also have far too much power in the hands of too few people. Sounds too familiar.
The difference with this technology versus tech of the past, is that DeFi has been financialized to an extreme. It's not ideal when a bunch of programmers start playing financiers.   
But we need to remember, we’re still experimenting with the technology. We’re not sure how to use it. Mistakes will be made.
What we’ve accomplished in the last few years is to build robust systems that don’t operate within the confines of traditional corporations, banking rails or even geographical borders. The system has been secure enough that the financial and corporate heavyweights like Mastercard, Visa, Coca Cola, Anheuser Busch, Nike, Starbucks, BNY Mellon, BlackRock and Fidelity are devoting money and internal resources to utilizing the technology for greater efficiency.
[[2]](https://www.coindesk.com/consensus-magazine/2023/08/05/defi-definitely-isnt-dead/  ) """)

# c1, c2, c3 = st.columns(3)

# with c1:
#     st.image(Image.open('Images/blend8.jpg'))

# with c2:
#     st.image(Image.open('Images/blend5.jpeg'))

# with c3:
#     st.image(Image.open('Images/blend6.jpg'))

st.write("""
## Methodology ##   
We go in-depth on Blend protocol transactions in this dashboard.  we begin searching for Blend transactions using the contract address '0x29469395eaf6f95920e59f858042f0e28d98a20b' On the Flipside . This contract has 13 unique functions, and every one of them does certain tasks, some of which are not regarded as lending transactions. Due to the various structure of log saving, it is almost impossible to divide each function and combine the results in a single table.   
We discovered that there is unfortunately no decoded value for the LoanOfferTaken function in flipside tables by comparing the Etherscan result with flipside data, thus we went looking for a different data source. We discovered that the Blend transaction values are contained in a single table in Dune's 'blur_ethereum.Blend_evt_LoanOfferTaken'. We generated our queries using the Pandas tool after extracting the Dune source table. In the first component of this dashboard, we look into the ETH borrowed over the course of the last ten days starting on May 1 and attempt to divide the results by collections as requested in the chart description.      
The activity of lenders and borrowers as well as daily and hourly NFT borrowing patterns are examined in the second section. After that, we assess how Blend's introduction has affected other platforms and the NFT market as a whole.  
""")
st.warning(""" Due to Blur's official announcement of three available collections—Azuki, Milady, and Cryptopunk—there were five lending transactions on the first day Blend commenced trading NFT in the Boner collection. These 5 transactions were omitted from the data set and they were considered as system checks transactions.    """)


st.text(" \n")
st.write("""   
#### Sources ####  """)
st.write("""    1.https://decrypt.co/150606/attackers-steal-24-million-from-several-defi-projects-in-curve-pool-exploits     
                2.https://www.coindesk.com/consensus-magazine/2023/08/05/defi-definitely-isnt-dead/   
        3.https://www.paradigm.xyz/2023/05/blend     
        4.[Image Source]https://twitter.com/blur_io
            """)


st.text(" \n")
c1, c2 = st.columns(2)
with c1:
    st.info(
        '**Twitter:  [Ludwig.1989](https://twitter.com/Ludwig_1989/status/1656498361527140352)**', icon="🕊️")
    st.info(
        '**Data Set (1):  [Dune-Blend LoanOfferTaken](https://dune.com/queries/2456014?category=decoded_project&namespace=blur&blockchains=ethereum&contract=Blend&abi=Seize)**', icon="🧠")

with c2:
    st.info(
        '**Project Github:  [Blend Portocol Activity](https://github.com/Kaizen-Step/Blend_Protocol_Activity)**', icon="💻")
    st.info(
        '**Data Set (2):  [Flipside](https://flipsidecrypto.xyz/)**', icon="🧠")
