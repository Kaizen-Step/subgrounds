# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image
from subgrounds import Subgrounds


# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title='Curve liqudity Pools - DeFi In Danger',
                   page_icon=':bar_chart:🌌', layout='wide')
st.title('🌌 Curve liqudity Pools')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# # Data Sources
# @st.cache_data()
sg = Subgrounds()

curve = sg.load_subgraph(
    "https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum"
)

# Partial FieldPath selecting the top 4 most traded pools on Curve
most_traded_pools = curve.Query.liquidityPools(
    orderBy=curve.LiquidityPool.cumulativeVolumeUSD,
    orderDirection="desc",
    first=4,
)

# Partial FieldPath selecting the top 2 pools by daily total revenue of
#  the top 4 most traded tokens.
# Mote that reuse of `most_traded_pools` in the partial FieldPath
most_traded_snapshots = most_traded_pools.dailySnapshots(
    orderBy=curve.LiquidityPoolDailySnapshot.dailyTotalRevenueUSD,
    orderDirection="desc",
    first=3,
)

# Querying:
#  - the name of the top 4 most traded pools, their 2 most liquid
# pools' token symbols and their 2 most liquid pool's TVL in USD
df = sg.query_df(
    [
        most_traded_pools.name,
        most_traded_snapshots.dailyVolumeUSD,
        most_traded_snapshots.dailyTotalRevenueUSD,
    ]
)

############################


# datetime_obj=datetime.fromtimestamp(epoch)


st.table(df.head(10))


#################################################################################################
st.write(""" ### ETH Borrowing Volume ##  """)

st.write("""
If you're looking to buy non-fungible tokens (NFTs) on the Blur platform using Blend portocol, you may want to consider borrowing Ethereum (ETH) to do so. 
By borrowing ETH on Blur, you can get the funds you need to buy the NFTs you want without having to sell other cryptocurrencies or dip into your savings. Plus, borrowing ETH can be a more cost-effective way to access liquidity than selling other NFTs, especially if you believe that the value of those NFTs will appreciate over time.
To borrow ETH on Blur, you'll need to have some collateral to put up.    
Collateral is a NFT that you own that you pledge as security for the loan. In the case of borrowing ETH to buy NFTs. Once you've put up your collateral, you can borrow ETH at a competitive interest rate and use it to purchase NFTs on the Blur platform .You can then pay back the loan at your own pace, depending on the loan terms you choose. In this section we dipe dive on ETH volume borrow using Blend portocol on blur platform.

  """)


st.info(""" ##### In This User Growth Section you can find: ####

* Daily Number of BNPL (Borrowed) NFT on Blur Platform
* Volume of Borrowed Transactions  
* ETH Volume Borrowed In each NFT Collection




""")


#################################################################################################
